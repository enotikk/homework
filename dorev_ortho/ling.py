from json import loads
import re
# from pymystem3 import Mystem
import os
from flask import Markup

def needs_yat(lemma):
    v = lemma.split("|")
    for n in v:
        if "ед" in n:
            if "дат" in n or "пр" in n:
                return True
    return False

def change_aend(adj):
    changes = {"iе": "iя", "іе": "iя", "ые": "ыя", "iеся":  "iяся"}
    for change in changes:
        if adj[-len(change):] == change:
            adj = adj[:-len(change)] + changes[change]
    return adj

def ortho(lemma, this_one, next_one):
    word = lemma.split("=")[0]
    glas = ['а','о','и','е','ы','у','я','ю','ё','э','й']
    if needs_yat(lemma):
        word += "&#1122;"
    if word[-1:] not in glas+["ь", "ъ", " ", "\n"] and not word.endswith("&#1122;"):
        word = word + 'ъ'
    if 'и' in word:
        pos = word.find('и')
        while pos<len(word)-1:
            if word[pos+1] in glas:
                word=word[:pos]+'i'+word[pos+1:]
            pos = word.find('и', pos+1)
            if pos == -1:
                break
    for n in ["через", "чрез", "без"]:
        if word.startswith(n[:-1]+"с"):
            word = word.replace(n[:-1]+"с", n)
    if "=A" in this_one['lemma']:
        if "жен" in next_one['lemma'] or "сред" in next_one['lemma']:
            word = change_aend(word)
    return word

def load_data():
    with open("data.txt", "r", encoding="utf-8") as f:
        return loads(f.read())

def translate(word):
    data = load_data()
    return data.get(word.lower().split(",")[0].strip(), ortho(word))

def is_rus_word(word):
    r = re.findall("[а-яА-Я\-]+", word)
    if len(r) == 1 and r[0] == word:
        return True
    else:
        return False

def get_from_data(key, data):
    if key.capitalize() in data:
        a = data[key.capitalize()]
    elif key.lower() in data:
        a = data[key.lower()]
    else:
        a = key
    return a.split(",")[0].split(" ")[0].strip("?") + "      "

def compare_to_slovar(word, lemma_word, data):
    dif = []
    for letter in range(len(word)):
        if letter >= len(lemma_word) or word[letter] != lemma_word[letter]:
            dif.append(letter)
    dorev = get_from_data(lemma_word, data)
    unis = re.findall("&[^;]+;", dorev)
    alternatives = ["A", "B", "C", "D", "E", "F"]
    alter_uni = {}
    for uni in unis:
        alter_uni[alternatives[-1]] = uni
        dorev = re.sub(uni, alternatives[-1], dorev)
        alternatives.pop(-1)
    dorev = dorev[:len(word)]
    for letter in dif:
        dorev = dorev[:letter] + word[letter] + dorev[letter+1:]
    for alter in alter_uni:
        dorev = re.sub(alter, alter_uni[alter], dorev)
    return dorev.strip()

def translate_text(text):
    li = lemmatize(text)
    data = load_data()
    new = []
    for di in li:
        lemma = di['lemma']
        lemma_word = lemma.split("=")[0]
        if is_rus_word(di['word']):
            slovar = compare_to_slovar(di['word'], lemma_word, data)
            next_word = False
            if not li.index(di)+1 >= len(li):
                next_word = li[li.index(di) + 1]
            translated = ortho(slovar, di, next_word)
            new.append(translated)
    return " ".join(new)

def lemmatize(text):
    with open("input.txt", "w", encoding='utf-8') as f:
        f.write(text)
    os.system(r"mystem.exe -i input.txt output.txt")
    with open("output.txt", "r", encoding='utf-8') as f:
        s = f.read()
    regLem = re.compile('([^{]+{.*?)}', re.DOTALL)
    li = regLem.findall(s)
    result = []
    for n in li:
        result.append({"lemma": n.split("{")[-1], "word": n.split("{")[0]})
    return result

