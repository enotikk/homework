#Программа должна просмотреть все папки и файлы, находящиеся в одной папке с ней, и сообщить 
#Сколько найдено файлов, не содержащих цифр в названии.
#Кроме этого, программа должна выводить на экран названия всех файлов или папок, которые она нашла, без повторов
import os
def digitsin(f):
    flag = False
    digits = [0,1,2,3,4,5,6,7,8,9]
    for i in digits:
        if str(i) in f:
            flag = True
            break
    return flag

def f_in_dir():
    res = []
    folder = '.'
    for f in os.listdir(folder):
        if not digitsin(f):
            name = f[:f.rfind('.')]
            if (not name in res):
                res.append(name)
    return res

def main():
    res = f_in_dir()
    print('В данной директории не содержат цифр в названии',len(res), 'файлов и папок:\n')
    for name in res:
        print(name)
main()
                
