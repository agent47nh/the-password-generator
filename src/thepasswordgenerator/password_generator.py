from ast import Num
import string
import random


class PasswordGenerator:
    """
    Generate passwords with complexity of your choice.
    """

    def __init__(self, length=30, upper=3, lower=3, numbers=3, special=3):
        self._length = length
        self._numbers = numbers
        self._special = special
        self._upper = upper
        self._lower = lower

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        self._numbers = numbers

    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, upper):
        self._upper = upper

    @property
    def lower(self):
        return self._lower

    @lower.setter
    def lower(self, lower):
        self._lower = lower

    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, special):
        self._special = special

    def generate_password(self):
        """Generate a random password"""

        complexity_length = self._numbers + self._special\
            + self._upper + self._lower
        # Check if total length is greater than complexity length.
        if complexity_length > self._length:
            raise ValueError(
                "Complexity length cannot be greater than total length,"
                " Total Length: {}, Complexity Length: {}"
                .format(self._length, complexity_length)
            )
        character_list = {
            "numbers": string.digits,
            "lowercase": string.ascii_letters,
            "uppercase": string.ascii_letters.upper(),
            "special": string.punctuation
        }

        password = ""
        compile_character_list = ""
        for key, value in character_list.items():
            char_list = list(value)
            compile_character_list += value
            random.shuffle(char_list)
            if key == "numbers":
                password += "".join(char_list)[:self._numbers]
            elif key == "lowercase":
                password += "".join(char_list)[:self._lower]
            elif key == "uppercase":
                password += "".join(char_list)[:self._upper]
            elif key == "special":
                password += "".join(char_list)[:self._special]

        # Add remaining characters to password.
        remain_length = self._length - complexity_length
        password += "".join(compile_character_list)[:remain_length]
        
        # Shuffle password.
        password = list(password)
        random.shuffle(password)
        return "".join(password)
