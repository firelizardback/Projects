from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        ml = len(matrix)
        nl = len(matrix[0])
        for m in range(ml):
            for n in range(nl):
                if (matrix[m][n] == 0):
                    row.add(m)
                    col.add(n)
        while(row):
            matrix[row.pop()] = [0] * nl
        while(col):
            val = col.pop()
            for m in range(ml):
                matrix[m][val] = 0   

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] 
Solution().setZeroes(matrix)
print(matrix)      