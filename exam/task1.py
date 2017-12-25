import os
import re
import json
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

def parser():
    dic = {}
    f = open('thai_letters.txt', 'r', encoding='utf-8')
    letters = f.read().split('\n')
#    print(letters)
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                with open(os.path.join(root, f), 'r', encoding='utf-8') as text:
                    text = clean_html(text.read())
                    sent = text.split('     ')
                    for i in sent:
                        if '&#' in i:
                            thai_word=i[:i.find('   ')]
                            if thai_word!='':
                                if thai_word[0] in letters:
                                    if thai_word not in dic:
                                        dic[thai_word]=i[i.find(';')+1:i.rfind('&#')]
#                    if f == '187.35.html':
#                        print(dic)
                                                 
    return dic

def make_json(d, filename):
    f = open(filename, 'w', encoding='utf-8')
    json.dump(d, f, ensure_ascii = False)
    f.close()

def inverse_dict(d):
    new_d={}
    for item in d.items():
        if item[1] not in new_d:
            new_d[item[1]]=[item[0],]
        else:
            new_d[item[1]].append(item[0])
    return new_d
        

d = parser()    
make_json(d,'data.json')
make_json(inverse_dict(d),'data1.json')
