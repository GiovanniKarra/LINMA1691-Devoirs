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
    s = 0
    t = 0
    graph = []
    return s, t, graph


def get_residual(graph):
    N = len(graph)
    graph_residual = [[] for _ in range(N)]

    for u in range(N):
        for edge in graph[u]:
            graph_residual[u].append(Edge(edge.u, edge.v, edge.capa, edge.weight))
            graph_residual[edge.v].append(Edge(edge.v, edge.u, 0, -edge.weight))
            graph_residual[u][-1].residual = graph_residual[edge.v][-1]

    return graph_residual


def get_path(s, t, parents: list[Edge]):
    tmp = parents.copy()
    tmp[s] = 0
    if None in tmp:
        return False, INF
    path = []
    mincap = INF
    current = parents[t]
    while current != None:
        if current.capa < mincap:
            mincap = current.capa
        path.append(current)
        current = parents[current.u]

    path.reverse()
    return path, mincap


def min_cost_max_flow(s, t, graph_residual: list[list[Edge]]):

    N = len(graph_residual)

    # for l in graph_residual:
    #     for edge in l:
    #         edge.residual = Edge(edge.u, edge.v, edge.capa, edge.weight)

    def BellmanFord():
        parents = [None]*N
        d = [INF]*N
        d[s] = 0
        inque = set()
        queue = deque()
        queue.append(s)
        inque.add(s)
        while queue:
            u = queue.popleft()
            inque.remove(u)
            for edge in graph_residual[u]:
                if edge.weight + d[u] < d[edge.v]:
                    d[edge.v] = edge.weight + d[u]
                    parents[edge.v] = edge
                    if edge.v not in inque:
                        inque.add(edge.v)
                        queue.append(edge.v)
        return get_path(s, t, parents)

    maximum_flow = 0
    minimum_cost = 0

    path, mincap = BellmanFord()
    while path and mincap > 0:
        maximum_flow += mincap
        for edge in path:
            minimum_cost += mincap*edge.weight
            edge.capa -= mincap
            edge.residual.capa += mincap
        path, mincap = BellmanFord()

    print(maximum_flow)
    return maximum_flow, minimum_cost
