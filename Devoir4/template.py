from collections import deque


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


def min_cost_max_flow(s, t, graph_residual):

    # TODO

    def BellmanFord():
        return False

    maximum_flow = 0
    minimum_cost = 0

    return maximum_flow, minimum_cost
