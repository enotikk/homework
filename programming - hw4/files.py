f = open('information.txt', 'w')
name = input("Как тебя зовут?")
f.write(name)
age = input("Сколько тебе лет?")
f.write(age)
color = input("Какой твой любимый цвет?")
f.write(color)
singer = input("Кто твой любимый музыкальный исполнитель?")
f.write(singer)
dream = input("Какая у тебя мечта?")
f.write(dream)
f.close()
f = open('information.txt','r')
answ = input("Как зовут твоего соседа?")
if answ == name:
    print("Правильно")
else:
    print("Неправильно. Ты плохо знаешь своего соседа. Его зовут", name)
answ = input("Сколько лет твоему соседу?")
if answ == age:
    print("Правильно")
else:
    print("Неправильно. Ты плохо знаешь своего соседа. Ему", age)
answ = input("Какой у него любимый цвет?")
if answ == color:
    print("Правильно")
else:
    print("Неправильно. Ты плохо знаешь своего соседа. Его любимый цвет", color)
answ = input("Его любимый музыкальный исполнитель?")
if answ == singer:
    print("Правильно")
else:
    print("Неправильно. Ты плохо знаешь своего соседа. Его любимый исполнитель", singer)
answ = input("О чем мечтает твой сосед?")
if answ == dream:
    print("Правильно")
else:
    print("Неправильно. Ты плохо знаешь своего соседа. Его мечта", dream)
f.close()
