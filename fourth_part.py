# Выполнил: Георгий Павлович Мальцев


# 1
a = [1, 2, 3, 4, 5]
print(f"Первый элемент: {a[0]}, \n Третий элемент: {a[2]}, \n Срез: {a[:3]}")


#2
a = ["Ростов", "+", "на", "-", "Дону"]
a[1] = '-'
print(''.join(a))

#3 + 4
a = ["a", "s", "1", "a", "32", "23"]
def let_cir(a: list):
    b = []
    c = []
    for i in a:
        if i.isdigit() == True:
            b.append(i)
        else:
            c.append(i)

    return b, c

b, c = let_cir(a)
print(f"Cписок с буквами: {c}, \nC цифрами: {b}")


c.pop(-1)
c.reverse()
print(c)

#5

a = ["a", "s", "1", "a", "32", "23"]
a = set(a)
print(a) # Индексы элементов в наборах не фиксированы(они хаотично меняются),
         # неизменными остаются сами элементы при этом элементы не могут повторяться
        # (в нашем случае улетела буква "а")

