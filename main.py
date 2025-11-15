from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ✅ Reemplaza esto con tu TOKEN y CHAT_ID de Telegram
TELEGRAM_TOKEN = "7862504796:AAGMdA8GMfgTunmILPDRHYpDgA7BWWRvSDo"
CHAT_ID = "6136038577"

@app.route('/')
def home():
    return "🚀 Breakout Alert Bot activo - by Vanegas"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return {"status": "error", "message": "No JSON recibido"}, 400

    # Mensaje recibido desde TradingView
    message = data.get("message", "Sin mensaje")

    # Enviar mensaje a Telegram
    send_to_telegram(message)

    return {"status": "ok", "message_sent": message}, 200


def send_to_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("❌ Error al enviar a Telegram:", e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
