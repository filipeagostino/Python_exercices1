def create_array(n):
	res=[]
	i = 1
	while i <= n:
		res += [i]
		n -= 1
	return res

print(create_array(20))
print(create_array(-10))