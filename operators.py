if __name__ == "__main__":
    # --- ARITHMETIC OPERATORS ---
    # These are used to perform mathematical calculations
    x = 10
    y = 3
    z = 3

    print(x + z)  # Addition: Adds two values (10 + 3 = 13)
    print(x - z)  # Subtraction: Subtracts right from left (10 - 3 = 7)
    print(x * z)  # Multiplication: (10 * 3 = 30)
    print(x / z)  # Division: Always returns a float/decimal (3.333...)
    print(x % z)  # Modulo: Returns the REMAINDER of the division (10 ÷ 3 = 3 remainder 1)

    # --- COMPARISON OPERATORS ---
    # These return a Boolean value: True or False
    print(x > z)   # Greater than: Is 10 > 3? (True)
    print(x < z)   # Less than: Is 10 < 3? (False)
    print(x != z)  # Not Equal to: Are they different? (True)
    print(y == z)  # Equal to: Are they exactly the same? (True)

    # --- CONDITIONAL STATEMENTS (IF-ELIF-ELSE) ---
    # This controls the "flow" of the program based on logic
    if x > 10:
        print("x is greater than 10")
    elif x == 10:
        # 'elif' runs only if the first 'if' was False
        print("x is equal to 10")
    else:
        # 'else' runs if none of the above conditions were met
        print("x is less than 10")
