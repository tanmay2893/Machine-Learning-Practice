import matplotlib.pyplot as plt
import random
import numpy as np
#x=[0,0,1,1,0.5,5,5,6,6,5.5]
plt.axis([-1, 21, -1, 21])
#y=[0,1,1,0,0.5,5,6,6,5,5.5]
#points=[(0,0),(0,1),(1,0),(1,1),(0.5,0.5),(5,5),(5,6),(6,6),(6,5),(5.5,5.5)]
#f=open('data.txt').readlines()
#import ast
#x=ast.literal_eval(f[0])
#print x[0]
#y=ast.literal_eval(f[1])
#print y[0]
#l=len(x)
#points=[]
#for i in range(l):
#    points+=[(x[i],y[i])]
points=[(0,0),(0,1),(19,0),(20,0),(8,20),(9,20),(1,11),(2,11),(10,5),(10,6)]
x,y=[],[]
for i in points:
    x+=[i[0]]
    y+=[i[1]]

#initializing partitions
k=2
len_points=len(points)
def seed_points(k):
    global len_points
    answer=[]
    global points
    r=random.choice(points)
    #print r
    answer+=[r]
    prob=[]
    count=1
    while count<k:
        prob=[]
        for i in points:
            temp=[]
            for j in answer:
                x=distance(i,j)
                temp+=[x]
            prob+=[min(temp)]
        s=sum(prob)
        #print prob
        index=prob.index(max(prob))
        #print index
        x=points[index]
        #print points
        #print prob
        for i in range(len(prob)):
            prob[i]/=float(s)
        #print prob
        #x=points[np.random.choice(np.arange(len_points),p=prob)]
        answer+=[x]
        #print x
        count+=1
    return answer
    '''
    raw_input('')
    for i in range(k):
        a=random.uniform(0,21)
        b=random.uniform(0,21)
        answer+=[(a,b)]
    #print answer
    #return points[:k]
    return answer
    '''

def distance(x,y):
    dis=(((x[0]-y[0])**2)+((x[1]-y[1])**2))**0.5
    return dis


def find_clusters(points,cluster_centers):
    global k
    clusters=[[] for i in range(k)]
    for i in points:
        dis=[]
        #print '********************'
        #print i
        for j in cluster_centers:
            #print j
            tanmay=distance(i,j)
            #print tanmay
            dis+=[tanmay]
        
        minimum=min(dis)
        position=dis.index(minimum)
        clusters[position]+=[i]
        #print clusters
        #print 'asdfkjasdlkfjlksdafjlkkasdjfa'
    return clusters


def compute_new_center(points):
    l=len(points)
    x,y=[],[]
    for i in range(l):
        x+=[points[i][0]]
        y+=[points[i][1]]
    #print x
    #print y
    try:
        new_x=float(sum(x))/float(l)
        new_y=float(sum(y))/float(l)
        return (new_x,new_y)
    except:
        return False
    #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    #print new_x
    #print new_y

def plot_cluster_centers():
    global clusters,new_cluster_centers,points,cluster_centers
    global x,y
    plt.axis([-1, 21, -1, 21])
    plt.plot(x,y,'ro')
    w,b=[],[]
    #print cluster_centers
    for i in cluster_centers:
        w+=[i[0]]
        b+=[i[1]]
    plt.plot(w,b,'bo')
    plt.show()

cluster_centers=seed_points(k)
clusters=find_clusters(points,cluster_centers)
new_cluster_centers=[]
for i in clusters:
    answer=compute_new_center(i)
    if answer:
        new_cluster_centers+=[answer]
#print new_cluster_centers
#print clusters
#print cluster_centers
#print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
plot_cluster_centers()
while new_cluster_centers!=cluster_centers:
    #print new_cluster_centers
    cluster_centers=new_cluster_centers
    clusters=find_clusters(points,new_cluster_centers)
    #print 'asdfafasfdasdfasdf'
    #print clusters
    new_cluster_centers=[]
    for i in clusters:
        answer=compute_new_center(i)
        if answer:
            new_cluster_centers+=[answer]
    #print new_cluster_centers
    plot_cluster_centers()
cluster_centers=new_cluster_centers
plot_cluster_centers()
colors=['bo','ro','go','co','mo','yo','ko']
counter=0
plt.axis([-1, 21, -1, 21])
for i in clusters:
    x=[]
    y=[]
    for j in i:
        x+=[j[0]]
        y+=[j[1]]
    #print x
    #print y
    plt.plot(x,y,colors[counter])
    #print '@@@@@@@@@@@@@@@@@@@'
    counter+=1
plt.show()
