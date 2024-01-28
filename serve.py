from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"])  # Run stress_cpu.py in a separate process
        return "Stress CPU script started!", 200
    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return f"Private IP address: {private_ip}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the server on port 80
