def read_from_file(filename):

    #For each clause (a v b), where a and b are literals, create an edge from !a to b and from !b to a. 
    #These edges mean that if a is not true, then b must be true and vica-versa.
    
    edges_1 = {}
    edges_2 = {}
    node_set = set()

    file = open(filename)
    file_list = file.readlines()[1:]
        
    for line in file_list:
        x,y = line.split()
        v1,v2 = int(x),int(y)

        node_set.add(v1)
        node_set.add(-v1)
        node_set.add(v2)
        node_set.add(-v2)

        if -v1 not in edges_1:
            edges_1[-v1] = [v2]
        else:
            edges_1[-v1].append(v2)

        if -v2 not in edges_1:
            edges_1[-v2] = [v1]
        else:
            edges_1[-v2].append(v1)
        
        if v2 not in edges_2:
            edges_2[v2] = [-v1]
        else:
            edges_2[v2].append(-v1)
        
        if v1 not in edges_2:
            edges_2[v1] = [-v2]
        else:
            edges_2[v1].append(-v2)


    return node_set, edges_1, edges_2

def BFS_2SET(node_set,e_dic,reverse_e_dic):

    visited = set()
    time = 0
    finish_time_dic = {}
    time_to_vertex_dic = {}

    for i in node_set:
        queue = [i]
        while queue:
            v = queue.pop()
            if v not in visited:
                visited.add(v)
                queue.append(v)
                if v in reverse_e_dic:
                    for w in reverse_e_dic[v]:
                        if w not in visited: queue.append(w)

            else:
                if v not in finish_time_dic:
                    time += 1
                    finish_time_dic[v] = time
                    time_to_vertex_dic[time] = v


    new_e_dic = {}
    new_node_set = set()
    for key in e_dic:
        new_key = finish_time_dic[key]
        new_e_dic[new_key] = []
        if new_key not in new_node_set:
            new_node_set.add(new_key)
        for value in list(e_dic[key]):
            new_value = finish_time_dic[value]
            new_e_dic[new_key].append(new_value)
            if new_value not in new_node_set:
                new_node_set.add(new_value)


    visited = set()
    for i in range(len(new_node_set),-1,-1):
        if i in new_node_set:
            if i not in visited:
                s = i
                leader[s] = []
                queue = [s]
                while queue:
                    v = queue.pop()
                    if v not in visited:
                        visited.add(v)
                        leader[s].append(v)
                        if v in new_e_dic:
                            for w in new_e_dic[v]:
                                if w not in visited: queue.append(w)

    #go through the graph and see if there is a cycle that contains both a and !a for some variable a. 
    #If there is, then the 2SAT is not satisfiable

    leader = {}
    for l in leader.values():
        converted_back = set()
        for t in l:
            converted_back.add(time_to_vertex_dic[t])
        for i in converted_back:
            if i * -1 in converted_back:
                return 0
    return 1

def start(filename):
    node_set,e_dic,reverse_e_dic = read_from_file(filename)
    satisfied = BFS_2SET(node_set,e_dic,reverse_e_dic)


if __name__ == "__main__":

    print (start("2sat1.txt"))
    print (start("2sat2.txt"))
    print (start("2sat3.txt"))
    print (start("2sat4.txt"))
    print (start("2sat5.txt"))
    print (start("2sat6.txt"))

#10110
