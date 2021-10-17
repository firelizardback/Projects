# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn.linear_model import LinearRegression
import numpy as np

[F,H] = list(map(int,input().split(' ')))
train_data = []
for i in range(H):
    train_data.append(list(map(float,input().split(' '))))

T = int(input())
test_data = []
for i in range(T):
    test_data.append(list(map(float,input().split(' '))))        
#print(train_data)
#print(test)

td = np.array(train_data)

X = td[:,:-1]
y = td[:,-1]
#print(y)
reg = LinearRegression().fit(X,y)

X_test = np.array(test_data)
y_test = reg.predict(X_test)
for i in y_test:
    print("%.2f" % i)
#print(y_test)