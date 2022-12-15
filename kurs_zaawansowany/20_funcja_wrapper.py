import datetime
import functools


def CreateFunctionWitchWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" started at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result

    return func_with_wrapper


@CreateFunctionWitchWrapper  # dekorowanie funkcji, będzie uruchamiana z wrapperem powyżej
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('Changing salary for {} to {} as bonus = {}'.format(emp_name, new_salary, is_bonus))
    return new_salary


print(ChangeSalary('Johnson', 20000, True))

# ChangeSalaryWithLog = CreateFunctionWitchWrapper(ChangeSalary)
# print(ChangeSalaryWithLog('Johnson', 2000, True))
# print(ChangeSalaryWithLog('Johnson', 2000, is_bonus=True))
