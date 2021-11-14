def zeroMatrix(matrix):
    columnIndex = [False] * len(matrix[0])
    rowIndex = [False] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rowIndex[i] = True
                columnIndex[j] = True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rowIndex[i]:
                matrix[i][j] = 0

    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if columnIndex[j]:
                matrix[i][j] = 0

matrix = [[1,2,0],[1,1,1],[0,1,1]]
print(matrix)
zeroMatrix(matrix)
print(matrix)