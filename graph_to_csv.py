# https://networkx.org/documentation/stable/tutorial.html
# https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_pandas_edgelist.html#networkx.convert_matrix.from_pandas_edgelist

import networkx as nx
import pandas as pd
import osmnx as ox
#from networkx.convert_matrix import from_pandas_edgelist
# given a pandas dataframe with all edge details, the following function generates a graph

def gen_graph(dataframe):
    df = dataframe[['src', 'dest', 'dist']]
    graph_src_dest = nx.Graph()
    GRAPH = nx.from_pandas_edgelist(df, edge_attr= 'dist', create_using= graph_src_dest)
    return GRAPH

def create_graph_fromOSM():
    return ox.graph_from_point((17.5499, 78.5718), 200000, dist_type='network',network_type='drive')


def nodes_to_csv(G, savepath):
    unpacked = [pd.DataFrame({**{'node': node, **data}}, index=[i]) for i, (node, data) in enumerate(G.nodes(data=True))]
    df = pd.concat(unpacked)
    df.to_csv(savepath)
    print('success')
    return df

def edges_to_csv(savepath):
    df = nx.to_pandas_edgelist(create_graph_fromOSM())
    df = df.drop(columns=['maxspeed', 'oneway', 'lanes', 'highway', 'geometry', 'width', 'access', 'bridge', 'service', 'name', 
                          'area', 'ref', 'junction', 'tunnel'])
    df.to_csv('savepath')
    return df.head()

#nodes_to_csv(create_graph_fromOSM(), 'nodes.csv')
#edges_to_csv(savepath='edges.csv')