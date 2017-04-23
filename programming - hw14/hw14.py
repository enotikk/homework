#сколько в дереве папок с полностью кириллическими названиями
import os
def cyrillic(name):
    flag = True
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя _,.!?"«»()-:;/\|“—”1234567890'
    for s in name:
        if not s.lower() in alf:
            flag = False
            break
    return flag
            
def count_dirs(tree):
    res = 0
    for root, dirs, files in os.walk(tree):
        for d in dirs:
            print(d)
            if cyrillic(d):
                res += 1
    return res

def main():
    print('Количество папок в дереве с кириллическими названиями:',count_dirs('.'))
    
main()
