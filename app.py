from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# JWT proxy
@app.route("/get_jwt")
def get_jwt():
    token = request.args.get("token")
    if not token:
        return "Error: token missing"
    try:
        url = f"https://access-token-to-jwt-token.onrender.com/rizer?access_token={token}"
        r = requests.get(url, timeout=15)
        return r.text
    except:
        return "Error: failed to fetch JWT"

# Bio proxy
@app.route("/set_bio")
def set_bio():
    bio = request.args.get("bio")
    jwt = request.args.get("jwt")
    if not jwt:
        return "Error: JWT missing"
    try:
        url = f"https://long-bio-api.onrender.com/bio_upload?bio={bio}&jwt={jwt}"
        r = requests.get(url, timeout=15)
        return r.text
    except:
        return "Error: failed to apply bio"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)