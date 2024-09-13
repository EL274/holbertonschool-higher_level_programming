#!/usr/bin/python3
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    printed = 0

    while printed < x:
        try:
            print(my_list[count], end=' ')
            count += 1
            printed += 1
        except IndexError:
            break

    print()
    return printed
