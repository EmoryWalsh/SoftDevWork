from flask import Flask
from flask import render_template
from flask import request
import cgi

app = Flask(__name__)

head = """
Emory Walsh & Elizabeth Doss -- Flower Power
SoftDev1 pd1
K15 -- ?
2019-09-26
"""

@app.route("/")
def form():
    return render_template("temp.html",
                               header = head)
user = "mykolyk"
passw = "?"

@app.route("/auth")
def authenticate():
    print("/n/n/n")
    print("app: " + str(app))
    print("request: " + str(request))
    print("args: " + str(request.args))
    print(request.headers)
    username = request.args['username']
    password = request.args['password']
    if (username == user and password == passw):
        return render_template("authTemp.html",
                                username = request.args['username'],
                                password = request.args['password'])
    else:
        return render_template("authTempError.html",
                                username = request.args['username'],
                                password = request.args['password'])

if __name__ == "__main__":
    app.debug = True
    app.run()
