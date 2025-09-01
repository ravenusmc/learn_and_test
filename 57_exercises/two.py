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
    return answer
  elif answer == "N":
    print('I understand, you may be busy!')



answer = greet()
choice(answer)
