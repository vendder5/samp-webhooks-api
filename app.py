from flask import Flask
from routes.embed import embed_bp
from routes.message import message_bp

app = Flask(__name__)

app.register_blueprint(embed_bp)
app.register_blueprint(message_bp)

if __name__ == '__main__':
    app.run(debug=True)
