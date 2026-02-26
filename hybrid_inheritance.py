class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Student(Person):
  def __init__(self,name,age,roll_no):
    super().__init__(name,age)
    self.roll_no=roll_no

class Teacher(Person):
  def __init__(self,name,age,subject):
    super().__init__(name,age)
    self.subject=subject


class Academic:
  def __init__(self,course,cgpa):
    self.course=course
    self.cgpa=cgpa
  
class Sports:
  def __init__(self,sport_name,level):
    self.sport_name=sport_name
    self.level=level

class AllRounderStudent(Student,Academic,Sports):
  def __init__(self, name, age, roll_no, course=None, cgpa=None, sport_name=None, level=None,is_Academic=False,is_Sports=False):
    Student.__init__(self,name,age,roll_no)
    self.is_Academic=is_Academic
    self.is_Sports=is_Sports
    if is_Academic:Academic.__init__(self,course,cgpa)
    if is_Sports:Sports.__init__(self,sport_name,level)
  def display(self):
      print(f"Student Details\nname:-{self.name}\nage:-{self.age}\nroll_no:-{self.roll_no}")
      if self.is_Academic:
        print(f"course:-{self.course}\ncgpa:-{self.cgpa}")
      if self.is_Sports:
        print(f"sport_name:-{self.sport_name}\nlevel:-{self.level}")
      if self.is_Academic and self.is_Sports:print("All rounder student")
obj = AllRounderStudent(

    "Tausif",
    21,
    101,
    course="B.Tech IT",
    cgpa=8.51,
    sport_name="Cricket",
    level="State",
    is_Academic=False,
    is_Sports=True
)

obj.display()


    