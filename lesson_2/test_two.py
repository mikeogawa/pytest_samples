import pytest

# Basic
# ----------------------------
a = True
def test_a():
    assert a == True
    print("yeah")

# Using as function
# ----------------------------
@pytest.fixture
def variable():
    return "hi"

def test_00(variable):
    assert variable == "hi"

# Using as class type
# ----------------------------
class TestOne:
    def test_00(self, variable):
        assert variable == "hi"

# Using fixture inside a class
# ----------------------------
class TestTwo:

    @pytest.fixture
    def variable_in_c(self):
        return "hi"

    def test_01(self, variable_in_c):
        assert variable_in_c == "hi"


# pre and post process using yield
# ----------------------------
@pytest.fixture
def variable_w_pre_post():
    print("hi-pre")
    yield "hi"
    print("hi-post")

def test_01(variable_w_pre_post):
    assert variable_w_pre_post == "hi"
    print(variable_w_pre_post)

# import fixture from context using pytest.mark
# ----------------------------
@pytest.mark.usefixtures("hello")
def test_hello(hello):
    print(hello)
    assert hello == "what have you got there?"

@pytest.mark.usefixtures("hello")
class TestThree:

    def test_hello(self, hello):
        print(hello)
        assert hello == "what have you got there?"