#!/usr/bin/python 

import json 

from pprint import pprint 



json_data="/Users/kosalan/Documents/GitHub/Brampton_Hack/data/Bus_Stops.geojson"

file = open("/Users/kosalan/Documents/GitHub/Brampton_Hack/data/cleaned_data.json","a")

with open(json_data) as data_file:
	data = json.load(data_file)


for item in data["features"]:
	stop_id = (item['properties']['stop_id'])
	stop_name = (item['properties']['stop_name'])
	stop_name = stop_name.replace("'","")
	lat = (item['properties']['stop_lat'])
	lon = (item['properties']['stop_lon'])
	
	#bus_stop = "['" + stop_id + ", " + stop_name + "', " + lat + "," + lon + "],"

	bus_stop = "['" + stop_id +  "', " + lat + "," + lon + ", '" + stop_name + "'],\n" 

	file.write(bus_stop)
	print bus_stop