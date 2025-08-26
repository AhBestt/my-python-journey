# Type Error, Checking and Conversion
### TypeError
These errors occur when you are using the wrong data type. e.g. `len(12345)` <br>

Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer) <br>

### Task1: Fix the len() function so it has no more warnings or errors. <br>
Original code: 
```bash
len(12345)
```

### Type Checking
You can check the data type of any value or variable in python using the type() function <br>
```bash
print(type("abc")) # will give you <class 'str'>
```

### Task2: Write out 4 type checks to print all 4 data types
Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <br>
<class 'str> <class 'int'> <class 'float'> and <class 'bool'> <br>

### Type Conversion
You can convert data into different data types using special functions.  <br>
output: <br>
```bash
float()
int()
str()
```

### Task3: Make this line of code run without errrors
```bash
print("Number of letters in your name: " + len(input("Enter your name")))
```

___
### Solution
[Solution](https://github.com/AhBestt/my-python-journey/blob/main/solution/day-002-type_error_checking_and_conversion.py)
