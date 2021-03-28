import pandas as pd
from haversine import haversine


node_data = pd.read_csv('nodes.csv')
def heuristic(curr):
    lat = node_data[node_data.node == curr].iloc[0][["y"]]
    lon = node_data[node_data.node == curr].iloc[0][["x"]]
    curr = (lat, lon)
    dest = (17.240673, 78.432342)
    return haversine(curr, dest)


def makePath(parent, curr):
    path = [curr]
    while curr in parent.keys():
        curr = parent[curr]
        path.insert(0, curr)
    return path

def get_nodes_from_csv():
    return pd.read_csv('nodes.csv')

def get_edges_from_csv():
    df = pd.read_csv('edges.csv')
    return df[['source', 'target', 'length']]