"""
Friends Manager(manage a list of friends)
Numbers Analyzer(Find largest, smallest, and total of a list.)
Shopping List App(Manage items in a shopping list.)
Marks Calculator(Find total, average, and highest marks)
2D Matrix Printer
"""
#............1................
friends = ["Ali", "Sara", "Ahmed", "Bilal", "Zara"]
# Add a new friend
friends.append("Hassan")
# Remove one friend
friends.remove("Sara")
# Display the final list
print("My Friends:", friends)
print("Total friends:", len(friends))
#.................2.............
numbers = [23, 5, 89, 12, 56]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Sum:", sum(numbers))
#............3................
shopping_list = ["Milk", "Eggs", "Bread"]
# Add and remove items
shopping_list.append("Butter")
shopping_list.remove("Eggs")
# Print results
print("Updated Shopping List:", shopping_list)
print("Total items:", len(shopping_list))
#........4....................
marks = [78, 92, 65, 88, 75]
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest:", highest)
print("Lowest:", lowest)
#...............5................
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(row)
