from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_video():
    data = request.json
    youtube_url = data.get('url')
    
    if not youtube_url:
        return jsonify({"error": "Link nahi mila!"}), 400

    # यहाँ हम आगे चलकर yt-dlp और AI मॉडल्स जोड़ेंगे जो वीडियो काटेंगे
    print(f"Received URL: {youtube_url}")
    
    # अभी के लिए हम एक डमी सक्सेस रिस्पॉन्स भेज रहे हैं
    return jsonify({
        "status": "success",
        "message": "Video successfully queue mein lag gayi hai! AI clips jald hi taiyar hong jinfo."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
