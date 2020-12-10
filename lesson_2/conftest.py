import pytest

@pytest.fixture
def hello():
    print("hello big brother")
    yield "what have you got there?"
    print("you only see air")