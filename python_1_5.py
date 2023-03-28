def somatorio(num):
	list = []
	for i in range(0, abs(num)+1, 1):
		list.append(str(i))
	if num > 0:
		return '+'.join(list)
	else:
		return '-'.join(list)

print(somatorio(10))
print(somatorio(-10))
