#Emory Walsh
#SoftDev1 pd1
#K24 -- A RESTful Journey Skyward
#2019-11-12

#prepares flask
from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__) #create instance of class Flask

def getStars():
    url = urlopen("https://api.nasa.gov/planetary/apod?api_key=75pcuZwFaaKindhBtxeK4vfGqbEVbgzRQbZU5g4s")
    data = url.read() #turns api data into a dictionary
    dict = json.loads(data)
    pic = dict["url"]
    print(pic)
    return pic



#normal route
@app.route("/") #assign following fxn to run when root route requested
def stars():
    return render_template("nasa.html",
                           pic = getStars())

#main
if __name__ == "__main__":
    app.debug = True
    app.run()
