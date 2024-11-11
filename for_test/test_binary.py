from binary_func import binary_search


def test_binary():
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13) == -1, "Error, this number in list or something was wrong"

