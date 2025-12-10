from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Replace this with your real sensor/attendance data fetching logic
attendance_data = []
sensor_data = {"temperature": 0, "light": 0}

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API endpoint for RFID/facial recognition data
@app.route('/api/attendance', methods=['POST'])
def save_attendance():
    data = request.json
    attendance_data.append(data)
    return jsonify({"status": "success"})

# API endpoint to get latest attendance + sensor info
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "attendance": attendance_data,
        "sensors": sensor_data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
