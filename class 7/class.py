from typing import List,Dict

class Student:
    def __init__(self, id:int, name:str, courses:Dict[str,List[int]]):
        self.id:int = id 
        self.name = name 
        self.courses:Dict[str,List[int]] = courses 

    def add_course(self, name_curse:str):
        self.courses[name_curse] = []

    def add_grade(self,name_curse:str, grade:int):
        self.courses[name_curse].append(grade)

    def get_average_grade(self,name_course:str):
        if name_course in self.courses:
            sum:int = 0
            for i in range(0,len(self.courses[name_course])):
                sum += self.courses[name_course][i]
            return sum/len(self.courses[name_course])
        else:
            return
        
class University:
    students:List[Student] = []
    def __init__(self, student:Student):
        self.students.append(student)
        
    def add_student(self, student:Student):
        self.students.append(student)
            
    def get_average_grade(self, id:int):
        for student in self.students:
            if student.id == id:
                sum:float = 0
                for course in student.courses:
                    sum+=student.get_average_grade(course)
                return sum/len(student.courses)
            
        return
            
stud1 = Student(1,"VLAD",{"Heograf":[7,3,10],"Math":[11,10,6]})
# print(stud1.get_average_grade("Math"))
stud1.add_course("Bibi")
stud1.add_grade("Bibi",10)
stud1.add_grade("Bibi",6)
# print(stud1.get_average_grade("Bibi"))

stud2 = Student(2,"Gavbr",{"Heograf":[7,3,1],"Math":[5,1,7]})
stud3 = Student(3,"Bior",{"Heograf":[5,3,10],"Math":[6,7,7]})
stud4 = Student(4,"aggs",{"Heograf":[7,3,3],"Math":[7,10,6]})
    
univesrite = University(stud1)
univesrite.add_student(stud2)
univesrite.add_student(stud3)
univesrite.add_student(stud4)

print(univesrite.get_average_grade(1))

print(univesrite.get_average_grade(2))
print(univesrite.get_average_grade(3))