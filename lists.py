list1 = ["apple", "banana", "cherry", "pineapple", "orange"]
tropical = ["watermelon", "coconut", "papaya"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets

# Accessing lists
l1 = list1[-1]  # cherry
l2 = list1[0:6:2]  # ['apple', 'cherry', 'orange']

# Changing elements
list1[0:6:2] = ['passion fruit', 'strawberry', 'peach']

# Add items
list1.append("avocado")
list1.insert(2, "mango")
list1.extend(tropical)

# Remove items
list1.remove("banana")
list1.pop(1)  # remove 2nd element
list1.pop()  # remove last element
del thislist[0]  # deletes 1st element
del thislist  # this variable becomes deleted from memory and undefined:
list2.clear()  # empties the list

# Loop Lists
for x in list1:
    print(x, end=" ")
for i in range(len(list1)):
    print(i, end=" ")
c = 0
while c < len(list1):
    print(c, end=" ")
    c += 1
[print(x) for x in list1]

# List Comprehension
newList = []
for x in list1:
    if "a" in x:
        newList.append(x)
print(newList)
#[expression for item in iterable if condition == True]
newList2 = [fruit for fruit in list1 if "a" in fruit]
print(newList2)  # newList1=newList2

newList3 = [x for x in range(5)]  # [0, 1, 2, 3, 4]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = [x if x != "banana" else "orange" for x in fruits]
print(newlist4)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# Sorting Lists
list1.sort()
list1.sort(reverse=True)

list1=[x.upper() if list1.index(x)< len(list1)/2 else x for x in list1 ]
list1.sort(key = str.lower)
list1.reverse()

# Copy a list
newList5=list1.copy()

#Join lists
newList6=newList5+list3