from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Hello from Secure DevOps Pipeline!",
        "status": "running"
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok"
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # fixed security issue!
