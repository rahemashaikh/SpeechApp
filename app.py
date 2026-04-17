from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files['audio']

    with open("temp.mp3", "wb") as f:
        f.write(audio.read())

    with open("temp.mp3", "rb") as f:
        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )

    os.remove("temp.mp3")

    return jsonify({"text": result.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)