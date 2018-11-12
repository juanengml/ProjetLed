
import paho.mqtt.client as mqtt
from flask import Flask
from flask import render_template, request,url_for
 
app = Flask(__name__, static_url_path='/static')

client = mqtt.Client()
# conecta no broker
client.connect("192.168.100.3", 1883)


 
@app.route("/")
def index():
    file = open("data.txt","r").read().split("\n")[0].split(" ")[1]
    data = {"lampada",file}
    return render_template('index.html',data=data)

@app.route('/led1-ON')
def left_side():
   file = open("data.txt","w")
   print "led1-ON" 
   client.publish("/led1/","1")
    
   file.write("Lampada 1")
   file.close()
   return "True"

 
@app.route('/led1-OFF')
def right_side():
   file = open("data.txt","w")
   print "led1-OFF"
   client.publish("/led1/","0")
   file.write("Lampada 0")
   file.close() 
   return "false"
 
if __name__ == "__main__":
 print "Start"

 app.run(host='0.0.0.0',port=80,debug=True)



