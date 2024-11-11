# Выполнил: Георгий Павлович Мальцев


def first(a: int) -> object:
    p = 4 * a
    return f"Периметр квадрата: {p}"

    first(2)

def second(a: int):
    s = a ** 2
    return f"Площадь квадрата: {s}"

second(2)

def third(a: int, b: int):
    return f"Площадь прямоугольника: {a * b}"

third(2, 3)

def fourth(a: float):
    return f"Длина окружности: {3.14 * a}"

fourth(5)

def fifth(a: float):
    return f"Объем куба: {a ** 3}, площадь поверхности: {6 * a ** 2}"

fifth(5)

def sixth(a: float, b: float,
          c: float):
    return f"Объем: {a * b * c}, Площадь поверхности: {2 * (a * b + a * c + b * c)}"

sixth(1, 2, 3)

def seventh(r: float):
    return f"Длина окружности: {2 * 3.14 * r}, Площадь круга: {3.14 * r ** 2}"

seventh(2)

def eight(a: float, b: float):
    return f"Среднее арифметическое: {(a + b) / 2}"

eight(2, 1)

def ninth(a: float, b: float):
    return f"Среднее геометрическое: {(a * b) ** 0.5}"

ninth(1, 2)

def tenth(a: float, b: float):
    if (a == 0) or (b == 0):
        return print("Используется ноль")
    else:
        return f"Сумма: {a + b}, Разность: {a - b}, Произведение: {a * b}, Частное квадратов: {(a ** 2) / (b ** 2)}"

tenth(1, 2)
