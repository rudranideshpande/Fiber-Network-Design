from flask import Flask, request, jsonify, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/run', methods=['POST'])
def run_kruskal():
    data = request.json
    n = data['n']
    edges = data['edges']

    input_data = f"{n} {len(edges)}\n"
    for u, v, w in edges:
        input_data += f"{u} {v} {w}\n"

    result = subprocess.run(
        ["./kruskal"],   # Windows → "kruskal.exe"
        input=input_data,
        text=True,
        capture_output=True
    )

    return jsonify({"output": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)