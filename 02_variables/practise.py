# Working With Variables 

# Assign Data
# variable_name = value 
Employee_name = "Mona" # string 
Employee_age = 25 # int
Employee_gpa = 9.5 # float
Employee_passed = True # boolean

# Retrieve Data 
print(Employee_name)
print(Employee_age)
print(Employee_gpa)
print(Employee_passed)

# Get Identity/Memory Address Of Variables 
print(id(Employee_name))

# Get data type of the variables
print(type(Employee_name))
print(type(Employee_age))
print(type(Employee_gpa))
print(type(Employee_passed))

#Assigning single variable
price = 250
print(price)

#Assigning multiple variable
a,b,c,d = 10,20,30,40
print(a,b,c,d)

#Assigning same value to multiple variables
w = x = y = z = 10
print(w,x,y,z)

#Changing the Value of Variable
a = 10
a = "Hi Good Morning"
print(a)

#Global variable (Available throughout the program)
x = 100         # Assiging a value to variable

def value () :   #defining a function (def is a keyword used to define function) / : ends the funtiocn header
    print(x)

value()          #calling 
print(x)         #output

#Local variable (Available only inside function)

def value():
    f = 200
    print(f)


#value()
#print(f) #NameError: name 'f' is not defined


#Global + Local (modify global inside function)
Add = 1         #(Add)variable is defined outside the function and using the same variable inside stating 
                   # global Add to be used as global variable inside the function
def value():
    global Add 
    Add += 2

value()
print(Add) 

def value():            #even if the variable(sub) is defined inside the function oython takes it as 
                            #global variable and runs the function 
    global Sub 
    Sub = 2
    Sub -= 6

value()
print(Sub) 