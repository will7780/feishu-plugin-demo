from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def root():
    return "Feishu Plugin Server Running", 200

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data
    })

def handler(environ, start_response):
    return app(environ, start_response)

