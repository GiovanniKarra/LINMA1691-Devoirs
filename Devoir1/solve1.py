from collections import deque

def dfs(x, visited, g):
    q = [x]
    while q:
        x = q.pop()
        visited[x] = True
        for adj in g[x]:
            if visited[adj]: continue
            q.append(adj)

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

    L = []
    
    # queue of nodes to process with their associated status (i,False/True) i is the node index and True/False describes if we are appending the node to L or not when processing it
    q = []
    visited = [False]*N
    ### loop on every node and launch a visit of its descendants
    for x in range(N):
        if visited[x]:
            continue
        q.append((x,False))

        while q:
            x, to_add = q.pop()
            
            if to_add:
                L.append(x)
                continue
            visited[x] = True
            q.append((x,True))
            for y in adj[x]:
                if not visited[y]:
                    q.append((y,False))

    ### reverse the list to obtain the post-order
    L.reverse()
    # print(L)
    ### find the strongly connected components
    ans = 0

    visited = [False]*N
    for x in L:
        if visited[x]:
            continue
        ans += 1
        dfs(x, visited, adj_out)
    return ans


"""
    Transpose the adjacency matrix
        Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
"""
def transpose(adj):
    adj_in = [list() for _ in range(len(adj))]

    for i in range(len(adj)):
        for x in adj[i]:
            adj_in[x].append(i)
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