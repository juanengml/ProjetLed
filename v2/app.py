
import paho.mqtt.client as mqtt
from flask import Flask
from flask import render_template, request,url_for
 
app = Flask(__name__, static_url_path='/static')

client = mqtt.Client()
# conecta no broker
client.connect("192.168.100.10", 1883)


 
@app.route("/")

def index():
    return render_template('index.html')

@app.route('/led1-ON')
def left_side():
   data1="led1-ON"
   print data1
   client.publish("/led1/","1")

   return 'true'
 
@app.route('/led1-OFF')
def right_side():
   data1="led1-OFF"
   print data1
   client.publish("/led1/","0")
   return 'true'
 
if __name__ == "__main__":
 print "Start"
 app.run(host='0.0.0.0',port=80,debug=True)



