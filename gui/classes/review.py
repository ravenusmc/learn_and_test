class Person:
  
  def __init__(self, name):
    self.name = name 

  def set_name(self, name): 
    self.name = name 

  def get_name(self): 
    return self.name 

obj = Person('Mike')
obj.set_name('Mike')
print(obj.get_name())
