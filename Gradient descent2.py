import numpy as np
import matplotlib.pyplot as plt

def Read():
    global X, Y, n
    file = open('gradientsample2.inp')
    content = file.readlines()
    n = int(content[0].strip())
    content.pop(0)
    X = np.full((n,3),1,dtype = np.float64)
    Y = np.zeros((n,1),dtype = np.float64)
    for i in range(len(content)):
        tmp = content[i].strip('\n').split()
        X[i,1] = float(tmp[0])
        X[i,2] = X[i,1]**2
        Y[i,0] = float(tmp[1])
        #plt.plot(X[i,1], Y[i,0], 'ob', markersize = 5)
        #maxc = max(maxc,float(tmp[0]),float(tmp[1]))
    file.close()

def Gradient():
    global X, Y, W, n
    file = open('gradientdata.out')
    tmp = file.read().split()
    W = np.array([[float(tmp[0])],[float(tmp[1])],[float(tmp[2])]], dtype = np.float64)
    file.close()
    #W = np.zeros((3,1),dtype = np.float64)
    #W = np.array([[0.11035629],[-35.50975537],[0.52569422]],dtype = np.float64)
    numiter = 100000
    learnrate = 0.0000000022
    loss = []
    for i in range(numiter):
        tmp = X.dot(W) - Y
        W[0] -= learnrate*np.sum(tmp)
        W[1] -= learnrate*np.sum(X[:,1].reshape(-1,1)*(tmp))
        W[2] -= learnrate*np.sum(X[:,2].reshape(-1,1)*(tmp))
        #loss.append(0.5*np.sum(tmp*tmp))
        #if len(loss)>1: print(loss[len(loss)-2]-loss[len(loss)-1],loss[len(loss)-1])
        #if i%1000==0: Plot(i)
    Plotres()
    print(0.5*np.sum(tmp*tmp))
    file = open('gradientdata.out','w')
    file.write('%.16f %.16f %.16f'%(W[0],W[1],W[2]))

def Plotres():
    global X, Y, W, n
    plt.clf()
    plt.scatter(X[:,1], Y.reshape(-1), color = 'blue', marker = 'o', s = 5)
    x = np.arange(X[0,1], X[n-1,1], 0.01)
    y = W[0] + W[1]*x + W[2]*x**2
    plt.plot(x,y,'r')
    plt.show()
    
def Plot(it):
    global X, Y, W
    plt.clf()
    #plt.axis([-5,maxc+5,-5,maxc+5])
    plt.title('Iteration %d'%it)
    plt.scatter(X[:,1], Y.reshape(-1), color = 'blue', marker = 'o', s = 5)
    x = np.arange(X[0,1], X[n-1,1], 0.01)
    y = W[0] + W[1]*x + W[2]*x**2
    plt.plot(x,y,'r')
    plt.draw()
    plt.pause(0.001)
    
n = 0
#---------- main -----------#
Read()
plt.ion()
plt.show(block = False)
Gradient()
#input()
#---------------------------#

#ax^2+bx+c-y
#x*(ax^2+bx+c-y)
#x^2*(ax^2+bx+c-y)
