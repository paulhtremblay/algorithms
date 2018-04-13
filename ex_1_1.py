import unittest

class TestPdf(unittest.TestCase):

    def setUp(self):
        pass

    def test_foo_is_false(self):
        self.assertFalse(is_unique('foo'))

    def test_fo_is_true(self):
        self.assertTrue(is_unique('fo'))
        pass

def is_unique(s):
    s = sorted(s)
    for i in range( len(s) -1):
        if s[i] == s[i + 1]:
            return False
    return True


if __name__ == '__main__':
    unittest.main()
