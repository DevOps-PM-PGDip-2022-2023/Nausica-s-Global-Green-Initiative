from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from auth import search, getrole
from db_methods import *
from flask_swagger_ui import get_swaggerui_blueprint



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
    'app_name':'Green Giants'
    }

 )

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

@app.route("/")
def main():
    # data = getall_grants()
    data = {}
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html', name=session.get("name"), role=session.get("role"), data = data)

@app.route("/team")
def team():
    if not session.get("name"):
        return redirect("/login")
    return render_template('Teamdetails.html', name=session.get("name"), role=session.get("role"))

@app.route("/customer")
def customer():
    if not session.get("name"):
        return redirect("/login")
    return render_template('CustomerDetails.html', name=session.get("name"), role=session.get("role"))



@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username =  request.form.get("name")
        password =  request.form.get("password")
        session["name"] = username
        return redirect("/")
        # if search(username, password):
        #     session["name"] = username
        #     session["role"] = getrole(username, password)
        #     return redirect("/")
        # else:
        #     return redirect("/login")
    return render_template('login.html')

#admin routes

@app.route("/admin/main")
def admin_main():
    # data = getall_grants()
    data = {}
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    return data

@app.route("/admin/user/add")
def admin_user_add():
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    return render_template('CustomerDetails.html', name=session.get("name"), role=session.get("role"))

@app.route("/admin/user/remove")
def admin_user_remove():
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    return render_template('CustomerDetails.html', name=session.get("name"), role=session.get("role"))

@app.route("/admin/grant/add")
def admin_grant_add():
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    return render_template('CustomerDetails.html', name=session.get("name"), role=session.get("role"))

@app.route("/admin/grant/remove")
def admin_grant_remove():
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    return render_template('CustomerDetails.html', name=session.get("name"), role=session.get("role"))


if __name__ == "__main__":
    app.run(debug=True)
