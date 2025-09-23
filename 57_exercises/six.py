#Area of rectangle room

def program_start():
  print('Welcome to room calculation program!')
  answer = input('Do you want to play? (y/n) ').lower() 
  if answer == 'n':
    print("Thank you for using!")
  else: 
    get_length_of_room()

def get_length_of_room():
  length_of_room = input("What is the length of your room: ")

program_start()