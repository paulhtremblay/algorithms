import unittest

class TestFind(unittest.TestCase):

    def setUp(self):
        pass

    def test_50_is_found(self):
        a = find_num(1, 100, 50)
        self.assertEqual(a, (49, 51, 6))

    def test_49_is_found(self):
        a = find_num(1, 100, 49)
        self.assertEqual(a, (48, 50, 7))

    def test_49_point_5_is_found(self):
        a = find_num(1, 100, 49.5)
        self.assertEqual(a, (49, 50, 8))

def num_found(high, low, mid, num):
    if num == mid:
        return num -1, num + 1
    if high - low == 1:
        return low, high

def find_num(low, high, num):
    counter = 0
    while True:
        counter += 1
        mid = round((high - low)/2) + low
        f = num_found(high, low, mid, num)
        if  f != None:
            return f[0], f[1], counter
        elif mid > num:
            high = mid
        elif mid < num:
            low = mid
        if counter > num:
            raise ValueError("too many times should not happend")
    raise ValueError("should not happend")

if __name__ == '__main__':
    unittest.main()
