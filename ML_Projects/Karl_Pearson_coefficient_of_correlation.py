import numpy as np
from math import sqrt

n = int(input())
arr1 = input()   
l1 = list(map(int,arr1.split(' ')))

arr2 = input()   
l2 = list(map(int,arr2.split(' ')))

#phy_sc = [15,12,8,8,7,7,7,6,5,3]
#his_sc = [10,25,17,11,13,17,20,13,9,15]

phy_sc = l1
his_sc = l2

phy_sc_mean = np.mean(phy_sc)
his_sc_mean = np.mean(his_sc)

xy = 0
x2 = 0
y2 = 0
for i in range(len(phy_sc)):
    xy = xy + (phy_sc[i] - phy_sc_mean) * (his_sc[i] - his_sc_mean)
    x2 = x2 + (phy_sc[i] - phy_sc_mean) * (phy_sc[i] - phy_sc_mean)
    y2 = y2 + (his_sc[i] - his_sc_mean) * (his_sc[i] - his_sc_mean)
    
res = xy / sqrt (x2 * y2)
print(res)