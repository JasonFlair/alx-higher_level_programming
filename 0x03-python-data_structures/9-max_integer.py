#!/usr/bin/python3

def max_integer(my_list=[]):
    for i in my_list:
        max_value = my_list[0]
        if i < 0:
            new_list = sorted(my_list)
            return new_list[-1]
        else:
            if i >= 0:
                if i > max_value:
                    max_value = i
                    return max_value

        
