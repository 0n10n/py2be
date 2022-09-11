# Python program to demonstrate
# lambda functions


def power(n):
	print('n: ', n)
	#print('a: ', a)
	return lambda a: a ** n


# base = lambda a : a**2 get
# returned to base
base = power(2)

print("Now power is set to 2")

# when calling base it gets
# executed with already set with 2
print("8 powerof 2 = ", base(3))

# base = lambda a : a**5 get
# returned to base
base = power(5)
print("Now power is set to 5")

# when calling base it gets executed
# with already set with newly 2
print("8 powerof 5 = ", base(8))
