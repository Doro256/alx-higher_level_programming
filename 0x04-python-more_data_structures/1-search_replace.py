#!/usr/bin/python
def search_replace(my_list, search, replace):
    return list(map(lambda x: x.replace(search, replace), my_list))
