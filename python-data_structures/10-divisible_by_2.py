#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
for i, res in enumerate(divisible_by_2(my_list)):
    print(f"{my_list[i]} is {'is' if res else 'is not'} divisible by 2")
