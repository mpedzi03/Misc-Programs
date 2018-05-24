# Author: Michael Pedzimaz
#                                   Program Name: Client-side Student Database          Version: 0.0.1
# This is a Python program that asks the user to create students, stores them in an array, then displays them out to the console
#  should the user choose to do so. It utilizes a structure, various control schemes, and the use of multiple functions.
#  This program was written in IDLE and can be run via the command prompt in Windows OS.
import sys
# Class 'Student' we will be using to create our student objects
class Student(object):
    fname = ""
    lname= ""
    idNo = 0
# Constructor for our class
    def __init__(self, firstname, lastname, idnumber):
        self.fname = firstname
        self.lname = lastname
        self.idNo = idnumber
# Function used to create a student object from our class.
def make_student(fname, lname, idNo):
  student = Student(fname, lname, idNo)
  return student
# Main function we will use for the process of creating our student list. 
def main():
# Variables;    'maxStudCount': makes sure we don't have more than 10 students on the roster.
#                   'studentList[]: our student objects will be stored in this list
#                   'studQuery: will store our answer as to whether we want to add another student
    maxStudCount = 0
    studentList = []
    studQuery = raw_input("Would you like to add a student? (Type 'Yes' or 'No'): ")
# While loop that will pull user inputs & throw the to our 'Student' class constructor
    while studQuery == 'Yes' and maxStudCount < 10:
        fname = raw_input("Enter first name: ")
        lname = raw_input("Enter last name: ")
        idNo = raw_input("Enter ID No: ")
        person = make_student(fname, lname, idNo)
        studentList.append(person)
        maxStudCount = maxStudCount + 1
        studQuery = raw_input("Add another student? ('Yes' or 'No'): ")    
# For loop that we will iterate through our list of students and print out their information.
    for item in studentList:
        print item.fname, item.lname, item.idNo
    sys.exit()
if __name__ =='__main__':
    main()


