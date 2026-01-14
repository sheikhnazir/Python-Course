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

    # ----------------------------
    # SET → Unique elements & Fast lookup
    # ----------------------------

    # Creating a set (duplicates are NOT allowed)
    roll_numbers = {1, 2, 3}
    print(roll_numbers)

    # Add a new element to the set
    # Sets automatically avoid duplicates
    roll_numbers.add(4)
    print(roll_numbers)

    # Sets can contain mixed data types
    roll_numbers.add("a")
    print(roll_numbers)

    # Remove a specific element from the set
    # If the element does not exist → KeyError
    roll_numbers.remove(2)
    print(roll_numbers)

    # Remove and return a random element from the set
    # (Sets are unordered, so we don’t know which element will be removed)
    roll_numbers.pop()
    print(roll_numbers)

    # ----------------------------
    # Set Operations
    # ----------------------------

    set1 = {1, 2, 3}
    set2 = {4, 5, 6, 3}

    # Union → All unique elements from both sets
    print(set1 | set2)

    # Intersection → Common elements in both sets
    print(set1 & set2)

    # Difference → Elements present in set1 but not in set2
    print(set1 - set2)

    # Difference → Elements present in set2 but not in set1
    print(set2 - set1)

    # ----------------------------
    # --- Dictionary ---
    # Dictionaries store data in key:value pairs.
    # Characteristics: Ordered (since Python 3.7), Changeable, and No Duplicate Keys.

    # Initializing a dictionary
    my_car = {
        "brand": "Suzuki",
        "Model": 2024,
        "Model": 2025,  # Duplicate keys are not allowed; "2025" will override "2024"
        "Variant": "K10",
        "Colour": "White"
    }

    # Printing the entire dictionary
    print(my_car)

    # Accessing specific values using their keys
    print(my_car["brand"], " : ", my_car["Model"])

    # --- Modifying Data ---
    # Dictionaries are 'Changeable', meaning we can update values of existing keys
    my_car["Colour"] = "Black"
    my_car["Variant"] = "K20"
    print(my_car)

    # --- Removing Data ---
    # Using 'del' to remove a specific key-value pair
    del my_car["Colour"]
    print(my_car)

    # Adding a new key-value pair back into the dictionary
    my_car["Colour"] = "White"
    print(my_car)

    # --- Iteration Methods ---

    # 1. Iterating through keys (default behavior)
    print("\nKeys:")
    for key in my_car:
        print(key)

    # 2. Iterating through values only using .values()
    print("\nValues:")
    for value in my_car.values():
        print(value)

    # 3. Iterating through both keys and values using .items()
    print("\nKey-Value Pairs:")
    for key, value in my_car.items():
        print(key, value)

    # Checking the number of items (key-value pairs) in the dictionary
    print("\nDictionary Length:", len(my_car))











