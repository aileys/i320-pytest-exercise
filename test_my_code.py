import pytest
from my_code import fix_phone_num

def test_fix_phone_num():
    assert fix_phone_num("5554321234") == "(555) 432-1234"
    assert fix_phone_num("5554429876") == "(555) 442-9876"
    assert fix_phone_num("3216543333") == "(321) 654-3333"

def test_fix_phone_num_raises_on_wrong_length():
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761")
    with pytest.raises(ValueError):
        fix_phone_num("(3213) 654 3333")
