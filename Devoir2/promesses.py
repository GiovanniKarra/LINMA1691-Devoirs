"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
import heapq
    

def prim_mst(N, roads):
    """ 
    INPUT : 
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved
        
        See homework statement for more details
    """

    adj = [set() for _ in range(N)]
    for road in roads:
        if road[1] not in adj[road[0]]:
            adj[road[0]].add((road[2], road[1]))
            adj[road[1]].add((road[2], road[0]))


    satisfaction = 0
    
    explored_nodes = {0}
    explored_roads = set()
    heap = []

    for node in adj[0]:
        heapq.heappush(heap, (node[0], (0, node[1])))

    while len(explored_nodes) != N:
        _, min_road = heapq.heappop(heap)
        other_node = min_road[1] #if min_road[0] in explored_nodes else min_road[0]
        if other_node in explored_nodes:
            continue

        explored_roads.add(min_road)

        for node in adj[other_node]:
            if node[1] not in explored_nodes:
                heapq.heappush(heap, (node[0], (other_node, node[1])))

        explored_nodes.add(other_node)

    for road in roads:
        if road[:2] not in explored_roads:
            satisfaction += road[2]

    return satisfaction


if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        roads = []
        for road in range(m):
        
            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))
            
    # Compute answer for the first exercice
     
    ans1 = prim_mst(n, roads)
     
    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output)) 
        

