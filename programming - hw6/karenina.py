f = open("karenina.txt",'r',encoding='utf-8')
maxline = 0
minline = 1000000
line = f.readline()
for line in f:
    l = len(line)
    if l > maxline:
        maxline = l
    if l < minline:
        minline = l
    line = f.readline()
print("Разница между наибольшей и наименьшей строкой файла равна", maxline-minline,"символ(ов)")
f.close()

