# Выполнил: Георгий Павлович Мальцев



def first(a: int):
    return a > 0

first(1)



def second(a: int):
    return a % 2 == 1

second(3)


def third(a: int):
    return a % 2 == 0

third(2)



def fourth(a: int, b: int):
    return (a>2) & (b<=3)

fourth(4, 1)


def fifth(a: int, b: int):
    return (a>=0) & (b<-2)

fifth(1, 2)


def sixth(a: int, b: int, c: int):
    return a<b<c

sixth(1, 2, 3)



def seventh(a: int, b: int, c: int):
    return (a<b<c) or (a>b>c)

seventh(1, 2, 3)



def eigth(a: int, b: int):
    return (a%2==1) & (b%2==1)

eigth(2, 3)


def ninth(a: int, b: int):
    return (a%2==1) or (b%2==1)

ninth(1, 2)


def tenth(a: int, b: int):
    return ((a%2==1) & (b%2==0)) or ((a%2==0) & (b%2==1))

tenth(1, 2)



