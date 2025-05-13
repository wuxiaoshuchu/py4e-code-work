# practice1
# define a class student
# request1:attributes includes name,student_number,score for kokugo,math,english
# 2:can set students'score
# 3:can print the student's all score

class Student:
  def __init__(self, name, student_id): #attributes
    self.name = name #self.name is the attribute to object, name is parameter from name on the last line
    self.student_id = student_id
    self.grades = {"kokugo":0, "math":0, "english":0} #crate a dic for grades

  def set_grade(self, course, grade): #method
    if course in self.grades:
      self.grades[course] = grade

  def print_grade(self): #method
    print(f"student{self.name}(student_id:{self.student_id})'s grade is:")
    for course in self.grades:
      print(f"{course}:{self.grades[course]}")

sakuma = Student("佐久間", "22311001")
sakuma.set_grade("kokugo", 95)
sakuma.set_grade("math", 92)
sakuma.set_grade("english", 91)
sakuma.print_grade()

honnma = Student("本間", "22311002")

# print(sakuma.name) # object.attributes
# sakuma.set_grade("math",95)
# print(sakuma.grades)