from string import ascii_lowercase

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session

app = Flask(__name__)
app.secret_key = "beseda"

@app.route("/")
def index():
    return render_template("domaca_stran.html")

@app.route("/vislice/<znak>")
def ugibaj(znak):
    if len(znak) == 1 and znak.isalpha():
        session["ugibal"] += znak
        if znak not in session ["beseda"]:
            session ["slika"] += 1
    return render_template("vislice.html", session=session, vse_crke=ascii_lowercase)

@app.route("/vislice")
def vislice():
    session ["beseda"] = "mojabeseda"
    session ["slika"] = 0
    session ["ugibal"] = ""
    return render_template("vislice.html", session=session, vse_crke=ascii_lowercase)

if __name__ == "__main__":
    app.run(host="0.0.0.0")