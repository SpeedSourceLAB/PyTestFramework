import pytest
"""Use conftest.py while running this test"""

def test_add(numbers):
    assert numbers[0] + numbers[1] == numbers[2], \
        "Expected: {}, Result: {}".format(numbers[0]+numbers[1],numbers[2])

def testsubtract(numbers):
    assert numbers[0] - numbers[1] == numbers[3], \
        "Expected: {}, Result: {}".format(numbers[0] - numbers[1], numbers[3])

def testmultiply(numbers):
    assert numbers[0] * numbers[1] == numbers[4], \
        "Expected: {}, Result: {}".format(numbers[0] * numbers[1], numbers[4])

def test_divide(numbers):
    assert (numbers[0] / numbers[1]) == numbers[5], \
        "Expected: {}, Result: {}".format(numbers[0] / numbers[1], numbers[5])



# @pytest.fixture
# def numbers():
#     a=6
#     b=3
#     return a,b