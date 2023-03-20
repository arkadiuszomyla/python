var_x = 10

source = 'var_x + 4'

result = eval(source)    #pozwala budować tylko wyrażenia
print(result)

source = 'var_x = 4'

result = exec(source)    #pozwala budować tylko wyrażenia
print(result)
print(var_x)

var_x = 10
source = '''
new_var = 1
for i in range(var_x):
    print('-'*i)
    new_var +=i
'''
result = exec(source)    #pozwala budować tylko wyrażenia
print(result)
print(new_var)