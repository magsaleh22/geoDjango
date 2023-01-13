import geopandas as gpd
import requests 
import json

# datasoure GeoJSON file
url = "municipalities_nl.geojson"

# defining the api-endpoint 
API_ENDPOINT = "http://localhost:8000/api/municipalities/"


# read the file to geopandas object
gdf = gpd.read_file(url,driver='GeoJSON')


# post request to localhost
for i,row in gdf.iterrows():
    
    
    name = row['name']
    type = row['geometry'].geom_type
    
    row_GeoSeries = gpd.GeoSeries(row.geometry)
    row_GeoSeries_json = json.loads(row_GeoSeries.to_json())
    coordinates = row_GeoSeries_json["features"][0]['geometry']['coordinates']
    
    # create dictionary and convert it to json to post it to the url
    municipality = {"name" : name}
    municipality["location"] = {
		"type" : type,
		"coordinates": coordinates
		}
    
    json_municipality = json.dumps(municipality) 
    
       
    print(f"Post: {name}")
    
  
    y = requests.post(API_ENDPOINT, data = json_municipality, timeout=2.50,headers = {'Content-type': 'application/json'})
    print(f"response:{y}")

    # input("Press Enter to continue...")

# print(gdf.head())



