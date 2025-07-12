from flask import Flask, request, jsonify
import requests
import random
from config import *

app = Flask(__name__)

def send_telegram_message(message):
    token = TELEGRAM_BOT_USERNAME.replace("@", "")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def place_trade(direction):
    amount_percent = random.randint(*TRADE_SIZE_PERCENT_RANGE)
    message = f"הבוט פותח עסקת {direction.upper()} בגודל של {amount_percent}% מהיתרה\nעם סטופ-לוס של {STOP_LOSS_PERCENT}% וטייק פרופיט של {TAKE_PROFIT_PERCENT}%"
    send_telegram_message(message)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'status': 'invalid data'}), 400

    msg = data['message'].lower()
    if "long" in msg:
        place_trade("long")
    elif "short" in msg:
        place_trade("short")
    else:
        return jsonify({'status': 'ignored'}), 200

    return jsonify({'status': 'executed'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
