class Person:
  def __init__(self, name, age,gpa):
    self.name = name
    self.age = age
    self.gpa=gpa

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36,3.23)
p1.myfunc()
print(p1.age)
print(p1.gpa)
