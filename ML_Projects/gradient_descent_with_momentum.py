import numpy as np
import matplotlib.pyplot as plt
from random import random 
import itertools

class gradient_descent:

    def __init__(self,X,y, add0 = True, c2r = True) -> None:
        if add0:
            self.X = self.add_column0(X)
        else:
            self.X = X
        if c2r:
            self.y = self.col2row(y)
        else:
            self.y = y
        self.ax=plt.gca()
        #print(self.X)
        #print(self.y)
    
    def add_column0(self,X):
        X0 = np.ones((len(X),1))
        return(np.hstack((X0,X)))

    def col2row(self,y):
        return(np.reshape(y,(len(y),1)))

    def der(self,x,st):
        pass
    
    def delt(self,theta,st):
        der = []
        #print(theta)
        for i in range(len(theta)):
            vr = theta[0:i]+[theta[i]+st]+theta[i+1:]
            vl = theta[0:i]+[theta[i]-st]+theta[i+1:]
            #print(vl,vr)
            #ss = func(theta[0:,i]+[theta[i]+st]+theta[i+1:])
            der.append((self.func(vr)-self.func(vl))/(2.0*st))
        #print(der)
        return(der)

    def findmin_gd(self,theta0,lr,st,thr,gamma):
        theta = theta0
        li = self.delt(theta,st)
        dd = [i * lr for i in li]
        j = 0
        #print(theta)
        #print("dd",dd)
        #print("li",li)
        v = np.array(dd)
        while (abs(max(li, key=abs)) > thr):            
            theta = list(np.array(theta) - v)
            li = self.delt(theta,st)
            dd = [i * lr for i in li]
            j += 1
            v =  np.array(dd) + v * gamma
            self.ax.plot(theta[0], theta[1],'+')
            #print(theta)
            #print("dd",dd)
            #print("li",li)
        #plt.show()
        print(theta)
        print(j)
        
    
    def func(self,theta):
        M = np.matmul(self.X,self.col2row(theta))-self.y
        return(float(np.matmul(np.transpose(M),M)/(2*len(self.y))))
    
    def funcxy(self,x,y):
        return(self.func([x,y]))

    def draw(self):
        delta = 0.05
        xp = np.arange(-20, 20 + delta, delta)
        yp = np.arange(-5, 5 + delta, delta)
        #xp = np.linspace(-3,delta,3)
        #yp = np.linspace(-3,delta,3)

        #X, Y = np.meshgrid(xp, yp)
        #Z = self.funcxy(X, Y)
        #plt.contour(X, Y, Z, colors='black');


        #print(xp)
        #X, Y = np.meshgrid(x, y)
        #print (X)
        #print (Y)
        zp = np.ndarray((len(yp),len(xp)))
        for x in range(0,len(xp)):
            for y in range(0,len(yp)):
                zp[y][x] = self.funcxy(xp[x],yp[y])
                #zp[x][y] = self.funcxy(1+random(),1+random())
        #print(zp)
        #print(self.funcxy(X,Y))
        #Z = self.funcxy(X,Y) 
        #X, Y = np.meshgrid(xp, yp)
        #plt.figure(figsize=(7, 5))
        #plt.title('Contour Plot')
        rr = itertools.chain(range(10), range(10,100,10))
        rr = itertools.chain (rr, range(100,300,50))
        contours = self.ax.contourf(xp, yp, zp, [i for i in rr])
        #plt.clabel(contours, inline=1, fontsize=12)        
        #fig, ax = plt.subplots()
        #CS = ax.contour(X, Y, self.func())


#X = np.array([[1],[3],[6],[9]])
#y = np.array([1,3,5,7])
arr1 = [15,12,8,8,7,7,7,6,5,3]
arr2 = [10,25,17,11,13,17,20,13,9,15]
X = np.reshape(np.array(arr1),(len(arr1),1))
y = np.array(arr2)

X = np.array([[1],[3],[5],[7]])
y = np.array([1,3,5,7])

gd = gradient_descent(X,y)

#print(gd.func(np.array([[0],[1]])))

#print(gd.func([0,1]))

gd.draw()

gd.findmin_gd([10,10],0.05,0.01,0.001,0.8) # with momentum

#gd.findmin_gd([10,10],0.09,0.01,0.001,0.0) # without momentum

plt.show()

#gd.draw()




#print(gd.func(np.array([[13.375],[0.2083333]])))

#print(gd.func(np.array([[13.0],[0.2083333]])))

#print(gd.func(np.array([[13.375],[0.22]])))

#print(gd.func(np.array([[13.375],[0.19]])))

# print(gd.func(np.array([[14],[0.2083333]])))