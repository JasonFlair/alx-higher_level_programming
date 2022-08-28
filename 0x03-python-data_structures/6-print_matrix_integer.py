#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        output = ' '.join(map(str, line))
        print("{}".format(output))
        
