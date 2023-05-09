from flask import Flask

app = Flask(__name__)

@app.route("/")
def ph_ar():
    return"<p><a href="">PA</a></p>"
