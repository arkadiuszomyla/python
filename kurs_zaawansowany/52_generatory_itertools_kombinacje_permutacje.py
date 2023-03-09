import itertools as it

mylist = ['a', 'b', 'c', 'd']

# kombinacje, kolejność bez znaczenia, bez powtórzeń
for combination in it.combinations(mylist, 3):
    print(combination)

print('---------------')

# permutacje, kolejność ma znaczenie, powtórzenia
for combination in it.permutations(mylist, 3):
    print(combination)

print('---------------')

# kombinacje z powtórzeniami
for combination in it.combinations(mylist, 3):
    print(combination)

print('---------------')
#na ile sposobów jesteśmy w stanie zapłacić 100zł, zawartość potfela:
money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

result = [] #bo wyniki będą się powtarzać

for i in range(1, 101):
    for combination in it.combinations(money, i):
        if sum(combination) == 100:
            result.append(combination)

result = set(result)   #w zbiorze wyniki się nie powtarzają
for r in result:
    print(r)

print('---------------')
#na ile sposobów jesteśmy w stanie zapłacić 100zł, zawartość potfela, jednak wartości mogą się powtarzać:
money = [50, 20, 10]

for i in range(1, 101):
    for combination in it.combinations_with_replacement(money, i):
        if sum(combination) == 100:
            print(combination)