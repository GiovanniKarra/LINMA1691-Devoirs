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

    #M = len(roads)

    satisfaction = 0
    
    explored_nodes = {0}
    explored_roads = set()
    heap = []

    for road in roads:
        if 0 in road[:2]:
            heapq.heappush(heap, (1/road[2], road))

    while len(explored_nodes) != N:
        _, min_road = heapq.heappop(heap)
        other_node = min_road[1] if min_road[0] in explored_nodes else min_road[0]
        if other_node in explored_nodes:
            continue

        explored_roads.add(min_road)
        satisfaction += min_road[2]

        for road in roads:
            if road not in explored_roads and other_node in road[:2]:
                heapq.heappush(heap, (1/road[2], road))

        explored_nodes.add(other_node)

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
        

