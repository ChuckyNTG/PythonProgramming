from itertools import combinations
import random as rand
import sys
import networkx as nx

# Create fully connected graph with 7 nodes
size = 7
S = list(range(size))
all_combos = list(combinations(S,2))
edges_weight = []
for edge in all_combos:
    edges_weight.append((edge[0],edge[1],rand.choice(range(20)))) 
G = nx.Graph()
G.add_weighted_edges_from(edges_weight)

#####################
#
#   Prims Algorithm
#   By Charles Glaser
#
#####################

v_distance = {}
edge_min = {}

# Initialize minimum distances to largest value
for node in G.nodes():
    v_distance[node] = sys.maxint

# Create an empty graph that will hold the minimum spanning tree
MST = nx.Graph()
node_list = list(G.nodes()) # List of nodes

# Choose a random node as a starting point
v = rand.choice(list(G.nodes()))
# Repeat for all nodes
node_list.remove(v)
del v_distance[v]
MST.add_node(v)
while(node_list):

    # Update min distance vertex list
    for node in node_list:
        if v_distance[node] > G[v][node]['weight']:
            v_distance[node] = G[v][node]['weight']

    print v_distance
    # Find smallest vertex and add to list
    v_new = min(v_distance,key=v_distance.get)
    weight=v_distance[v_new]
    MST.add_edge(v,v_new,weight=weight)
    v = v_new
    node_list.remove(v)
    del v_distance[v]

print G.edges()    
print MST.edges()
         
