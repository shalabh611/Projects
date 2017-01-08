path='C:\\Users\\Shalabh\\Desktop\\books\\2nd_sem\\AI\\assignment2\\distance.csv'

def makeDictionary():
    dict={}
    list=[]
    count=0
    with open(path) as entry:
        for line in entry:
            count=count+1
            arr=line.split(',')
            if (count == 1):
                list.append(arr[0])
                list.append(arr[1])
            elif (count > 1):
                flag0=0;
                flag1=0;
                for item in list:
                    if (arr[0]==item):
                        flag0=1
                        break
                for item in list:
                    if (arr[1]==item):
                        flag1=1
                        break
                if (flag0==0):
                    list.append(arr[0])
                if (flag1==0):
                    list.append(arr[1])
    #print "The list is ",list
    for item in list:
        dict1={}
        with open(path) as entry:
            for line in entry:
                arr=line.split(',')
                cost=int(arr[2])
                if (item in arr[0]):
                    dict1.update({arr[1]:cost})
                elif (item in arr[1]):
                    dict1.update({arr[0]:cost})
        dict.update({item:dict1})
    #print "The dictionary is ",dict
    return dict

def bfs(source,dest):
    class Node:
        def __init__(self,cost,list,name):
            self.cost=cost
            self.list=list
            self.name=name
    dict_bfs={}
    child_bfs={}
    list_explored=[]
    list_discovered=[]
    dict_bfs=makeDictionary()
    first=Node(0,[],source)
    start=Node(None,None,None)#initialize an empty object reference
    index=-1
    list_discovered.append(first)
    while (len(list_discovered)!=0):
        index=index+1
        start=list_discovered[index]
        if start.name in dest:
            start.list.append(dest)
            list_explored.append(start)
            print "Congrats !!!  The destination was reached via BFS !!!!!!!!"
            print "The cost of travelling from ",source," to ",dest," is ",start.cost
            print "The route followed was ", start.list
            return
        for i in  dict_bfs:
            if i in start.name:
                child_bfs=dict_bfs[i]
                for j in child_bfs:#check if a node to be added(j) in the discovered list has already been traversed or not
                    found=0
                    if (len(list_explored)!=0):
                        for k in list_explored:
                            if k.name in j:
                                found=1
                                break;
                    if list_discovered:
                        for k in list_discovered:
                            if k.name in j:
                                found=1
                                break;
                    if (found==0):
                        temp_list=[]
                        spend=0
                        temp1=Node(0,None,None)
                        for l in list_discovered:
                            if l.name in start.name:
                                temp1=l
                        spend=temp1.cost+child_bfs[j]
                        for l in temp1.list:
                            temp_list.append(l)
                        temp_list.append(i)
                        temp=Node(spend,temp_list,j)
                        list_discovered.append(temp)
        list_explored.append(temp)
    return

def dfs(source,dest,list_explored=[]):
    class Node:
        def __init__(self,cost,list,name):
            self.cost=cost
            self.list=list
            self.name=name
    #initialize an empty object reference
    start=Node(None,None,None)
    list_discovered=[]
    dict_dfs=makeDictionary()
    if (len(list_explored)==0):
        last=Node(0,[],source)
    else:
        last=Node(None,None,None)
        last=list_explored[len(list_explored)-1]
    list_discovered.append(last)
    if (len(list_discovered)!=0):
        start=list_discovered[0]
        #print "start.name=",start.name
        if start.name in dest:
            start.list.append(dest)
            list_explored.append(start)
            print "Congrats !!!  The destination was reached via DFS !!!!!!!!"
            print "The cost of travelling from ",start.list[0]," to ",dest," is ",start.cost
            print "The route followed was ", start.list
            return
        if (len(list_explored)==0):
            list_explored.append(start)
        for i in  dict_dfs:
            if i in start.name:
                child_dfs=dict_dfs[i]
                for j in child_dfs:#check if a node to be added(j) in the discovered list has already been traversed or not
                    found=0
                    if (len(list_explored)!=0):
                        for k in list_explored:
                            if k.name in j:
                                found=1
                                break;
                    if list_discovered:
                        for k in list_discovered:
                            if k.name in j:
                                found=1
                                break;
                    if (found==0):
                        temp_list=[]
                        spend=0
                        temp1=Node(0,None,None)
                        for l in list_discovered:
                            if l.name in start.name:
                                temp1=l
                        spend=temp1.cost+child_dfs[j]
                        for l in temp1.list:
                            temp_list.append(l)
                        temp_list.append(i)
                        temp=Node(spend,temp_list,j)
                        list_explored.append(temp)
                        dfs(j,dest,list_explored)
    return

def LDFS(source,dest,limit=10,list_explored=[]):
    class Node:
        def __init__(self,cost,list,name):
            self.cost=cost
            self.list=list
            self.name=name
    #initialize an empty object reference
    if (len(list_explored)==0):
        last=Node(0,[],source)
    else:
        last=Node(None,None,None)
        last=list_explored[len(list_explored)-1]
    if limit>=0:
        if last.name in dest:
            last.list.append(dest)
            list_explored.append(last)
            print "Congrats !!!  The destination was reached via IDFS !!!!!!!!"
            print "The cost of travelling from ",last.list[0]," to ",dest," is ",last.cost
            print "The route followed was ", last.list
            return 0
        else:
            if (len(list_explored)==0):
                list_explored.append(last)
            dict_ldfs=makeDictionary()
            for key in  dict_ldfs:
                if last.name in key:
                    child_ldfs=dict_ldfs[key]
                    list_discovered=[]
                    for key1 in child_ldfs:
                        found=0
                        if (len(list_explored)!=0):
                            for k in list_explored:
                                if k.name in key1:
                                    found=1
                                    break;
                        if (found==0):
                            temp_list=[]
                            spend=0
                            temp1=Node(0,None,None)
                            temp1=last
                            spend=temp1.cost+child_ldfs[key1]
                            for l in temp1.list:
                                temp_list.append(l)
                            temp_list.append(last.name)
                            temp=Node(spend,temp_list,key1)
                            list_explored.append(temp)
                            list_discovered.append(key1)
            for item in list_discovered:
                LDFS(item,dest,limit-1,list_explored)
    elif limit<0:
            return -1


def idfs(source,dest,limit=5):
    flag=0
    for i in range(limit):
        flag=LDFS(source,dest,i)
        #print  flag
        if flag==0:
            return




#idfs("Arad","Bucharest")
#idfs("Sibiu","Eforie")
#idfs("Drobeta","Fagaras")
idfs("Oradea","Hirsova")
#bfs("Neamt","Giurgiu")
#dfs("Arad","Bucharest")
#dfs("Sibiu","Eforie")
#dfs("Drobeta","Fagaras")
#dfs("Oradea","Hirsova")