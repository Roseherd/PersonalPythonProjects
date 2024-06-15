from bank import value


def test_lowercase_hello():
    assert value("hello") == 0


def test_uppercase_hello():
    assert value("HELLO") == 0


def test_titlecase_hello():
    assert value("Hello") == 0


def test_startswith_h():
    for word in ["hey there", "howdy partner", "how are you"]:
        assert value(word) == 20


def test_startswith_H():
    for word in ["Hey there", "Howdy partner", "How are you"]:
        assert value(word) == 20


def test_lowercase_acceptable():
    for word in ["who are you", "where are you", "what's up"]:
        assert value(word) == 100


def test_uppercase_acceptable():
    for word in ["WHO ARE YOU", "WHERE ARE YOU", "WHAT'S UP"]:
        assert value(word) == 100


def test_titlecase_acceptable():
    for word in ["Who are you", "What's your name", "Why are you sad"]:
        assert value(word) == 100


def test_hello_with_whitespace():
    assert value("     hello    ") == 0


def test_startswith_h_with_whitespace():
    for word in ["    hey there     ", "howdy partner    ", "      how are you"]:
        assert value(word) == 20


def test_acceptable_with_whitespace():
    for word in ["      who are you    ", "where are you       ", "       what's up"]:
        assert value(word) == 100
