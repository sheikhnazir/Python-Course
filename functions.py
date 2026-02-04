# ----------------------------
# Function without parameters
# ----------------------------

def my_function():
    # This function does not take any input
    # It simply prints a message when called
    print("Hello My First Function...")


# ----------------------------
# Function with parameters
# ----------------------------

def add(a, b):
    # a and b are parameters (inputs to the function)
    # This function adds two numbers and prints the result
    print(a + b)

    # Homework:
    # 1. Write a function to subtract two numbers
    # 2. Write a function to multiply two numbers
    # 3. Write a function to divide two numbers

# ----------------------------
# Function: Fahrenheit to Celsius
# ----------------------------

def fahrenheit_to_celsius(fahrenheit):
    # 'fahrenheit' is the input temperature value
    # Formula to convert Fahrenheit to Celsius:
    # (F - 32) × 5 / 9
    celsius = (fahrenheit - 32) * 5 / 9

    # Return the converted Celsius value
    return celsius


# ----------------------------
# Function: Return a String
# ----------------------------

def print_string(cityName):
    # This function receives a string as input
    # and returns the same string
    return cityName


# ----------------------------
# Program Execution Starts Here
# ----------------------------

# This condition ensures the code below runs
# only when this file is executed directly
# (not when imported into another file)
if __name__ == "__main__":

    # Calling a function without parameters
    # (Function definition should exist above)
    my_function()

    # Printing a number directly
    print(1777288288)

    # Calling the add function with different arguments
    add(5, 9)
    add(100929, 882772)

    # Convert temperature from Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(77)

    # Print the returned Celsius value
    print(celsius)

    # Call function that returns a string
    cityName = print_string("Srinagar")

    # Print returned string
    print(cityName)


# ----------------------------
# Homework
# ----------------------------
# 1. Write a function get_greeting(name)
#    → Returns "Hello <name>"
# 2. Write a function to calculate sum of 3 numbers
# 3. Convert Celsius to Fahrenheit


