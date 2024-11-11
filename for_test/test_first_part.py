from first_part import *
import pytest


def test_zero():
    assert 1 == 1, "Number is not equal"

def test_first():
    assert first(2) == f"Периметр квадрата: 8", "Это не периметр прямоугольника"

def test_second():
    assert  second(2) == f"Площадь квадрата: 4", "Неправильная площадь"

def test_third():
    assert third(2, 3) == f"Площадь прямоугольника: 6", "Неправильная площадь"

def test_fourth():
    assert fourth(5) == f"Длина окружности: {3.14 * 5}", "Неправильная длина окружности"

def test_fifth():
    assert fifth(2) == f"Объем куба: {2 ** 3}, площадь поверхности: {6 * 2 ** 2}", "Неправильно"

def test_sixth():
    assert sixth(1, 2, 3) == f"Объем: {1 * 2 * 3}, Площадь поверхности: {2 * (1 * 2 + 1 * 3 + 2 * 3)}", "Неправильно"

def test_seventh():
    assert seventh(2) == f"Длина окружности: {2 * 3.14 * 2}, Площадь круга: {3.14 * 2 ** 2}", "Неправильно"

def test_eight():
    assert eight(2, 1) == f"Среднее арифметическое: {(2 + 1) / 2}", "Неправильно"

def test_ninth():
    assert ninth(2, 1) == f"Среднее геометрическое: {(2 * 1) ** 0.5}", "Неправильно"

def test_tenth():
    assert tenth(2, 1) == f"Сумма: {2 + 1}, Разность: {2 - 1}, Произведение: {2 * 1}, Частное квадратов: {(2 ** 2) / (1 ** 2)}", "Неправильно"
