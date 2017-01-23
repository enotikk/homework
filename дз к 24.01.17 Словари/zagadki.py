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
     print(words)
     return words
def make_dict(words):
    d={}
    for i in range(0,len(words),2):
        d[words[i]] = words[i+1]
    return d

def interact(d):
    for k in d:
        dots = ''
        for i in range(len(k)):
                 dots = dots + '.'      
        print(d[k], dots)
        answer = input()
        if answer == k:
            print('Правильно!')
        else:
            print('Не угадал :(',d[k],k)

def main():
    filename = input('Введите имя файла: ')
    words = split_text(filename)
    d = make_dict(words)
    interact(d)
main()
