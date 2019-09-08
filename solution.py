from typing import List
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [i for i, row in enumerate(matrix) if 0 in row]
        cols = [i for i, col in enumerate(zip(*matrix)) if 0 in col]

        emptyRow = [0] * len(matrix[0])
        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = emptyRow
            else:
                for j in cols:
                    matrix[i][j] = 0
