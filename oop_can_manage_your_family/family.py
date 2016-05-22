#!/usr/bin/env python
import json
import os.path
import io

'''Class'''
class Person():

	'''Class attributes'''
	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]
	
	'''Constructor'''
	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

		'''Private attributes'''
		if id < 0 and isinstance(id, int):
			raise Exception("id is not an integer")
		self.__id = id

		if isinstance(eyes_color, str) and eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")		 
		self.__eyes_color = eyes_color

		if isinstance(genre, str) and  genre not in Person.GENRES:
			raise Exception("genre is not valid")
		self.__genre = genre

		if ((len(date_of_birth) is not 3) and (all(isinstance(x, int) for x in date_of_birth))) or ((date_of_birth[1] < 1) or (date_of_birth[1] > 31)) or ((date_of_birth[0] < 1) or (date_of_birth[0] > 12)):
			raise Exception("date_of_birth is not a valid date")
		self.__date_of_birth = date_of_birth

		if first_name is not str and first_name is None:
			raise Exception("string is not a string")
		self.__first_name = first_name 

		'''Public attribute'''
		self.last_name = ""
		self.is_married_to = 0
		self.children = []

	'''Getters'''

	def get_id(self):
		return self.__id

	def get_eyes_color(self):
		return self.__eyes_color
		
	def get_genre(self):
		return self.__genre
		
	def get_date_of_birth(self):
		return self.__date_of_birth

	def get_first_name(self):
		return self.__first_name

	'''public methods'''
	def __str__(self):
		return 	self.__first_name+ ' ' +self.last_name

	def is_male(self):
		if self.GENRES == "Male":
			return True
		else:
			return False			

	def age(self):
		'''return 2016 - self.__date_of_birth[-1]'''
		today = [5, 20, 2016]
    	#his_age = today.year - self.__date_of_birth.year[2] - ((today.month, today.day) < (self.__date_of_birth[0], self.__date_of_birth[1]))
		return (today[2] - self.__date_of_birth[2] - ((today[0], today[1]) < (self.__date_of_birth[0], self.__date_of_birth[1])))

	def json(self):
		return {'id': self.__id, 'eyes_color': self.__eyes_color, 'genre': self.__genre, 'date_of_birth': self.__date_of_birth, 'first_name': self.__first_name, 'last_name': self.last_name, 'is_married_to': self.is_married_to}
    
	def load_from_json(self, json):
		if not isinstance(json, dict):
   			raise Exception("json is not valid")
  		self.__id = json['id']
   		self.__eyes_color = json['eyes_color']
   		self.__genre = json['genre']
   		self.__date_of_birth = json['date_of_birth']
   		self.__first_name = json['first_name']    	
   		self.last_name = json['last_name']
   		self.is_married_to = json['is_married_to']
    	

def save_to_file(list, filename):
	my_family_d = []
	for per in list:
		d = per.json()

		if isinstance(per,Baby):
			d['type'] = "Baby"
		elif isinstance(per,Teenager):
			d['type'] = "Teenager"
		elif isinstance(per,Adult):
			d['type'] = "Adult"
		elif isinstance(per,Senior):
			d['type'] = "Baby"			
		elif isinstance(per,Person):
			d['type'] = "Person"	
		my_family_d.append(d)
	
	with open(filename, 'w') as outfile:
		json.dump(my_family_d, outfile)

