class CuteCat: # create a class
  # create attributes(what CuteCat looks like etc.)
  def __init__ (self, cat_name, cat_age, cat_color): #define object's attributes
    self.name = cat_name
    self.age = cat_age
    self.color = cat_color
  #create methods(what CuteCat can do etc.)
  def speak(self):
    print("miao" * self.age) #pretend when cat is 3 years old it goes miaomiaomiao. methods gonna change by attributes
  #methods2
  def think(self,content): #parameter
    print("CuteCate{self.name}is thinking{content}")

cat1 = CuteCat("JoJo",2,"orange") #use init to create new objects and put into attributes
cat1.speak() #how to call method: attributes.name_of_method()
cat1.think("sleep on sofa or bed")