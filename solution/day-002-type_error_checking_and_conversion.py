# TypeError
#len(123)

# SolutionTask1
# No TypeError
len("Hello")

# SolutionTask2
# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
str()
int()
float()
bool()

# SolutionTask3

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))
