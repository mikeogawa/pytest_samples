import pytest


# @pytest.fixture(scope="class")
# def passing_var():
#     print("passing_var start")
#     yield ["a"]
#     print("passing_var end")


# class Test00:

#     def test_a(self, passing_var):
#         print("test_a")
#         print(passing_var[0])
#         assert passing_var[0] == "a"

#         passing_var[0] = "b"

#     def test_b(self, passing_var):
#         print("test_b")
#         print(passing_var[0])
#         assert passing_var[0] == "b"

#         passing_var[0] = "c"

#     def test_c(self, passing_var):
#         print("test_c")
#         print(passing_var[0])
#         assert passing_var[0] == "c"


@pytest.mark.parametrize("x", [0, 3, 6])
def x2(x):
    return x

@pytest.fixture(scope="class",params=[0,3,6])
def passing_var_2(request):
    print("passing_var start")
    yield [request.param]
    print("passing_var end")


class Test01:

    def test_1(self, passing_var_2):
        print("test_1")
        print(passing_var_2[0])
        assert passing_var_2[0] % 3 == 0

        passing_var_2[0] += 1

    def test_2(self, passing_var_2):
        print("test_2")
        print(passing_var_2[0])
        assert passing_var_2[0] % 3 == 1

        passing_var_2[0] += 1

    def test_3(self, passing_var_2):
        print("test_3")
        print(passing_var_2[0])
        assert passing_var_2[0] % 3 == 2
