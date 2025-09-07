#Create a madlib program 
# Sentence: The NOUN ADVERB VERB to the ADJ STORE 

def program_start():
  choice = input('Good day! Do you want to play a short mad lib game? (Y/N) ').lower()
  if choice == 'n': 
    print("Sorry you don't want to play!")
  else: 
    gamestart()
    noun = enter_noun()
    print(noun)

def gamestart(): 
  print('Here we go!')

def enter_noun(): 
  return input('Please enter a noun: ')

choice = program_start()
