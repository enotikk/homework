import sqlite3
conn = sqlite3.connect('hittite.db')
c = conn.cursor()
conn = sqlite3.connect('my.db')
q = conn.cursor()
q1 = conn.cursor()
q.execute('DROP TABLE IF EXISTS words')
q.execute("CREATE TABLE IF NOT EXISTS words(id INTEGER PRIMARY KEY, Lemma TEXT, Wordform TEXT, Glosses TEXT)")
for row in c.execute('SELECT * FROM wordforms'):
    q.execute("INSERT INTO words (Lemma, Wordform, Glosses) VALUES (?,?,?)", row)
q.execute('DROP TABLE IF EXISTS glosses')
q.execute("CREATE TABLE IF NOT EXISTS glosses(id INTEGER PRIMARY KEY, name TEXT, meanings TEXT)")
filename = 'glossing_rules.txt'
f = open(filename, 'r', encoding='utf-8')
dic = {}
g_list = []
for s in f.readlines():
    if '\ufeff' in s:
        s = s[1:]
    dic[s[0:s.find(' ')]]= s[s.find(' ')+3:-1]
    
for pair in dic.items():
    q.execute("INSERT INTO glosses (name, meanings) VALUES (?,?)", pair)
    g_list.append(pair[0])
q.execute('DROP TABLE IF EXISTS words_glosses')
q.execute("CREATE TABLE IF NOT EXISTS words_glosses(id_of_word INTEGER, id_of_gloss INTEGER)")
for row in q.execute('SELECT id, Glosses FROM words'):
    a = str(row[1]).split('.')
    for gloss in a:
        if gloss in dic:
            gloss_id = g_list.index(gloss)+1
            q1.execute("INSERT INTO words_glosses (id_of_word, id_of_gloss) VALUES (?,?)", (row[0], gloss_id))
    
#PART 2
           
import matplotlib
import matplotlib.pyplot as plt
import seaborn
wordcount = {}
for row in q.execute('SELECT * FROM words_glosses'):
    gloss = g_list[row[1]-1]
    if gloss not in wordcount:
            wordcount[gloss] = 1
    else:
        wordcount[gloss] +=1
dots = []
Y = []
X = []
n = 1
for word in sorted(wordcount):
    dots.append(word)
    Y.append(wordcount[word])
    X.append(n)
    n+=1
for x, y, d in zip(X, Y, dots):
    plt.scatter(x, y, marker='o', s=100)
    plt.text(x+0.1, y+0.1, d)
plt.ylabel('Количество глосс')
plt.show()
    


