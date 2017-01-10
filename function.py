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

def syl (arr, k):
    result = []
    for word in arr:
        v = 0
        for letter in word:
            if letter in 'ёуеэоаыяию':
                v += 1
        if v == k:
            result.append(word)
    return result

def letter (arr,l):
    result = []
    for word in arr:
        if word[0] == l.lower:
            result.append(word)
    return result
    
def main():
    filename = input('Введите имя файла: ')
    w  = split_text (filename)
    print(w)
    m = input('Чтобы вывести слова, имеющие определенное кол-во слогов, введите 1. Чтобы вывести слова, начинающиеся с определенной буквы, введите любой другой символ.')
    if m == '1':
        k = int(input('Введите количество слогов: '))
        result = syl(w,k)
        print(result)
    else:
        k = int(input('Введите первую букву: '))
        result = letter(w,k)
        print(result)
main()

