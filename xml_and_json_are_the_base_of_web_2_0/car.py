import json
from xml.dom.minidom import Document
class Car():

	'''Constructor'''
	def __init__(self, *args, **kwargs):
		#Private attributes
		#print args[0]
		if len(args) > 0 and isinstance(args[0], dict):
			hash = args[0]
			name = hash.get('name')
			brand = hash.get('brand')
			nb_doors = hash.get('nb_doors')
		else:
			name = kwargs.get('name')
			brand = kwargs.get('brand')
			nb_doors = kwargs.get('nb_doors')

		if name == None or not isinstance(name, str):
			raise Exception("name is not a string")
		if brand == None or not isinstance(brand, str):
			raise Exception("brand is not a string")	
		if not isinstance(nb_doors, int) or nb_doors <= 0:
			raise Exception("nb_doors is not > 0")	
	
		self.__name = name
		self.__brand = brand
		self.__nb_doors = nb_doors

	'''Getter'''
	def get_name(self):
		return self.__name

	def get_brand(self):
		return self.__brand

	def get_nb_doors(self):
		return self.__nb_doors

	'''Public methods'''
	def to_hash(self):
		return {'name': self.__name, 'brand': self.__brand, 'nb_doors': self.__nb_doors}

	def __str__(self):
		return self.__name + ' ' + self.__brand + ' (' + str(self.__nb_doors) + ')'

	def set_nb_doors(self, number):
		self.__nb_doors = number

	def to_json_string(self):
		to_string = json.dumps(self.to_hash())
		return to_string

	def to_xml_node(self, doc):
		car = doc.createElement('car')
		car.setAttribute('nb_doors', str(self.__nb_doors))
		doc.appendChild(car)
		name = doc.createElement('name')
		name_content = doc.createCDATASection(self.__name)
		name.appendChild(name_content)
		car.appendChild(name)
		brand = doc.createElement('brand')
		brand_content = doc.createTextNode(self.__brand)
		brand.appendChild(brand_content)
		car.appendChild(brand)
		return car

			