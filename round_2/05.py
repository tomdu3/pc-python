# Custom Sorter: Write a function that sorts a list of tuples based
# on the second value in each tuple.

def custom_sort(tuples):   
    '''Sort the list of tuples based on the second value'''
    tuples.sort(key=lambda x: x[1])
    return tuples


tuples = [('c', 3), ('a', 1), ('b', 2), ]
print(custom_sort(tuples))
