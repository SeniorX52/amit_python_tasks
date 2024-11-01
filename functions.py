def my_function(x):
    return 5 * x


def pos_function(x, y, /):
    return y * x


def keyword_function(*, x, y):
    return y * x


def combine_function(a, b, /, *, c, d):
    return a * b * c * d


print(my_function(5))
print(pos_function(5, 3))  # ordered parameters
print(keyword_function(y=2, x=3))  # specify parameters with no order
print(combine_function(3, 4, d=3, c=3))

# Lambda functions
x = lambda a : a + 10
print(x(5)) #15
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
print(myfunc(2)(11)) # same as mydoubler = myfunc(2)
