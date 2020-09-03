import pytest

@pytest.fixture
def numbers():
    a=9
    b=3
    return a,b


@pytest.fixture(scope='module')
def numbers_setup_teardown():
    print("\nsetup")
    a=9
    b=3
    #return a,b
    yield a,b
    print("\nteardown")



































































































# @pytest.fixture(params=[(1,1,2,0,1,1),(2,2,4,0,4,1),(3,3,6,0,9,1)])
# def numbers(request):
#     return request.param

