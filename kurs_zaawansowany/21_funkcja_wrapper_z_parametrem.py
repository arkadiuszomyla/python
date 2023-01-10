import datetime
import functools


# logFilePath = r'c:\temp\function_log.txt'

def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWitchWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a")
            file.write('-' + '\n')
            file.write('Function "{}" started at {}\n'.format(func.__name__.datetime.datetime.now().isoformat()))
            file.write(" ".join("{}".format(x) for x in args))  # x jest kolejnymi wartościami tablicy args
            file.write("\n")
            file.write(" ".join(
                "{}={}".format(k, v) for (k, v) in kwargs.items()))  # kwarg to klucz i wartosc, dlatego dwie zmienne
            file.write("\n")
            result = func(*args, **kwargs)
            print('Function returned {}'.format(result))
            file.write('Function returned {}\n'.format(result))
            file.close()
            return result

        return func_with_wrapper

    return CreateFunctionWitchWrapper


@CreateFunctionWithWrapper_LogToFile(
    r'c:\temp\change_salary_log.txt')  # dekorowanie funkcji, będzie uruchamiana z wrapperem powyżej
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('Changing salary for {} to {} as bonus = {}'.format(emp_name, new_salary, is_bonus))
    return new_salary


@CreateFunctionWithWrapper_LogToFile(
    r'c:\temp\change_position_log.txt')  # dekorowanie funkcji, będzie uruchamiana z wrapperem powyżej
def ChangeSalary(emp_name, new_position):
    print('Changing position for {} to {}'.format(emp_name, new_position))
    return new_position


print(ChangeSalary('Johnson', 20000, True))

# ChangeSalaryWithLog = CreateFunctionWitchWrapper(ChangeSalary)
# print(ChangeSalaryWithLog('Johnson', 2000, True))
# print(ChangeSalaryWithLog('Johnson', 2000, is_bonus=True))
