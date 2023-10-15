from collections import deque


"""
    Solves the problem defined in the statement for adj an adjacency list of the dispersion dynamics of rumors in LLN
        adj is a list of length equal to the number of kots
        adj[i] gives a list of kots touched by i with direct edges (0-based)

    You are free to change the code below and to not use the precompleted part. The code is based on the high-level description at https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
    You can also define other sub-functions or import other datastructures from the collections library
"""
def solve(adj):
    # adjacency of the graph and its transpose
    adj_out = adj
    adj_in = transpose(adj_out)

    # number of nodes
    N = len(adj_in)

    # is a node already visited?
    visited = [False]*N
    # list of node to process in the second step
    L = []
    # queue of nodes to process with their associated status (i,False/True) i is the node index and True/False describes if we are appending the node to L or not when processing it
    q = deque()

    ### loop on every node and launch a visit of its descendants
    for x in range(N):
        q.append((x, not visited[x]))

        while q:
            x,to_append = q.pop()

            if to_append:
                visited[x] = True

                out_neighbours = adj_out[x]
                for v in out_neighbours:
                    q.append((v, not visited[v]))
                L.append(x)


    ### reverse the list to obtain the post-order
    L.reverse()


    ### find the strongly connected components
    
    assigned = [False]*N
    roots = dict()

    for x in L:
        q.append((x, x, not assigned[x]))

        while q:
            x, root, to_assign = q.pop()

            if to_assign:
                assigned[x] = True

                if root not in roots:
                    roots[root] = []

                roots[root].append(x)

                in_neighbours = adj_in[x]
                for v in in_neighbours:
                    q.append((v, x, assigned[x] == -1))


    

    ### compute answer
    ans = len(roots)
    # TO COMPLETE

    return ans

"""
    Transpose the adjacency matrix
        Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
"""
def transpose(adj):
    n = len(adj)
    adj_in = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(len(adj[i])):
            adj_in[j].append(i)

    return adj_in


if __name__ == "__main__":
    matrix = [[1, 2],
              [2],
              [],
              [],
              [0]]
    
    print(solve(matrix))