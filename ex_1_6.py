import unittest

class TestStringComprehension(unittest.TestCase):

    def setUp(self):
        pass

    def test_2_as(self):
        self.assertEqual(compress_string('aa'), 'a2')

    def test_not_aab(self):
        self.assertEqual(compress_string('aab'), 'a2b1')

    def test_abccaad(self):
        self.assertEqual(compress_string('abccaad'), 'a1b1c2a2d1')

    def test_abc(self):
        self.assertEqual(compress_string('abc'), 'abc')

def compress_string(s):
    new_s = ''
    num = 1
    needs_compression = False
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            needs_compression = True
            num += 1
        else:
            new_s += '{l}{n}'.format(l =  s[i -1], n = num)
            num = 1
    new_s += '{l}{n}'.format(l =  s[-1], n = num)
    if needs_compression:
        return  new_s
    return s


if __name__ == '__main__':
    unittest.main()
