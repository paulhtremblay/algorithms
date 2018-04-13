import unittest
import math
import random

class TestRotation(unittest.TestCase):

    def setUp(self):
        self.set_1 = [3, 4, 5, 6, 7, 8, 9, 0, 2]
        self.set_2 = [5, 6, 7, 8, 9, 10, 3, 4 ]
        self.set_3 = [7, 1, 2, 3, 4, 5, 6 ]

    def test_set_1(self):
        a = brute_force(self.set_1)
        b = binary_search(self.set_1)
        self.assertEqual(a, b[0])
        self.assertTrue( b[1] < math.log(len(self.set_1), 2))

    def test_set_2(self):
        a = brute_force(self.set_2)
        b = binary_search(self.set_2)
        self.assertEqual(a, b[0])
        self.assertTrue( b[1] < math.log(len(self.set_1), 2))

    def test_set_3(self):
        a = brute_force(self.set_3)
        b = binary_search(self.set_3)
        self.assertEqual(a, b[0])
        self.assertTrue( b[1] < math.log(len(self.set_1), 2))

    def make_random_list(self, length):
        l = []
        for k in range(length):
            l.append(k)
        i = random.sample(range(length), 1)[0]
        f = []
        for j in l[i:]:
            f.append(j)
        for j in l[:i]:
            f.append(j)
        return f

    def test_temp(self):
        for i in range(100):
            l = self.make_random_list(100)
            a = brute_force(l)
            b = binary_search(l)
            self.assertEqual(a, b[0])
            if b[1] >= math.log(len(l),2) + 1:
                print(b[1], math.log(len(l), 2))
            self.assertTrue( b[1] < math.log(len(l), 2) + 1)


def _is_rotation(l, mid):
    if l[mid] > l[mid + 1]:
        return mid
    if l[mid - 1] > l[mid]:
        return mid - 1
    return None


def binary_search(l):
    start = 0
    end = len(l) - 1
    counter = 0
    while True:
        counter += 1
        mid = (end - start)//2 + start
        is_rotation = _is_rotation(l, mid)
        if is_rotation != None:
            return is_rotation, counter
        if l[mid] < l[start]:
            end = mid
        elif l[mid] > l[end]:
            start = mid
        if counter == 10:
            print('too many')
            break

def brute_force(l):
    for counter, i in enumerate(l):
        if i > l[counter + 1]:
            return counter 
    return False

if __name__ == '__main__':
    unittest.main()
