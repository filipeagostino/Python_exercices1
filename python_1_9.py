list = [1, 2, 3, 4, 5, 6, 7]

def invert_list(list):
	print(list[len(list) // 2])
	if len(list) % 2 == 0:
		head = list[0:int((len(list) / 2)):1]
		tail = list[int((len(list) / 2)):len(list):1]		  
		result = tail + head	
		return result
	else:
		head = list[0:int((len(list) / 2)):1]
		middle = int(list[len(list) // 2])
		tail = list[int((len(list) / 2)):len(list):1]		  
		result = tail + middle + head	
		return result
print(invert_list(list))