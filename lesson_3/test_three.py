import pytest

@pytest.fixture(scope="class")
def variable_c():
    print("variable_c_start")
    yield "variable_c"
    print("variable_c_end")


@pytest.fixture(scope="function")
def variable_f():
    print("variable_f_start")
    yield "variable_f"
    print("variable_f_end")


# Scope in class
# ----------------------------
class TestC:
    
    def test_00(self,variable_c,variable_f):
        assert variable_c == "variable_c"
        assert variable_f == "variable_f"
    
    def test_01(self,variable_c,variable_f):
        assert variable_c == "variable_c"
        assert variable_f == "variable_f"


# Scope in function
# ----------------------------
def test_02(variable_c,variable_f):
    assert variable_c == "variable_c"
    assert variable_f == "variable_f"