#Area of rectangle room

def program_start():
  print('Welcome to room calculation program!')
  answer = input('Do you want to play? (y/n) ').lower() 
  if answer != 'y':
    print("Thank you for using!")
  else: 
    length_of_room = get_length_of_room()
    width_of_room = get_width_of_room()
    tell_user_what_entered(length_of_room, width_of_room)
    area = get_area(length_of_room, width_of_room)

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

def tell_user_what_entered(length_of_room, width_of_room):
  print('You entered dimensions of', length_of_room, 'feet by', width_of_room, 'feet.')

def get_area(length_of_room, width_of_room): 
   return length_of_room * width_of_room

def show_user_area_result(area):
   pass
  
    
program_start()
