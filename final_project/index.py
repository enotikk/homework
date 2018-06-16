from flask import Flask, render_template, Markup, request
from my_parser import parse
from graph import graph_info

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyse")
def analyse():
    url = request.args['adress']
    text = parse(url)
    answer = graph_info(text)
    return render_template("answer.html", req=url, answer=Markup(answer))


if __name__ == "__main__":
    app.run(port=88, debug=True)
