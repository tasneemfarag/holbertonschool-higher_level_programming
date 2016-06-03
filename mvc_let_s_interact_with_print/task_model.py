'''Class'''
class TaskModel ():

	'''Public method'''

	'''Constructor'''
	def __init__(self, title):
		#Private attributes
		if title is not str and title is None:
			raise Exception("title is not a string")	
		self.__title = title
		self.__callback_title = callback_title#pointer to function

		
	'''Getter'''
	def get_title(self):
		return self.__title

	'''Setter'''
	def set_callback_title(self, callback_title):
		self.__callback_title = callback_title

	def toggle(self):	