def load_from_file(filename):
	list_of_dict = []
	if type(filename) is not str or os.path.exists(filename) == False :
		raise Exception("filename is not valid or doesn't exist") 
 	with io.open(filename) as data_file:
 		list_of_dict = json.load(data_file)
 	
 	list_of_persons = []
	for person in list_of_dict:
		if person['type'] == "Person" :
			p = Person(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
			p.last_name = person['last_name']
			p.is_married_to = person['is_married_to']
			list_of_persons.append(p)
	#		print person['first_name']
		elif person['type'] == "Baby" :
			b = Baby(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
			b.last_name = person['last_name']
			b.is_married_to = person['is_married_to']
			list_of_persons.append(b)

		elif person['type'] == "Teenager" :
			b = Teenager(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
			b.last_name = person['last_name']
			b.is_married_to = person['is_married_to']
			list_of_persons.append(b)
		
		elif person['type'] == "Adult" :
			b = Adult(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
			b.last_name = person['last_name']
			b.is_married_to = person['is_married_to']
			list_of_persons.append(b)

		elif person['type'] == "Senior" :
			b = Senior(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
			b.last_name = person['last_name']
			b.is_married_to = person['is_married_to']
			list_of_persons.append(b)
	return list_of_persons

class Baby(Person):

	def can_run(self):
		return False
	
	def need_help(self):
		return True

	def is_young(self):	
		return True

	def can_vote(self):
		return False

	def can_be_married(self):
		return False

	def is_married(self):
		if self.is_married_to != 0:
			return True
		else:
			return False 

	def divorce(self, p):
		self.is_married_to = 0
		p.is_married_to = 0	

	def just_married_with(self, p):
		if p.GENRES == "Male" and self.GENRES == "Female":
			self.last_name = p.last_name
		if self.is_married() == True or p.is_married() == True:
			raise Exception("Already married")
		if self.can_be_married() == False or p.can_be_married() == False:
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()

	def can_have_child(self):
		return False	

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
		if p is None or not (isinstance(p,Adult) or isinstance(p,Senior)):
			raise Exception("p is not an Adult or Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if type(first_name) is not str or first_name is None:
			raise Exception("string is not a string")
		if ((len(date_of_birth) is not 3) and (all(isinstance(x, int) for x in date_of_birth))):
			raise Exception("date_of_birth is not a valid date")
		if isinstance(genre, str) and  genre not in Person.GENRES:
			raise Exception("genre is not valid")
		if isinstance(eyes_color, str) and eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")
		if self.can_have_child() == False or p.can_have_child() == False :
			raise Exception("Can't have baby")	
		new_baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
		self.children.append(new_baby.get_id())
		p.children.append(new_baby.get_id())
		return new_baby

	def adopt_child(self, c):
		if self.can_have_child == False:
			raise Exception("Can't adopt child")
		self.children.append(c.get_id())	

class Teenager(Person):

	def can_run(self):
		return True

	def need_help(self):
		return False

	def is_young(self):	
		return True	

	def can_vote(self):	
		return False

	def can_be_married(self):
		return False	

	def is_married(self):
		if self.is_married_to != 0:
			return True
		else:
			return False 

	def divorce(self, p):
		self.is_married_to = 0
		p.is_married_to = 0	

	def just_married_with(self, p):
		if p.GENRES == "Male" and self.GENRES == "Female":
			self.last_name = p.last_name
		if self.is_married() == True or p.is_married() == True:
			raise Exception("Already married")
		if self.can_be_married() == False or p.can_be_married() == False:
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()

	def can_have_child(self):
		return False	

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
		if p is None or not (isinstance(p,Adult) or isinstance(p,Senior)):
			raise Exception("p is not an Adult or Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if type(first_name) is not str or first_name is None:
			raise Exception("string is not a string")
		if ((len(date_of_birth) is not 3) and (all(isinstance(x, int) for x in date_of_birth))):
			raise Exception("date_of_birth is not a valid date")
		if isinstance(genre, str) and  genre not in Person.GENRES:
			raise Exception("genre is not valid")
		if isinstance(eyes_color, str) and eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")
		if self.can_have_child() == False or p.can_have_child() == False :
			raise Exception("Can't have baby")	
		new_baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
		self.children.append(new_baby.get_id())
		p.children.append(new_baby.get_id())
		return new_baby

	def adopt_child(self, c):
		if self.can_have_child == False:
			raise Exception("Can't adopt child")
		self.children.append(c.get_id())				

class Adult(Person):

	def can_run(self):
		return True

	def need_help(self):
		return False

	def is_young(self):	
		return False

	def can_vote(self):	
		return True	

	def can_be_married(self):
		return True	

	def is_married(self):
		if self.is_married_to != 0:
			return True
		else:
			return False 

	def divorce(self, p):
		self.is_married_to = 0
		p.is_married_to = 0	 

	def just_married_with(self, p):
		if p.GENRES == "Male" and self.GENRES == "Female":
			self.last_name = p.last_name
		if self.is_married() == True or p.is_married() == True:
			raise Exception("Already married")
		if self.can_be_married() == False or p.can_be_married() == False:
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()

	def can_have_child(self):
		return True	

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
		if p is None or not (isinstance(p,Adult) or isinstance(p,Senior)):
			raise Exception("p is not an Adult or Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if type(first_name) is not str or first_name is None:
			raise Exception("string is not a string")
		if ((len(date_of_birth) is not 3) and (all(isinstance(x, int) for x in date_of_birth))):
			raise Exception("date_of_birth is not a valid date")
		if isinstance(genre, str) and  genre not in Person.GENRES:
			raise Exception("genre is not valid")
		if isinstance(eyes_color, str) and eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")
		if self.can_have_child() == False or p.can_have_child() == False :
			raise Exception("Can't have baby")	
		new_baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
		self.children.append(new_baby.get_id())
		p.children.append(new_baby.get_id())
		return new_baby

	def adopt_child(self, c):
		if self.can_have_child == False:
			raise Exception("Can't adopt child")
		self.children.append(c.get_id())			

class Senior(Person):

	def can_run(self):
		return False			
				 	
	def need_help(self):
		return True	

	def is_young(self):	
		return False

	def can_vote(self):
		return True	

	def can_be_married(self):
		return True	

	def is_married(self):
		if self.is_married_to != 0:
			return True
		else:
			return False 

	def divorce(self, p):
		self.is_married_to = 0
		p.is_married_to = 0	


	def just_married_with(self, p):
		if p.GENRES == "Male" and self.GENRES == "Female":
			self.last_name = p.last_name
		if self.is_married() == True or p.is_married() == True:
			raise Exception("Already married")
		if self.can_be_married() == False or p.can_be_married() == False:
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()

	def can_have_child(self):
		return False	

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
		if p is None or not (isinstance(p,Adult) or isinstance(p,Senior)):
			raise Exception("p is not an Adult or Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if type(first_name) is not str or first_name is None:
			raise Exception("string is not a string")
		if ((len(date_of_birth) is not 3) and (all(isinstance(x, int) for x in date_of_birth))):
			raise Exception("date_of_birth is not a valid date")
		if isinstance(genre, str) and  genre not in Person.GENRES:
			raise Exception("genre is not valid")
		if isinstance(eyes_color, str) and eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")
		if self.can_have_child() == False or p.can_have_child() == False :
			raise Exception("Can't have baby")	
		new_baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
		self.children.append(new_baby.get_id())
		p.children.append(new_baby.get_id())
		return new_baby

	def adopt_child(self, c):
		if self.can_have_child == False:
			raise Exception("Can't adopt child")
		self.children.append(c.get_id())							 	
'''
p = Person(1, "Julien", [12, 24, 1980], "Male", "Blue")
p.last_name = "Dupont"
print "New person %s %s" % (p.get_first_name(), p.last_name)
'''
'''
p = Person(1, "Julien", [12, 24, 1980], "Male", "Blue")
p.last_name = "Dupont"
print "%s has %d years old" % (p, p.age())

p2 = Person(2, "Marc", [2, 4, 1986], "Male", "Green")
p2.last_name = "Zuckerberg"

if p > p2:
    print "%s is older than %s" % (p, p2)
else:
    print "%s is younger than %s" % (p, p2)
'''
'''
a = Adult(1, "Marc", [12, 24, 1980], "Male", "Blue")
a.last_name = "Zuckerberg"
b = Baby(3, "Steeve", [7, 4, 2015], "Male", "Green")
b.last_name = "Rod"

if a.can_vote():
    print "%s can vote" % (a)
if b.can_vote():
    print "%s can vote" % (b)
if a.is_young():
    print "%s is young" % (a)
if b.need_help():
    print "%s needs help" % (b)
'''  
'''
my_family_p = []
my_family = load_from_file("my_family.json")
#print "I have %d members in my family" % len(my_family)
for person in my_family:
	if person['type'] == "Person" :
		p = Person(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
		p.last_name = person['last_name']
		my_family_p.append(p)
#		print person['first_name']
	elif person['type'] == "Baby" :
		b = Baby(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
		b.last_name = person['last_name']
		my_family_p.append(b)

	elif person['type'] == "Teenager" :
		b = Teenager(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
		b.last_name = person['last_name']
		my_family_p.append(b)
		
	elif person['type'] == "Adult" :
		b = Adult(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
		b.last_name = person['last_name']
		my_family_p.append(b)

	elif person['type'] == "Senior" :
		b = Senior(person['id'], person['first_name'], person['date_of_birth'], person['genre'], person['eyes_color'])
		b.last_name = person['last_name']
		my_family_p.append(b)			
#print [per.json() for per in my_family_p]				 
#print my_family_p[1].last_name 

save_to_file(my_family_p, "my_family2.json")
'''
'''
my_family = load_from_file("my_family.json")
print "I have %d members in my family" % len(my_family)
	
# new baby!
b = Baby(3, "Tony", [7, 4, 2015], "Male", "Green")
b.last_name = "Foto"
my_family.append(b)
save_to_file(my_family, "my_family.json")
'''
'''
my_family = load_from_file("my_family.json")

marc = my_family[0]
vanessa = my_family[1]

if marc.is_married():
    print "Marc is married"

marc.just_married_with(vanessa)
if marc.is_married():
    print "Marc is NOW married"

save_to_file(my_family, "my_family.json")
'''

my_family = load_from_file("my_family.json")

marc = my_family[0]
vanessa = my_family[1]
boby = my_family[2]

vanessa.adopt_child(boby)
marc.adopt_child(boby)
monica = vanessa.has_child_with(marc, 5, "Monica", [5, 6, 2016], "Female", "Blue")

print "Vanessa has %d children" % (len(vanessa.children))

save_to_file(my_family, "my_family.json")

