from flask import Flask

app = Flask(__name__)

#todo: write security wrapper
@app.route("/")
def main():
    return render_template('index.html')


#todo: login method

#todo: write security wrapper
@app.route("/")
def main():
    return render_template('login.html')