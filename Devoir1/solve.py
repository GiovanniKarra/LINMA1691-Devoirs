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
        if not visited[x]:
            q.append((x, False))

            while q:
                u, to_add = q.pop()

                if to_add:
                    L.append(u)
                    continue
                visited[u] = True
                q.append((u, True))
                out_neighbours = adj_out[u]
                for v in out_neighbours:
                    if not visited[v]:
                        q.append((v, False))

    ### reverse the list to obtain the post-order
    L.reverse()

    ### find the strongly connected components
    ans = 0
    visited = [False]*N
    for x in L:
        if not visited[x]:
            ans += 1
            q = deque()
            q.append(x)
            while q:
                x = q.pop()
                visited[x] = True
                out_neighbours = adj_out[x]
                for v in out_neighbours:
                    if not visited[v]:
                        q.append(v)

    
    return ans

"""
    Transpose the adjacency matrix
        Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
"""
def transpose(adj):
    n = len(adj)
    adj_in = [[] for _ in range(n)]
    
    for i in range(n):
        for j in adj[i]:
            adj_in[j].append(i)

    return adj_in


if __name__ == "__main__":
    matrix = [[1],
              [2, 4],
              [3, 6],
              [2, 7],
              [0, 5],
              [6],
              [5],
              [6, 3]]
    
    solve(matrix)