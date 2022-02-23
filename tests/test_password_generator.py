import pytest
import string
import re
from thepasswordgenerator import PasswordGenerator


def test_password_length(password_generator):
    """Check the password output length."""

    test_password = password_generator.generate_password()
    assert len(test_password) == 20, \
        "The password length is set to 20. " \
        "Current length is: " + str(len(test_password))


def test_generate_multiple_passwords(password_generator):
    """Check the multiple password output length"""

    password_generator.length = 30
    password_list = password_generator.generate_multiple_passwords(15)
    assert len(password_list) == 15, "By default password length is 30."
    for i in password_list:
        assert len(i) == 30, "By default password length is 30."


def test_password_complexity(uppercase_check, numbers_check, special_check):
    """_summary_: Check the password complexity:
    Args:
        password_generator (thepasswordgenerator.PasswordGenerator()):
            The password generator object.
    """

    assert uppercase_check, "Uppercase characters are not " \
        "generated correctly."
    assert numbers_check, "Numbers are not generated correctly."
    assert special_check, "Special characters are not generated correctly."


@pytest.fixture
def uppercase_check(password_generator):
    """Check number of uppercase characters in the password"""
    password_generator.length = 30
    password_generator.upper = 27
    password_generator.numbers = 1
    password_generator.special = 1
    password_generator.lower = 1
    test_password = password_generator.generate_password()
    uppercase_count = sum(1 for c in test_password if c.isupper())

    return uppercase_count == password_generator.upper


@pytest.fixture
def numbers_check(password_generator):
    """Check number of integers in the password"""
    password_generator.length = 30
    password_generator.upper = 10
    password_generator.numbers = 15
    password_generator.special = 4
    password_generator.lower = 1
    test_password = password_generator.generate_password()
    numbers_list = re.findall(r'\d', test_password)
    return len(numbers_list) == password_generator.numbers


@pytest.fixture
def special_check(password_generator):
    """Check number of integers in the password"""
    password_generator.length = 30
    password_generator.upper = 10
    password_generator.numbers = 9
    password_generator.special = 10
    password_generator.lower = 1
    test_password = password_generator.generate_password()
    special_count = sum(1 for c in test_password if c in string.punctuation)
    return special_count == password_generator.special


@pytest.fixture
def password_generator():
    """Fixture to create a password generator object."""
    return PasswordGenerator(length=20)
