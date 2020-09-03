import pytest

@pytest.fixture
def numbers():
    a=9
    b=3
    return a,b

@pytest.mark.xfail
def test_smaller(numbers):
    assert numbers[0] < numbers[1],\
        "{} not less than {}".format(numbers[0],numbers[1])

def test_greater(numbers):
    assert numbers[0] > numbers[1],\
        "{} not greater than {}".format(numbers[0],numbers[1])

@pytest.mark.xfail
def test_equalto(numbers):
    assert numbers[0] == numbers[1],\
        "{} not equal to {}".format(numbers[0],numbers[1])


def test_smaller_equal(numbers):
    assert numbers[0] <= numbers[1],\
        "{} not less than {}".format(numbers[0],numbers[1])

@pytest.mark.xfail
def test_greater_equal(numbers):
    assert numbers[0] >= numbers[1],\
        "{} not less than {}".format(numbers[0],numbers[1])
    
