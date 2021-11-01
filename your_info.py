# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def askName():
    _yrName = input("Name: ")
    return _yrName

def askAge():
    _yrAge = input("Age: ")
    return _yrAge

def askAdress():
    _yrAdress = input("Adress: ")
    return _yrAdress

def display(nameA, ageA, addressA):
    print(f"Hi, my name is {nameA}. I am {ageA} years old and I live in {addressA} .")

#steps
# 1. Ask for the name then save the variable
name = askName()
# 2. Ask for age then the variable.
age = askAge()
# 3. Ask for the address then save the variable
adress = askAdress()
# 4. Display the details.
display(name, age, adress)