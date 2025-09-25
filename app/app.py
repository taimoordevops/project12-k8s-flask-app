from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"✅ Hello from Project 12 Kubernetes! Environment: {os.getenv('APP_ENV', 'dev')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)