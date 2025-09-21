# Retirement Calculator. 
# Make a calculator that asks for your age, shows how many years you have until retirement - based on the 
# users desired retirment age 
from datetime import datetime

def start_program():
  answer = input("Do you want to use the retirement calculator? (y/n) ").lower()
  if answer == 'n':
    print('Sorry to see you go!')
  else: 
    age = get_age()
    desired_retirement_age = get_desired_retirement_age()
    years_until_retirement = calculate_years(age, desired_retirement_age)
    calculate_retirement_year(years_until_retirement)

def get_age():
  return int(input('Please enter your current age: '))

def get_desired_retirement_age():
  return int(input("What is your desired retirement age: "))

def calculate_years(age, desired_retirement_age):
  return desired_retirement_age - age

def calculate_retirement_year(years_until_retirement): 
  current_year = datetime.now().year
  retirement_year = current_year + years_until_retirement
  print('It is currently', current_year,", so you can retire in", retirement_year)


start_program()