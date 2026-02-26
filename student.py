class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  display=lambda self:f"{self.name}\t{self.marks}"
    