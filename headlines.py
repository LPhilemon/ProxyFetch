# from flask import render_template
# from flask import Flask

# app = Flask(__name__)
# @app.route("/")
# @app.route("/<publication>")
# def get_news(publication="bbc"):
#     feed = feedparser.parse(RSS_FEEDS[publication])
#     first_article = feed['entries'][0]
#     return render_template("home.html")
