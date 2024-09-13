def safe_print_integer(value):
        try:
                    # Try to format and print the value as an integer using "{:d}".format()
                            print("{:d}".format(value))
                                    return True
                                    except (ValueError, TypeError):
                                                # If value is not an integer, return False
                                                        return False
                                                
