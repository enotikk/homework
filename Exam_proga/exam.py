import os
def split_text(filename):
    f = open(filename, 'r', encoding='ANSI')
    words = []
    s = f.read()
    a = s.split()
    for word in a:
        if '<w>' in word:
            word = word.strip()
            word = word.lower()
            words.append(word.strip(',.!?"()-:;/\|'))
    f.close()
    return words

def task1():
    res1 = open('res1.txt','w',encoding='utf-8')
    for root, dirs, files in os.walk('news'):
        for f in files:
            f1 = open('news/'+f, 'r', encoding=None)
            words = []
            s = f1.read()
            a = s.split()
            for word in a:
                if '<w>' in word:
                    words.append(word)
            res1.write(f+'  '+str(len(words))+'\n')
    res1.close()

def bigram(f):
    f1 = open('news/'+f, 'r', encoding=None)
    res3 = open('res3.txt','w',encoding='utf-8')
    file = f1.read()
    ares = []
    s = file.split('se>')
    for sen in s:
        w = sen.split('w>')
        cont = ''
        for word in w:
            cont = cont+word[word.rfind('>')+1:word.rfind('</')].strip('\n')+' '
        cont = cont+'\n'
        for i in range(len(w)-2):
            if 'gr="A' in w[i] and 'gen' in w[i]:
                if 'gr="S' in w[i+2] and 'gen' in w[i+2]:
                    res = w[i+2][w[i+2].rfind('>')+1:w[i+2].rfind('</')]+'  '+cont
                    res = w[i][w[i].rfind('>')+1:w[i].rfind('</')]+'  '+res
                    ares.append(res)
                    res3.write(res)
                    res = ''
    return ares

def task3():
    res3 = open('res3.txt','w',encoding='utf-8')
    string = ''
    for root, dirs, files in os.walk('news'):
        for f in files:
            for srting in bigram(f):
                res3.write(string)
    res3.close()

def main():
    task1()
    task3()

main()
    
    
                    
                    
                
                
    
