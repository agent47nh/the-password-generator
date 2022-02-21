import unittest

from thepasswordgenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    """
    Test cases for password generator
    """
    def test_generate_password(self):
        """
        Check the password output length.
        """
        generator = PasswordGenerator()
        self.assertEqual(len(generator.generate_password()), 30, "By default password length is 30.")

if __name__ == '__main__':
    unittest.main()
