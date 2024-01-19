from flask import Flask, request, redirect, url_for, render_template

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

# Pagine per i singoli pulsanti
@app.route("/prodotto", methods=['GET', 'POST'])
def prodotto():
    return render_template("prodotto.html")

@app.route("/pagina1", methods=['GET', 'POST'])
def pagina1():
    return render_template("pagina1.html")

@app.route("/pagina2", methods=['GET', 'POST'])
def pagina2():
    return render_template("pagina2.html")

@app.route("/vendite")
def vendite():
    return render_template("vendite.html")

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

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)
