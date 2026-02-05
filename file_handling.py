# Entry point of the program
# Code inside this block runs only when the file is executed directly
if __name__ == '__main__':

    # Try block is used to handle file-related runtime errors
    try:
        # Opening a file in default read mode ('r')
        f = open("file.txt")

        # Printing the file object reference
        print(f)

        # -------- File Properties --------

        # Displays the name of the file
        print("FileName : ", f.name)

        # Displays the mode in which file is opened
        print("Mode: ", f.mode)

        # Checks whether the file is closed (False means file is open)
        print("Is Closed  : ", f.closed)

        print("_______________")

        # Reads and prints entire content of the file
        print(f.read())

        print("_______________")

        # Closing the file manually
        f.close()

        # Checking file status after closing
        print("Is Closed  : ", f.closed)

    # Handles the case when the file does not exist
    except FileNotFoundError:
        print("File Not Found")

    # Using 'with' statement to open a file in write mode
    # 'with' automatically closes the file after block execution
    with open("file.txt", "w") as f:

        # Writing data into the file
        f.write("Hello Python File Handling\n")
        f.write("File Handling Operations in Python")

    # This line executes regardless of exception
    print("After file not found try except block")