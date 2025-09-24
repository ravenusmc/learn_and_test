#Area of rectangle room

def program_start():
  print('Welcome to room calculation program!')
  answer = input('Do you want to play? (y/n) ').lower() 
  if answer == 'n':
    print("Thank you for using!")
  else: 
    length_of_room = get_length_of_room()
    width_of_room = get_width_of_room()

def get_length_of_room():
  while True: 
    length_of_room = input("What is the length of the room in feet: ")
    result = number_check(length_of_room)
    if result is not None:  # valid number
        return result  # exit loop and return number

def get_width_of_room():
  while True: 
    width_of_room = input('What is the width of the room in feet: ')
    result = number_check(width_of_room)
    if result is not None:  # valid number
        return result  # exit loop and return number

def number_check(number):
    try:
        return int(number)
    except ValueError:
        print("Please enter a valid number.")
        return None
    
program_start()
