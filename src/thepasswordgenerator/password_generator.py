#!/bin/sh/python
# coding= utf-8

from ast import Num
import string
import random
import logging
import logging.handlers


class PasswordGenerator:
    """
    Generate passwords with complexity of your choice.
    """

    def __init__(self, length=30, upper=3, lower=3,
                 numbers=3, special=3,
                 log_file='./thepasswordgenerator.log') -> None:
        self._length = length
        self._numbers = numbers
        self._special = special
        self._upper = upper
        self._lower = lower
        self._logging_enabled = False
        if log_file:
            self._gen_str = string.ascii_letters + string.digits
            self._log_id = ''.join(
                random.choice(self._gen_str) for i in range(10)
                )
            self._logging_enabled = True
            self._generator_log = logging.getLogger("PasswordGenerator")
            self._generator_format = logging.Formatter("%(asctime)s "
                                                       "- %(name)s "
                                                       f"- {self._log_id} "
                                                       "- %(levelname)s "
                                                       "- %(message)s")
            self._generator_log.setLevel(logging.INFO)
            self._generator_handler = logging.handlers\
                .RotatingFileHandler(log_file, maxBytes=1048576,
                                     backupCount=5, encoding="utf-8")
            self._generator_handler.setFormatter(self._generator_format)
            self._generator_log.addHandler(self._generator_handler)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length: int):
        self._length = length

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, numbers: int):
        self._numbers = numbers

    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, upper: int):
        self._upper = upper

    @property
    def lower(self):
        return self._lower

    @lower.setter
    def lower(self, lower: int):
        self._lower = lower

    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, special: int):
        self._special = special

    def _shuffle_string(self, string_to_shuffle: str) -> str:
        """_summary_: Shuffle a string.

        Args:
            string_to_shuffle (str): String to be shuffled.
        """

        string_to_shuffle = list(string_to_shuffle)
        random.shuffle(string_to_shuffle)
        return "".join(string_to_shuffle)

    def _check_string_length(self, string_to_check: str) -> bool:
        """_summary_: Check if the string is of the required length.

        Args:
            string_to_check (str): String to be checked.

        Returns:
            bool: True if the string is of the required length.
        """

        if len(string_to_check) == self._length:
            return True
        else:
            return False

    def _write_to_log(self, severity: int, message: str) -> None:
        """_summary_: Write to the logs if logging is enabled.
        Args:
            severity (int): Logging level.
            message (str): Message to be logged.
        """
        if self._logging_enabled:
            self._generator_log.log(severity, message)

    def _complexity_check(self) -> bool:
        """_summary_: Check if the password has the required complexity.

        Returns:
            bool: True if the password has the required complexity.
        """

        if self._numbers + self._special + self._upper + self._lower == 0:
            self._write_to_log(20, "No complexity set. Will use"
                               " all lowercase characters.")
            self._lower = self._length
            return False

        elif self._numbers + self._special + self._upper + self._lower != 0:
            self._write_to_log(
                20, f"Complexity set to as follows:\n Numbers:"
                f" {self._numbers}\n Special: {self._special}\n "
                f"Upper: {self._upper}\n Lower: {self._lower}"
                )
            return True

    def _check_character_pool(self, type, character_pool: str) -> str:
        """_summary_: Check if the character pool is valid.

        Args:
            type (str): Type of character pool.
            character_pool (str): Character pool to be checked.

        Returns:
            str: Character pool length is sufficient.
        """

        if type == "upper":
            uppercase_pool_status = len(character_pool) >= self._upper
            self._write_to_log(20, "Checking uppercase character pool.")
            if uppercase_pool_status:
                self._write_to_log(20, "Uppercase character pool is "
                                   "sufficient.")
                return self._shuffle_string(character_pool)
            else:
                self._write_to_log(20, "Uppercase character pool "
                                   "needs more charaters. Generating more...")
                while not uppercase_pool_status:
                    character_pool += string.ascii_uppercase
                    uppercase_pool_status = (
                        len(character_pool) >= self._numbers
                        )
                return self._shuffle_string(character_pool)

        elif type == "lower":
            lowercase_pool_status = len(character_pool) >= self._lower
            self._write_to_log(20, "Checking lowercase character pool.")
            if lowercase_pool_status:
                self._write_to_log(20, "Lowercase character pool is "
                                   "sufficient.")
                return self._shuffle_string(character_pool)
            else:
                self._write_to_log(20, "Lowercase character pool "
                                   "needs more charaters. Generating more...")
                while not lowercase_pool_status:
                    character_pool += string.ascii_lowercase
                    lowercase_pool_status = (
                        len(character_pool) >= self._numbers
                        )
                return self._shuffle_string(character_pool)

        elif type == "numbers":
            numbers_pool_status = (
                len(character_pool) >= self._numbers
                )
            self._write_to_log(20, "Checking numbers pool.")
            if numbers_pool_status:
                self._write_to_log(20, "Numbers pool is sufficient.")
                return character_pool
            else:
                self._write_to_log(20, "Numbers pool needs more "
                                   "digits. Generating more...")
                while not numbers_pool_status:
                    character_pool += string.digits
                    numbers_pool_status = len(character_pool) >= self._numbers
                return character_pool

        elif type == "special":
            special_pool_status = len(character_pool) >= self._special
            self._write_to_log(20, f"Checking special characters.")
            if special_pool_status:
                self._write_to_log(20, "Special characters pool is"
                                   "sufficient.")
                return character_pool
            else:
                self._write_to_log(20, "Special characters pool"
                                   "needs more charaters. Generating more...")
                while not special_pool_status:
                    character_pool += string.punctuation
                    special_pool_status = len(character_pool) >= self._numbers
                return character_pool

    def generate_password(self) -> str:
        """Generate a random password"""

        if not self._complexity_check():
            self._write_to_log(
                20, f"Complexity set to as follows:\n Numbers:"
                f" {self._numbers}\n Special: {self._special}\n "
                f"Upper: {self._upper}\n Lower: {self._lower}")
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
            "lowercase": string.ascii_letters.lower(),
            "uppercase": string.ascii_letters.upper(),
            "special": string.punctuation
        }

        password = ""
        if self._numbers > 0:
            character_list["numbers"] = self._check_character_pool(
                "numbers", character_list["numbers"]
            )
            password += character_list["numbers"][:self._numbers]
        if self._special > 0:
            character_list["special"] = self._check_character_pool(
                "special", character_list["special"]
            )
            password += character_list["special"][:self._special]
        if self._upper > 0:
            character_list["uppercase"] = self._check_character_pool(
                "upper", character_list["uppercase"]
            )
            password += character_list["uppercase"][:self._upper]
        if self._lower > 0:
            character_list["lowercase"] = self._check_character_pool(
                "lower", character_list["lowercase"]
            )
            password += character_list["lowercase"][:self._lower]

        remain_length = self._length - complexity_length
        password += "".join(character_list["lowercase"])[:remain_length]

        # Check if the password is of the required length.
        while not self._check_string_length(password):
            required_length = self._length - len(password)
            # Fill remaining length with random lowercase alphabet characters.
            password += "".join(character_list["lowercase"])[:required_length]
            password = self._shuffle_string(password)
        # Shuffle password.
        return self._shuffle_string(password)

    def generate_multiple_passwords(self, number_of_passwords=5) -> list:
        """_summary_: Generate multiple passwords.

        Args:
            number_of_passwords (int, optional): Variable name
                            is descriptive enough. Defaults to 5.
        """

        passwords = []
        self._write_to_log(20, f"Generating {number_of_passwords}"
                           " passwords.")
        for i in range(number_of_passwords):
            passwords.append(self.generate_password())

        return passwords
