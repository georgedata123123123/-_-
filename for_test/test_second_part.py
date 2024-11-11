from second_part import *

def test_first():
    assert first(2) == f"Количество полных метров: {2//100}", "Неправильно"

def test_second():
    assert second(2) == f"Количество полных тонн: {2//100}", "Неправильно"

def test_third():
    assert third(2) == f"Количество полных килобайт: {2 // 1024}", "Неправильно"

def test_fourth():
    assert fourth(-2, 1) == "Используйте положительные числа", "Неправильно"

def test_fifth():
    assert fifth(2, 1) == f"Длина незанятой части отрезка a: {2%1}", "Неправильно"

def test_sixth():
    assert sixth(33) == f"Количество десятков: {33//10}, единиц: {33%10}", "Неправильно"

def test_seventh():
    assert seventh(-33) == "Используйте правильные числа", "Неправильно"

def test_eigth():
    assert eigth(-2) == "Используйте правильные числа", "Неправильно"

def test_ninth():
    assert ninth(101) ==  f"Первая цифра числа: {101//100}", "Неправильно"

def test_tenth():
    assert tenth(-2) == "Используйте правильные числа", "Неправильно"

