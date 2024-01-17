# Max Heap Checker: Write a function that checks if a given list of numbers represents a valid max heap.

def heap_checker(list):
    n = len(list)
    for i in range(n):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < n and list[i] < list[left_child_index]:
            return False

        if right_child_index < n and list[i] < list[right_child_index]:
            return False

    return True

list1 = [10, 8, 7, 6, 5, 4, 3]
list2 = [10, 8, 7, 6, 9, 4, 3]

print(heap_checker(list1))
print(heap_checker(list2))

