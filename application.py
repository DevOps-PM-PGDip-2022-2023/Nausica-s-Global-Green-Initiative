from flask import Flask, render_template, redirect, request, session, make_response, jsonify
from flask_session import Session
from db_methods import *
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
application = app

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Nausicaas-Global-Green-Initiative API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route("/")
def main():
    if not session.get("name"):
        return redirect("/login")
    data = getall_grants()
    return render_template('userdetails.html', name=session.get("name"), role=session.get("role"), data=data)


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


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("name")
        print(search(username))
        if search(username):
            session["name"] = username
            session["role"] = getrole(username)
            return redirect("/")
        else:
            return redirect("/login")
    return render_template('login.html')

#admin routes

@app.route("/admin/main",methods=["GET"])
def admin_main():
    data = getall_grants()
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    return data

@app.route("/admin/user/add/<name>/<password>", methods=["POST"])
def admin_user_add(name,password):
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    register_user(name,password)
    return redirect("/")

@app.route("/admin/user/remove/<name>", methods=["POST"])
def admin_user_remove(name):
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    remove_user(name)
    return redirect("/")

@app.route("/admin/grant/add/<name>/<amount>/<site>", methods=["POST"])
def admin_grant_add(name,amount,site):
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    add_grant(name,amount,site)
    return redirect("/")

@app.route("/admin/grant/remove/<name>", methods=["POST"])
def admin_grant_remove(name):
    if not session.get("name"):
        return redirect("/login")
    if not session.get("role") == "admin":
        return redirect("/")
    remove_grant(name)
    return redirect("/")

@app.route("/datapull", methods=["GET"])
def datapull():
    if not session.get("name"):
        data = {"message":"bad request"}
        return make_response(jsonify(data), 500)
    data = getall_grants()
    return make_response(jsonify(data), 200)


if __name__ == "__main__":
    app.run(debug=True)
