list1 = [

{ "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },

{ "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },

{ "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }

]

  

list2 = [

{ "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },

{ "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "C#" },

{ "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }

]

  

list3 = [

{ "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },

{ "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },

{ "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure"},

{ "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "Python"}

]

def find_in_list(list):
    name = ''
    country = ''
    for i in range(0, len(list), 1):
        if list[i]['language'] == 'Python':
            name = list[i]['first_name']
            country = list[i]['country']
        else:
            pass

    if name != '':
        strings = 'Nome: ' + name + ', País: ' + country
    else:
        strings = 'Não há desenvolvedor python aqui'

    return strings

print(find_in_list(list1))
print(find_in_list(list2))
print(find_in_list(list3))