import json
from xml.dom.minidom import Document

with open('5-main.json') as f:
    entry = json.load(f)

#Print the number of different brands
alist = []
for car in entry:
    alist.append(car['brand']) #Make all the brands to a list
print len(set(alist)) #Set() removes duplicates

#Cumulative number of doors for all cars
doors = 0
for car in entry:
    doors = doors + car['nb_doors']
print doors

#Print car description of the 4th car of the list
print entry[3]['name'] + " " + entry[3]['brand'] + " " + "(" + str(entry[3]['nb_doors']) + ")"

#Create a DOM document with all cars and print it
doc = Document()
cars = doc.createElement('cars')
doc.appendChild(cars)
for element in entry:
    car = doc.createElement('car')
    car.setAttribute('nb_doors', str((element['nb_doors'])))
    cars.appendChild(car)
    name = doc.createElement('name')
    name_content = doc.createCDATASection(element['name'])
    name.appendChild(name_content)
    car.appendChild(name)
    brand = doc.createElement('brand')
    brand_content = doc.createTextNode(element['brand'])
    brand.appendChild(brand_content)
    car.appendChild(brand)
print doc.toxml(encoding='utf-8')
