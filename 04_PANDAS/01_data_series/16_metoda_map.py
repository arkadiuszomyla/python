import pandas as pd

team = pd.Series(data=[5, 3, 2, 4, 4, 4, 5],
                 index=['Andy', 'Bob', 'Chris', 'Dirk', 'Francis', 'George', 'Henry', 'Ivan'])
print(team)

notes = pd.Series(data=['C', 'B', 'A', 'A+', 'A++'], index=[1, 2, 3, 4, 5])
print(notes)

print(team.map(notes))  #wartościami będą oceny amerykańskie, notes mogłoby tu być też słownikiem