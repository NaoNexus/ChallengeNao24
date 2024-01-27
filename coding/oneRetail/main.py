'''
pip2 install -r requirements.txt
python2 main.py
''' 

# Modules
from naoqi import ALProxy
from flask import Flask, render_template, Response, jsonify, request, redirect, url_for
import cv2
import time
import numpy as np
import random
from selenium import webdriver
import paramiko

import utilities
import config_helper
from logging_helper import logger
from speech_recognition_helper import SpeechRecognition
import db_helper


config_helper  = config_helper.Config()
db_helper      = db_helper.DB()

nao_ip         = config_helper.nao_ip
nao_port       = config_helper.nao_port
nao_user       = config_helper.nao_user
nao_password   = config_helper.nao_password

path_drivers   = config_helper.srv_drivers


face_detection = True
face_tracker   = True
local_db       = []
local_rec      = []
local_dialog   = []


app  = Flask(__name__)


def nao_speech_to_text(sec_sleep):
    audio_device_proxy = ALProxy("ALAudioRecorder", nao_ip, nao_port)
    remote_path = "/data/home/nao/recordings/microphones/microphone_audio.wav" # sul nao
    sample_rate = 16000
    
    # Registra l'audio dal microfono del NAO per 5 secondi
    audio_data = audio_device_proxy.startMicrophonesRecording(remote_path, "wav", sample_rate, [0, 0, 1, 0])

    time.sleep(sec_sleep)

    # Attendi il completamento della registrazione
    audio_device_proxy.stopMicrophonesRecording()

    # Connessione SSH
    try:
        transport = paramiko.Transport((nao_ip, 22))                 # Create an SSH client
        transport.connect(username=nao_user, password=nao_password)  # Connect to the SSH server with a username and password
        scp = paramiko.SFTPClient.from_transport(transport)          # Create an SCP client

        local_path  = "recordings/microphone_audio.wav"
        scp.get(remote_path, local_path)
    except Exception as e:
        logger.error(str(e))
    finally:
        scp.close()         # Close the SCP connection
        transport.close()   # Close the SSH connection

    # Speech To Text
    speech_recognition = SpeechRecognition(local_path)
    
    text = speech_recognition.result
    local_rec.append(text)
    audio_device_proxy = None

    return text


def nao_face_detection(image_data):
    face_cascade    = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')     # Create a face cascade for detecting faces
    gray            = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)                                             # Convert the image to grayscale for face detection
    faces           = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))   # Detect faces in the image

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image_data, (x, y), (x+w, y+h), (255, 0, 0), 2)


def nao_face_tracker():
    tracker_proxy = ALProxy("ALTracker", nao_ip, nao_port)
    targetName = "Face"
    faceWidth  = 0.1
    tracker_proxy.setMode("Head")
    tracker_proxy.registerTarget(targetName, faceWidth)
    tracker_proxy.track(targetName)


def nao_stop_face_tracker():
    tracker_proxy = ALProxy("ALTracker", nao_ip, nao_port)
    tracker_proxy.stopTracker()
    tracker_proxy.unregisterAllTargets()


def nao_generate_frames(face_detection):
    video_proxy = ALProxy("ALVideoDevice", nao_ip, nao_port)            # NAO webcam

    # Set the camera parameters
    name_id          = "video_image_" + str(random.randint(0,100))      # The same Name could be used only six time
    camera_id        = 0                                                # Use the top camera (1 for bottom camera)
    resolution       = 1                                                # Image of 320*240px
    color_space      = 13                                               # RGB
    camera_fps       = 30                                               # fps
    brightness_value = 55                                               # default of 55
    video_proxy.setParameter(camera_id, 0, brightness_value)            # brightness

    # Subscribe to the video feed
    video_client = video_proxy.subscribeCamera(name_id, camera_id, resolution, color_space, camera_fps)
    try:
        while True:
            image          = video_proxy.getImageRemote(video_client)   # Capture a frame from the camera
            
            image_width    = image[0]
            image_height   = image[1]
            image_channels = 3
            image_data     = np.frombuffer(image[6], dtype=np.uint8).reshape((image_height, image_width, image_channels))
            
            if face_detection:
                nao_face_detection(image_data)

            desired_width  = 640
            desired_height = 480
            resized_image  = cv2.resize(image_data, (desired_width, desired_height))

            ret, buffer    = cv2.imencode('.jpg', resized_image)            
            frame          = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    except Exception as e:
        print "Error: %s" % e
    finally:
        video_proxy.unsubscribe(video_client)                               # Unsubscribe from the video feed and release resources


