from flask import Flask, request
import requests

# 🔹 ДАННЫЕ ДЛЯ ТЕЛЕГРАМА
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_chat_id"

app = Flask(__name__)

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

@app.route("/google-chat-webhook", methods=["POST"])
def google_chat_webhook():
    data = request.json
    if "message" in data:
        user = data.get("user", {}).get("displayName", "Неизвестный пользователь")
        message = data["message"]
        chat_name = data.get("space", {}).get("displayName", "Неизвестный чат")
        
        telegram_text = f"📢 [Чат: {chat_name}]\n👤 {user}: {message}"
        send_telegram_message(telegram_text)
    
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
