import numpy as np

# Random Array 0 to 0.99
x = np.random.random((3, 3))
x = np.random.randint(0, 11, (3, 3))

# Random Choice
a = np.array(["Mostafa", "Ali", "Marwan", "Hazem", "Goldy"])
x = np.random.choice(a, (5, 2))

# Saving arrays as NPZ files
np.savez("file.npz", Choice=x, Names=a)

# Load files
with np.load('file.npz') as file:
    Mat1 = file['Choice']
    Mat2 = file['Names']

# Comparison
v1 = np.array([1, 2, 3, 4])
v2 = np.array([1, 2, 3, 4])
equals1 = v1 == v2  # [ True  True  True  True]
greater_than_one = v1 > 1  # [False  True  True  True]
greater_than_v2 = v1 > v2
equals2 = np.all(v1 >= 1)  # True

# Is close with tolerance
close = np.isclose(v1, v2, atol=1)

# Conditional access
condition = v1 >= 3
conditional_access = v1[condition]  # [3 4]

# Conditional modifying
v1[condition] = -1  # Will change all elements in the conditional access to -1

# Conditional Modifying using 'where'
new_arr = np.where(condition, -1, v1) # [ 1  2 -1 -1]

# Arithmatic operations
new_arr2=v1 * np.where(condition,6,v2) # [1  4 -6 -6]

