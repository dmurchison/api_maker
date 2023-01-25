import pytest



def test_true():
    print("In test_true")
    assert True


def test_false():
    var_1 = 'a'
    var_2 = 'b'
    print("In test_false")
    assert var_1 == var_2

