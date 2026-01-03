# 1. Add a list of element to a set
''''
Given - sample_set = {"Yellow", "Orange", "Black"} Sample_list = ["Blue", "Green", "Red"]
Expected output: {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
'''
from Python_DataStructure_Assignment import sample_list

# Solution
sample_set = {"Yellow", "Orange", "Black"}
Sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

# 2. Return a new set of identical items from two sets
''''
Given - set1 = {10, 20, 30, 40, 50}  set2 = {30, 40, 50, 60, 70}
Expected output: {40, 50, 30}
'''

# Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

# 3. Get Only unique items from two sets
''''
Given - set1 = {10, 20, 30, 40, 50}  set2 = {30, 40, 50, 60, 70}
Expected output: {70, 40, 10, 50, 20, 60, 30}
'''

# Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))

# 4. Update the first set with items that don't exist in the second set
''''
Given - set1 = {10, 20, 30}  set2 = {20, 40, 50}
Expected output: set1 {10, 30}
'''

# Solution
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

# 5. Remove items from the set at once
''''
WAP to remove items 10, 20, 30 from the following set at once
Given - set1 = {10, 20, 30, 40, 50}
Expected output: {40, 50}
'''

# Solution
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

# 6. Return a set of elements present in Set A or B, but not both
''''
Given - set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}
Expected output: {20, 70, 10, 60}
'''

# Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

# 7. Check if two sets have any elements in common. If yes, display the common elements
''''
Given - set1 = {10, 20, 30, 40, 50}  set2 = {60, 70, 80, 90, 10}
Expected output: Two sets have items in common {10}
'''

# Solution
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("Two sets have no item in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))

# 8. Update set1 by adding items from set2, except common items
''''
Given - set1 = {10, 20, 30, 40, 50}  set2 = {30, 40, 50, 60, 70}
Expected output: {70, 10, 20, 60}
'''

# Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

# 9. Remove items from set1 that are not common to both set1 and set2
''''
Given - set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}
Expected output: {40, 50, 30}
'''

# Solution

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)

# 10. Find elements unique to each set (The "Only-In-One" Challenge)
''''
Given three sets, find a new set containing elements that are unique to their respective sets.
In other words, find elements that appear in only one of the three sets and not in any others.

Given: set1 = {10, 20, 30, 40} set2 = {30, 40, 50, 60} set3 = {10, 40, 70, 80}
Expected output: {20, 50, 60, 70, 80}
'''

# Solution

# Given sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
set3 = {10, 40, 70, 80}

# Method: Combine all symmetric differences
# Or find the union and subtract all possible intersections
all_elements = set1.union(set2, set3)

# Find elements that appear in more than one set
common_1_2 = set1.intersection(set2)
common_2_3 = set2.intersection(set3)
common_3_1 = set3.intersection(set1)

# Combine all common elements
all_common = common_1_2.union(common_2_3, common_3_1)

# Unique elements = All elements - Common elements
unique_elements = all_elements.difference(all_common)

print(unique_elements)

# ========================== COMPLETED ==================== #