from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def test():
    try:
        with open("data/links.txt", "r") as f_link:
            links = f_link.readlines()
        with open("data/titles.txt", "r") as f_title:
            titles = f_title.readlines()
        if request.method == "GET":
            return render_template("home.html", links= links, titles = titles)
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)