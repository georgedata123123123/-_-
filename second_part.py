# Выполнил: Георгий Павлович Мальцев



def first(l: int):
    return  f"Количество полных метров: {l//100}"

first(1)



def second(m: int):
    return f"Количество полных тонн: {m//1000}"

second(1)


def third(m: int):
    return f"Количество полных килобайт: {m // 1024}"

third(1)

def fourth(a: int, b: int):
    if (a < 1) or (b < 1):
        return "Используйте положительные числа"
    else:
        return f"Количество отрезков: {a//b}"

fourth(1, 2)



def fifth(a: int, b: int):
    if (a < 1) or (b < 1):
        return "Используйте положительные числа"
    else:
        return f"Длина незанятой части отрезка a: {a%b}"

fifth(1, 2)



def sixth(a: int):
    if (a < 10) or (a>99):
        return "Используйте правильные числа"
    else:
        return f"Количество десятков: {a//10}, единиц: {a%10}"

sixth(1)



def seventh(a: int):
    if (a < 1) or (a>99):
        return "Используйте правильные числа"
    else:
        d=a//10
        c=a%10
        return f"Сумма цифр: {d+c}, произведение: {d*c}"

seventh(1)


def eigth(a: int):
    if (a < 1) or (a>99):
        return "Используйте правильные числа"
    else:
        d = a // 10
        c = a % 10
        return f"Новое число: {c}{d}"

eigth(1)

def ninth(a: int):
    if (a < 100) or (a>999):
        return "Используйте правильные числа"
    else:
        return f"Первая цифра числа: {a//100}"

ninth(1)

def tenth(a: int):
    if (a < 100) or (a>999):
        return "Используйте правильные числа"
    else:
        c = a%10
        d = (a//10) % 10
        return f"Полученное число: {c}{d}"

tenth(1)


