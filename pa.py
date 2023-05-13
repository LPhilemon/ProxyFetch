import feedparser

from flask import Flask
from flask import render_template
from flask import request

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

app = Flask(__name__)

# @app.route("/")
# def ():
#     return"<p><a href="">PA</a></p>"


@app.route("/", ['GET', 'POST'])
@app.route("/<publication>")
def get_ph_ar_news():
    query = request.form.get("publication")

    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
