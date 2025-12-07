import os
from flask import Flask

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
APP_NAME = os.getenv("APP_NAME", "MyApp")

@app.route("/")
def index():
    return f"{APP_NAME} is running in {APP_ENV} mode 🚀"

@app.route("/secret")
def secret():
    return f"Secret key is: {SECRET_KEY}"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
