from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Azure Web App with Python 🚀"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # להרצה מקומית
    app.run(host="0.0.0.0", port=8000, debug=True)
