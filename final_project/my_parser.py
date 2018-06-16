from urllib.request import urlopen
import urllib.request
from urllib.parse import quote
import re
from flask import Markup


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

def parse(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       code = response.read().decode('utf-8')
    text = clean_html(code)
    return text
