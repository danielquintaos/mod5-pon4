from flask import render_template, request, jsonify
from app import app
from .models import get_all_logs, insert_log
from .dobot_controller import is_dobot_connected, send_command_to_dobot

@app.route('/')
def index():
    # Check if Dobot is connected
    dobot_connected = is_dobot_connected()
    return render_template('base.html', dobot_connected=dobot_connected)

@app.route('/dashboard')
def dashboard():
    logs = get_all_logs()
    return render_template('dashboard.html', logs=logs)

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/send-command', methods=['POST'])
def send_command():
    command = request.form.get('command')
    if command:
        insert_log({'command': command})  # Ensure to log the command as a dictionary
        success = send_command_to_dobot(command)  # Attempt to send the command to the Dobot
        if success:
            return jsonify({"status": "Success", "message": "Command sent successfully."})
        else:
            return jsonify({"status": "Error", "message": "Failed to send command to Dobot."})
    return jsonify({"status": "Error", "message": "No command provided."})
