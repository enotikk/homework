import re
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

def naity(words):
    regex = 'на((ш((е|ё)л|ла|ло|едш(ий|его|ему|им|ем|ая|ей|ую|ее|ие|их|ими)))|(йд(ут?|ё(м|шь|те?)|и(те)?|ен(н(ый|ого|ому?|ая|ой|ую|ою|ое|ые|ых|ыми?)|о|а|ы)?)))'
    for word in words:
        m = re.match(regex, word)
        if m != None:
            print(word)


def main():
    filename = input('Введите имя файла: ') 
    w  = split_text (filename)
    naity(w)

main()
        
