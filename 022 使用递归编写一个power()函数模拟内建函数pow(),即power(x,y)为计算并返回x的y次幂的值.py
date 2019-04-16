def powerq(x,y):
	if y == 1:
		return x
	else:
		return x * powerq(x,y-1)

