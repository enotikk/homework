import re
def utc(fname):
    f = open(fname, 'r', encoding='utf-8')
    s = f.read()
    print(s)
    regex = '"UTC.*"'
    r = re.search(regex, s)
    if r != None:
        print(r.group())
    else:
        print('I did not find:(')
    
def main():
    fname = input('Введите название файла: ')
main()
