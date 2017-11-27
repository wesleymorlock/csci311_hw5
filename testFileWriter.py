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

def test_network_generator():
    vertices = random.randint(7, 15)
    edges = random.randint(vertices, vertices+5)

    graph_list = []
    connections = []
    used_vertices = []
    start_vertices = []
    end_vertices = []
    v1 = 0
    v2 = 0

    for i in range(0, edges):
      while v1 == v2:
        v2 = random.randint(0, vertices - 1)
      if str(v1) not in used_vertices:
        used_vertices.append(str(v1))
        start_vertices.append(str(v1))
      if str(v2) not in used_vertices:
        used_vertices.append(str(v2))
        end_vertices.append(str(v2))

      weight = random.randint(1, 15)

      if [str(v1), str(v2)] not in connections:
        graph_list.append([str(v1), str(v2), weight])
        connections.append([str(v1), str(v2)])

      v1 = v2

    if len(start_vertices) < vertices - 1:
      for x in range(vertices):
        if str(x) not in start_vertices:
          v1 = x
          v2 = x
          while v1 == v2:
            v2 = random.randint(0, vertices - 1)
          if str(v1) not in used_vertices:
            used_vertices.append(str(v1))
            start_vertices.append(str(v1))
          if str(v2) not in used_vertices:
            used_vertices.append(str(v2))
            end_vertices.append(str(v2))
          weight = random.randint(1, 15)

          if [str(v1), str(v2)] not in connections:
            graph_list.append([str(v1), str(v2), weight])
            connections.append([str(v1), str(v2)])
     

    if len(used_vertices) < vertices:
      for x in range(vertices): 
        if str(x) not in used_vertices:
          v1 = x
          v2 = x
          while v1 == v2 and ([str(v1), str(v2)] not in connections):
            v2 = random.randint(0, vertices - 1)
            print(v2)

            print(str([str(v1), str(v2)]))

          if str(v1) not in used_vertices:
            used_vertices.append(str(v1))
            start_vertices.append(str(v1))
          if str(v2) not in used_vertices:
            used_vertices.append(str(v2))
            end_vertices.append(str(v2))
          weight = random.randint(1, 15)

          graph_list.append([str(v1), str(v2), weight])

    return graph_list, used_vertices


