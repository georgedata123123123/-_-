from third_part import *


def test_first():
    assert first(1) == True, "Error"


def test_second():
    assert second(3) == True, "Error"


def test_third():
    assert third(2) == True, "Error"


def test_fourth():
    assert fourth(3, 1) == True, "Error"


def test_fifth():
    assert fifth(1, -4) == True, "Error"


def test_sixth():
    assert sixth(1, 2, 3) == True, "Error"


def test_seventh():
    assert seventh(1, 2, 3) == True, "Error"


def test_eigth():
    assert eigth(3, 3) == True, "Error"


def test_ninth():
    assert ninth(2, 3) == True, "Error"


def test_tenth():
    assert tenth(3, 2) == True, "Error"
