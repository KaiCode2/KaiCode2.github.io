from flask import Flask, render_template, url_for
from post import Post
from posts import posts

PORT = 443
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'yudrfyshumqfbnivests'

@app.route('/')
def home():
    latest = posts[-5:]
    return render_template("index.html", posts=latest)

@app.route('/posts/')
def blogPosts():
    return render_template("posts.html", posts=posts)

@app.route('/posts/<name>')
def blogPost(name):
    return render_template("Posts/" + name + ".html")

if __name__ == '__main__':
	app.run(host=HOST, port=PORT)
