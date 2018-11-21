# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 00:17:50 2018

@author: Leila
"""
#%%

#Exercise 1
# Create a Student class that has the following attributes:
#
#name
#last name
#age
#master (either MCSBT or MDBI)
# Make sure you parametrize all those fields in the constructor.

#Exercise 2
#Add a print_student method in the Student class that prints a line like follows for the object.
#
#Pepe García is a 55 year old student of the MCSDBI masters programme
#
#Create a list of all 28 Students representing all students in this class.  
#Then iterate over all of them and call print_student on each one to print its description.

class Student:
    
    def __init__(self,name,last_name,age,master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
    
    def print_student(self,student):
        print(student.name + " " + student.last_name + " is a " + student.age + 
              " year old student of the " + student.master + " programme")
            
class Programme:
    
    students_list = []
    
    def __init__(self,programme_name):
        self.programme_name = programme_name
        
    def add_students_to_list(self,student):
        self.students_list.append(student)
            
    def print_students_list(self):
        for student in self.students_list:
            student.print_student(student)
            

MCSBTBDI = Programme("MCSBTBDI")

MCSBTBDI.add_students_to_list(Student("Alejandro", "Meneses", "27", "MCSBT")) 
MCSBTBDI.add_students_to_list(Student("Agata", "Kaczmarek", "31","MDBI"))
MCSBTBDI.add_students_to_list(Student("Anastasia", "Lasunina", "25", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Anikken", "Barstad", "27", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Candela", "Noya", "24", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Daniil", "Osipov", "21", "MDBI"))
MCSBTBDI.add_students_to_list(Student("David", "Barrero Gonzalez", "31", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Edem", "Francois", "28", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Eduardo", "Paraja", "23", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Florian", "Diegruber", "25", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Hannah", "Oldorf", "23", "MCBT"))
MCSBTBDI.add_students_to_list(Student("Isabella", "Rosenthal", "27", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Javier", "Fernandez", "24", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Lukas", "Hauser", "28","MDBI"))
MCSBTBDI.add_students_to_list(Student("Leila", "Tazi", "27", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Laura", "Kageneck", "23", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Monica", "Alvarenga","28", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Natalie", "Cedeno", "26", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Octavio", "Ramírez", "28", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Tancredi", "Bernard", "21", "MCSBT"))
MCSBTBDI.add_students_to_list(Student("Yasmine", "Lyagoubi", "23", "MDBI"))
MCSBTBDI.add_students_to_list(Student("Arthur", "Maroquene-Froissart","23", "MCSBT"))

MCSBTBDI.print_students_list()



