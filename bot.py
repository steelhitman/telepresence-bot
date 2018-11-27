from flask import Flask, render_template, Response,stream_with_context,request,json,jsonify
from camera import VideoCamera
#from audio_get import *
import socket               # Import socket module

app = Flask(__name__)
ip='192.168.100.2:8080'
@app.route('/')
def index():
    return render_template('bot.html',ip=ip)

@app.route('/feed', methods=['POST'])
def feed():
	global text
	feedback=text
	return json.dumps("feedback");

def gen(camera):
	try:
		while True:
			frame = camera.get_frame()
			yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
	except:
		pass

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)