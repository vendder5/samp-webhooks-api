from flask import Flask
from routes import embed, message

app = Flask(__name__)

app.register_blueprint(embed.bp)
app.register_blueprint(message.bp)

if __name__ == '__main__':
    app.run(debug=True)
