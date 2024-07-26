from flask import Blueprint, jsonify, request
from discord_webhook import DiscordWebhook, DiscordEmbed

bp = Blueprint('embed', __name__, url_prefix='/api/webhook')

@bp.route('/send_embed', methods = ['GET', 'POST'])
def send_webhook_embed():
    data = request.get_json(force=True) # "force = true" it sucks, but it forces flask to parse the json without having the Content-Type

    webhook_url = data.get('webhook_url')
    webhook_username = data.get('webhook_username')
    embed_data = data.get('embed')
    
    if not embed_data or not all(key in embed_data for key in ('title', 'description', 'color')):
        return {'error': 'Invalid embed data. Required keys: title, description, color.'}, 400

    webhook = DiscordWebhook(url=webhook_url, username=webhook_username)
    
    embed = DiscordEmbed(
        title=embed_data['title'],
        description=embed_data['description'],
        color=embed_data['color']
    )
    webhook.add_embed(embed)
    
    response = webhook.execute()

    if response.status_code == 200:
        return jsonify({"status": "message sent"}), 200
    else:
        return jsonify({"error": "could not send message"}), 500