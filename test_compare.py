def test_small(numbers):
    assert numbers[0] < numbers[1],\
        "{} not less than {}".format(numbers[0],numbers[1])

def test_greater(numbers):
    assert numbers[0] > numbers[1],\
        "{} not greater than {}".format(numbers[0],numbers[1])


def test_equalto(numbers):
    assert numbers[0] == numbers[1],\
        "{} not equal to {}".format(numbers[0],numbers[1])