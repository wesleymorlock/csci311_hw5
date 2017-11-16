import os
import random

def write_dot_file(Y, name):

    f = open(name+ ".dot", "w+")
    f.write(" digraph g{ ")
    f.write("  rankdir = LR ")
    for i in range(len(Y)):
        (u,v,w) = Y[i]
        my_str = str(u) + "-> "+str(v)+ " [label = \""+ str(w) +"\"]\n"
        f.write(my_str)
    f.write("label =  "+ name)
    f.write(" } ")
    f.close()
    os.system("dot -T pdf "+ name + ".dot" + " -o " + name + ".pdf")

def random_graph_creator():
    vertices = random.randint(7, 15)
    edges = random.randint(vertices, vertices*3)

    graph_list = []
    used_vertices = []
    v1 = 0
    v2 = 0

    for i in range(0, vertices):
        while v1 == v2:
            v2 = random.randint(0, vertices)
        used_vertices.append(str(v2))
        weight = random.randint(1, 15)

        graph_list.append([str(v1), str(v2), weight])
        v1 = v2

    return graph_list, used_vertices


