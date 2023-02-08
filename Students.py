class students:
   name = ""
   rollNo = ""
   standard = ""
   section = ""

   def get_info(self):
    print(f'{self.name} studies in {self.standard}{self.section} having roll.no - {self.rollNo}')



student1 = students()
student1.name = "Harsh Sharma"
student1.rollNo = 19
student1.section = "C"
student1.standard  = "10th"
student1.get_info()

