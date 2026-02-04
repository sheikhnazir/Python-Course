# This block ensures the code runs only when the file
# is executed directly (not when imported)
if __name__ == "__main__":

    # Creating a string variable
    string1 = "hello python"

    # Converts all characters of the string to UPPERCASE
    print(string1.upper())

    # Converts all characters of the string to lowercase
    print(string1.lower())

    # Replaces a part of the string with another string
    # NOTE: "Hello" will NOT match "hello" because Python is case-sensitive
    print(string1.replace("Hello", "Hi"))

    # Capitalizes only the first character of the string
    print(string1.capitalize())

    # Checks whether the string contains only numbers
    # Returns False because the string has alphabets and space
    print(string1.isnumeric())

    # Splits the string into a list of words using space as default separator
    print(string1.split())