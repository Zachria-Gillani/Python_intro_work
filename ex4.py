cars=100
#I had poor form, all operators such as plus, minus and equal all need a space around operators.
#The equals sign sets a variable equal to another making them sysnonymous
space_in_a_car=4.0
#Even if I used 4 instead of 4.0 it will give the same answer
drivers=30
#Using a single equal space makes the variable assigned to the left of the equal.
#Using the equals sign sets a variable equal to something else.  No quatiations needed.
passengers=90
#No quotatios were needed, just a name and a equal and a variable.
cars_not_driven=cars-drivers
#Here we start using variable names and naming math functions no quoatations need.
cars_driven=drivers
#Here we set a varaible equal to another variable in a logical manner.
carpool_capacity=cars_driven*space_in_a_car
#The _ character is an underscore. * is times and / is divide.
average_passengers_per_car=passengers/cars_not_driven


print("There are",cars,"cars available.")
#Here I used cars to equal 100.  Therefore when I write cars, the variable associated with cars variable will appear, here it is 100.
print("There are only",drivers,"drivers available")
#Here the drivers variable is made equal to the number I made driver equal.I place it in between 2 strings to make it appear.
print("There will be",cars_not_driven,"empty cars today.")
#Here cars not driven was set equal to a math function which is executed when I run the sentence.  It is offset by 2 seperate strings.
print("We can transport",carpool_capacity,"people today")
#Carpool capacity is a math function executed when I run the print code.
print("We have",passengers,"to carpool today.")
#Passengers is a variable=90.When printed will say 90
print("We need to put about",average_passengers_per_car,
"in each car.")
#This is another math function that when run gives the average and also 2 pritned strings.
