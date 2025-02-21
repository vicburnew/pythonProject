from src.main import divide, reverse_list


def test_divide():
    assert divide(2, 1) == 2

def test_zero_divide():
    assert divide(2, 0) == 0

def test_reverse_list_numbers():
    assert reverse_list("123") == "321"

def test_reverse_list_letters():
    assert reverse_list("hello") == "olleh"
