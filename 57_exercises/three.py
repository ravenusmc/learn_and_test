#Create a madlib program 
# Sentence: The NOUN ADVERB VERB to the ADJ STORE 

def program_start():
  choice = input('Good day! Do you want to play a short mad lib game? (Y/N) ').lower()
  if choice == 'n': 
    print("Sorry you don't want to play!")
  else: 
    gamestart()
    noun = enter_noun()
    adverb = enter_adverb()
    verb = enter_verb()
    adjective = enter_adjective()
    build_sentence(noun, adverb, verb, adjective)

def gamestart(): 
  print('Here we go!')

def enter_noun(): 
  return input('Please enter a noun: ')

def enter_adverb(): 
  return input('Please enter an adverb: ')

def enter_verb():
  return input('Please enter a verb: ')

def enter_adjective(): 
  return input("Please enter an adjective: ")

def build_sentence(noun, adverb, verb, adjective): 
  print('The', noun, adverb, verb, 'to the', adjective, 'store')


choice = program_start()
