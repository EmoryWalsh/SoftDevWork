#Emory Walsh
#SoftDev1 pd1
#K25 -- Getting More REST
#2019-11-12

#prepares flask
from flask import Flask, render_template, request
from urllib.request import urlopen
import json

app = Flask(__name__) #create instance of class Flask

#normal route
@app.route("/") #assign following fxn to run when root route requested
def main():
    url = urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/437133")
    data = url.read()
    dict = json.loads(data)
    artist = dict["artistDisplayName"]
    artwork = dict["title"]
    year = dict["objectEndDate"]

    url = urlopen("https://api.agify.io/?name=Emory&country_id=US")
    data = url.read()
    dict = json.loads(data)
    count = dict["count"]
    name = dict["name"]
    country = dict["country_id"]

    url = urlopen("https://www.metaweather.com/api/location/search/?query=london")
    data = url.read()
    dict = json.loads(data)
    place = dict[0]["title"]
    type = dict[0]["location_type"]
    latlong = dict[0]["latt_long"]

    return render_template("tmplt.html",
                            artist = artist,
                            artwork = artwork,
                            year = year,
                            count = count,
                            name = name,
                            country = country,
                            place = place,
                            type = type,
                            latlong = latlong)

#main
if __name__ == "__main__":
    app.debug = True
    app.run()
