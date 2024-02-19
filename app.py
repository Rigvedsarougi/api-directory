from flask import Flask, request, jsonify
from io import BytesIO
from app_functions import process_audio_files

app = Flask(__name__)

@app.route('/audio-fraud-detection', methods=['GET'])
def audio_fraud_detection():
    if 'audio_files' not in request.files:
        return jsonify({"error": "No audio files uploaded"}), 400
    
    audio_files = request.files.getlist('audio_files')
    
    keywords = [
        'Global',
        'HANA',
        'Server',
        'Software'
    ]

    results = process_audio_files(audio_files, keywords)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
