from flask import Flask
from flask import render_template
from flask import Response
import cv2 

app = Flask(__name__)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def generate():
    while True:
        ret, frame = cap.read()
        if ret: 
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle( frame, (x,y), (x + w, y + h), (0, 255,0), 2 )
                cv2.putText( frame,'DETECCION',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            if not flag:
                continue
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
                  bytearray(encodedImage) + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate(), 
            mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80 ,debug=False, threaded=True)

cap.release()
