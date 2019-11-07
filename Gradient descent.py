import numpy as np
import matplotlib.pyplot as plt

def Read():
    global X, Y, maxc, n
    file = open('gradientsample.inp')
    content = file.readlines()
    n = int(content[0].strip())
    content.pop(0)
    X = np.full((n,2),1,dtype = np.float64)
    Y = np.zeros((n,1),dtype = np.float64)
    for i in range(len(content)):
        tmp = content[i].strip('\n').split()
        X[i,1] = float(tmp[0])
        Y[i,0] = float(tmp[1])
        plt.plot(X[i,1], Y[i,0], 'ob', markersize = 5)
        maxc = max(maxc,float(tmp[0]),float(tmp[1]))
    file.close()

def Gradient():
    global X, Y, W, n
    W = np.zeros((2,1),dtype = np.float64)
    numiter = 100
    learnrate = 0.00005
    loss = []
    for i in range(numiter):
        tmp = X.dot(W) - Y
        W[0] -= learnrate*np.sum(tmp)
        W[1] -= learnrate*np.sum(X[:,1].reshape(-1,1)*(tmp))
        loss.append(0.5*np.sum(tmp*tmp))
        #Plot(i)
    plt.plot((X[0,1], X[n-1,1]),(W[0] + W[1]*X[0,1],W[0] + W[1]*X[n-1,1]), 'r')
    plt.show()
    #print(loss)

def Plot(it):
    global X, Y, W
    plt.clf()
    #plt.axis([-5,maxc+5,-5,maxc+5])
    plt.title('Iteration %d'%it)
    for i in range(n):
        plt.plot(X[i,1], Y[i,0], 'ob', markersize = 5)
    plt.plot((X[0,1], X[n-1,1]),(W[0] + W[1]*X[0,1],W[0] + W[1]*X[n-1,1]), 'r')
    plt.draw()
    plt.pause(0.001)
    
maxc = 0.0
n = 0
#---------- main -----------#
Read()
plt.ion()
plt.show(block = False)
Gradient()
#input()
#---------------------------#
