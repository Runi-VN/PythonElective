import numpy as np
import wget
import gzip
import networkx as nx
import shutil

# myfile = wget.download(
#    'https://snap.stanford.edu/data/twitter_combined.txt.gz')


"""
Which node in the twitter data has the most connections?
"""

# convert .gz to .txt https://stackoverflow.com/a/52333182


def gunzip_shutil(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        shutil.copyfileobj(s_file, d_file, block_size)


#gunzip_shutil('twitter_combined.txt.gz', 'twitter_combined.txt')

graph = nx.read_edgelist('./twitter_combined.txt')
print(nx.info(graph))

# get degrees for every node
in_deg_vec = np.array([graph.degree(n) for n in graph.nodes()])
# get highest value degree
max_ind_deg = in_deg_vec.max()
print('Highest amount of degrees:', max_ind_deg)
# get index of max
index_max = np.argmax(in_deg_vec)
print('index of max:', index_max)
# get info of node at index
max_name = list(graph.nodes)[index_max]
print('ID of max:', max_name)

print('The node {} has the most connections with {} connections'.format(
    max_name, len(list(graph.neighbors(max_name)))))  # same as max_ind_deg
