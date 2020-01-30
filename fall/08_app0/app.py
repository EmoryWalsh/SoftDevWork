## Emory Walsh
##SoftDev1 pd1>
##K08 -- Lemme Flask You Sump’n
##2019-09-17    


from flask import Flask
app = Flask(__name__)

@app.route("/") #assign following fxn to run when route requested
def hello_world():
    print(__name__) #where will this go
    return "No hablo queso!"

@app.route("/em")
def emory():
    print("weeooooo")
    return "hello Emory"

@app.route("/ducky")
def broda():
    print("new route")
    return "Broda I am"

if __name__ == "__main__":
    app.debug = True
    app.run()
