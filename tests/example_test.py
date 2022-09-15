from example import *

def test_hello_world():
    response = hello_world()
    assert(response == "Hello World!")