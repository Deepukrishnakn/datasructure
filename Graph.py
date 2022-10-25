
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



nodes=[]
graph=[]
node_count=0
add_Vertex("A")
add_Vertex("B")
print(nodes)
print(graph)
