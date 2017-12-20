from flask import Flask, render_template, Markup, request
from weather import get_weather
from news_parser import parse, get_top
from ling import translate_text
from test import generate_q

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", weather=get_weather())

@app.route("/news")
def news():
    text = parse()
    text = translate_text(text)
    top = get_top(text)
    return render_template("news.html", text = Markup(text), top = top)

@app.route("/translate")
def translate():
    text = request.args['word']
    answer = translate_text(text)
    return render_template("answer.html", req=text, answer=Markup(answer))

@app.route("/test")
def test():
    way = 2
    if "answered" in request.args:
        if request.args['answered'] == "0":
            way = 0
        else:
            way = 1
    return render_template("test.html", q=generate_q(), way=way, Markup=Markup)

if __name__ == "__main__":
    app.run(port=84, debug=True)
