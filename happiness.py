def split_text(filename):
    f = open(filename, 'r', encoding='utf-8')
    words = []
    s = f.read()
    a = s.split()
    for word in a:
        word = word.strip()
        word = word.lower()
        words.append(word.strip(',.!?"()-:;/\|'))
    f.close()
    return words

def ness(words):
    pattern = []
    count = []
    for word in words:
        flag = False
        if word[-4:] == 'ness':
            for p in range(len(pattern)):
                if word == pattern[p]:
                    flag = True
                    count[p] += 1
            if flag == False:
                pattern.append(word)
                count.append(1)
    m = 0
    imax = 0
    for i in range(len(count)):
        if count[i] > m:
            m = count[i]
            imax = i
    print (len(pattern),'существительных в тексте имеют суффикс -ness.')
    print (pattern[imax], '- самое частотное из них, оно встретилось', m, 'раз(а).')
#    for i in range(len(pattern)):
#        print(pattern[i],count[i])

def main():
    f = input('Введите имя файла:')
    words = split_text(f)
    ness(words)
main()
     
                    
                    
