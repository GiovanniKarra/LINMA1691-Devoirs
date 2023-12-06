from collections import deque

INF = 99999999999

class Edge:
    def __init__(self, u, v, capa, weight, residual=None):
        self.u = u
        self.v = v
        self.capa = capa  # capacity that there is left to the edge
        self.weight = weight  # weight of the edge
        self.residual = residual  # corresponding edge in the residual graph


def create_graph(capacities, costs, green_sources: dict, gas_centrals: dict, consumers: dict):

    # TODO

    s = 0
    t = 0
    graph = []
    return s, t, graph


def get_residual(graph):

    # TODO

    graph_residual = graph
    return graph_residual


def get_path(t, parents: list[Edge]):
    path = []
    mincap = INF
    current = parents[t]
    while current != None:
        if current.capa < mincap:
            mincap = current.capa
        path.append(current)
        current = parents[current.u]

    return path, mincap


def min_cost_max_flow(s, t, graph_residual: list[Edge]):

    N = len(graph_residual)

    def BellmanFord():
        parents = [None]*N
        d = [INF]*N
        d[s] = 0
        inque = set()
        queue = deque()
        while queue:
            u = queue.popleft()
            if u in inque: inque.remove(u)
            for edge in graph_residual[u]:
                if edge.weight + d[u] < d[edge.v]:
                    d[edge.v] = edge.weight + d[u]
                    parents[edge.v] = edge
                    if edge.v not in inque:
                        inque.add(edge.v)
                        queue.append(edge.v)
        return d, parents

    flow = [[0]*N for _ in range(N)]
    d, parents = BellmanFord()
    path, mincap = get_path(t, parents)
    if mincap >= 0:
        for edge in path:
            flow[edge.u][edge.v] += mincap
            flow[edge.v][edge.u] -= mincap

    maximum_flow = 0
    for i in range(N):
        for j in range(N):
            if f := flow[i][j] > maximum_flow:
                maximum_flow(f)
    minimum_cost = sum([edge.weight for edge in parents if edge != None])

    return maximum_flow, minimum_cost
