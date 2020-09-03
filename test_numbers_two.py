def test_arith_multiplytest():
    a = 6
    b = 3
    assert a * b == 18 , "Expected: {}, Result: {}".format(a * b, 18)

def test_arith_divide():
    a = 6
    b = 3
    assert a / b == 2, "Expected: {}, Result: {}".format(a / b, 2)

def test_compare_equalto(numbers):
    assert numbers[0] == numbers[1],\
        "{} not equal to {}".format(numbers[0],numbers[1])
