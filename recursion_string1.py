import unittest
import random

class TestRecuseString(unittest.TestCase):

    def setUp(self):
        pass

    def _test_forward_print_alphabet(self):
        s = recurse_string2(65)
        print('result from recurs is {s}'.format(s = s))

    def _test_backwards_print_alphabet(self):
        s = recurse_string3(65)
        print('result from recurs is {s}'.format(s = s))

    def _test_recurse_alphabet_method_4(self):
        s = recurse_string4(64 + 26)
        print('result from recurs is {s}'.format(s = s))

    def _test_recurse_alphabet_method_4(self):
        s = recurse_string5(64 )
        print(s)

    def test_new(self):
        n = recurse_string6(0)
        print('final is {n}'.format(n = n))

    def _test_new2(self):
        n = recurse_string7(0)
        print('final is {n}'.format(n = n))





def recurse_string2(num, s = ''):
    if num == 65 + 26:
        return 65 , ''
    else:
        num, s =  recurse_string2(num + 1)
    s += chr(num)
    num += 1
    return num, s

def recurse_string3(num, s = ''):
    if num == 65 + 26:
        return 65 + 26, ''
    else:
        num, s =  recurse_string3(num + 1)
    #stack returns 65 + 26 , '' as first values; then each stack call
    # subtracts one from num adds to string
    # [65 + 26, '',
    #  subtract 1 from previous, add to prvious second valuse,
    #  subtract 1 from previous, add to prvious second valuse,
    num -= 1
    s += chr(num)
    return num, s

def recurse_string4(num, s = ''):
    if num >= 65:
        s = recurse_string4(num - 1)
        #this doesn't get executed until done buidling the stack
        # stack is
        # [65, '',
        # get num, convert to str, add to previous,
        # get num, convert to str, add to previous,
        #print("below stack and num is {num}".format(num = num))
        s += chr(num)
    return s


def recurse_string5(num):
    c = chr(num)
    print(c)
    s = ''
    if num != 65 + 26:
        c = recurse_string5(num + 1)
        c += c
    return c

def recurse_string6(num):
    n = random.randint(1,9)
    f  = random.randint(1,9)
    print('entering func and n is {n} and num is {num}'.format(n=n, num = num))
    if num != 10:
        more  =  recurse_string6(num + 1) + 1
        print('after stack and n is {n} and f is {f}'.format(n = n, f = f))
        print('after stack and more is {more}'.format(more = more))
        n = more + n
    return n

def recurse_string7(num):
    n = 0
    if num != 10:
        n  =  recurse_string6(num + 1) 
    return n


if __name__ == '__main__':
    unittest.main()
