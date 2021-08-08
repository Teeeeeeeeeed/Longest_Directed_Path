import sys

def topoSort(graph):
    stack=[]
    n=len(graph)
    color=["w" for i in range(n)]
    order=[]
    for i in range(0,n):   #this is how the white vertices are picked will need to change for 
        if color[i]=="w":
            color[i]="g"
            stack.append(i)
            while len(stack)>0:
                node=stack[-1]
                hasNext=False
                for j in range(0,n):                          #Goes through each row of matrix to find all children of the current node
                    if (graph[node][j]==1 and color[j]=="w"): #if node has white child put it to the front of stack
                        color[j]="g"
                        stack.append(j)
                        hasNext=True
                        break
                if hasNext==False:
                    order.insert(0,stack.pop())
                    color[node]="b"
    return order

def dfsOrdered(graph,order):
    m=order.index(0)
    stack=[]
    n=len(graph)
    color=["w" for i in range(n)]
    maxDepth=0
    depth=0
    color[0]="g"
    stack.append(0)
    while len(stack)>0:
        node=stack[-1]
        hasNext=False
        for j in range(m,n):                     
            end=order[j]
            if (graph[node][end]==1 and color[end]=="w"): #if node has white child put it to the front of stack
                color[end]="g"
                stack.append(end)
                hasNext=True
                depth+=1
                if depth>maxDepth:
                    maxDepth=depth
                break
        if hasNext==False:
            stack.pop()
            color[node]="b"
            depth-=1
    return maxDepth


for line in sys.stdin:
    n=int(line)
    if n==0:
        break
    matrix=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        arc = input().strip()
        if arc == "\r\n" or arc=="\n":
            pass
        else:
            arc=arc.split()
            for x in arc:
                matrix[i][int(x)]=1
    order = topoSort(matrix)
    depth = dfsOrdered(matrix,order)
    print(depth)