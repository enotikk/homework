import re
def utc(fname):
    f = open(fname, 'r', encoding='utf-8')
    s = f.read()
    regex = '"(UTC.*?)"'
    r = re.search(regex, s)
    f1 = open('result_'+fname, 'w', encoding='utf-8')
    regex = 'PageName":"(.*?)"'
    title = re.search(regex, s)
    title1 = re.sub('_', ' ', title.group(1)) 
    if r != None:
        f1.write('Часовой пояс в городе '+ title1+' '+ r.group(1)+'.')
    else:
        f1.write('I did not find:(')
    
def main():
    fname = input('Введите название файла: ')
    utc(fname)
main()
