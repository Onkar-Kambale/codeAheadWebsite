import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Sample video data
featured_videos = [
    {
        "title": "The Last Journey",
        "thumbnail": "https://img.youtube.com/vi/LXb3EKWsInQ/maxresdefault.jpg",  # New thumbnail
        "views": "1.2M",
        "duration": "15:24"
    },
    {
        "title": "City Lights",
        "thumbnail": "https://img.youtube.com/vi/9bZkp7q19f0/maxresdefault.jpg",  # New thumbnail
        "views": "856K",
        "duration": "12:10"
    },
    {
        "title": "Mountain Echo",
        "thumbnail": "https://img.youtube.com/vi/tgbNymZ7vqY/maxresdefault.jpg",  # New thumbnail
        "views": "2.1M",
        "duration": "18:45"
    }
]

team_members = [
    {
        "name": "John Director",
        "role": "Creative Director",
        "image": "https://images.unsplash.com/photo-1633459947987-a32b39bc3875"
    },
    {
        "name": "Sarah Editor",
        "role": "Lead Editor",
        "image": "https://images.unsplash.com/photo-1633631986345-1d1bcaaa54bf"
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                         featured_videos=featured_videos,
                         team_members=team_members)
