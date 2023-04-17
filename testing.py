import requests

response = requests.get("https://appapi.littlefreelibrary.org/library/pin.json?page_size=100000")

if response.status_code == 200:
	print("Request succesful")
else:
	print(f'Request failed with status code {response.status_code}')

print("Response headers:")
for header, value in response.headers.items():
	print(f'{header}: {value}')


