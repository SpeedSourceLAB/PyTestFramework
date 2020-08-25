import pytest



def test_add(numbers):
    assert numbers[0] + numbers[1] == 5, "Expected: {}, Result: {}".format(numbers[0]+numbers[1],5)

def testsubtract(numbers):
    numbers[0] =10
    assert numbers[0] - numbers[1] == 3, \
        "Expected: {}, Result: {}".format(numbers[0] - numbers[1], 3)

def testmultiply(numbers):
    assert numbers[0] * numbers[1] == 18, \
        "Expected: {}, Result: {}".format(numbers[0] * numbers[1], 18)

def test_divide(num):
    assert (num[0] / num[1]) == 3, \
        "Expected: {}, Result: {}".format(num[0] / num[1], 3)

@pytest.fixture
def num():
    a=6
    b=3
    return a,b

@pytest.fixture
def numbers(num):
    a=num[0]
    b=num[1]
    return a,b