# Variables
a = 15
b = 12
print(type(a))
print(type(b))

# Arithmetic
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Type casting
c = int(a / b)
print(c, type(c))
c = float(c)
print(c, type(c))

# Strings
message = "The result of a divided by b is?"
print(message + " " + str(c))

# Comparison
print(a > b)
print(a == b)