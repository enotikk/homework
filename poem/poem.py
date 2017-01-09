import random
# Эта программа генерирует стихотворение из 4 строк с соблюдением метрической схемы - ямб

def imperative():
    # эта функция возвращает случайный глагол в повелительном наклонении; у неё нет аргументов
    f = open('imp.txt','r')
    imperative = f.readlines()
    f.close()
    s = random.choice(imperative)
    return s[:-1]

def verb_pl():
    # эта функция возвращает случайный глагол мн.ч.; у неё нет аргументов
    f = open('v_pl.txt','r')
    plural_verbs = f.readlines()
    f.close()
    s = random.choice(plural_verbs)
    return s[:-1]

def verb2():
    # эта функция возвращает случайный глагол ед.ч. из 2 слогов; у неё нет аргументов
    f = open('v2.txt','r')
    v2 = f.readlines()
    f.close()
    s = random.choice(v2)
    return s[:-1]

def verb3():
    # эта функция возвращает случайный глагол ед.ч. из 3 слогов; у неё нет аргументов
    f = open('v3.txt','r')
    v3 = f.readlines()
    f.close()
    s = random.choice(v3)
    return s[:-1]


def noun(number):
    # эта функция возвращает случайное существительное; у неё есть один аргумент - число существительного
    f = open('noun_sg.txt','r')
    singular_nouns = f.readlines()
    f.close()
    f = open('noun_pl.txt','r')
    plural_nouns = f.readlines()
    f.close()
    # мы ожидаем, что функция будет получать в качестве аргумента либо строку 'sg' - для сущ. ед.ч.
    if number == 'sg':
        s = random.choice(singular_nouns)
        return s[:-1]
    # либо любую другую строку - для сущ. мн.ч.
    s = random.choice(plural_nouns)
    return s[:-1]

def noun_acc():
    # эта функция возвращает случайное суш.в вин.пад.; у неё нет аргументов
    f = open('noun_acc.txt','r')
    noun = f.readlines()
    f.close()
    s = random.choice(noun)
    return s[:-1]

def adj():
    # эта функция возвращает случайное прил. мн.ч.; у неё нет аргументов
    f = open('adj.txt','r')
    adj_pl = f.readlines()
    f.close()
    s = random.choice(adj_pl)
    return s[:-1]

def adv2():
    # эта функция возвращает случайное нареч. с ударением на 2 слог; у неё нет аргументов
    f = open('adv2.txt','r')
    adv_2 = f.readlines()
    f.close()
    s = random.choice(adv_2)
    return s[:-1]

def adv1():
    # эта функция возвращает случайное нареч. с ударением на 1 слог; у неё нет аргументов
    f = open('adv1.txt','r')
    adv_1 = f.readlines()
    f.close()
    s = random.choice(adv_1)
    return s[:-1]

def punctuation():
    # эта функция возвращает случайный знак препинания из небольшого списка; у неё нет аргументов
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def verse1():
    # эта функция собирает строчку из сущ., глагола, нареч. и знака препинания
    # например "Кино идет сейчас."
    var = random.randint(1,3)
    if var == 1:
        return noun('sg') + ' ' + verb2() + ' ' + adv2() + punctuation()
    elif var == 2:
        return noun('sg') + ' ' + verb3() + ' ' + adv1() + punctuation()
    else:
        return noun('pl') + ' ' + verb_pl() + ' ' + adv2() + punctuation()

def verse2():
    # эта функция собирает строчку из сущ.ед.ч, гл. повел.накл., сущ. в вин.пад. и знака препинания
    # например "Чувак, лови момент!"
    return noun('sg') + ',' + ' ' + imperative() + ' '  + noun_acc() + punctuation()

def verse3():
    # эта функция собирает строчку из прил., сущ. и гл. мн.ч., и знака препинания
    # например "Счастливые грачи поют..."
    return adj() + ' ' + noun('pl') + ' ' + verb_pl() + punctuation()


def make_verse():
    # эта функция выбирает случайный номер из 1,2,3 и возвращает соответствующую строчку
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()

# тут начинается основной код. 
# Он распечатывает 4 случайные строчки, чтобы получилась строфа. 
for n in range(4):
    print(make_verse())

# ура! можем постить наши прекрасные опусы в твиттер! 
