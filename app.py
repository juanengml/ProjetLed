#!/usr/bin/python

from flask import Flask, request,render_template

import serial 

app = Flask(__name__)
try:
 try:   # crie um serial na porta ACM0
  ser = serial.Serial("/dev/ttyACM0",9600)
  status = True
 except: # crie um serial na porta ACM1
  ser = serial.Serial("/dev/ttyACM1",9600)
  status = True
except:
  status = False
global msg
@app.route("/",methods=["GET","POST"])  
def index():
  if request.method == "POST":
     if request.form['submit'] == "ON":
         print "Ligar Luz"
         # send comand RUN to robot 
         if status:
           ser.write("l")
           #msg = ser.readline()[0:-2]
         else:
            print "No Send comand "   
     elif request.form['submit'] == "OFF":
         print 'Desligar Luz'  	  
         # send comand BACK to robot 
         if status:
           ser.write("d")
           #msg = ser.readline()[0:-2]
         else:
            print "No Send comand "   
         
   
  return render_template('index.html')
  
  
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)  