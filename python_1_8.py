lists = ['1', 'amar', 'lent1dao']
lists2 = ['amor', 'elefante', 'python']


def remove_dups(lists):
    depara_list = []
    cleared_result = []
    depara_char = list(set(''.join(lists)))
    for i_element in lists:
        temp = []
        for i_char in i_element:
            if i_char in depara_char and i_char not in depara_list:
                depara_list.append(i_char)
                temp.append(i_char)
            else:
                pass
        temp_element = ''.join(temp)
        cleared_result.append(temp_element)
        temp = []
            
    return cleared_result

print(remove_dups(lists))
print(remove_dups(lists2))