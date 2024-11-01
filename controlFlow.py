a = 23
b = 432
c = 12
if not (a > b and (a < c or b > c)):
    print(a)
else:
    print(b)

# Ternary Operator
print(a) if a > b else print(b)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    elif i == 5:
        break
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

for x in range(7):
    print(x)

for x in range(6, 18, 2):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break  # This wont print "Finally finished!"
    print(x)
else:
    print("Finally finished!")
