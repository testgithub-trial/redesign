import time
import csv
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy, Model
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    #return render_template('index.html')
    return render_template('reVPC.html')

# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough
@app.route("/ncheck", methods=["GET", "POST"])
def ncheck():
    pass
@app.route("/vm", methods=["GET", "POST"])
def vm():
    pass
@app.route("/allhistroy", methods=["GET", "POST"])
def allhistroy():
    pass
@app.route("/logout", methods=["GET", "POST"])
def logout():
    pass
@app.route("/vpc", methods=["GET", "POST"])
def vpc():
    pass

@app.route("/feture", methods=["GET", "POST"])
def feture():
    fetmsg = 'See our  Feature Here...'
    fetmsg1 = '- U Can create u r VM Now'
    fetmsg2 = '- U Can create u r VPC'
    return render_template('fetCon.html',fetmsg=fetmsg,fetmsg1=fetmsg1,fetmsg2=fetmsg2)

@app.route("/id", methods=["GET", "POST"])
def id():
    conmsg = 'Contact @Tata Consultancy Services/Headquarters....'
    conmsg1 = '- Contact @TCS - Mumbai '
    conmsg2   =   '- TCS Mumbai (Nirmal) Registered Office'
    conmsg3   = '- Barrister Rajni Patel Marg, Nariman Point, Mumbai, Maharashtra 400021'

    return render_template('fetCon.html',conmsg=conmsg,conmsg1=conmsg1,conmsg2=conmsg2,conmsg3=conmsg3)
# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough# rough
if __name__ == "__main__":
    app.run(debug=True, port=46)