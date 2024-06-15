from twttr import shorten


def test_lowercase_vowels():
    assert shorten("How are you?") == "Hw r y?"


def test_uppercase_vowels():
    assert shorten("WHERE ARE yOU GOING") == "WHR R y GNG"


def test_mixedcase_vowels():
    assert shorten("My namE is ElizAbEth") == "My nm s lzbth"


def test_number():
    assert shorten("How ar3 y0u") != "Hw r y "
