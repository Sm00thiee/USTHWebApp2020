from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods = ["GET"])
@app.route('/<int:page>', methods=["GET"])
def home(page=1):
    try:
        with open("data/links.txt", "r") as f_link:
            links = f_link.readlines()
        with open("data/titles.txt", "r") as f_title:
            titles = f_title.readlines()
        if request.method == "GET":
            pages = int(len(titles)/9) +1
            return render_template("home.html", links= links, titles = titles, page=page, pages= pages)
    except:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)