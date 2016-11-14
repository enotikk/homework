words = []
w = input()
l = len(w)
while w != "":
    if l > 5 :
        words.append(w)
    w = input()
    l = len(w)
for elem in words:
    print(elem)
    
