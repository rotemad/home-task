import requests
import csv

response = requests.get("https://rickandmortyapi.com/api/character/?species=Human&status=alive")
new_list = response.json()
data = []

csv_header = ["Name", "Location", "Image"]

for pointer in new_list['results']:
    name = pointer['name']
    location = pointer['location']['name']
    image = pointer['image']
    data.append([name, location, image])
    
with open('rickandmortyapi.csv', 'w', encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)
    writer.writerows(data)
    file.close()
