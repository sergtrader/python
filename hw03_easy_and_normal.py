#easy

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits): 
    number1 = int(number * (10**ndigits))
    c = number1 % 10
    if c < 5:
        k = (number1 - (10 - c)) / (10**ndigits)
        return k
    elif c > 5:
        k = (number1 + (10 - c)) / (10**ndigits)
        return k
    elif c == 5:
        k = number1 / (10**ndigits)
        return k

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    strnum1 = 0
    strnum2 = 0
    lucky = "Неудача"
    if (len(str(ticket_number))) == 6:
        for num in str(ticket_number)[:3]:
            strnum1 += int(num)
        for num in str(ticket_number)[3:]:
            strnum2 += int(num)
            if strnum1 == strnum2:
                lucky = "Счастливый билет"
    else:
        lucky = "Билет неправильный"
    return lucky
print(lucky_ticket(123000))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


#normal

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    all_f = []
    f_num1 = 1
    f_num2 = 1
    s = 0
    while f_num1 < m:
        f_sum = f_num1 + f_num2
        f_num1 = f_sum - f_num1
        f_num2 = f_sum
        if f_num1 > n:
            all_f.append(f_num1)
        else:
            pass
        s +=1
    return print(all_f)

fibonacci(2,10)
fibonacci(5,8)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort = []
    n = 0
    while n < len(origin_list):
        f = min(origin_list)
        sort.append(f)
        origin_list.remove(f)
        if origin_list == 0:
            break
        
    return sort
        

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def func(usl,znach):
    lst = []
    for i in znach: 
        if i != usl : 
            lst.append(i)
    return lst


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


# 4 очень сложно