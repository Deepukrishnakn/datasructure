#Adjacency Matrix-------------------------------------

def add_Vertex(v):
    global node_count
    if v in nodes:
        print(v,'vertex is allready in the graph')
    else:
        node_count = node_count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'is not in graph')
    elif v2 not in nodes:
        print(v2,'is not in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph [index1][index2]=1
        graph [index2][index1]=1
        
def graph_by_matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=' ')
        print()


nodes=[]
graph=[]
node_count=0
add_Vertex("A")
add_Vertex("B")
add_edge("A","D")
print(nodes)
print(graph)
graph_by_matrix()