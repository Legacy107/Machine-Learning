#! python3
import math
import matplotlib.pyplot as plt
import copy

def Read():
    global n, data, maxc
    file = open('data.inp')
    content = file.readlines()
    n = int(content[0].strip())
    content.pop(0)
    for i in content:
        tmp = i.strip('\n').split()
        data.append((float(tmp[0]),float(tmp[1])))
        maxc = max(maxc,float(tmp[0]),float(tmp[1]))
    file.close()

def Dis(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

def Kmean():
    global n, m, data, centroid, num
    num = [-1]*n
    last = copy.deepcopy(centroid)
    it = 0
    while True:
        it += 1
        if it > maxit: break
        tmp = [[0.0 for i in range(2)] for j in range(m)]
        cnt = [0]*m
        d = 0.0
        f = True
        for i in range(n):                
            ind = 0
            mi = Dis(data[i][0],data[i][1],centroid[0][0],centroid[0][1])
            for j in range(m):
                d = Dis(data[i][0],data[i][1],centroid[j][0],centroid[j][1])
                if d<mi:
                    ind = j
                    mi = d
            num[i] = ind
            tmp[ind][0] += data[i][0]
            tmp[ind][1] += data[i][1]
            cnt[ind]+=1
        for i in range(m):
            if cnt[i]!=0:
                centroid[i][0] = tmp[i][0]/cnt[i]
                centroid[i][1] = tmp[i][1]/cnt[i]
        if last == centroid: break
        else: last = copy.deepcopy(centroid)
        Plot(it)
            
def Write():
    global m, centroid
    file = open('data.out','w')
    for i in range(m):
        file.write('%.3f %.3f\n'%(centroid[i][0],centroid[i][1]))

def Plot(it):
    global n, m, centroid, data, num
    plt.clf()
    plt.axis([-5,maxc+5,-5,maxc+5])
    plt.title('Iteration %d'%it)
    for i in range(n):
        plt.plot(data[i][0],data[i][1],form[num[i]],markersize=10)
    for i in range(m):
        plt.plot(centroid[i][0],centroid[i][1],'*r',markersize=10)
    plt.draw()
    plt.pause(0.1)
        
data = []
n = 0  # point
m = 3  # centroid
centroid = [[0.0 for i in range(2)] for j in range(m)]
num = []
form = ['ob','og','oy']
maxc = 0.0  # max cord
maxit = 100 # max iteration

#---------- main -----------#
Read()
plt.ion()
plt.show(block = False)
Kmean()
Write()
#input()
#---------------------------#
