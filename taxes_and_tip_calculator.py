"""this program made by Tasneem Farag student at Holberton school
the program name is calculator for taxes and tip thats calculat the total of meal after adding the
taxes and tip""" 


#welcoming the person
print("Welcome to the taxes and tip calculator!")
#ask the user(person) for the price before the tax
meal_bf_tax = input("What is the price before tax? ")

#ask the user the value of taxes
tax = input("What are the taxes? (in %) ")

#ask the user the value of the tip
tip = input("What do you want to tip? (in %) ") 


#the price of the meal after the taxes
meal =meal_bf_tax + (meal_bf_tax * tax/100) 
#the price of of the meal after the taxes and tip 
total = meal + (meal * tip/100)
 
#print the total price 
print "The price you need to pay is: $" ,total