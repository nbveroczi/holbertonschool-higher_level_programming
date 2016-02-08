""" My name is Naomi Veroczi and I am a student at Holberton School. The name of my program is "Taxes and tip calculator."  This program will prompt the user three questions one after the other to determine the price of a meal before tax, what the tax is and how much the user wishes to tip."""

print "Welcome to the taxes and tip calculator!"

#I created a variable called price and make it equvalent to the user input I also needed to convert the string of the price to a number so I could do artithmetic calculations
price = float(raw_input("What is the price before tax?"))

#I created a variable called tax and make it equivalent to the user input I also needed to convert the string of the price to a number so I could do artithmetic calculations   
tax = float(raw_input("What are the taxes? (in %)"))

#I created a variable called tip and make it equivalent to the user input I also needed to convert the string of the price to a number so I could do artithmetic calculations   
tip = float(raw_input("What do you want to tip? (in %)"))

#The tax is equal to the price of the meal multiplied by the tax (and the tax is divided by 100 because it was originally given as a percentage)  
tax = price * (tax / 100) 

#The tip is equal to the price of the meal plus the tax, multiplied by the tip (and the tip is divided by 100 because it was given as a percentage)
tip = (price + tax) * (tip / 100)

#I created a variable called total which is equal to the price of the meal plus the tip plus the tax
total = price + tip + tax
 
print "The price you need to pay is: $%s" %(total)

