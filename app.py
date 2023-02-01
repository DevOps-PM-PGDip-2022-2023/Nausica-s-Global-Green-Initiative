from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from auth import search
from db_methods import *



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def main():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')

@app.route("/team")
def team():
    if not session.get("name"):
        return redirect("/login")
    return render_template('Teamdetails.html')

@app.route("/customer")
def customer():
    if not session.get("name"):
        return redirect("/login")
    return render_template('CustomerDetails.html')



@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username =  request.form.get("name")
        password =  request.form.get("password")
        if search(username, password):
            session["name"] = username
            return redirect("/")
        else:
            return redirect("/login")
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)
