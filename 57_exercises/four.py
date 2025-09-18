# Fourth Exercise - Simple math problem
# Take two numbers and show all mathematical operations on them

def program_start():
  answer = input('Would you like to use a simple program? (y/n) ').lower()
  if answer == 'n':
    print('Sad...You dont want to play! Well, have a great day!')
  else:
    first_number = get_first_number()
    second_number = get_second_number() 
    addition(first_number, second_number)
    subtraction(first_number, second_number)
    multiply(first_number, second_number)
    divided(first_number, second_number)

def get_first_number():
    while True:
      first_number = input("Enter a number: ")
      result = number_check(first_number)
      if result is not None:  # valid number
          return result  # exit loop and return number

def get_second_number():
  while True:
    second_number = input("Enter a number: ")
    result = number_check(second_number)
    if result is not None:  # valid number
        return result  # exit loop and return number

def number_check(number):
    try:
        return int(number)
    except ValueError:
        print("Please enter a valid number.")
        return None

def addition(first_number, second_number):
  added = first_number + second_number
  print(first_number, '+', second_number, '=', added)

def subtraction(first_number, second_number):
  subtracted = first_number - second_number
  print(first_number, '-', second_number, '=', subtracted)

def multiply(first_number, second_number):
  multiplied = first_number * second_number
  print(first_number, '*', second_number, '=', multiplied)

def divided(first_number, second_number):
  divided = first_number / second_number
  print(first_number, '/', second_number, '=', divided)


program_start()