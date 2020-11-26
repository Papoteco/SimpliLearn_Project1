def greet(name, msg="Good Morning!"):
	"""this function greets to 
	the person with the provided message

	If the message is bot provided,
	it defaults to 'Good Morning!'"""

	print("Hello", name + ', ' + msg)

print("Enter your name:")
n = input()
print("Message:")
m = input()

if m == '':
	greet(n)
else:
	greet(n, m)

