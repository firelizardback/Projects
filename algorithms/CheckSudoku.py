from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print(board[0])
        for i in board:
            int1 = [int(item.replace('.','0')) for item in i]
            #print(int1)
            if (not self.checkRepetition(int1)):
                return False
            
        for j in range(9):
            da = [row[j] for row in board]
            int1 = [int(item.replace('.','0')) for item in da]
            #print(int1)
            if (not self.checkRepetition(int1)):
                return False
            
        for i in range(3):
            for j in range(3):
                da = [row[i*3:i*3+3] for row in board[j*3:j*3+3]]
                flatList = [item for elem in da for item in elem]        
                int1 = [int(item.replace('.','0')) for item in flatList]
                #print(int1)
                if (not self.checkRepetition(int1)):
                    return False
 
        return(True)
        
    def checkRepetition(self, data):
        arr = [0] * 10
        for i in data:
            if(arr[i] == 0):
                arr[i] = 1
            else:
                if(i != 0):
                    return False
        return True

input_data = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print((Solution().isValidSudoku(input_data)))
