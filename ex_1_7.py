import unittest
import pprint
import copy
pp = pprint.PrettyPrinter(indent = 4)

class TestStringComprehension(unittest.TestCase):

    def setUp(self):
        self.array1 = [
                [11,12,13,14,15],
                [21,22,23,24,25],
                [31,32,33,34,35],
                [41,42,43,44,45],
                [51,52,53,54,55]
                ]

        """
         11 12 13 14 15     15 25 35 45 55
         21 22 23 24 25     14 24 34 44 54
         31 32 33 34 35     13 23 33 43 53
         41 42 43 44 45     12 22 32 42 52
         51 52 53 54 55     11 21 31 41 51

         15 25 35 45 55
         14 22 23 24 54
         13 32 33 34 53
         12 42 43 44 52
         11 21 31 41 51


        """
        """
        m[0,n] => m[0,0]; m[0,0] => m[n,0]; m[n,0] => m[n,n]; m[n,n] => m[0,n];
        m[0,n-1] => m[1,0]; m[1,0] => m[n-1, 0]; m[n-1, 0] => m[n-1,n]; m[n-1,n] => m[0,n-1]
        """

    def test_not_sure(self):
        res = make_new_matrix(self.array1, len(self.array1[0]))

def make_new_matrix(matrix, n):
    for j in range(n//2):
        for i in range(j, n -1 -j ):
            temp = matrix[i ][j]
            matrix[i][j] = matrix[j] [n-1 -i ]
            temp2 = matrix[n-1 -j ][i ]
            matrix[n-1 -j][i] = temp
            temp3 = matrix[n-1-i][n-1 -j]
            matrix[n-1 -i][n-1 -j] = temp2
            matrix[j][n-1-i] = temp3
    pp.pprint(matrix)

def _make_new_matrix(matrix, n):
    o = copy.deepcopy(matrix)
    m = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(None)
        m.append(temp)
    for i in range(n):
        new_row2 = []
        new_row2.append(matrix[n -5][0])
        new_row2.append(matrix[n -4][0])
        new_row2.append(matrix[n -3][0])
        new_row2.append(matrix[n -2][0])
        new_row2.append(matrix[n -1][0])
        print(new_row2)
        new_row3 = []
        new_row3.append(matrix[n -1][0])
        new_row3.append(matrix[n -1][1])
        new_row3.append(matrix[n -1][2])
        new_row3.append(matrix[n -1][3])
        new_row3.append(matrix[n -1][4])
        print(new_row3)
        matrix[0][0] = matrix[0][n -1]
        matrix[1][0] = matrix[0][n -2]
        matrix[2][0] = matrix[0][n -3]
        matrix[3][0] = matrix[0][n -4]
        matrix[4][0] = matrix[0][n -5]
        pp.pprint(matrix)
        matrix[n-1][0] = new_row2[0]
        matrix[n-1][1] = new_row2[1]
        matrix[n-1][2] = new_row2[2]
        matrix[n-1][3] = new_row2[3]
        matrix[n-1][4] = new_row2[4]
        pp.pprint(matrix)
        matrix[0][n-1] = new_row3[4]
        matrix[1][n-1] = new_row3[3]
        matrix[2][n-1] = new_row3[2]
        matrix[3][n-1] = new_row3[1]
        matrix[4][n-1] = new_row3[0]
        pp.pprint(o)
        pp.pprint(matrix)
        return

if __name__ == '__main__':
    unittest.main()
