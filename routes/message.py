from flask import Blueprint, jsonify, request
from discord_webhook import DiscordWebhook

bp = Blueprint('message', __name__, url_prefix='/api/webhook')

@bp.route('/send_message', methods = ['GET', 'POST'])
def send_webhook_message():
    data = request.get_json(force=True) # "force = true" it sucks, but it forces flask to parse the json without having the Content-Type

    webhook_url = data.get('webhook_url')
    webhook_username = data.get('webhook_username')
    message = data.get('message')
    
    webhook = DiscordWebhook(
        url=webhook_url,
        username=webhook_username,
        content=message
    )
    
    response = webhook.execute()

    if response.status_code == 200:
        return jsonify({"status": "message sent"}), 200
    else:
        return jsonify({"error": "could not send message"}), 500