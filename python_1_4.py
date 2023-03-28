list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def raiz_perfeita(list):
	for i in list:
		result = i ** (1/2)
		if result.is_integer():
			print(f'A raiz quadrada de {i} é Perfeita!')
		else:
				print(f'A raiz quadrada de {i} não é perfeita!')

raiz_perfeita(list)