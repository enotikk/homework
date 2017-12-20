from urllib.request import urlopen
import re
from flask import Markup

link = "https://lenta.ru"

def clean_html(t):
    regTag = re.compile('<.*?>', re.DOTALL)
    regScript = re.compile('<script>.*?</script>', re.DOTALL)
    regComment = re.compile('<!--.*?-->', re.DOTALL)
    clean_t = regScript.sub("", t)
    clean_t = regComment.sub("", clean_t)
    clean_t = regTag.sub(" ", clean_t)
    clean_t = re.sub("(&quot;|&laquo;|&raquo;|&nbsp;|\n|\t)", " ", clean_t)
    clean_t = re.sub("&amp;", " ", clean_t)
    return clean_t.lower()

def parse():
    code = urlopen(link).read().decode("utf-8")
    text = clean_html(code)
    return text

def get_top(parsed):
    parsed = parsed.split()
    parsed = [n.strip(",.-;!?") for n in parsed]
    parsed = [n for n in parsed if len(re.findall("[а-яА-Я]+[\-\']*[а-яА-Я]*", n)) > 0]
    rate = {}
    for n in parsed:
        rate[n] = rate.get(n, 0) + 1
    li = list(rate.items())
    li.sort(key = lambda x: -x[1])
    return [Markup(n[0]) for n in li[:10]]
