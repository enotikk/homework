f = open ("freq.txt",'r',encoding='utf-8')
print("Part 1.")
for line in f:
    if "| союз" in line:
        print(line)
f.close()
f = open ("freq.txt",'r',encoding='utf-8')
print("Part 2.")
s = 0
for line in f:
    if ("| сущ" in line) and (" ед " in line):
        n = line.find("|")
        print(line[0:n-1],",",sep="",end=" ")
        n = line.rfind("|")
        s = s + float(line[n+1:-1])
print(s)
f.close()
f = open ("freq.txt",'r',encoding='utf-8')
print("Part 3.")
a = []
w = input("Введите слова\n")
while w != "":
    a.append(w)
    w = input()
for i in a:
    flag = False
    for line in f:
        n = line.find("|")
        if line[0:n-1] == i:
            print(line)
            flag = True
            break
    if flag == False:
        print(i,"is not found")
        
