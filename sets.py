thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  # 1 is considered a duplicate and won't be processed
# {'apple', True, 2, 'cherry', 'banana'}

# Accessing (sets are not indexed)
for x in thisset:
    if "banana" == x:
        print(x)
    else:
        print("not banana")

# Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]
thisset.update(tropical)
thisset.update(mylist)

# To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
# Remove a random item by using the pop() method:
thisset.pop()

# Operations
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set4 | set3  # = Union
set6 = set5 & set1  # = Intersect
set1.update(set2)
set1.intersection_update(set2)  # Keep the items that exist in both set1, and set2:
set3 = set1.difference(set2)  # Keep all items from set1 that are not in set2:
