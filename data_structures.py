# Entry point of the program
# This ensures the code runs only when this file is executed directly
if __name__ == "__main__":

    a = 9  # Simple variable (not related to list, just an example)

    print("Data Structures Learning ... ")

    # ----------------------------
    # 1. LIST (Ordered, Mutable)
    # ----------------------------

    # Creating a list of numbers
    list_numbers = [19, 25, 89, 10, 15]

    # Index positions of list elements
    # Index:   0   1   2   3   4
    # Values: 19  25  89  10  15

    # Access element using index
    print(list_numbers[2])   # Prints element at index 2 → 89
    print(list_numbers[0])   # Prints first element → 19

    # Length of the list (number of elements)
    print(len(list_numbers)) # Output → 5

    # Print the entire list
    print(list_numbers)

    # ----------------------------
    # List Operations
    # ----------------------------

    # Add an element at the end of the list
    list_numbers.append(50)
    print(list_numbers)

    # Remove a specific element (by value)
    list_numbers.remove(89)
    print(list_numbers)

    # Remove the last element and return it
    list_numbers.pop()
    print(list_numbers)

    # Insert an element at a specific index
    # Syntax: insert(index, value)
    list_numbers.insert(1, 99)
    print(list_numbers)

    # Sort the list in ascending order
    list_numbers.sort()
    print(list_numbers)

    # Reverse the list
    list_numbers.reverse()
    print(list_numbers)

    # ----------------------------
    # Iterating through a list
    # ----------------------------

    # Loop through each element in the list
    for n in list_numbers:
        print(n)
