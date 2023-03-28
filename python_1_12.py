def string_transform(text):
	lists = []
	result = []
	text = text.strip().lower()
	for i in text:
		lists.append(i)
	for i in lists:
		char = f'{i}:' + f'*' * lists.count(i)
		if char not in result:
			result.append(f'{i}:' + f'*' * lists.count(i))
			out = text + ' --> ' + ','.join(result)
				
	return out

print(string_transform('chicago'))
print(string_transform('Teste '))