class Tree:
  leafs = 53458224
  age = 67
  height = 365  

  def __init__(self, type):
     self.type = type
    
  def get_older(self):
     self.age += 1

my_tree = Tree("type")

print(my_tree.age)

print(my_tree.height)

my_tree.get_older()
print(my_tree.age)

