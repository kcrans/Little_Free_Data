import json
import csv

with open("locations.json", "r") as f:
	f_content = f.read()
data = json.loads(f_content)
libs = data["libraries"]
print(len(libs))
