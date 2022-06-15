#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, Response, request, redirect, url_for, render_template, json, render_template_string, jsonify, send_from_directory
from camera import VideoCamera
from IR_Led import irLed
import os

infraRedLED = irLed()
pi_camera = VideoCamera(flip=True) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"

# switch IR on/off
@app.route('/infrared')
def toggle_ir():
    infraRedLED.toggle()
    return "None"

# switch IR on/off
@app.route('/infraredSlide', methods=['GET', 'POST'])
def tune_ir():
    if request.method == 'POST':
        if request.form.get('slide'):
            intensity = request.form.get('slide')
            infraRedLED.slide(int(intensity))
            print(intensity)
            return "None"
        else:
            return "None"

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
