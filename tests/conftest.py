import pytest


@pytest.fixture
def numbers():
    return "123"

@pytest.fixture
def letters():
    return "hello"

@pytest.fixture
def numbers_2():
    return "87654321"

@pytest.fixture
def letters_2():
    return "olleh"