import unittest

class TestOneAway(unittest.TestCase):

    def setUp(self):
        pass

    def test_pale_ple_returns_true(self):
        self.assertTrue(is_one_away('pale', 'ple'))

    def test_pales_pale_returns_true(self):
        self.assertTrue(is_one_away('pales', 'pale'))

    def test_pale_bale_returns_true(self):
        self.assertTrue(is_one_away('pale', 'bale'))

    def test_pale_bake_returns_true(self):
        self.assertFalse(is_one_away('pale', 'bake'))

    def test_pale_bale_returns_true_method_2(self):
        self.assertTrue(is_one_away_2('pale', 'bale'))

    def test_pale_ple_returns_true_method_2(self):
        self.assertTrue(is_one_away_2('pale', 'ple'))

    def test_ple_pale_returns_true_method_2(self):
        self.assertTrue(is_one_away_2('ple', 'pale'))

    def test_aaa_pale_returns_false_method_2(self):
        self.assertFalse(is_one_away_2('aaa', 'pale'))

    def test_pales_pale_returns_true_method_2(self):
        self.assertTrue(is_one_away_2('pales', 'pale'))

def _create_record(s):
    record = {}
    for i in s:
        if not record.get(i):
            record[i] = 0
        record[i] += 1
    return record

def is_one_away(s1, s2):
    record1 = _create_record(s1)
    record2 = _create_record(s2)
    num_errors = 0
    for key in list(record1.keys()):
        if record1[key] != record2.get(key):
            num_errors += 1
    return num_errors <= 1

def is_one_away_2(s1, s2):
    if len(s1) == len(s2):
        num_diff = 0
        for counter, letter in enumerate(s1):
            if letter != s2[counter]:
                num_diff += 1
        return num_diff <= 1
    else:
        #pale bale
        num_diff = 0
        start_string = s1
        end_string = s2
        if len(s2) > len(s1):
            start_string = s2
            end_string = s1
        counter = 0
        for letter in start_string:
            if counter == len(end_string) - 1:
                return True
            if letter != end_string[counter]:
                num_diff += 1
            else:
                counter += 1
        return num_diff <= 1

def is_one_away_3(s1, s2):
    #ple, pale
    #pale, bale


if __name__ == '__main__':
    unittest.main()
