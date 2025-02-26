from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"  # Rasa API endpoint

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    sender_id = request.json.get("sender", "user")  # Unique user ID

    # Send message to Rasa
    rasa_response = requests.post(RASA_URL, json={"sender": sender_id, "message": user_message})
    bot_reply = rasa_response.json()

    # Extract bot responses
    messages = [resp.get("text", "I didn't understand that.") for resp in bot_reply]
    return jsonify({"responses": messages})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
