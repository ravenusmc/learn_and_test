# Create a program that prompts for an input string and displays the number of characters in the string 
# The original string must be seen 

def greet():
  print("Hello! I'm a simple program!")
  print("I will ask you for a word or sentence")
  print("I will then tell you how long it is.")
  answer = input("Do you want to play (Y/N): ")
  return answer


def choice(answer):
  if answer == "Y":
    print("Let us begin!")
    enter_string()
  elif answer == "N":
    print('I understand, you may be busy!')
    print('Program is now ending')

def enter_string():
  player_string = input('Please enter the word or sentence: ')
  string_length = len(player_string)
  print('The length of your word or sentence is ' )



answer = greet()
choice(answer)
