"""
Andrew Gray, John Piermatteo, Wesley Morlock
Homework 05
Main
11/13/2017
"""
from testFileWriter import *
from max_flow_generator import *
import os

def main():
    for z in range(10):
        g = FlowNetwork()
        g.addVertex('0', True, False)   ##source
        g.addVertex('6',False,True)     ##sink

        r = test_network_generator()
        vertices = r[1]
        vertices.remove('0')
        vertices.remove('6') ##sometime 6 ins't a vertex -> will give error

        for s in vertices:
            g.addVertex(s) 
        x = r[0]
        for i in range(len(x)):
            g.addEdge(x[i][0],x[i][1],x[i][2])
            
        file_name = "my_graph_" + str(z)
        name = os.path.join("./input_graphs/", file_name)
        print(file_name)
        write_dot_file(r[0], name)  

        max_edges = g.getMaxEdges()

        

        print('vertices: ' + str([vertex.name for vertex in g.vertices]) + '\n')
        print('edges: ' + str(['%s -> %s; %s/%s' % (e.start, e.end, e.flow, e.capacity) for e in g.getEdges()])+ '\n')
        print('max flow: ' + str(g.calculateMaxFlow()) + '\n')
        print('max edges: ' + str(max_edges))
        print("----------------------------------------------------------------------------------------\n")

        file_name = "max_edges_" + str(z)
        name = os.path.join("./output_graphs/", file_name)
        write_dot_file(max_edges, name)

        

main()
