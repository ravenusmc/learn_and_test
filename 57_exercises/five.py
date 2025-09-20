# Retirement Calculator. 
# Make a calculator that asks for your age, shows how many years you have until retirement - based on the 
# users desired retirment age 

def start_program():
  answer = input("Do you want to use the retirement calculator? (y/n) ").lower()
  if answer == 'n':
    print('Sorry to see you go!')
  else: 
    age = get_age()
    desired_retirement_age = get_desired_retirement_age()

def get_age():
  return input('Please enter your current age: ')

def get_desired_retirement_age():
  return input("What is your desired retirement age: ")

def calculate_years 


start_program()