def nao_autonomous_life(state="disabled"):
    life_proxy = ALProxy("ALAutonomousLife", nao_ip, nao_port)              # Creare un proxy per il servizio Autonomous Life
    life_proxy.setState(state)                                              # Ferma il comportamento autonomo di base
    life_proxy = None                                                       # Chiudi eventuali connessioni


def nao_wakeup():
    motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)                    # Creare un proxy per il servizio Motion
    motion_proxy.wakeUp()                                                   # Attivare il robot dallo stato di "sleep"
    motion_proxy = None                                                     # Chiudi eventuali connessioni


def nao_eye_white():
    leds_proxy = ALProxy("ALLeds", nao_ip, nao_port)                        # Creare un proxy per il servizio ALLeds
    eye_group_name = "FaceLeds"                                             # Specificare il nome del gruppo LED degli occhi
    eye_color = [255, 255, 255]                                             # RGB values for white
    value_color = 256*256*eye_color[0] + 256*eye_color[1] + eye_color[2]
    leds_proxy.fadeRGB(eye_group_name, value_color, 0.5)                    # 0.5 is the duration in seconds
    leds_proxy = None                                                       # Chiudi la connessione


def nao_animatedSayText(text_to_say):
    tts_proxy = ALProxy("ALAnimatedSpeech", nao_ip, nao_port)               # Connect to the text-to-speech module             
    animated_speech_config = {"bodyLanguageMode": "contextual"}             # Set the parameter for animated speech
    tts_proxy.say(text_to_say, animated_speech_config)                      # Say the text with animated speech                                        
    tts_proxy = None      


def nao_standInit():
    posture_proxy = ALProxy("ALRobotPosture", nao_ip, nao_port)             # Connect to the ALRobotPosture module             
    posture_proxy.goToPosture("StandInit", 0.8)                             # Make the robot stand up
    posture_proxy = None                                                  


def nao_stand():
    posture_proxy = ALProxy("ALRobotPosture", nao_ip, nao_port)             # Connect to the ALRobotPosture module             
    posture_proxy.goToPosture("Stand", 0.8)                                 # Make the robot stand up
    posture_proxy = None  


def nao_volume_sound(volume_level):
    audio_proxy = ALProxy("ALAudioDevice", nao_ip, nao_port)
    audio_proxy.setOutputVolume(volume_level)
    audio_proxy = None


def nao_dialog():
    dialogo = []

    text_to_say = "Come ti chiami?"
    nao_animatedSayText(text_to_say)
    dialogo.append({"nao":text_to_say})
    response = nao_speech_to_text(5)
    dialogo.append({"umano":response})

    text_to_say = "Come stai?"
    nao_animatedSayText(text_to_say)
    dialogo.append({"nao":text_to_say})
    response = nao_speech_to_text(5)
    dialogo.append({"umano":response})

    local_dialog.append(dialogo)

login = -1


# PAGINE WEB
@app.route("/", methods=['GET', 'POST'])
def login():
        
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
    

        # Verifica credenziali utente
        if username == "admin" and password == "admin":
            login = 1
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)


@app.route("/index", methods=['GET', 'POST'])
def index():
 if login == 1:
    if request.method == "POST":
        pagina = request.form.get("pagina")
        if pagina:
                return redirect(url_for(pagina))
    return render_template("index.html")
 else: 
    return redirect(url_for('login'))


@app.route('/analisi_morphcast', methods=['GET'])
def analisi_morphcast():
    if login == 1:
        return render_template('analisi_morphcast.html')
    else:
        return redirect(url_for('login'))

