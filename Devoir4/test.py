from template import *


"""
    Test min cost max flow
"""

def create_test_max_flow(N,K):
    assert N == 2*K +2
    graph = [[] for _ in range(N)]

    def add_edge(u, v, cost, capa):
        edge = Edge(u, v, capa, cost)
        graph[u].append(edge)

    for k in range(K):
        add_edge(k,k+K,0,1)
        if k!=K-1:
            add_edge(k,k+1,0,2*K)
            add_edge(k+K,k+K+1,0,2*K)
    add_edge(2*K,0,0,K)
    add_edge(2*K,K-1,1,K)
    add_edge(K-1,2*K+1,1000,K)
    add_edge(2*K-1,2*K+1,0,K)

    assert sum([len(x) for x in graph])==3*K+2

    return 2*K,2*K+1,graph

### Test with flow cancelling on a small example
K = 2
s,t,graph = create_test_max_flow(2*K+2,K)
maximum_flow, minimum_cost = min_cost_max_flow(s, t, get_residual(graph))

assert int(maximum_flow) == 2*K
assert int(minimum_cost) == K*1000+K

### Test multi-edge support
n = 3
s = 0
t = 2
graph = [[] for _ in range(n)]
def add_edge(u, v, cost, capa):
        edge = Edge(u, v, capa, cost)
        graph[u].append(edge)

add_edge(0,1,0,1)
add_edge(0,1,1,1)
add_edge(0,1,2,1)
add_edge(0,1,3,1)
add_edge(1,2,0,4)

maximum_flow, minimum_cost = min_cost_max_flow(s, t, get_residual(graph))

assert int(maximum_flow) == 4
assert int(minimum_cost) == 6

### Test ability to compute min cost in a Dijkstra failing example with flow cancelling
s = 0
t = 3
n = 6
graph = [[] for _ in range(n)]
add_edge(0,1,0,3)
add_edge(0,2,10,1)
add_edge(1,4,5,1)
add_edge(1,5,2,1)
add_edge(1,3,9,3)
add_edge(2,3,0,2)
add_edge(4,2,1,1)
add_edge(5,2,2,1)

maximum_flow, minimum_cost = min_cost_max_flow(s, t, get_residual(graph))

assert int(maximum_flow) == 4
assert int(minimum_cost) == 32


### Test with flow cancelling on a large example (this takes less than a few seconds with our implementation and a good cpu)
K = int(3e3)
s,t,graph = create_test_max_flow(2*K+2,K)
maximum_flow, minimum_cost = min_cost_max_flow(s, t, get_residual(graph))

assert int(maximum_flow) == 2*K
assert int(minimum_cost) == K*1000+K


"""
    Test problème de planification energétique
"""

### Test 1
green_sources = {0: 1, 1: 2}
gas_centrals = {2: [(0, 0), (1, 1), (6, 11)]}
consumers = {3: 2, 4: 3, 5: 2}
capacities = [[0, 0, 2, 1, 3, 2],
              [0, 0, 4, 2, 3, 1],
              [2, 4, 0, 1, 1, 1],
              [1, 2, 1, 0, 0, 0],
              [3, 3, 1, 0, 0, 0],
              [2, 1, 1, 0, 0, 0]]

costs = [[0, 0, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [1, 1, 1, 0, 0, 0]]

s, t, graph = create_graph(capacities, costs, green_sources, gas_centrals, consumers)
graph_residual = get_residual(graph)
maximum_flow, minimum_cost = min_cost_max_flow(s, t, graph_residual)


assert int(maximum_flow) == 7
assert int(minimum_cost) == 15


### Test 2
green_sources = {0: 1, 1: 2}
gas_centrals = {2: [(0, 0), (1, 1), (6, 11)], 6: [(0, 0), (1, 1), (6, 11)]}
consumers = {3: 2, 4: 3, 5: 2}
capacities = [[0, 0, 2, 1, 3, 2, 2],
              [0, 0, 4, 2, 3, 1, 4],
              [2, 4, 0, 1, 1, 1, 0],
              [1, 2, 1, 0, 0, 0, 1],
              [3, 3, 1, 0, 0, 0, 1],
              [2, 1, 1, 0, 0, 0, 1],
              [2, 4, 0, 1, 1, 1, 0]]

costs = [[0, 0, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1, 1],
         [1, 1, 0, 1, 1, 1, 0],
         [1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 0, 0, 0, 1],
         [1, 1, 0, 1, 1, 1, 0]]

s, t, graph = create_graph(capacities, costs, green_sources, gas_centrals, consumers)
graph_residual = get_residual(graph)
maximum_flow, minimum_cost = min_cost_max_flow(s, t, graph_residual)


assert int(maximum_flow)==7
assert int(minimum_cost)==13


### Test 3
green_sources = {0: 1, 1: 2}
gas_centrals = {2: [(0, 0), (1, 1), (8, 15)], 6: [(0, 0), (1, 1), (6, 11), (20,95)]}
consumers = {3: 2, 4: 3, 5: 2, 7: 20}
capacities = [[0, 0, 2, 1, 3, 2, 0, 0],
              [0, 0, 4, 2, 3, 1, 0, 0],
              [2, 4, 0, 1, 1, 1, 20, 0],
              [1, 2, 1, 0, 0, 0, 0, 0],
              [3, 3, 1, 0, 0, 0, 0, 0],
              [2, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 20, 0, 0, 0, 0, 20],
              [0, 0, 0, 0, 0, 0, 20, 0]]

costs = [[0, 0, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0],
         [1, 1, 0, 1, 1, 1, 2, 0],
         [1, 1, 1, 0, 0, 0, 1, 0],
         [1, 1, 1, 0, 0, 0, 1, 0],
         [1, 1, 1, 0, 0, 0, 1, 0],
         [1, 1, 2, 1, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]

s, t, graph = create_graph(capacities, costs, green_sources, gas_centrals, consumers)
graph_residual = get_residual(graph)
maximum_flow, minimum_cost = min_cost_max_flow(s, t, graph_residual)

assert int(maximum_flow) == 27
assert int(minimum_cost) == 122