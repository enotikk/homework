#взять какой-нибудь файл с достаточно большим текстом,
#прочитать его, поделить на предложения (просто по знакам конца предложения),
#удалить знаки препинания.
#Найти предложения длиннее 10 слов, и для этих предложений распечатать слова,
#начинающиеся с заглавной буквы
def split_text(filename): 
    f = open(filename, 'r', encoding='utf-8')
    s = f.read() 
    a = s.split()
    b = []
    sent = []
    for word in a:
        if word[-1] in '.!?…':
            word = word.strip('.!?…,"«»()-:;/\|“—”')
            b.append(word)
            sent.append(b)
            b = []
        else:
            word = word.strip('.!?…,"«»()-:;/\|“—”')
            b.append(word)
    return sent
def tenwsent (a):
    out = 'Cлова с большой буквы предложения {}:{}\n'
    index = 1
    result = ''
    for sent in a:
        if len(sent)>10:
            for word in sent:
                if word.istitle():
                    result = result+' '+word
            print(out.format(index,result))
            result = ''
        index += 1

def main():
    filename = 'paris.txt'
    a = split_text(filename)
    tenwsent (a)

main()
    
    
