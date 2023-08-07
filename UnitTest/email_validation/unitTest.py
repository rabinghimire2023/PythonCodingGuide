import unittest
from email_validation import validate_email

class TestClass(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email("rabin.ghimire@gmail.com"))
        self.assertTrue(validate_email("rabin_ghimire@yahoo.com"))
        self.assertTrue(validate_email("rabin123@outlook.com"))

    def test_invalid_format(self):
        self.assertFalse(validate_email("invalid_email_format"))
        self.assertFalse(validate_email("invalid.email.format"))
        self.assertFalse(validate_email("missing_at_symbol.com"))

    def test_space_in_address(self):
        self.assertFalse(validate_email("rabin ghimire@gmail.com"))
        self.assertFalse(validate_email("rabin ghimire @yahoo.com"))

    def test_invalid_providers(self):
        self.assertFalse(validate_email("rabinghimire@yopmail.com"))
        self.assertFalse(validate_email("rabinghimire@disposablemail.com"))
        self.assertFalse(validate_email("rabinghimire@invalidprovider.org"))

if __name__ == "__main__":
    unittest.main()

"""....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
"""