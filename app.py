
import os
import sys
import subprocess
import json
import platform
import urllib.request
import zipfile
import tarfile
import time
import shutil
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_FILE = 'tunnels.json'
active_processes = {}

def get_ngrok_bin():
    global_path = shutil.which("ngrok")
    if global_path:
        return global_path
    return 'ngrok.exe' if platform.system() == 'Windows' else './ngrok'

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    bin_path = get_ngrok_bin()
    installed = shutil.which("ngrok") is not None or os.path.exists(bin_path)
    return jsonify({"installed": installed})

@app.route('/api/install', methods=['POST'])
def install():
    sys_name = platform.system()
    bin_path = 'ngrok.exe' if sys_name == 'Windows' else './ngrok'
    
    if sys_name == 'Windows':
        url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"
        filename = "ngrok.zip"
    elif sys_name == 'Linux':
        url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"
        filename = "ngrok.tgz"
    elif sys_name == 'Darwin':
        url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.zip"
        filename = "ngrok.zip"
    else:
        return jsonify({"error": "Unsupported OS"}), 400

    try:
        urllib.request.urlretrieve(url, filename)
        if filename.endswith('.zip'):
            with zipfile.ZipFile(filename, 'r') as z:
                z.extractall('.')
        else:
            with tarfile.open(filename, 'r:gz') as t:
                t.extractall('.')
        os.remove(filename)
        if sys_name != 'Windows':
            os.chmod(bin_path, 0o755)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/auth', methods=['POST'])
def auth():
    token = request.json.get('token')
    if not token:
        return jsonify({"error": "Missing token"}), 400
    try:
        subprocess.run([get_ngrok_bin(), "config", "add-authtoken", token], check=True)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tunnels', methods=['GET'])
def get_tunnels():
    tunnels = load_db()
    for t in tunnels:
        t['status'] = 'running' if t['id'] in active_processes else 'stopped'
        t['url'] = active_processes.get(t['id'], {}).get('url', '')
    return jsonify(tunnels)

@app.route('/api/tunnels', methods=['POST'])
def add_tunnel():
    data = request.json
    tunnels = load_db()
    new_tunnel = {
        "id": str(int(time.time())),
        "name": data.get("name"),
        "protocol": data.get("protocol"),
        "port": data.get("port")
    }
    tunnels.append(new_tunnel)
    save_db(tunnels)
    return jsonify(new_tunnel)

@app.route('/api/tunnels/<tid>', methods=['DELETE'])
def delete_tunnel(tid):
    if tid in active_processes:
        stop_tunnel_internal(tid)
    tunnels = load_db()
    tunnels = [t for t in tunnels if t['id'] != tid]
    save_db(tunnels)
    return jsonify({"success": True})

@app.route('/api/tunnels/<tid>/start', methods=['POST'])
def start_tunnel(tid):
    tunnels = load_db()
    tunnel = next((t for t in tunnels if t['id'] == tid), None)
    if not tunnel:
        return jsonify({"error": "Not found"}), 404
        
    if tid in active_processes:
        return jsonify({"error": "Already running"}), 400

    cmd = [get_ngrok_bin(), tunnel['protocol'], str(tunnel['port'])]
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    time.sleep(2)
    
    try:
        req = urllib.request.Request("http://127.0.0.1:4040/api/tunnels")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            public_url = ""
            for t in data.get('tunnels', []):
                if str(tunnel['port']) in t.get('config', {}).get('addr', ''):
                    public_url = t.get('public_url')
                    break
            
            if public_url:
                active_processes[tid] = {"process": p, "url": public_url}
                return jsonify({"success": True, "url": public_url})
            else:
                p.terminate()
                return jsonify({"error": "No URL returned"}), 500
    except Exception as e:
        p.terminate()
        return jsonify({"error": str(e)}), 500

@app.route('/api/tunnels/<tid>/stop', methods=['POST'])
def stop_tunnel(tid):
    return stop_tunnel_internal(tid)

def stop_tunnel_internal(tid):
    if tid in active_processes:
        p = active_processes[tid]['process']
        p.terminate()
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            p.kill()
        del active_processes[tid]
        return jsonify({"success": True})
    return jsonify({"error": "Not running"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
