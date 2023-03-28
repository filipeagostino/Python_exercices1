from string import ascii_lowercase

def alfa(num):
    total = len(ascii_lowercase)
    resto = num % 26
    char = ''
    if num < 0:
        return 'Numero invalido'
    num -= 1
    if num <= 25:
        return ascii_lowercase[num]
    else:             
        return alfa(num // total) + ascii_lowercase[num % total]

    for i in range(1, num):
        char = alfa(i)
    return char

print(alfa(703))