string = 'frog'
print(string[3]) # wyświetla 3'cią literę z 'frog' czyli 'g'

list_of_strings = ['pig', 'cow', 'horse']
print(list_of_strings[1]) # wyświetla 1'wszą pozycję listy czyli 'cow'

string = 'computer'
# w slicingu mamy takie argumenty: [start:end+1:step]
print(string[1:4]) # wyświetla litery od 1 do 3 czyli 'omp'
print(string[1:6:2]) # wyświetla litery od 1 do 5 co 2 czyli 'opt'
print(string[3:]) # wyświetla litery od 3 do końca czyli 'puter'
print(string[:5]) # wyświetla litery od początku do 4 czyli 'compu'
print(string[-1]) # wyświetla ostatnią literę czyli 'r'
print(string[-3:]) # wyświetla 3 ostatnie litery czyli 'ter'
print(string[:-2]) # wyświetla litery od początku do przed ostatniej czyli 'comput'

string = 'horse' + 'shoe'
print(string) # wyświetli 'horsechoe'

list_of_strings = ['pig', 'cow'] + ['horse']
print(list_of_strings) # wyświetli ['pig', 'cow', 'horse']

string = 'bug'
print(string * 3) # wyświetli 'bugbugbug'

list = [8, 5]
print(list * 3) # wyświerli [8, 5, 8, 5, 8, 5]

string = 'bug'
print('u' in string) # wyświetli True

list_of_strings = ['pig', 'cow', 'horse']
print('cow' not in list_of_strings) # wyświetli False

list = [7, 8, 3]
for item in list:
    print(item * 2) # wyświetli 14, 16, 6

list = [7, 8, 3]
for index, item in enumerate(list):
    print(index, item) # wyświetli 0 7, 1 8, 2 3

string = 'bug'
print(len(string)) # wyświetla 3

string = 'bug'
print(min(string)) # wyświetla 'b'

list_of_strings = ['pig', 'cow', 'horse']
print(min(list_of_strings)) # wyświetla 'cow'

list = [2, 5, 8, 12]
print(sum(list)) # wyświetla 27
print(sum(list[-2:])) # wyświetla 20

string = 'bug'
print(sorted(string)) # wyświetla ['b', 'g', 'u']

string = 'hippo'
print(string.count('p')) # wyświetla 2

list_of_strings = ['pig', 'cow', 'horse', 'cow']
print(list_of_strings.count('cow')) # wyświetla 2

list_of_strings = ['pig', 'cow', 'horse']
a, b, c = list_of_strings # a to 'pig' b to 'cow' c to 'horse'
print(a, b, c)

list = [m for m in range(8)]
print(list) # wyświetla [0, 1, 2, 3, 4, 5, 6, 7]

list = [z ** 2 for z in range(10) if z > 4]
print(list) # wyświetla [25, 36, 49, 64, 81]

list = [5, 3, 8, 6]
del(list[1])
print(list) # wyświetla [5, 8, 6]

list = [5, 3, 8, 6]
print(list.append(7)) # wyświetla [5, 3, 8, 6, 7]

list2 = [12, 13]
print(list.append(list2)) # wyświetla [5, 3, 8, 6, 7, [12, 13]]
print(list.extend(list2)) # wyświetla [5, 3, 8, 6, 7, 12, 13]

list = [5, 3, 8, 6]
list.insert(1, 7) 
print(list) # wyświetla [5, 7, 3, 8, 6]
list.insert(1, ['a', 'm'])
print(list) # wyświetla [5, ['a', 'm'], 7, 3, 8, 6]

list = [5, 3, 8, 6]
list.pop()
print(list.pop()) # wyświetla 6 list to teraz [5, 3, 8]

list = [5, 3, 8, 6]
list.remove(3)
print(list) # wyświetla [5, 3, 6]

list = [5, 3, 8, 6]
list.reverse()
print(list) # wyświetla [6, 8, 3, 5]

list = [5, 3, 8, 6]
print(list.sort()) # wyświetla [3, 5, 6, 8]

set = {3, 5, 3, 5}
print(set) # wyświetla {3, 5} w losowej kolejności

set = {3 * x for x in range(10) if x > 5}
print(set) # wyświetla {18, 21, 24, 27} ale w losowej kolejności

set1 = {1, 2}
set2 = {2, 3}
print(set1 & set2) # wyświetla iloczyn zbiorów czyli {1, 2, 3}
print(set1 | set2) # wyświetla iloraz zbiorów czyli {2}
print(set1 ^ set2) # wyświetla XOR czyli {1, 3}
print(set1 - set2) # wyświetla różnicę zbiorów czyli {1}
print(set1 <= set2) # wyświetla False bo set1 nie jest podzbiorem set2

#sposoby tworzenia słownika
dictionary = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
dictionary = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])
dictionary = dict(pork=25.3, beef=33.8, chicken=22.7)
print(dictionary)

print(dictionary.keys()) # wyświetla listę kluczy czyli ['pork', 'beef', 'chicken']
print(dictionary.values()) # wyświetla listę wartości czyli [25.3, 33.8, 22.7]
print(dictionary.items()) # wyświetla listę par klucz-wartość czyli [('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)]