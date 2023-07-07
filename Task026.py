# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def enter_num(text):
    try:
        a = int(input(f"Enter the {text} :> "))
    except:
        print("Error! This is not integer number!")
    return a

def rec(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return rec(a, b-1) * a


def task():
    a = enter_num('number')
    b = enter_num('degree number')

    print(rec(a, b))

task()
