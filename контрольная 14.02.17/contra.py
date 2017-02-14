import re 

def f1(fname):
    f = open(fname, 'r', encoding='utf-8')
    strings = 0
    for line in f:
        strings += 1
    f.close()
    f = open('result1.txt', 'w', encoding='utf-8')
    f.write(str(strings))
    f.close()

def f2(fname):
    f = open(fname, 'r', encoding='utf-8')
    d = {}
    for line in f:
        if '<w lemma=' in line:
            key = line[line.find('type')+6: line.find('>')-1]
            if key in d:
                d[key] +=1
            else: d.update({key:1})
    f.close()
    f = open('result2.txt', 'w', encoding='utf-8')
    for key in sorted(d):
        f.write(key+'\n')
    f.close()
    return d


def f3(d):
    f = open('corpus.txt', 'r', encoding='utf-8')
    fr = open('result3.txt', 'w', encoding='utf-8')
    regex = 'type="l.f.*?"'
    for line in f:
        if '<w lemma=' in line:
            m = re.search(regex, line)
            if m != None:
                razbor = m.group()[m.group().find('"')+1:-1]
                fr.write(razbor+' - '+str(d[razbor])+'\n')
                

def f4(fname):
    f = open('corp.csv', 'r', encoding='utf-8')
    fr = open('result3a.txt', 'w', encoding='utf-8')
    for line in f:
        if '<w lemma=' in line:
            s = re.sub('<w lemma="(.*?)" type="(.*?)">(.*?)</w>', '\\1, \\2, \\3',line)
            fr.write(s+'\n')


    
def main():
    f1('corpus.txt')
    d = f2('corpus.txt')
    f3(d)
    f4('corp.csv')


main()
    
    
