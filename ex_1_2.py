import unittest

class TestPdf(unittest.TestCase):

    def setUp(self):
        pass

    def test_foo_is_perm_oof(self):
        self.assertTrue(is_permutation('foo', 'oof'))

def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

if __name__ == '__main__':
    unittest.main()
