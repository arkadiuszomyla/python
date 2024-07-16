import pandas as pd
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
#print(parent_directory)

print(pd.read_csv(parent_directory + "/course-files/pokemon.csv"))
obj = pd.read_csv(parent_directory + "/course-files/pokemon.csv")
print(type(obj)) #<class 'pandas.core.frame.DataFrame'>

print(pd.read_csv(parent_directory + "/course-files/pokemon.csv", usecols=['Name']))
obj = pd.read_csv(parent_directory + "/course-files/pokemon.csv", usecols=['Name'])
print(type(obj)) #<class 'pandas.core.frame.DataFrame'>

print(pd.read_csv(parent_directory + "/course-files/pokemon.csv", usecols=['Name']).squeeze())
obj = pd.read_csv(parent_directory + "/course-files/pokemon.csv", usecols=['Name']).squeeze()
print(type(obj)) #<class 'pandas.core.series.Series'> #jeden wymiar

dataFromClickboard = pd.read_clipboard(sep=',') #import ze schowka windows, podajemy separator

obj.head() #piec gornych wierszy
obj.tail() #piec dolnych wierszy

obj.head(3) #3 gornych wierszy
obj.tail(10) #10 dolnych wierszy
