import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(graph):
    adj = copy.deepcopy(graph)
    N = len(adj)

    odd_degree = 0
    for a in adj:
        odd_degree += len(a)%2

    if odd_degree not in (0, 2):
        return None

    eulerian_path = []
    stack = []

    visited_edges = set()

    stack.append(0)

    while stack:
        current_node = stack[-1]
        if len(adj[current_node]) > 0:
            while len(adj[current_node]) != 0 and\
                    ((current_node, adj[current_node][-1]) in visited_edges\
                     or (adj[current_node][-1], current_node) in visited_edges):
                adj[current_node].pop()
            if len(adj[current_node]) > 0:
                stack.append(adj[current_node][-1])
                adj[current_node].pop()
                visited_edges.add((current_node, stack[-1]))
                continue
        eulerian_path.append(current_node)
        stack.pop()

    return eulerian_path