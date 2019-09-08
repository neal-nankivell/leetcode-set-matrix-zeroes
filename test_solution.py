import solution
import unittest

'''
Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''


class Test_TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_setZeroes(self):
        input = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        expectedOutput = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]

        self.sut.setZeroes(input)

        self.assertEqual(input, expectedOutput)


if __name__ == '__main__':
    unittest.main()
