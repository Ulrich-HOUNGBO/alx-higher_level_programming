#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = []
        for i in my_list:
            if my_list[i] == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
        return new_list 


search_replace([1,2,2,2,4,4,1,3,2,2], 2, 8)