import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(graph):
    """https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/"""
    adj = copy.deepcopy(graph)
    N = len(adj)
    eulerian_path = []
    stack = []

    stack.append(0)

    while stack:
        current_node = stack[-1]
        if len(adj[current_node]) > 0:
            stack.append(adj[current_node][-1])
            adj[current_node].pop()
        else:
            eulerian_path.append(current_node)
            stack.pop()
            

    return eulerian_path
