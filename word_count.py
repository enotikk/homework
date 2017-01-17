def split_text(filename): 
     f = open(filename, 'r', encoding='utf-8') 
     words = [] 
     s = f.read() 
     a = s.split() 
     for word in a: 
         word = word.strip() 
         word = word.lower() 
         words.append(word.strip(',.!?"()-:;/\|“—”')) 
     f.close() 
     return words

def word_count(words):
    wordcount = {}
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] +=1
    for word in sorted(wordcount):
        if wordcount[word]>10:
            print(word, wordcount[word])
    return wordcount
def main():
    filename = input('Введите имя файла: ') 
    w  = split_text (filename)
    freq = word_count(w)
main()
