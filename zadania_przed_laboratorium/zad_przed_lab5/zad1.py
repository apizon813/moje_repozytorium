# Napisać funkcję, która dla podanego ciągu liczb całkowitych znajdzie
# dowolny spójn
# podciąg o podanej długości i największej sumie elementów. Napisać testy dla
# podanej funkcji.
# Proszę zastanowić się, co funkcja ma zwrócić w przypadku gdy długość
# szukanego podciągu jest większa
# niż wielkość kolekcji podanej na wejściu.


def substring(string, n):
    if n > len(string):
        raise ValueError('Substring longer than string')
    string = list(string)
    maxsub = []
    for i in range(len(string)-n + 1):
        if sum(maxsub) < sum(string[i:i + n]):
            maxsub = string[i:i + n]
    return maxsub
