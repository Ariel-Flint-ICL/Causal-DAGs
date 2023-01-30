# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:46:39 2023

@author: kevin
"""
#%%
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
import DAG_Library.module_path_algorithms as pa
import DAG_Library.module_random_geometric_graphs as rgg
import numpy as np
import random as random
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import matplotlib.colors as mcolors

def path_node_to_edges(path_list_in_nodes):
    path_list_in_edges = [(path_list_in_nodes[i], path_list_in_nodes[i+1]) for i in range(len(path_list_in_nodes) - 1)]
    return path_list_in_edges

def plt_edges(edge_list, pos, paths, labels = None, node_size = 0.5, show_nodes = False, **edge_kwargs):
    G = nx.DiGraph(edge_list)
    
    colors = iter(mcolors.TABLEAU_COLORS)
    labels = iter(labels)
    for path in paths:
        color = next(colors, 'black')
        label = next(labels)
        path = path_node_to_edges(path)
        nx.draw_networkx_edges(G, pos, path, arrows = False, label = label, edge_color = color, **edge_kwargs)
        plt.legend()
    if show_nodes == True:    
        nx.draw_networkx_nodes(G, pos, node_size = node_size)
    plt.axis('off')
#%%

R = 0.13

pos = rgg._poisson_cube_sprinkling(2000, 1, 2)
edge_list, graph_dict = rgg.lp_random_geometric_graph(pos, R, 0.5)

#%%
shortest_path, longest_path = pa.short_long_paths(graph_dict, edge_list = edge_list)
greedy_path = pa.greedy_path(graph_dict)

paths = [shortest_path, longest_path, greedy_path]
labels = ['short', 'long', 'greedy']

plt_edges(edge_list, pos, paths, labels = labels, show_nodes = True, style = 'dashed')

#%%
ariel_longest_path = pa.getLongestPath(graph_dict)
# %%
labels = ['ariel']
plt_edges(edge_list, pos, ariel_longest_path, labels = labels, show_nodes = True, style = 'dashed')

# %%