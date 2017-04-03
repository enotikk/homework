def split_text(filename): 
     f = open(filename, 'r', encoding='utf-8') 
     words = [] 
     s = f.read() 
     a = s.split() 
     for word in a: 
         word = word.strip() 
         word = word.lower() 
         words.append(word.strip(',.!?"«»()-:;/\|“—”')) 
     f.close() 
     return words

def word_count(words):
    wordcount = {}
    for word in words:
        if word not in wordcount:
            wordcount[word] = words.index(word)
    return wordcount
        

def printinfile(dic):
    f = open('result.tsv', 'w', encoding='utf-8')
    for word in sorted(dic):
        f.write(word+'\t'+str(dic[word])+'\n')
    return
def main():
    filename = 'gnv.txt' 
    words  = split_text (filename)
    wordcount = word_count(words)
    printinfile(wordcount)
main()
