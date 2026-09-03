from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "mensagem": "Ola, este e o app do trabalho de CI/CD!",
        "host": socket.gethostname(),
        "versao": os.environ.get("APP_VERSION", "1.0.0")
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
