from graph_to_csv import create_graph_fromOSM, edges_to_csv, nodes_to_csv
from Astar import aStar
from geolocation_processes import get_OSM_Id
from helpers import get_nodes_from_csv
import gmplot
import pandas as pd

#creating the csv files necessary for our graph data
#nodes_to_csv(create_graph_fromOSM(), 'nodes.csv')
#edges_to_csv(savepath='edges.csv')

node_data = get_nodes_from_csv()
src = get_OSM_Id(17.5472310, 78.5725623)
dest = get_OSM_Id(17.240673, 78.432342)

shortest_path = aStar(src, dest)
shortest_path.pop(0)


print('making html file')
if len(shortest_path) == 0:
    print(f"NO PATH!!!")

shortest_path_latlng = []
for node in shortest_path:
    [lat, lon] = node_data[node_data["node"] == node].iloc[0][["y", "x"]]
    shortest_path_latlng.append((lat, lon))


path_lat, path_lon = zip(*shortest_path_latlng)
gmap = gmplot.GoogleMapPlotter(lat= ((17.5472310 + 17.2403)/2), lng= ((78.5725623 + 78.4294)/2), zoom= 13)
gmap.plot(path_lat, path_lon,color= 'red', edge_width= 4)
gmap.draw("path.html")