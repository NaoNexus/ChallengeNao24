'''
python2 64 bit
pip install -r requirements.txt
python main.py
''' 

# Modules
from naoqi import ALProxy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask import Flask, render_template, Response, jsonify, request, redirect, url_for
from hashlib import md5, sha256
import cv2
import time
import numpy as np
import random
from selenium import webdriver
import paramiko
import os

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

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'
login_manager.session_protection = 'strong'


def make_md5(s):
    encoding = 'utf-8'
    return md5(s.encode(encoding)).hexdigest()


def make_sha256(s):
        encoding = 'utf-8'
        return sha256(s.encode(encoding)).hexdigest()


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
        logger.error(str(e))
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




# PAGINE WEB
# Per impedire all'utente di tornare indietro dopo aver fatto il logout
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

class User(UserMixin):
    def __init__(self, id = None, username = ''):
        self.id = id

users = {'1': {'id': '1', 'username': 'admin', 'password': '21232f297a57a5a743894a0e4a801fc3'}, #md5(admin)
         '2': {'id': '2', 'username': 'naonexus', 'password': '898d0dc0895b537fc1732a03cba7aff4'}} #md5(naonexus)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = make_md5(request.form["password"])

        # Verifica credenziali utente
        user = next((u for u in users.values() if u['username'] == username and u['password'] == password), None)
        if user:
            user_obj = User(user['id'])
            login_user(user_obj)
            return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == "POST":
        pagina = request.form.get("pagina")
        if pagina:
            return redirect(url_for(pagina))
    oggetto = db_helper.get_oggetto()
    return render_template("dashboard.html", oggetto=oggetto)


@app.route('/analisi_morphcast', methods=['GET'])
def analisi_morphcast():
    return render_template('analisi_morphcast.html')


