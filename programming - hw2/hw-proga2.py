slovo=input("Введите слово:")
for i in range (0,len(slovo),2):
    if slovo[i] in {"о","п","е"}:
        print(slovo[i])
