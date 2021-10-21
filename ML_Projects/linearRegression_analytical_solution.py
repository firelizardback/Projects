import numpy as np

def linearRegression(X,y):
    XT = np.transpose(X)
    return(np.matmul(np.linalg.inv(np.matmul(XT,X)),np.matmul(XT,y)))

#arr1 = list(map(float,input().strip().split()))
#arr2 = list(map(float,input().strip().split()))

arr2 = [10,25,17,11,13,17,20,13,9,15]
arr1 = [15,12,8,8,7,7,7,6,5,3] 

X0 = np.ones((len(arr1),1))
#print (X0)
#X  = np.array(arr1)
X = np.reshape(np.array(arr1),(len(arr1),1))
#print(X)
#print(XT)
Xnew = np.hstack((X0,X))
#print(Xnew)
y = np.array(arr2)
#print(y)
print(linearRegression(Xnew,y))