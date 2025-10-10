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
    program_intro()
    people = number_of_people() 
    number_pizzas = number_of_pizzas()
    slices = number_of_slices_per_pizza()
    total_slices = get_total_slices(number_pizzas, slices)

def program_intro():
   print("The program will now start!")

def number_of_people():
  while True:
    number_of_people = input('How many people will be attending the party: ')
    result = number_check(number_of_people)
    if result is not None: 
       return result

def number_of_pizzas():
  while True: 
    number_of_pizzas = input("How many pizzas will be ")
    result = number_check(number_of_pizzas)
    if result is not None:
      return result 

def number_of_slices_per_pizza():
  while True: 
    number_of_slices = input("How many slices per pizza: ")
    result = number_check(number_of_slices)
    if result is not None: 
      return result 

def get_total_slices(number_pizzas, slices):
  return number_pizzas * slices

def slices_per_person(people, total_slices):
  return total_slices / people
    
def number_check(number):
    try:
      return int(number)
    except ValueError:
      print("Please enter a valid number.")
      return None


program_start()
