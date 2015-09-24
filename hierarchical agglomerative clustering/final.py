import matplotlib.pyplot as plt
x=[0,1,3,2,6,6,5,3,0,2]
y=[0,1,1,4,3,6,2,5,2,1]
points=[(0,0),(1,1),(3,1),(2,4),(6,3),(6,6),(5,2),(3,5),(0,2),(2,1)]
clusters=[]
for i in points:
    clusters+=[[i]]
clusters=points
def distance(x,y):
    dis=(((x[0]-y[0])**2)+((x[1]-y[1])**2))**0.5
    return dis
minimum_distance=100000000
def distance_matrix():
    matrix=[]
    global points
    l=len(points)
    global minimum_distance
    minimum=[]
    dis=[]
    dis_points=[]
    for i in range(l):
        sub=[]
        for j in range(i+1,l):
            a=distance(points[i],points[j])
            dis+=[a]
            dis_points+=[[points[i],points[j]]]
            if a<minimum_distance:
                minimum_distance=a
                minimum=[points[i],points[j]]
            sub+=[a]
        matrix+=[sub]
    my=[b for (a,b) in sorted(zip(dis,dis_points))]
    return my
check_dict={(0,0):0,(1,1):1,(3,1):2,(2,4):3,(6,3):4,(6,6):5,(5,2):6,(3,5):7,(0,2):8,(2,1):9}
def update_clusters(minimum):
    global clusters,check_dict
    answer=[]
    remove_list=[]
    keys=[]
    for i in minimum:
        x=check_dict[i]
        for key in check_dict:
            if check_dict[key]>x:
                keys+=[key]
        answer+=[clusters[x]]
        print clusters
        print x
        remove_list+=[x]
    print answer
    print 'asdfasdfasdfasdfasdf'
    for index in sorted(remove_list, reverse=True):
        del clusters[index]
    clusters.append(answer)
    for i in minimum:
        check_dict[i]=len(clusters)-1
    for i in keys:
        if i not in minimum:
            check_dict[i]-=1
    print check_dict
        
#minimum=distance_matrix()
#update_clusters(minimum)
#print clusters
basis=distance_matrix()
#print basis
l=len(points)
#print l
for i in range(l-1):
    minimum=basis[i]
    print 'asdfasdf'
    print minimum
    update_clusters(minimum)
    print clusters
    raw_input('')

