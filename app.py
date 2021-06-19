from flask import Flask, render_template
from flask_session import Session

#configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

"""Fill video links in video_urls = [] Note: will render as many videos as you fill, eg. 100 links means 100 videos streaming at once """


@app.route("/")
def index():
    video_urls = ['https://www.youtube.com/embed/lwN4-W1WR84', 'https://www.youtube.com/embed/VrKW58MS12g', 'https://www.youtube.com/embed/pEme5AO-SpA', 'https://www.youtube.com/embed/vVlEVRKv4is']
    return render_template("index.html", video_urls=video_urls)



