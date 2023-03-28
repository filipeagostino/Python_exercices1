from string import ascii_lowercase

def alfa(num):
    letters = []
    char = ''
    vezes = num // 26
    resto = num - 26
    cont = 0
    if num <= 26:
        return ascii_lowercase[num - 1]
    else:
        cont = 0
        for i in range(vezes):
            num -= 26
            resto = num - 26
            cont += 1
            char = ascii_lowercase[cont - 1]
            print(f'num: {num} resto: {resto}, cont: {cont}, char: {char}')

            

print(alfa(52))




