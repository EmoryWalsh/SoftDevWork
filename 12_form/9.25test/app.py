from flask import Flask
from flask import render_template
from flask import request
import cgi

app = Flask(__name__)

@app.route("/")
def norm():
    print(app)
    return "normal"

@app.route("/form")
def form():
    return render_template("temp.html")

@app.route("/auth")
def authenticate():
    return "form handled"


if __name__ == "__main__":
    app.debug = True
    app.run()
