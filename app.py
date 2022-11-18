from flask import Flask, render_template, request
from extractor import extract_video_data_from_url
from settings import FEATURES, FAQS

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", features=FEATURES, faqs=FAQS)


@app.route("/download", methods=["POST"])
def download():
    video_url = request.form["video_url"]
    video_data = extract_video_data_from_url(video_url)
    title = video_data["title"]
    thumbnail = video_data["thumbnail"]
    formats = video_data["formats"]
    return render_template("download.html",
                           title=title,
                           thumbnail=thumbnail,
                           formats=formats,
                           features=FEATURES,
                           faqs=FAQS)


if __name__ == "__main__":
    app.run(debug=True)
