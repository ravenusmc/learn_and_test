# Seventh program - Pizza Party - write a program to evenly divide pizza's. prompt for the number of people
# The number of pizza's and the number of slices per pizza. Ensure that the number turns out even. Display
# the number of pieces of pizze each person should get. If there are left overs show the number of leftovers.
# How many people 
# How many pizzas do you have 

def program_start():
  response = input("Do you want to use the program (y/n) ").lower()
  if response != "y":
    print('Ok, no problem, come back again!')
  else: 
    pass 

def number_of_people():
  pass

def number_check(number):
    try:
        return int(number)
    except ValueError:
        print("Please enter a valid number.")
        return None

program_start()
