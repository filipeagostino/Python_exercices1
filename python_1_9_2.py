lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def invert_lists(lists):
    if len(lists) % 2 == 0:
        head = lists[0:int((len(lists) / 2)):1]
        tail = lists[int((len(lists) / 2)):len(lists):1]		  
        result = tail + head	
    else:
        middle = []
        head = lists[0:int((len(lists) // 2)):1]
        tail = lists[int((len(lists) // 2) + 1):len(lists):1]		          
        middle.append(lists[len(lists) // 2])
        result = tail + middle + head

    return result
    
print(invert_lists(lists))