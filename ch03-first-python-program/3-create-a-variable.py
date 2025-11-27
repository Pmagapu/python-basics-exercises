# 3.3 - Create a Variable
# Solutions to review exercies


# Exercise 3 (exercises 1 and 2 are done in interactive window)
# This solution works for Exercises 1 and 2 by typing the same lines into the
# interactive window.

# Display a string directly
print("hello")


# Display the contents of a string variable
my_string = "hi"
print(my_string)

#adding extra line for commit

#Want to add this line to a new branch created locally 
# as a local commit


# EXTRA SCENARIO: Variable Types and Type Conversion
# Understanding data types is crucial in Python

# Scenario 4: Exploring different variable types
print("\n--- Scenario: Variable Types ---")

# Integers (whole numbers)
age = 25
print(f"My age: {age}, Type: {type(age)}")

# Floats (decimal numbers)
height = 5.9
print(f"My height: {height}, Type: {type(height)}")

# Strings (text)
name = "Alice"
print(f"My name: {name}, Type: {type(name)}")

# Booleans (True/False)
is_student = True
print(f"Is student: {is_student}, Type: {type(is_student)}")

# Type conversion - converting one type to another
print("\n--- Type Conversion ---")
number_string = "42"
converted_number = int(number_string)
print(f"String '{number_string}' converted to integer: {converted_number}")

# Converting number to string
count = 100
count_string = str(count)
print(f"Integer {count} converted to string: '{count_string}'")