#Турбо калькулятор

from math import *

import math

print('Турбо-калькулятор 3000')

print('Выберите режим:')

print('1 - калькулятор')

print('2 - решение квадратных уравнений')

choise = int(input())

if choise == 1:

    print('Калькулятор')

    print('Введите выражение, разделяя каждый символ пробелом. Например: (2 + 3 / 4 * 2 ^ 2)')

    print('Приоритеты выполнения: Степень, Умножение, Деление, Сложение/Вычитание')

    query = input()

    corrected_query = query.replace(',', '.').split()   #Исправление , на . в дробных числах

    numberlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    actions = []

    arg = []

    for i in corrected_query:       #Определение действий, внесение их в список

        if i == '+':

            actions.append('+')

        elif i == '-':

            actions.append('-')

        elif i == '/' or i == ':':

            actions.append('/')

        elif i == '*':

            actions.append('*')

        elif i == '^':

            actions.append('^')



    for i in corrected_query:           #Определение числе, внесение их в список

        if i[0:1].isnumeric() == True:

            arg.append(float(i))

        else:

            continue

    while('^' in actions):                            #Выполнение возведений в степень

        for i in actions:

            if i == '^':

                ind = actions.index(i)

                halfres = arg[ind:ind+2]

                b = math.pow(halfres[0], halfres[1])

                arg.pop(ind+1)

                arg[ind] = b

                actions.pop(actions.index(i))           #Замена 2ух чисел на результат действия. Аналогично во всех действиях

    while('*' in actions):                               #Выполнение умножений

        for i in actions:

                if i == '*':

                    ind = actions.index(i)

                    halfres = arg[ind:ind+2]

                    b = halfres[0] * halfres[1]

                    arg.pop(ind + 1)

                    arg[ind] = b

                    actions.pop(actions.index(i))

    while('/' in actions):                              #Выполнение делений

        for i in actions:

            if i == '/':

                ind = actions.index(i)

                halfres = arg[ind:ind+2]

                b = halfres[0]/halfres[1]

                arg.pop(ind + 1)

                arg[ind] = b

                actions.pop(actions.index(i))

    while('+' in actions or '-' in actions):          #Выполнения сложений, вычитаний

        for i in actions:

            if i == '+':

                ind = actions.index(i)

                halfres = arg[ind:ind + 2]

                b = halfres[0] + halfres[1]

                arg.pop(ind + 1)

                arg[ind] = b

                actions.pop(actions.index(i))

            elif i == '-':

                ind = actions.index(i)

                halfres = arg[ind:ind + 2]

                b = halfres[0] - halfres[1]

                arg.pop(ind + 1)

                arg[ind] = b

                actions.pop(actions.index(i))

    print(float(arg[0]))

elif choise == 2:

    print('Решение квадратных уравнений')

    print('Введите квадратное урванение по форме a * x ^ 2 + b * x + c')

    func = input()                                  

    funcforarg = func.split()

    arg = []

    flag = 0                                       #Введение флага для работы как ввода вида "X^2", так и "x ^ 2"

    minus = False

    for i in funcforarg:                            #Определение к-тов a, b и c, внесение их в список

        if i == '-':

            minus = True

        if i.isnumeric() == True:

            if minus == True:

                arg.append(float('-'+i))

                minus = False

            else:

                if flag == '^':

                    continue

                else:

                    arg.append(float(i))

        else:

            flag = i

            continue

    a, b, c = arg

    d = float()

    d = (math.pow(b, 2)) - (4*a*c)

    if d < 0:                                       #Решение уравнения

        print('Действительных решений нет =(')

    elif d == 0:

        x = (-b/a)

        print('x1,x2 = ', x)

    else:

        x1 = (-b + math.sqrt(d)) / a

        x2 = (-b - math.sqrt(d)) / a

        print('x1 = ', x1, 'x2 = ', x2)

