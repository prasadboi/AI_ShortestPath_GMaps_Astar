import heapq as heap
from helpers import get_edges_from_csv, heuristic, makePath
import networkx as nx


print("generating graph")
# generating a graph from a csv file, using the networkx library
GRAPH = nx.from_pandas_edgelist(get_edges_from_csv(), edge_attr="length", create_using=nx.Graph())


def aStar(src, dest):
    # initialize values
    print("AStar called")
    open_list = []
    parent = {}
    parent[src] = None
    f_vals = {}
    f_vals[src] = 0
    g_vals = {}
    g_vals[src] = 0
    cost = {}
    cost[src] = 0


    # Astar starts from here
    heap.heappush(open_list, (src, f_vals))
    while len(open_list) >= 1:
        curr = heap.heappop(open_list)

        if curr[0] == dest:
            print('success!!!')
            return makePath(parent, curr[0])

        nghbrs = list(GRAPH.neighbors(curr[0]))

        for nghbr in nghbrs:
            print(nghbr)
            # dist = distance b/w current node and nghbr
            dist = GRAPH[ curr[0] ][ nghbr ]['length']

            # obviously we do not want to go back to a node that has already been traversed. that would simply be inefficient
            if nghbr not in parent:
                cost[ nghbr ] = g_vals[ curr[0] ] + dist
                if cost[ nghbr ] < g_vals.get(nghbr, float("inf")):

                    # calculating value of f = g + h
                    parent[ nghbr ] = curr[0]
                    g_vals[ nghbr ] = cost[ nghbr ]
                    f_vals[ nghbr ] = g_vals[ nghbr ] + heuristic(nghbr)

                    if nghbr not in open_list:
                        heap.heappush(open_list, (nghbr, f_vals))
    return open_list