@app.route('/webcam', methods=['GET'])
def webcam():
    if login == 1:
        return Response(nao_generate_frames(face_detection), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return redirect(url_for('login'))

@app.route("/prodotto", methods=['GET', 'POST'])
def prodotto():
    if login == 1:
        return render_template("prodotto.html")
    else:
        return redirect(url_for('login'))

@app.route("/vendite")
def vendite():
    if login == 1:
        return render_template("vendite.html")
    else:
        return redirect(url_for('login'))

@app.route("/utenti")
def utenti():
    if login == 1:
        cliente = db_helper.get_cliente()
        count_cliente = db_helper.get_count_cliente()
        return render_template("utenti.html", cliente=cliente, count_cliente=count_cliente)
    else:
        return redirect(url_for('login'))

@app.route("/carrelli")
def carrelli():
    if login == 1:
        return render_template("carrelli.html")
    else:
        return redirect(url_for('login'))

@app.route("/scaffale")
def scaffale():
    if login == 1:
        return render_template("scaffale.html")
    else:
        return redirect(url_for('login'))

@app.route("/magazzino")
def magazzino():
    if login == 1:
        return render_template("magazzino.html")
    else:
        return redirect(url_for('login'))



# API
@app.route('/api', methods=['GET'])
def api():
    if login == 1:
        return render_template('api.html')
    else:
        return redirect(url_for('login'))


@app.route('/api/info', methods=['GET'])
def api_info():
    return jsonify({'code': 200, 'status': 'online', 'elapsed time': utilities.getElapsedTime(startTime)}), 200

@app.route('/api/audio_rec', methods=['GET'])
def api_audio_rec():
    return jsonify({'code': 200, 'status': 'online', 'recordings': local_rec}), 200


@app.route('/api/dialogo', methods=['GET'])
def api_dialogo():
    return jsonify({'code': 200, 'status': 'online', 'dialogo': local_dialog}), 200


@app.route('/api/morphcast', methods=['GET', 'POST'])
def api_morphcast():
    if request.method == 'GET':
        try:
            return jsonify({'code': 200, 'message': 'OK', 'data': local_db}), 200
        except Exception as e:
            logger.error(str(e))
            return jsonify({'code': 500, 'message': str(e)}), 500
    elif request.method == 'POST':
        try:
            dati = request.get_json()   

            # salvare dati nel DB e non in una variabile locale                                
            local_db.append(dati)

            # creare una funzione che analizzi i dati
            nao_animatedSayText("Hai " + str(dati['age']) + "anni e in questo momento sei: " + str(dati['emo_dom']))

            return jsonify({'code': 201, 'message': 'OK', 'data': dati}), 201                  
        except Exception as e:
            logger.error(str(e))
            return jsonify({'code': 500, 'message': str(e)}), 500




# SERVICES
@app.route('/services', methods=['GET'])
def services():
    if login == 1:
        return render_template('services.html')
    else:
        return redirect(url_for('login'))

# Servizio START morphcast
@app.route('/services/start_morphcast', methods=['GET'])
def services_start_morphcast():
    # Aprire il link nel browser predefinito
    try:
        global driver
        driver = webdriver.Chrome(path_drivers)
        driver.get("http://127.0.0.1:5010/analisi_morphcast")
        return jsonify({'code': 200, 'message': 'START morphcast'}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500


# Servizio STOP morphcast
@app.route('/services/stop_morphcast', methods=['GET'])
def services_stop_morphcast():
    # Chiudere il link nel browser predefinito
    try:
        driver.close()
        return jsonify({'code': 200, 'message': 'STOP morphcast'}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500


# Servizio START STOP dialogo
@app.route('/services/start_dialogo', methods=['GET'])
def services_start_dialogo():
    try:
        nao_dialog()
        return jsonify({'code': 200, 'message': 'dialogo completato', 'data':local_dialog}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500


'''
CODICI JSON
200 messaggio inviato
201 messaggio ricevuto
500 errore
'''


if __name__ == "__main__":
    startTime     = time.time()
    '''
    nao_volume_sound(60)
    nao_autonomous_life("disabled")
    nao_eye_white()
    nao_wakeup()
    nao_animatedSayText("Ciao sono Lesso, benvenuti al mio Riteil")
    nao_stand()
    if face_tracker:
        nao_face_tracker()
    else:
        nao_stop_face_tracker()
    '''
    app.run(host=config_helper.srv_host, port=config_helper.srv_port, debug=config_helper.srv_debug)


'''
TO DO
-dialogo con le funzioni Shenal
-db_helper con query
-decision tree Giacomo
-dashboard Edoardo: logout, login "sicuro" se cambio link
'''