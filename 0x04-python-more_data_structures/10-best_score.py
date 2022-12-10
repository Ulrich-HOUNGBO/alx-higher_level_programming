#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        best = None
        person = None
        for i in a_dictionary:
            if a_dictionary[i] > best:
                best = a_dictionary[i]
                person = i
        return person
