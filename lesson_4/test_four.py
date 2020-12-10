import pytest


# METHOD 1 FIXTURE PARAMS
# ----------------------------

# # preprocess before using as variable
# # ----------------------------
# @pytest.fixture(params=[0,1])
# def x2(r):
#     return request.param + 1

# def test_01(x2):
#     assert x2 < 3
#     assert x2 > 0
#     print("-->",x2)

# # NxM test using fixture params
# # ----------------------------

# @pytest.fixture(params=[0, 1])
# def x3(request):
#     return request.param

# @pytest.fixture(params=[2, 3, 4])
# def y3(request):
#     return request.param

# def test_02(x3,y3):
#     assert x3*y3 > -1
#     print(x3*y3,"=",x3*y3)

# # N zip using fixture params
# # ----------------------------
# @pytest.fixture(params=[
#     [0, 1, 0],
#     [0, 2, 0],
#     [1, 2, 2],
#     [2, 2, 4],
#     ])
    
# def arr(request):
#     return request.param


# def test_03(arr):
#     assert arr[0] * arr[1] == arr[2]
#     print(arr[0] * arr[1], "==", arr[2])


# METHOD 2 PARAMETRIZE
# ----------------------------

# # NxM test using parametrize
# # ----------------------------
# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3, 4])
# def test_04(x,y):
#     assert x*y > -1
#     print(x*y)

# N zip using parametrize
# ----------------------------
@pytest.mark.parametrize("x,y,z", [
    [0, 1, 0],
    [0, 2, 0],
    [1, 2, 2],
    [2, 2, 4],
    ])
def test_05(x,y,z):
    assert x*y == z
    print(x*y,"=",z)
