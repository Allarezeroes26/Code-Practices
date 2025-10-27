class Student:
  def __init__ (self, name, subjects):
    self.name = name
    self.subjects = subjects
    
  def study(self, days):
    for days in range(1, days+1):
      print(f"Day {days} of studying")
      for subject in self.subjects:
        print(f"Studying {subject}")
      print(f"Finished Day {days}")


stu = Student("Erwin", ['Math', 'English', 'Science', 'Programming'])
stu.study(3)