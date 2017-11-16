"""
Andrew Gray and John Piermatteo
Homework 05
Finding Maximum Flow
11/13/2017
"""
#import os
#os.environ["PATH"] += os.pathsep + '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages'
# from graphviz import Digraph

class Edge(object):

    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.rEdge = None

    def __repr__(self):
        return str(self.source) + " , " + str(self.sink) + " , " + str(self.capacity)

class FlowNetwork(object):

    def __init__(self):
        self.adj = {}
        self.flow = {}

    def addVertex(self, vertex):
        self.adj[vertex] = []

    def getEdges(self, vertex):
        return self.adj[vertex]

    def addEdge(self, source, sink, capacity = 0):
        if source == sink:
            print("Error: not allowed to have a self cycle within the graph\n")
            return
        currEdge = Edge(source, sink, capacity)
        rEdge = Edge(source, sink, 0)
        currEdge.rEdge = rEdge
        rEdge.rEdge = currEdge
        self.adj[source].append(currEdge)
        self.adj[sink].append(rEdge)
        self.flow[currEdge] = 0
        self.flow[rEdge] = 0

    def findPath(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.getEdges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.findPath(edge.sink, sink, path + [(edge, residual)])
                if result != None:
                    return result

    def maxFlow(self, source, sink):
        path = self.findPath(source, sink, [])
        print ('path after enter MaxFlow: ' + str(path))
        for f in self.flow:
            print (str(f) + " , FLOW : " + str(self.flow[f]))
        print ('-' * 20)
        while path != None:
            flow = min(residual for edge, residual in path)
            for edge, residual in path:
                self.flow[edge] += flow
                self.flow[edge.rEdge] -= flow
            for f in self.flow:
                print (str(f) + " , FLOW : " + str(self.flow[f]))
            path = self.findPath(source, sink, [])
            print ('path inside of while loop: ' + str(path))
        for f in self.flow:
            print (str(f) + " , FLOW : " + str(self.flow[f]))
        print("\nMAX FLOW : ")
        return sum(self.flow[edge] for edge in self.getEdges(source))

def main():
    print("hi")
    g = FlowNetwork()
    vertices = ['1', '2', '3', '4', '5', '6']
    for s in vertices:
        g.addVertex(s)
    #print(g.adj)
    g.addEdge('1', '2', 5)
    g.addEdge('1', '3', 10)
    g.addEdge('2', '4', 5)
    g.addEdge('3', '5', 6)
    g.addEdge('4', '6', 3)
    g.addEdge('4', '3', 2)
    g.addEdge('5', '2', 3)
    g.addEdge('5', '4', 2)
    g.addEdge('5', '6', 4)
    g.addEdge('2', '6', 3)
    print("hi")
    print (str(g.maxFlow('1', '6')))  

main()
