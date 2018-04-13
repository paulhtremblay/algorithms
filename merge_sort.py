import unittest

class TestMergeSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_list_of_2(self):
        self.assertEqual(merge_sort([2,1]), [1,2])

    def test_list_of_4(self):
        self.assertEqual(merge_sort([2,3,4,1]), [1,2,3,4])

    def test_list_of_3(self):
        self.assertEqual(merge_sort([3,2,4]), [2,3,4])

    def test_list_of_1(self):
        self.assertEqual(merge_sort([3]), [3])

def _sort_2_halves(start, end, the_list, new_list):
    if start == end:
        new_list.append(the_list[start])
        return
    midpoint =  (end - start)//2
    first_half = (start, start + midpoint)
    second_half = (start + midpoint + 1, end)
    i = first_half[0]
    j = second_half[0]
    while i <= first_half[1] and j <= second_half[1]:
        if the_list[j] > the_list[i]:
            new_list.append(the_list[i])
            i += 1
        if the_list[i] > the_list[j]:
            new_list.append(the_list[j])
            j += 1
    while i <= first_half[1]:
        new_list.append(the_list[i])
        i += 1

    while j <= second_half[1]:
        new_list.append(the_list[j])
        j += 1

def merge_sort(the_list):
    window = 1
    while True:
        window = window * 2
        start = 0
        new_list = []
        while True:
            end = window + start - 1
            if end > len(the_list) - 1:
                end = len(the_list) - 1
            _sort_2_halves(start, end, the_list, new_list)
            start = end + 1
            if end == len(the_list) - 1:
                the_list = new_list
                break
        if window >= len(the_list):
            return the_list

if __name__ == '__main__':
    unittest.main()
