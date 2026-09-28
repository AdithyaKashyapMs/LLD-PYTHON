import copy

list1 = [1, 4, [65, 88, 44], 5, 6, 7]

# list2 = copy.copy(list1)  # Create a shallow copy of list1
list2 = copy.deepcopy(list1)  # Create a deep copy of list1
list2[2][1] = 100  # Modify the first element of list2

print("list1:", list1)  # Output: list1: [1, 4, [65, 88, 44], 5, 6, 7]
print("list2:", list2)  # Output: list2: [100, 4, [65, 88, 44], 5, 6, 7

print(id(list1[2]))
print(id(list2[2]))  # Output: True, because both list1 and list2 share the same reference to the nested list