import requests
import json
import csv

url = "https://appapi.littlefreelibrary.org/library/pin.json"
payload = {"page_size": "100000"}
response = requests.get(url, params = payload)
data = response.json()
libs = data["libraries"]

with open("locations.csv", "w+", newline='') as f:
	writer = csv.writer(f)
	
	# Write the header to the file
	# The labels are based off inspecting the json
	header = ["id", "Library_Geolocation__Latitude__s", "Library_Geolocation__Longitude__s"]
	writer.writerow(header)

	for lib in libs:
		newrow = [lib[col] for col in header]
		writer.writerow(newrow)
	

