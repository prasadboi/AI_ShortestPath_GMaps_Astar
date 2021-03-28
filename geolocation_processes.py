import osmapi as OSM
import pandas as pd


#given OSM id returns the lat lon of that location irrespective of whether it exists in the graph network or not
def get_lat_lon(OSM_id):
    osm_obj = OSM.OsmApi()
    node = osm_obj.NodeGet(OSM_id)
    return (node['lat'], node['lon'])


def get_OSM_Id(lat, lon):
    OSMId = 0
    nodes_df = pd.read_csv('nodes.csv').drop(columns = ['highway', 'ref', 'street_count'])
    nodes_df['EvaluatingFunc'] = ((nodes_df.y - lat)**2 + (nodes_df.x - lon)**2).abs()
    idx = nodes_df[['EvaluatingFunc']].idxmin().values[0]
    OSMId = nodes_df.loc[idx]
    #print(OSMId)
    return OSMId.node

# BITS- hyderabad osm lat lon = [17.5472310 N, 78.5725623 E]
# RGITA lat lon = [17.2403° N, 78.4294° E]
#testing
#print(get_OSM_Id(17.5472310, 78.5725623))
#print(get_OSM_Id(17.2403, 78.4294))