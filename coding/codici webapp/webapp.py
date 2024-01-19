import psycopg2
from flask import Flask, request, redirect, url_for, render_template

myHost = "localhost"
myDB = "postgres"
myUser = "postgres"
myPasswd = "postgres"

conn = psycopg2.connect(host=myHost, database=myDB, user=myUser, password=myPasswd)

app = Flask(__name__)

# Pagina di login
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Verifica credenziali utente
        if username == "admin" and password == "admin":
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

# Pagina homepage (index)
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        pagina = request.form.get("pagina")
        if pagina:
            return redirect(url_for(pagina))
    
    return render_template("index.html")

# Pagina Pagina1
@app.route("/pagina1")
def pagina1():
    return render_template("prodotto.html")

# Pagina Pagina2
@app.route("/pagina2")
def pagina2():
    return render_template("prodotto.html")


@app.route("/vendite")
def vendite():
    return render_template("bilancio.html")

@app.route("/utenti")
def utenti():
    return render_template("utenti.html")


@app.route("/carrelli")
def carrelli():
    return render_template("carrelli.html")

@app.route("/scaffale")
def scaffale():
    return render_template("scaffale.html")

@app.route("/magazzino")
def magazzino():
    return render_template("magazzino.html")

# ... Altre pagine ...

if __name__ == "__main__":
    app.run(debug=True)