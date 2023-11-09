#SyntaxError
x = 10
if x == 10
print("x is 10")
#error
#SyntaxError: expected ':'

#solution
x = 10
if x == 10:
print("x is 10")

#Namederror
def calculate_sum(a, b):
    total = a + b
    return total

x = 5
y = 10
z = calculate_sum(x, w)
print(z)
#error
NameError: name 'w' is not defined
#solution
def calculate_sum(a, b):
    total = a + b
    return total

x = 5
y = 10
z = calculate_sum(x, y)
print(z)

#typeerror
x = "10"
y = 5
Z = x + y
print(z)
#error
# TypeError: can only concatenate str (not "int") to str
#solution 
x = "10"
y = 5
Z = x + str(y)
print(z)

#indexerror
my_list = [100, 200, 300, 400, 500]
print(my_list[5])
#error
IndexError: list index out of range
#solution
my_list = [100, 200, 300, 400, 500]
print(my_list[4])
