list1 = [1, 2, 3]
list2 = [4, 5]
# Concatenation
combined = list1 + list2       # [1, 2, 3, 4, 5]
# Repetition
repeat = list1 * 2             # [1, 2, 3, 1, 2, 3]
# Membership
print(3 in list1)              # True
print(10 not in list1)         # True
#Useful Functions
nums = [10, 20, 5, 8, 30]
print(len(nums))   # 5
print(min(nums))   # 5
print(max(nums))   # 30
print(sum(nums))   # 73
#Nested Lists (List inside a List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # Access 6 (row 2, column 3)
