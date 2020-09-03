def test_arithadd():
    a = 6
    b = 3
    assert a + b == 9, "Expected: {}, Result: {}".format(a + b, 9)

def test_arithsubtract():
    a = 6
    b = 3
    assert a - b == 3, "Expected: {}, Result: {}".format(a - b, 3)

def test_compare_small(numbers):
    assert numbers[0] < numbers[1],\
        "{} not less than {}".format(numbers[0],numbers[1])

def test_compare_greater(numbers):
    assert numbers[0] > numbers[1],\
        "{} not greater than {}".format(numbers[0],numbers[1])


