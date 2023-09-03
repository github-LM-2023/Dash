from flask import Falsk
app=Flask(__name__)
@app.route("/")
def home():
    return "<h2>Flask vercel</h2>"
