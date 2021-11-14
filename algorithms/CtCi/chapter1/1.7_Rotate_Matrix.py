def rotateMatrix90(matrix):
    n = len(matrix)
    mid1 = n // 2
    if n % 2 == 0:
        mid2 = mid1
    else:
        mid2 = mid1 + 1
    for i in range(mid1):
        for j in range(mid2):
            #print (i,j)
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n-i-1]
            matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
            matrix[n-j-1][i] = temp


#matrix = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
matrix = [[11,12,13],[21,22,23],[31,32,33]]
print(matrix)
rotateMatrix90(matrix)
print(matrix)