def add(a, b):
	return a + b

print(id(add))
print("0x%X" % id(add))

fn = add
print("0x%X" % id(fn))
print(id(fn))
a = fn(3, 4)
print(a)



def calc(a,b,fn):
	c = fn(a,b)
	return c


x = calc (5, 7, lambda x, y: x + y)
print(x)
