import serial
import json
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import threading

ser = serial.Serial("COM7",115200)

app = Flask(__name__, static_folder="dashboard")
socketio = SocketIO(app)

@app.route("/")
def index():
    return send_from_directory("dashboard", "defect_dashboard.html")

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("dashboard/js", path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("dashboard/css", path)

@app.route("/images/<path:path>")
def send_img(path):
    return send_from_directory("dashboard/images", path)


def read_serial():

    while True:

        try:
            line = ser.readline().decode().strip()

            data = json.loads(line)

            socketio.emit("sensor_data", data)

        except:
            pass


thread = threading.Thread(target=read_serial)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    socketio.run(app, port=5000)