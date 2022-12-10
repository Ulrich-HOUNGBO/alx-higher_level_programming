#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_dictionary = sorted(a_dictionary.keys())
        for k in sorted_dictionary:
            print("{:s}:".format(k, sorted_dictionary))
