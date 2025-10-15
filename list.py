'''
What is a List?
A list is a collection of items in a single variable.
Lists can hold different data types — numbers, strings, even other lists.
'''
friends = ["Ali", "Sara", "Ahmed", "Bilal", "Zara"]
print(friends)
numbers = [10, 20, 30, 40, 50]
mixed = [10, "Umair", True, 3.14]
print(numbers)
print(mixed)
#Indexing & Slicing:
friends = ["Ali", "Sara", "Ahmed", "Bilal", "Zara"]
print(friends[0])   # Ali
print(friends[-1])  # Zara (last element)
print(friends[1:4]) # Sara, Ahmed, Bilal (slice)
#Adding Items
friends.append("Hassan")      # Adds at the end
friends.insert(2, "Usman")    # Adds at index 2
print(friends)
#Remove items:
friends.remove("Sara")  # Removes by value
friends.pop()           # Removes last element
friends.pop(1)          # Removes element at index 1
print(friends)
