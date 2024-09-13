def safe_print_list_integers(my_list=[], x=0):
    count = 0  # To keep track of the number of integers printed
    for i in range(x):  # Access x elements of the list
        try:
            print("{:d}".format(my_list[i]), end="")  # Try to print the integer
            count += 1  # Increment the count if successful
        except (ValueError, TypeError, IndexError):
            # Skip if it's not an integer or if we go out of bounds
            pass
    print()  # Move to the next line after printing the integers
    return count  # Return the number of integers printed
