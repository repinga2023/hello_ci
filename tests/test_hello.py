from hello.hello import hello


def test_hello_default():
    assert hello() == "Hello world!"


def test_hello_upper():
    assert hello("upper") == "HELLO WORLD!"


def test_hello_lower():
    assert hello("lower") == "hello world!"


def test_hello_title():
    assert hello("title") == "Hello World!"


def test_hello_unknown_mode():
    assert hello("something") == "Hello world!"
