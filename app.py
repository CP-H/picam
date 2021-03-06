from flask import Flask, render_template, request, url_for, redirect, flash, Response, request
from camera import VideoCamera
from IR_Led import irLed


infraRedLED = irLed()
pi_camera = VideoCamera(flip=True) # flip pi camera if upside down.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/infraredSlide',methods=["GET","POST"])
def ir_slide():
    x = request.form.get('slide')
    infraRedLED.slide(int(x));
    return "None"

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
