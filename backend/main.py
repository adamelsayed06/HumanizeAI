import json
from dotenv import load_dotenv
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

load_dotenv
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/humanized", methods=["POST"])
def humanize_text():
    data = request.json
    ai_text = data.get("aiText")

    if not ai_text:
        return jsonify({"error": "u gotta put in text bro"}), 400

    prompt = f"""

    """

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )

    print(completion.choices[0].message)

