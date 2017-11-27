"""
Andrew Gray, John Piermatteo, Wesley Morlock
Homework 05
Main
11/13/2017
"""
from testFileWriter import *
from max_flow_generator import *

def main():
    for z in range(10):
        g = FlowNetwork()
        g.addVertex('0', True, False)   ##source
        g.addVertex('6',False,True)     ##sink

        r = test_network_generator()
        vertices = r[1]
        print("vertices: " + str(vertices) + "\n")
        vertices.remove('0')
        vertices.remove('6') ##sometime 6 ins't a vertex -> will give error

        for s in vertices:
            g.addVertex(s) 
        x = r[0]
        for i in range(len(x)):
            g.addEdge(x[i][0],x[i][1],x[i][2])
            
        file_name = "my_graph_" + str(z)
        write_dot_file(r[0], file_name)  

        max_edges = g.getMaxEdges()

        print('vertices: ' + str([vertex.name for vertex in g.vertices]) + '\n')
        print('edges: ' + str(['%s -> %s; %s/%s' % (e.start, e.end, e.flow, e.capacity) for e in g.getEdges()])+ '\n')
        print('max flow: ' + str(g.calculateMaxFlow()) + '\n')
        print('max edges: ' + str(max_edges))

        file_name = "max_edges_" + str(z)
        write_dot_file(max_edges, file_name)

main()

def main() :
   #assume, X is your graph.
   
       # X = [(1, 2, 4), (2, 3, 9), (3, 2, 4), (3, 3, 1)]
       X = test_network_generator()
       file_name = "my_graph_" + str(i)
       write_dot_file(X, file_name)   
   # done 



##def main():
##    g = FlowNetwork()
##    g.addVertex('1', True, False)   ##source
##    g.addVertex('6',False,True)     ##sink
##    vertices = ['2', '3', '4', '5']
##    for s in vertices:
##        g.addVertex(s)
##    g.addEdge('1', '2', 5)
##    g.addEdge('1', '3', 10)
##    g.addEdge('2', '4', 5)
##    g.addEdge('3', '5', 6)
##    g.addEdge('4', '6', 3)
##    g.addEdge('4', '3', 2)
##    g.addEdge('5', '2', 3)
##    g.addEdge('5', '4', 2)
##    g.addEdge('5', '6', 4)
##    g.addEdge('2', '6', 3)
##
