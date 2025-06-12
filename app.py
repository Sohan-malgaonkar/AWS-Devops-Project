from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

posts = []

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    content = request.form.get("content")
    if title and content:
        posts.append({"title": title, "content": content})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
