import re
def burunduk(fname):
    f = open(fname, 'r', encoding='utf-8')
    s = f.read()
    regex = '((В|в)и(|́)кинг(и|-| |»|,|\.|\)|\?|!|:|;|"|ов|ам|ами|а|ах|у|ом|е))'
    s = re.sub(regex,'\\2урунду\\3к\\4' ,s)
    s = re.sub('Вурунду','Бурунду', s)
    s = re.sub('вурунду','бурунду', s)
    s = re.sub('(Б|б)урунду́к([а-я])','\\1урундук\\2́', s)
    return s


def make_file(s):
    f = open('result.txt', 'w', encoding='utf-8')
    f.write(s)

    
def main():
    fname = input('Введите название файла: ')
    s = burunduk(fname)
    print(s, '\nСтатья сохранена в файле result.txt')
    make_file(s)


main()
