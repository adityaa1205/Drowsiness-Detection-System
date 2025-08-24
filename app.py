from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Drowsiness Detection Running on Render 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
