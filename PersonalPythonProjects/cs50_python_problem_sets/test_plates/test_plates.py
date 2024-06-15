from plates import is_valid


def test_length_of_plate():
    assert is_valid("AAA222") == True
    assert is_valid("A") == False
    assert is_valid("AAAA222") == False

def test_all_numbers():
    assert is_valid("22222") == False

def test_first_2_chars_isalphabet():
    assert is_valid("AA345") == True
    assert is_valid("2A345") == False
    assert is_valid("22AA22") == False


def test_num_not_in_middle_of_plate():
    assert is_valid("BC2334") == True
    assert is_valid("BC23B4") == False
    assert is_valid("CG21HH") == False


def test_num_in_plate_not_startwith_0():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AZ068") == False


def test_punctation_mark_not_in_plate():
    assert is_valid("AZ397") == True
    assert is_valid("AB.99") == False
    assert is_valid("CA9,22") == False
    assert is_valid("VA1:8") == False
    assert is_valid("MZ;12") == False
    assert is_valid('NX"290') == False
    assert is_valid("MC'23") == False
    assert is_valid("LX 79") == False
