# This block ensures that the code runs only when this file
# is executed directly, not when it is imported as a module
if __name__ == '__main__':

    # Printing a message before exception handling logic starts
    print("Exception Handling")

    # Example of an exception (division by zero)
    # This line is commented to prevent program crash
    # a = 10/0

    # This line will execute normally since the exception above is commented
    print("After Exception Handling ")

    # Try block contains code that may cause an exception
    try:
        # Taking user input and converting it to an integer
        a = int(input("Enter a number: "))

        # Performing division which may raise ZeroDivisionError
        dividedNumber = 10 / a

        # Printing the result if no exception occurs
        print(dividedNumber)

    # Except block handles the specific exception
    except ZeroDivisionError:
        # This message is printed if user enters 0
        print("Cannot divide by zero")

    # This statement will always execute
    # whether an exception occurs or not
    print("After Try Catch/ Except Block")
