import requests
import csv
import json

# Take in CSV of libraries
with open("locations.csv", newline = "") as f:
	reader = csv.reader(f, delimiter = ",")
	reader.__next__() # Skip the top row
	with open("libraries.csv", "w+", newline = "") as new_f:
		writer = csv.writer(new_f)
		header = ["id", "Name", "Street__c", "City__c", "State_Province_Region__c", "Postal_Zip_Code__c", "Country__c", "Traveling_Library__c", "Official_Charter_Number__c", "First_Map_Date__c", "Map_Me__c", "Map_Date__c", "Duplicate_Charter_Number__c", "Count_of_Primary_Stewards__c", "Latitude_MapAnything__c", "Longitude_MapAnything__c", "Library_Geolocation__Latitude__s",  "Library_Geolocation__Longitude__s", "check_in_count"]
		writer.writerow(header)
		count = 0
		for lib in reader:
			# Take id number and look up expanded info
			id = lib[0]
			url = f"https://appapi.littlefreelibrary.org/libraries/{id}.json"
			response = requests.get(url)
		
			if response.status_code != 200:
				print(f'Got status code {response.status_code}, exiting')
				break

			data = response.json()
			newrow = [data[col] for col in header]
			writer.writerow(newrow)
			count += 1
			if count == 10:
				break

