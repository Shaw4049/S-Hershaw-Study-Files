# Define a Student class, with a constructor to take in name and year as parameters 
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    # Create an instance variable called self.attendance and set it to an empty dictionary
    self.attendance = {}
  # Add add_grade method taking grade as a parameter. Verify that grade is of type Grade, and if so add to the student grades list
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  #Write a method that returns the student's average score
  def get_average(self):
    if self.grades == 0:
      return 0
    total = 0
    for grade in self.grades:
      total += grade.score
    return total / len(self.grades)
    
# Create a Grade class, with .minimum_passing as an attribute set to 65
class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  # Write a grade method that returns whether a grade has a passing score
  def is_passing(self):
    return self.score >= self.minimum_passing

# Three instances of the Student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Create a new Grade with a score of 100 and add to Pieters grades attribute using add_grade
pieter.add_grade(Grade(100))
pieter.attendance["2024-06-01"] = True

print(pieter.attendance)
