import unittest
from thepasswordgenerator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    """
    Test cases for password generator
    """
    _generator = PasswordGenerator()

    def test_generate_password(self):
        """
        Check the password output length.
        """
        self.assertEqual(len(self._generator.generate_password()),
                         30, "By default password length is 30.")

    def test_generate_multiple_passwords(self):
        """_summary_: Check the multiple password output length."""
        password_list = self._generator.generate_multiple_passwords(15)
        self.assertEqual(len(password_list),
                         15, "By default password length is 30.")
        for i in password_list:
            self.assertEqual(len(i), 30, "By default password length is 30.")


if __name__ == '__main__':
    unittest.main()
