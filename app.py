from flask import Flask, jsonify
from datetime import datetime, timezone
import os
import socket

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
AUTOR = "Gabriel Bielick"


@app.route("/")
def home():
    """Rota principal — mensagem de boas-vindas do app."""
    return jsonify({
        "mensagem": "Olá, este é o app do trabalho de CI/CD!, Marcos Nielsen, vulgo Professor Mestre dos Magos",
        "autor": AUTOR,
        "host": socket.gethostname(),
        "versao": APP_VERSION,
    })


@app.route("/health")
def health():
    """Rota de health check — usada para monitoramento e testes automatizados."""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/info")
def info():
    """Rota extra — informações sobre o ambiente de execução."""
    return jsonify({
        "hostname": socket.gethostname(),
        "versao": APP_VERSION,
        "porta": os.environ.get("PORT", 8080),
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
