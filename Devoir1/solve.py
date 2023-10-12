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

    """
    For each vertex u of the graph, mark u as unvisited. Let L be empty.
    For each vertex u of the graph do Visit(u), where Visit(u) is the recursive subroutine:

        If u is unvisited then:
            Mark u as visited.
            For each out-neighbour v of u, do Visit(v).
            Prepend u to L.
        Otherwise do nothing.

    For each element u of L in order, do Assign(u,u) where Assign(u,root) is the recursive subroutine:

        If u has not been assigned to a component then:
            Assign u as belonging to the component whose root is root.
            For each in-neighbour v of u, do Assign(v,root).
        Otherwise do nothing.
    """

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
    
    assigned = [-1 for i in range(N)]

    for x in L:
        q.append((x, x, assigned[x] != -1))

        while q:
            x, root, to_assign = q.pop()

            if to_assign:
                assigned[x] = root

                in_neighbours = adj_in[x]
                for v in in_neighbours:
                    q.append((v, x, assigned[x] != -1))


    ### compute answer
    ans = 0
    # TO COMPLETE

    return ans

"""
    Transpose the adjacency matrix
        Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
"""
def transpose(adj):
    n = len(adj)
    adj_in = []
    
    for i in range(n):
        new_row = adj[i].copy()
        new_row.reverse()
        adj_in.append(new_row)

    return adj_in


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    print(transpose(matrix))