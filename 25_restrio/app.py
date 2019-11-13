#Emory Walsh
#SoftDev1 pd1
#K25 -- Getting More REST
#2019-11-12

#prepares flask
from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__) #create instance of class Flask

def painting():
    url = urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/437133")
    data = url.read()
    dict = json.loads(data)
    artist = dict["artistAlphaSort"]
    return artist
#normal route
@app.route("/") #assign following fxn to run when root route requested
def main():
    return render_template("tmplt.html",
                            artist = painting())

#main
if __name__ == "__main__":
    app.debug = True
    app.run()
