from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

scanned = []
attendance_log = []

uid_to_usn = {
    "123ABC": "1RN24CS295",
    "456DEF": "1RN24CS244"
}

@app.route("/")
def home():
    return "Smart Attendance Server Running"

@app.route("/api/nfc_event", methods=["POST"])
def nfc_event():
    data = request.json
    uid = data.get("uid")
    scanned.append({"uid": uid, "ts": time.time()})
    return jsonify({"status": "ok", "received_uid": uid})

@app.route("/list")
def list_scanned():
    return jsonify(scanned)

@app.route("/map")
def map_data():
    return jsonify(uid_to_usn)

@app.route("/api/attendance", methods=["POST"])
def attendance_record():
    data = request.json
    attendance_log.append({
        "usn": data.get("usn"),
        "status": data.get("status"),
        "timestamp": time.time()
    })
    return jsonify({"status": "stored"})

@app.route("/attendance_log")
def attendance_logs():
    return jsonify(attendance_log)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
