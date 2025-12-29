if __name__ == "__main__":
    print("Learning Loops ...")

    # Loops, Break and Continue Statements
    # --- 4. BREAK AND CONTINUE ---
    # 'break' stops the loop entirely
    # 'continue' skips the current step and moves to the next one

    # for i in range(10):
    #     print(i)
    #     if i == 4:
    #         break
    #     # 0 1 2 3 4 5 6 7 8 9

    # Continue
    # --- 1. FOR LOOP WITH RANGE ---
    # range(start, stop) starts at the first number and stops BEFORE the second
    for i in range(10):
        if i == 4:
            continue
        print(i)
        # 0 1 2 3 4 5 6 7 8 9

    a = 3
    # a =     3, 4, 5, 6
    # print = h, h, h, out

    # --- 3. WHILE LOOP ---
    # This runs as long as the condition remains True
    while a < 5:
        print("Hello")
        a = a + 1

