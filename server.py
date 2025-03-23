from flask import Flask, request
import base64

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "ESP-01 Image Upload Server is Running!"

@app.route("/upload", methods=["POST"])
def upload_image():
    try:
        image_data = request.form["image"]
        image_bytes = base64.b64decode(image_data)
        
        with open("captured_image.jpg", "wb") as f:
            f.write(image_bytes)
        
        return "Image uploaded successfully!", 200
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