@app.route('/webcam', methods=['GET'])
def webcam():
    return Response(nao_generate_frames(face_detection), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/prodotti", methods=['GET'])
@login_required
def prodotti():
    ordine_oggetto = db_helper.get_ordine_oggetto()
    return render_template("prodotti.html", ordine_oggetto=ordine_oggetto)


@app.route("/abbinamenti", methods=['GET'])
@login_required
def abbinamenti():
    oggetti = db_helper.get_oggetto()
    abbinamenti = db_helper.get_abbinamento()
    lista_oggetti = []
    for abb in abbinamenti:
        id_oggetto1 = db_helper.get_id_oggetto(abb['id_oggetto1'])
        id_oggetto2 = db_helper.get_id_oggetto(abb['id_oggetto2'])
        lista_oggetti.append({'id':abb['id'],'oggetto1':id_oggetto1,'oggetto2':id_oggetto2})
    return render_template("abbinamenti.html", oggetti=oggetti, lista_oggetti=lista_oggetti)


@app.route("/gestione_prodotto/<id>", methods=['GET'])
@login_required
def gestione_prodotto(id):
    if (id != None and id != ''):
        try:
            prodotto = db_helper.get_id_oggetto(id)
            return render_template('gestione_prodotto.html', prodotto=prodotto)
        except Exception as e:
            logger.error(str(e))
            return redirect("/dashboard", code=500)
    return redirect("/dashboard", code=500)


@app.route("/nuovo_prodotto", methods=['GET'])
@login_required
def nuovo_prodotto():
    prodotto = db_helper.get_id_oggetto(0)
    return render_template('gestione_prodotto.html', prodotto=prodotto)


@app.route("/vendite")
@login_required
def vendite():
    return render_template("vendite.html")


@app.route("/utenti")
@login_required
def utenti():
    cliente = db_helper.get_cliente()
    count_cliente = db_helper.get_count_cliente()
    return render_template("utenti.html", cliente=cliente, count_cliente=count_cliente)


@app.route("/gestione_utente/<id>", methods=['GET'])
@login_required
def gestione_utente(id):
    if (id != None and id != ''):
        try:
            cliente = db_helper.get_id_cliente(id)
            return render_template('gestione_utente.html', cliente=cliente)
        except Exception as e:
            logger.error(str(e))
            return redirect("/utenti", code=500)
    return redirect("/utenti", code=500)


@app.route("/nuovo_utente", methods=['GET'])
@login_required
def nuovo_utente():
    cliente = db_helper.get_id_cliente(0)
    return render_template('gestione_utente.html', cliente=cliente)
        

@app.route("/carrelli", methods=['GET'])
@login_required
def carrelli():
    carrello = db_helper.get_carrello()
    carrello_oggetto = db_helper.get_carrello_oggetto()
    result = []
    for item in carrello:
        key   = 'carrello'
        value = {'id':item['id']}
        oggetto = []
        for index in carrello_oggetto:
            if(item['id'] == index['carrello']['id']):
                oggetto.append(index['oggetto'])

            if(item['id_cliente'] == index['cliente']['id']):
                if('cliente' not in value):
                    value['cliente'] = index['cliente']

        value['oggetto'] = oggetto
        if (len(oggetto) > 0):
            result.append({key:value})
    carrello_oggetto = result
    count_carrello = 0
    for item in carrello_oggetto:
        totale_carrello = 0
        if(len(item['carrello']['oggetto']) != 0):
            count_carrello += 1
        for index in item['carrello']['oggetto']:
            totale_carrello += index['prezzo']
        item['carrello']['totale'] = totale_carrello
    return render_template("carrelli.html", carrello_oggetto=carrello_oggetto, count_carrello=count_carrello)


@app.route("/scaffale", methods=['GET'])
@login_required
def scaffale():
    oggetto = db_helper.get_oggetto()
    count_scaffale = 0
    for item in oggetto:
        count_scaffale += item['qta_scaffale']
    return render_template("scaffale.html", oggetto=oggetto, count_scaffale=count_scaffale)


@app.route("/magazzino", methods=['GET'])
@login_required
def magazzino():
    oggetto = db_helper.get_oggetto()
    count_magazzino = 0
    for item in oggetto:
        count_magazzino += item['qta_magazzino']
    return render_template("magazzino.html", oggetto=oggetto, count_magazzino=count_magazzino)




# API
@app.route('/api', methods=['GET'])
def api():
    return render_template('api.html')


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


@app.route('/api/utente/<id>', methods=['POST', 'DELETE'])
def api_utente(id):
    if (id != None and id != ''):
        if request.method == 'POST':
            try:
                username = request.form["username"]
                nome     = request.form["nome"]
                cognome  = request.form["cognome"]
                password = make_md5(request.form["password"])
                data     = db_helper.set_id_cliente(id,username,nome,cognome,password)
                return redirect("/utenti")  #return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_id_cliente(id,username,nome,cognome,password)}), 200
            except Exception as e:
                logger.error(str(e))
                return redirect("/utenti")  #return jsonify({'code': 500, 'message': str(e)}), 500
        elif request.method == 'DELETE':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.delete_cliente(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No id argument passed')
        return redirect("/utenti")          #return jsonify({'code': 500, 'message': 'No id was passed'}), 500


@app.route('/api/nuovo_utente', methods=['POST'])
def api_nuovo_utente():
    if request.method == 'POST':
        try:
            username = request.form["username"]
            nome     = request.form["nome"]
            cognome  = request.form["cognome"]
            password = make_md5(request.form["password"])
            data     = db_helper.set_cliente(username,nome,cognome,password)
            return redirect("/utenti")      #return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_cliente(username,nome,cognome,password)}), 200
        except Exception as e:
            logger.error(str(e))
            return redirect("/utenti")
    return redirect("/utenti")


@app.route('/api/prodotto/<id>', methods=['POST', 'DELETE'])
def api_prodotto(id):
    if (id != None and id != ''):
        if request.method == 'POST':
            try:
                titolo              = request.form["titolo"]
                categoria           = request.form["categoria"]
                prezzo              = request.form["prezzo"]
                descrizione         = request.form["descrizione"]
                foto                = request.form["foto"]
                qta_magazzino       = request.form["qta_magazzino"]
                qta_scaffale        = request.form["qta_scaffale"]
                sconto              = request.form["sconto"]
                eta_consigliata     = request.form["eta_consigliata"]
                sesso_consigliato   = request.form["sesso_consigliato"]
                data = db_helper.set_id_oggetto(id,titolo,categoria,prezzo,descrizione,foto,qta_magazzino,qta_scaffale,sconto,eta_consigliata,sesso_consigliato)
                return redirect("/dashboard")  #return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_id_oggetto(id,titolo,categoria,prezzo,descrizione,foto,qta_magazzino,qta_scaffale,sconto,eta_consigliata,sesso_consigliato)}), 200
            except Exception as e:
                logger.error(str(e))
                return redirect("/dashboard")  #return jsonify({'code': 500, 'message': str(e)}), 500
        elif request.method == 'DELETE':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.delete_oggetto(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No id argument passed')
        return redirect("/dashboard")          #return jsonify({'code': 500, 'message': 'No id was passed'}), 500


@app.route('/api/nuovo_prodotto', methods=['POST'])
def api_nuovo_prodotto():
    if request.method == 'POST':
        try:
            titolo              = request.form["titolo"]
            categoria           = request.form["categoria"]
            prezzo              = request.form["prezzo"]
            descrizione         = request.form["descrizione"]
            foto                = request.form["foto"]
            qta_magazzino       = request.form["qta_magazzino"]
            qta_scaffale        = request.form["qta_scaffale"]
            sconto              = request.form["sconto"]
            eta_consigliata     = request.form["eta_consigliata"]
            sesso_consigliato   = request.form["sesso_consigliato"]
            data = db_helper.set_oggetto(titolo,categoria,prezzo,descrizione,foto,qta_magazzino,qta_scaffale,sconto,eta_consigliata,sesso_consigliato)
            return redirect("/dashboard")      #return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_oggetto(titolo,categoria,prezzo,descrizione,foto,qta_magazzino,qta_scaffale,sconto,eta_consigliata,sesso_consigliato)}), 200
        except Exception as e:
            logger.error(str(e))
            return redirect("/dashboard")
    return redirect("/dashboard")


@app.route('/api/qta_scaffale/<id>', methods=['PLUS', 'MINUS'])
def api_qta_scaffale(id):
    if (id != None and id != ''):
        if request.method == 'PLUS':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_qta_scaffale_plus(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
        elif request.method == 'MINUS':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_qta_scaffale_minus(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No id argument passed')
        return jsonify({'code': 500, 'message': 'No id was passed'}), 500


@app.route('/api/qta_magazzino/<id>', methods=['PLUS', 'MINUS'])
def api_qta_magazzino(id):
    if (id != None and id != ''):
        if request.method == 'PLUS':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_qta_magazzino_plus(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
        elif request.method == 'MINUS':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.set_qta_magazzino_minus(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No id argument passed')
        return jsonify({'code': 500, 'message': 'No id was passed'}), 500


@app.route('/api/abbinamenti', methods=['POST'])
def api_abbinamenti():
    if request.method == 'POST':
        try:
            id_oggetto1 = request.form["productSelect1"]
            id_oggetto2 = request.form["productSelect2"]
            data = db_helper.set_abbinamento(id_oggetto1, id_oggetto2)
            return redirect("/abbinamenti")
        except Exception as e:
            logger.error(str(e))
            return redirect("/abbinamenti")
    return redirect("/abbinamenti")


@app.route('/api/delete_abbinamenti/<id>', methods=['DELETE'])
def api_delete_abbinamenti(id):
    if request.method == 'DELETE':
        try:
            data = db_helper.delete_abbinamento(id)
            return redirect("/abbinamenti")
        except Exception as e:
            logger.error(str(e))
            return redirect("/abbinamenti")
    return redirect("/abbinamenti")




# SERVICES
@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')

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
    app.secret_key = os.urandom(12)
    app.run(host=config_helper.srv_host, port=config_helper.srv_port, debug=config_helper.srv_debug)


'''
TO DO
-creare/cancellare carrello quando si crea/cancella utente
-decision tree: manca abbinamento + db
-report nao x scaffale e magazzino sotto una certa soglia (con dialogo nao)

-relazione: architettura MCV
'''