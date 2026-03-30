# content of test_app.py

def add(a, b):
    return a + b

def test_add_integers():
    """Test that adding two integers works correctly."""
    assert add(1, 2) == 3

def test_add_floats():
    """Test that adding floats works."""
    assert add(1.5, 2.5) == 4.0

def test_add_strings():
    """Test that adding strings (concatenation) works."""
    assert add("hello", " world") == "hello world"
