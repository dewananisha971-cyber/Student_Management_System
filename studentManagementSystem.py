class Student:
 def __init__(self,name,Student_Id,email,age,department):
  self.name=name
  self.Stu_id=Student_Id
  self.__email=email
  self._age=age
  self.department=department
  #Getter
 def get_email(self):
   return self.__email
  #Setter
 def set_email(self,email):
    if "@" in email and "." in email:
     self.__email=email
     print("Email updated successfully")
    else:
     print("Invalid email")


 def display_info(self):
   print(f"-------Student Info------")
   print(f"Name:{self.name}")
   print(f"Id:{self.Stu_id}")
   print(f"Department:{self.department}")
 @staticmethod
 def search_stu_system():
   record={ }
   for i in range(5):
    Stu_N = input(" Enter student Name : ")
    Stu_id=input("Enter student Id")
    record[Stu_id]=Stu_N
   search_name=input(" Enter student name to search : ")
   if search_name in record.values():
      print(f"{search_name} found in the system")
   else:
      print(f"{search_name} not found")
  #Method overloading using args
 def calculate_result(self,*marks):
   if len(marks)==0:
    print("No marks entered")
    return
   T_m=sum(marks)
   A_m=(T_m/len(marks))
   print("Total:",T_m)
   print("Average:",A_m)
   #Static Method
 @staticmethod
 def calculate_grade(score):
   if 80<= score <=100:
      print("Excellent Student")
      return "A+"
   elif 70<= score <=79:
    print("Good Student")
    return "B"
   elif 60<= score <=69:
      print("Average Student")
      return "C"
   elif 50<= score <=59:
      print("Medium Student")
      return "D"
   else:
      print("Weak Student")
      return "F"

   
 def get_student_type(self):
      print("General Student")
#Method overriding   
class UnderGrad_Student(Student):
  def __init__(self,name,Student_Id,email,age,department,semester):
    super().__init__(name,Student_Id,email,age,department)
    self.semester=semester
  def display_info(self):
      super().display_info()
      print(f"Semester ,{self.semester}")  
  def get_student_type(self):
      print("UnderGraduate Student")
#Method overriding
class Graduate_Student(Student):
  def __init__(self,name,Student_Id,email,age,department,research_topic):
    super().__init__(name,Student_Id,email,age,department)
    self.research_t=research_topic
  def display_info(self):
    super().display_info()
    print(f"Research Topic ,{self.research_t}")
  def get_student_type(self):
       print("Graduate Student")


student1=Student("Anisha","233009712","anisha@eamil.com",22,"CSE")
student2=UnderGrad_Student("Nishat","233004112","nish@eamil.com",22,"CSE",10)
student3=Graduate_Student("Shruti","233003812","Shuti@eamil.com",22,"CSE","AI")
print(student1.get_email())
student1.calculate_result(80,97,56)
student2.display_info()
student3.display_info()
grade=Student.calculate_grade(85)
print("Grade",grade)
students=[student1,student2,student3]
for student in students:
  student.get_student_type()
  