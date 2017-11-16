import os

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


def main() :
    #assume, X is your graph.
    X = [(1, 2, 4), (2, 3, 9), (3, 2, 4), (3, 3, 1)]
    write_dot_file(X, "flow_graph_1")    


main()
