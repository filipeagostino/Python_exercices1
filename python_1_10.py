list1 = ['1234', '12345678', '12', '12345', '123','1']
list2 = ['12345678', '123', '12345', '123','12']

def sort_list(lists):
	return sorted(lists, key=len)

print(sort_list(list1))
print(sort_list(list2))