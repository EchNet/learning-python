# Variable scoping by assignment in Python is weird.

a, b = (1, 2)

print(a, b)   # prints 1 2

def fun():
	# print(a, b)   # can't do this here because the assignment below implies a is local and not yet assigned
	a = 3
	# b -= 2        # can't do this here because it implies b is local would read it before assigning it
	print(a, b)     # prints 3 2

fun()
print(a, b)   # prints 1 2   local a was assigned to 
