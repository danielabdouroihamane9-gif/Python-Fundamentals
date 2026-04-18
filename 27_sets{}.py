#27 SETS = They are built-in data structures in Python that store unordered, unique, and mutable collections of items.
#            They are defined using curly braces {} or the set() constructor.
# GENERAL SYNTAX:   my_set = {item1, item2, item3, ...} or my_set = set([item1, item2, item3, ...])

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5} (since sets are unordered, the output may not be in the same order as the input)
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5} (since sets are unordered, the output may not be in the same order as the input)

#* define empty set using set() constructor (since using {} would create an empty dictionary instead of a set):
empty_set = set()

#* The .add() method is used to add an item to a set:
my_set.add(6)   # Output: {1, 2, 3, 4, 5, 6} (since the item 6 has been added to the set)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6} (since the item 6 has been added to the set)

#* The .remove() and .discard() methods are used to remove an item from a set. If the item does not exist, .remove() raises a KeyError while .discard() does nothing:
my_set.remove(6)   # Output: {1, 2, 3, 4, 5} (since the item 6 has been removed from the set)
my_set.discard(7)  # Output: {1, 2, 3, 4, 5} (since the item 7 does not exist in the set, the discard() method does nothing and the set remains unchanged)
print(my_set)  # Output: {1, 2, 3, 4, 5} (since the item 6 has been removed from the set and the item 7 was not in the set)

#* The .clear() method is used to remove all items from a set, leaving it empty:
my_set.clear()  # Output: set() (since all items have been removed from the set and it is now empty)

#* The .issubset() and .issuperset() methods are used to check if a set is a subset or superset of another set:
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))  # Output: True (since set_a is a subset of set_b)
print(set_b.issuperset(set_a))  # Output: True (since set_b is a superset of set_a)

#* The .isdisjoint() method is used to check if two sets have no items in common:
set_c = {6, 7, 8}   
print(set_a.isdisjoint(set_c))  # Output: True (since set_a and set_c have no items in common)

#* The union (|), intersection (&), difference (-), and symmetric difference (^) operators can be used to perform set operations:
set_d = {1, 2, 3, 4}    
set_e = {3, 4, 5, 6}
print(set_d | set_e)  # Output: {1, 2, 3, 4, 5, 6} (since the union of set_d and set_e includes all unique items from both sets)

print(set_d & set_e)  # Output: {3, 4} (since the intersection of set_d and set_e includes only the items that are present in both sets)

print(set_d - set_e)  # Output: {1, 2} (since the difference of set_d and set_e includes only the items that are in set_d but not in set_e)

print(set_d ^ set_e)  # Output: {1, 2, 5, 6} (since the symmetric difference of set_d and set_e includes only the items that are in either set but not in both)

#* corresponding compound assignment operators for set operations:
set_d |= set_e  # Output: {1, 2, 3, 4, 5, 6} (since the union of set_d and set_e has been assigned back to set_d)
set_d &= set_e  # Output: {3, 4} (since the intersection of set_d and set_e has been assigned back to set_d)
set_d -= set_e  # Output: set() (since the difference of set_d and set_e has been assigned back to set_d, leaving it empty)
set_d ^= set_e  # Output: {3, 4} (since the symmetric difference of set_d and set_e has been assigned back to set_d)

#* The in operator can be used to check if an item is in a set:
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True (since the item 3 is in the set)
print(6 in my_set)  # Output: False (since the item 6 is not in the set)
