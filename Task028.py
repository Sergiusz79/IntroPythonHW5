# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def enter_num(text):
    try:
        a = int(input(f"Enter the {text} :> "))
    except:
        print("Error! This is not integer number!")
    return a

def rec(a, b):
    if b == 0:
        return a
    elif b == 1:
        return a + 1
    else:
        return rec(a, b-1) + 1


def task():
    a = enter_num('number')
    b = enter_num('degree number')

    print(rec(a, b))

task()





