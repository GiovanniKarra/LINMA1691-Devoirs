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
        q.append(x)

        while q:
            u = q.popleft()

            if not visited[u]:
                visited[u] = True

                out_neighbours = adj_out[u]
                for v in out_neighbours:
                    q.append(v)
                L.append(u)

    # for x in range(N):
    #     if visited[x]:
    #         continue

    #     visited[x] = True
    #     q.append(x)

    #     while q:
    #         u = q[0]
    #         out_neighbours = adj_out[u]
    #         for v in out_neighbours:
    #             if not visited[v]:
    #                 visited[v] = True
    #                 q.append(v)
    #                 break
    #         #if not list(filter(lambda x : not visited[x], out_neighbours)):
    #         L.append(q.popleft())

    # def visit(x):
    #     if not visited[x]:
    #         visited[x] = True
    #         out_neighbours = adj_out[x]
    #         for v in out_neighbours:
    #             visit(v)
    #         L.insert(0, x)

    # for x in range(N):
    #     visit(x)


    ### reverse the list to obtain the post-order
    L.reverse()
    #print(L)
    ### find the strongly connected components
    
    assigned = [False]*N
    roots = dict()

    for x in L:
        q.append((x, x))

        while q:
            u, root = q.popleft()

            if not assigned[u]:
                assigned[u] = True

                if root not in roots:
                    roots[root] = []

                roots[root].append(u)

                in_neighbours = adj_in[u]
                for v in in_neighbours:
                    q.append((v, u))


    ans = 0
    
    for root in roots:
        source = True
        for x in roots[root]:
            if list(filter(lambda v : v not in roots[root], adj_in[x])):
                source = False
                break
        if source:
            ans += 1

    #print(roots)
    # print(adj_in)

    
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