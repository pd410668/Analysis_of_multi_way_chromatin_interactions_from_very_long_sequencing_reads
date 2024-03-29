#!/usr/bin/env python

from cwalks_analysis import load_cwalk_graph, load_files, histogram
from filtering import typical_chromosomes, collect_data
import networkx as nx

# graphs, _ = load_files("output_cadj/txt/", load_cwalk_graph)  # load cwalk graphs
graphs, _ = load_files("output_tsv/txt/", load_cwalk_graph)

i, j, k = 0, 0, 0
inter_cwalks_len, intra_cwalks_len = [], []
for graph in graphs:
    print(f"self_loops: {nx.number_of_selfloops(graph)}")
    for cwalk in list(nx.connected_components(graph)):
        cwalk = list(cwalk)
        # if len(cwalk) > 4: # 3 len cwalks can be removed
        k += 1
        if all(cwalk[i][2] == cwalk[0][2] for i in range(0, len(cwalk))):
            inter_cwalks_len.append(len(cwalk))
            i += 1
        else:
            intra_cwalks_len.append(len(cwalk))
            j += 1

print(f"Number of intra-chromosomal cwalks: {i}")
print(f"Number of inter-chromosomal cwalks: {j}")
print(f"Number of all cwalks: {k}")
print(f"Percentage f intra-chromosomal cwalks is {round((i/k)*100, 3)}%")
print(i + j == k)

"""
k562.cadj:
self_loops: 21
Number of intra-chromosomal cwalks: 19
Number of inter-chromosomal cwalks: 18240
Number of all cwalks: 18259
Percentage of intra-chromosomal cwalks is 0.104%
True
"""

"""
3 cwalk graphs: 
self_loops: 985
self_loops: 1211
self_loops: 1511
Number of intra-chromosomal cwalks: 17782
Number of inter-chromosomal cwalks: 12278
Number of all cwalks: 30060
Percentage of intra-chromosomal cwalks is 59.155%
True
"""

# Distribution of cwalks length
histogram(inter_cwalks_len, "inter-chromosomal")
histogram(intra_cwalks_len, "intra-chromosomal")




