import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import pygraphviz
import numpy as np
import wget
import networkx as nx
import gzip


# https://stackoverflow.com/a/52333182
def gunzip(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        while True:
            block = s_file.read(block_size)
            if not block:
                break
            else:
                d_file.write(block)
        d_file.write(block)


# Part 1: Preparing data
# Download the data
# Unpack the data
# Import the data as an undirected graph in networkx
#_URL = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
# wget.download(_URL)
#gunzip('facebook_combined.txt.gz', './facebook_combined.txt')

graph = nx.read_edgelist('./facebook_combined.txt')

# Part 2: Analyse the data
# The number of nodes in the network
# The number of edges in the network
# The average degree in the network
# A visualisation of the network inside your notebook


def exercise2():
    print(nx.info(graph))
    degrees = dict(graph.degree)  # https://stackoverflow.com/a/16567881
    nx.draw(graph, nodelist=degrees.keys(), pos=graphviz_layout(graph),
            node_size=[v * 1.2 for v in degrees.values()], width=.05, cmap=plt.cm.GnBu,
            with_labels=True, font_size=4, node_color=range(len(graph)))
    plt.show()  # output saved in visualization.png
# exercise2()
# Output
# Name:
# Type: Graph
# Number of nodes: 4039
# Number of edges: 88234
# Average degree:  43.6910

# Part 3: Find the most popular people
# extract and report the 10 people with the most connections in the network


def exercise3():
    """
    https://stackoverflow.com/a/48382895
    """
    return sorted(graph.degree, key=lambda x: x[1], reverse=True)[:10]


# print(exercise3())
# Output (Node, degrees):
#[('107', 1045), ('1684', 792), ('1912', 755), ('3437', 547), ('0', 347), ('2543', 294), ('2347', 291), ('1888', 254), ('1800', 245), ('1663', 235)]
