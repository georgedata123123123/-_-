from fourth_part import let_cir

def test_let_cir():
    assert let_cir(["a", "s", "1", "a", "32", "23"]) == (["1", "32", "23"], ["a", "s", "a"])