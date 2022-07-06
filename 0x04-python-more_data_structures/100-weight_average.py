#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    else:
        top = 0
        bottom = 0
        for x in my_list:
            top += x[0] * x[1]
            bottom += x[1]
        return top / bottom
