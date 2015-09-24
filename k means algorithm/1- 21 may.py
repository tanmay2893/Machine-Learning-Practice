import matplotlib.pyplot as plt
#x=[0,0,1,1,0.5,5,5,6,6,5.5]
x=[0,0,1,2,3,4,4,5,10,10]
y=[0,1,6,6,0,0,11,11,5,6]
plt.axis([-1, 15, -1, 15])
#y=[0,1,1,0,0.5,5,6,6,5,5.5]
#points=[(0,0),(0,1),(1,0),(1,1),(0.5,0.5),(5,5),(5,6),(6,6),(6,5),(5.5,5.5)]
points=[(0,0),(0,1),(1,6),(2,6),(3,0),(4,0),(4,11),(5,11),(10,5),(10,6)]

#initializing partitions
k=5
def seed_points(k):
    global points
    return points[:k]

def distance(x,y):
    dis=(((x[0]-y[0])**2)+((x[1]-y[1])**2))**0.5
    return dis

cluster_centers=seed_points(k)

def find_clusters(points,cluster_centers):
    global k
    clusters=[[] for i in range(k)]
    for i in points:
        dis=[]
        #print '********************'
        #print i
        for j in cluster_centers:
            #print j
            dis+=[distance(i,j)]
        minimum=min(dis)
        position=dis.index(minimum)
        clusters[position]+=[i]
        #print clusters
    return clusters


def compute_new_center(points):
    l=len(points)
    x,y=[],[]
    for i in range(l):
        x+=[points[i][0]]
        y+=[points[i][1]]
    #print x
    #print y
    new_x=float(sum(x))/float(l)
    new_y=float(sum(y))/float(l)
    return (new_x,new_y)
    #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    #print new_x
    #print new_y

clusters=find_clusters(points,cluster_centers)
new_cluster_centers=[]
for i in clusters:
    new_cluster_centers+=[compute_new_center(i)]
print new_cluster_centers
print clusters
print cluster_centers
print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
while new_cluster_centers!=cluster_centers:
    print new_cluster_centers
    cluster_centers=new_cluster_centers
    clusters=find_clusters(points,new_cluster_centers)
    print 'asdfafasfdasdfasdf'
    print clusters
    new_cluster_centers=[]
    for i in clusters:
        new_cluster_centers+=[compute_new_center(i)]
    print new_cluster_centers
    print 
plt.plot(x, y, 'ro')
plt.show()
colors=['bo','ro','go','co','mo','yo']
counter=0
plt.axis([-1, 15, -1, 15])
for i in clusters:
    x=[]
    y=[]
    for j in i:
        x+=[j[0]]
        y+=[j[1]]
    print x
    print y
    plt.plot(x,y,colors[counter])
    print '@@@@@@@@@@@@@@@@@@@'
    counter+=1
plt.show()
