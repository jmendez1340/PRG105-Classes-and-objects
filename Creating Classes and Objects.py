class Student(object): # Make sure the class name is capitalized
    """
    The first statement inside of class is the docstring and it documents
    the program and explains what the class will do. The Student class will define:
    StudentID, First Name, Last Name and Email as the attributes.
    """

# Classes can be used by using instantiation
# The object is the instance

logic = Student()

# Assign the values you wish to use

logic.studentID = ""
logic.firstname = ""
logic.lastname = ""
logic.email = ""

# reference the object by typing logic.(insert value like email here)
print logic.studentID

def student_info():
    s = Student()
    s.studentID = raw_input("Please enter your student id number: ")
    s.firstname = raw_input("Please enter your first name: ")
    s.lastname = raw_input("Please enter your last name: ")
    s.email = raw_input("Please enter your email address: ")
    return s

student1 = student_info()
print ("\n" + student1.studentID + " " + student1.firstname + " " + student1.lastname + " " + student1.email + "\n")

student2 = student_info()
print ("\n" + student2.studentID + " " + student2.firstname + " " + student2.lastname + " " + student2.email + "\n")

student3 = student_info()
print ("\n" + student3.studentID + " " + student3.firstname + " " + student3.lastname + " " + student3.email + "\n")
