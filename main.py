from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/webhook', methods=["GET", "POST"])
def webhook():
    print("webhook was hitted!")
    return jsonify({"message": "webhook was hitted"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
