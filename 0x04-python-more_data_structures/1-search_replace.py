#!/usr/bin/python
def search_replace(my_list, search, replace):
    return (list(map(lambda x: x.replace if x is search else x, my_list)))
