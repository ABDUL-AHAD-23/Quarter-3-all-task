# Task 1; Create account on Twitter X and upload post on Quarter 3 !st class review.

      # https://x.com/mhanifh046/status/1895807501234573688

# Task 2; Create account on LinkedIn and upload post on Quarter 3 !st class review.

     # https://www.linkedin.com/posts/abdul-ahad-63344329b_giaic-activity-7302012950461005826-w7CA?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEiAe8cB_vULzQ8RGUrq04Khlt0CUcXp3Rg

# Task 3; Create 1 Folder for All assignments/porjects/tasks and upload on GitHub

     # https://github.com/ABDUL-AHAD-23/Quarter-3-all-task

# Task 4; Create 1st python code `Hello world` and upload on GitHub

print("Hello world")
print()

# Task 5: Create 2nd Python code on different data types and upload on GitHub

       # Integer Data Type Example: Age Verification System

print("Welcome to the age verification system!")
try:
    age = int(input("Enter your age:"))  

    if age >= 18:
        print("You are eligible for voting") 
        print() 
    else:
        print("You are not eligible for voting")  
        print()
except ValueError:
    print("Please enter a numeric age only")
    print()

        # Float Data Type Example: Temperature Checker

print("Welcome to the temperature checker!")
try:
    temperature = float(input("Enter the temperature: "))  

    if temperature == 36.1 :
        print("You have a healthy temperature")
        print()
    elif temperature < 35.5:
        print("You have a Hypothermia (dangerous) temperature")  
        print()
    elif temperature > 38.5:
        print("You have a Fever (dangerous) temperature")
        print()
    elif temperature > 41.:
        print("You have a Life-threatening temperature")
        print()
except ValueError:
    print("Please enter a numeric temperature only")
    print()

        # String Data Type Example: Name Length Checker

print("Welcome to the name length checker!")
try:
    name = str(input("Enter your name: "))

    if len(name) > 12:
        print("You have a long name")
    elif len(name) == 12:
        print("you have a perfect name")
    else:
        print("You have a short name")
        print()
except ValueError:  
    print("Please enter a alphabetic name only")
    print()

        # Boolean Data Type Example: Simple Login System

print("Welcome to the login system!")
try:
    password = input("Enter the password: ")  

    if password == "123":
        print("Access granted!")
    elif password == "abc":
        print("Access granted!")
    else:
        print("Access denied!")
        print()
except ValueError:
    print("Please enter a valid password")
    print()

        # List Data Type Example: Student Marks System  

print("Welcome to the student marks system!")
try:    
    marks = [int(x) for x in input("Enter the marks separated by space: ").split()]  

    total_marks = 0
    for mark in marks:
        total_marks += mark

    print("Total marks:", total_marks)
    print()
except ValueError:
    print("Please enter valid marks")
    print()

        # Tuple Data Type Example: Student Information System   

print("Welcome to the student information system!")
try:
    student = tuple(input("Enter the student information separated by space: ").split())  

    print("Student information:", student)
    print() 
except ValueError:
    print("Please enter valid student information")
    print()

        # Dictionary Data Type Example: Student Result System     

print("Welcome to the student result system!")
try:
    student = {"Name": input("Enter the name: "), "Roll No": int(input("Enter the roll no: ")), "Marks": int(input("Enter the marks: "))}  

    print("Student result:", student)
    print()
except ValueError:
    print("Please enter valid student information")
    print() 



