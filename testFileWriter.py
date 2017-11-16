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
        used_vertices.append(v2)
        weight = random.randint(1, 15)

        graph_list.append((v1, v2, weight))
        v1 = v2

    # if len(used_vertices) != vertices:
    #     for i in range(vertices):
    #         v2 = i
    #         if i not in used_vertices:
    #             v1 = rand(0, vertices)
    #             weight = rand(1, 15)
    #         graph_list.append((v1, v2, weight))

    return graph_list


def main() :
    #assume, X is your graph.
    for i in range(10):
        # X = [(1, 2, 4), (2, 3, 9), (3, 2, 4), (3, 3, 1)]
        X = random_graph_creator()
        file_name = "my_graph_" + str(i)
        write_dot_file(X, file_name)   
    # done 


main()
