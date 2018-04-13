import unittest

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        pass

    def test_bob_is_palindrome(self):
        self.assertTrue(is_palindrome('bob'))

    def test_tact_coa_lower_is_palindrome(self):
        self.assertTrue(is_palindrome('tact coa'))

    def test_tact_coa_upper_is_palindrome(self):
        self.assertTrue(is_palindrome('Tact Coa'))

    def test_tact_the_is_not_palindrome(self):
        self.assertFalse(is_palindrome('the'))

    def test_tact_the_the_is_palindrome(self):
        self.assertTrue(is_palindrome('thethe'))


def is_palindrome(s):
    record = {}
    for c in s:
        if c == ' ':
            continue
        _c = c.lower()
        if not record.get(_c):
            record[_c] = 0
        record[_c] += 1
    num_odds = 0
    for j in list(record.keys()):
        if record[j] % 2 != 0:
            num_odds += 1
    return num_odds < 2


if __name__ == '__main__':
    unittest.main()
