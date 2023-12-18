from collections import deque

INF = float("Inf")

class Edge:
    def __init__(self, u, v, capa, weight, residual=None):
        self.u = u
        self.v = v
        self.capa = capa  # capacity that there is left to the edge
        self.weight = weight  # weight of the edge
        self.residual = residual  # corresponding edge in the residual graph


def create_graph(capacities, costs, green_sources: dict, gas_centrals: dict, consumers: dict):
    N = len(costs)+2
    
    s = N-2
    t = N-1
    graph = [[] for _ in range(N)]

    for src in green_sources:
        graph[s].append(Edge(s, src, green_sources[src], 0))

    for src in gas_centrals:
        var_points = gas_centrals[src]

        for i in range(1, len(var_points)):
            prev = var_points[i-1]
            current = var_points[i]
            dx = current[0]-prev[0]
            dy = current[1]-prev[1]
            graph[s].append(Edge(s, src, dx, dy/dx))

    for sink in consumers:
        graph[sink].append(Edge(sink, t, consumers[sink], 0))

    for i in range(N-2):
        for j in range(N-2):
            graph[i].append(Edge(i, j, capacities[i][j], costs[i][j]))

    return s, t, graph


def get_residual(graph):
    N = len(graph)
    graph_residual = [[] for _ in range(N)]

    for u in range(N):
        for edge in graph[u]:
            edge.residual = Edge(edge.v, edge.u, 0, -edge.weight, edge)
            graph_residual[u].append(edge)
            graph_residual[edge.v].append(edge.residual)

    return graph_residual


def min_cost_max_flow(s, t, graph_residual: list[list[Edge]]):

    N = len(graph_residual)

    def BellmanFord(parents):
        d = [INF]*N
        d[s] = 0
        
        inqueue = set()

        queue = deque()
        queue.append(s)
        inqueue.add(s)
        
        while queue:
            u = queue.popleft()
            inqueue.remove(u)
            for edge in graph_residual[u]:
                if edge.capa > 0 and edge.weight + d[u] < d[edge.v]:
                    d[edge.v] = edge.weight + d[u]
                    parents[edge.v] = edge
                    if edge.v not in inqueue:
                        queue.append(edge.v)
                        inqueue.add(edge.v)

        return d[t] < INF

    maximum_flow = 0
    minimum_cost = 0
    parents = [None]*N

    while BellmanFord(parents):
        flow = INF
        current = t
        while current != s:
            flow = min(flow, parents[current].capa)
            current = parents[current].u
            
        maximum_flow += flow
        
        current = t
        while current != s:
            minimum_cost += flow*parents[current].weight
            
            parents[current].capa -= flow
            parents[current].residual.capa += flow
            current = parents[current].u

    return maximum_flow, minimum_cost
