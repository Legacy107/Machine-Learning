import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def read():
    global X, X2, Y, n
    file = open('logistic regression.csv')
    data = list(csv.reader(file))
    X = np.full((n,3), 1, dtype = np.float64)
    Y = np.zeros((n,1), dtype = np.float64)
    for i in range(n):
        X[i,1] = float(data[i][0])
        X[i,2] = float(data[i][1])
        Y[i,0] = float(data[i][2])

def regression():
    global X, X2, Y, W
    numiter = 1000
    learnrate = 0.01
    for i in range(numiter):
        tmp = sigmoid(X.dot(W)).reshape(-1,1) - Y
        W[0] -= learnrate*np.sum(tmp)
        W[1] -= learnrate*np.sum(X[:,1].reshape(-1,1)*(tmp))
        W[2] -= learnrate*np.sum(X[:,2].reshape(-1,1)*(tmp))
        ypre = sigmoid(X.dot(W))
        #print(W)
        #print(-np.sum(np.log(ypre)*Y) + np.sum((1-Y)*np.log(1-ypre)))

def plotres():
    global X, Y, W, n
    t = 0.5
    plt.clf()
    plt.xlabel('mức lương (triệu)')
    plt.ylabel('kinh nghiệm (năm)')
    plt.scatter(X[0:9,1], X[0:9,2], color = 'green', marker = 'o', s = 20)
    plt.scatter(X[10:19,1], X[10:19,2], color = 'red', marker = 'o', s = 20)
    plt.plot((4,10),(-(W[0]+4*W[1]+np.log(1/t-1))/W[2],-(W[0]+10*W[1]+np.log(1/t-1))/W[2]),'b')
    #x = np.arange(4, 10, 0.01)
    #y = (W[0] + W[1]*x)/(-W[2])
    #plt.plot(x,y,'b')
    plt.show()

#########main############
n=20
W = np.array([0.,0.1,0.1], dtype = np.float64)
read()
regression()
plotres()
