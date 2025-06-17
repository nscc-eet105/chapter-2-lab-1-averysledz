first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

numbers_marbles = input ("Enter the number of marbles you wish to purchase: ")
print(" ")
print(" ")
print ("Order prepared for " + first_name + " "+  last_name)
numbers_marbles = int(numbers_marbles)
cost_per = 1.20
total_cost = numbers_marbles * cost_per
print(" ")
print (f"{numbers_marbles} marbels orderd @ ${cost_per:.2f}") 
print(f"Total cost is ${total_cost:.2f} ")
