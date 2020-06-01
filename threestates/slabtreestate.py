# Допуск 2
# Описание задачи:
# Смоделировать работу Марковской цепи с тремя состояниями.
# Оценить при помощи моделирования стационарное распределение и сравнить с теоретическим расчетом.

import random as rnd
import numpy as np
from scipy import linalg

# матрица переходов
m = np.array([
    [0.4, 0.6, 0],
    [0.2, 0.5, 0.3],
    [0.2, 0.3, 0.5]
])

T = 100000

def theorValue(matrix):
    A = np.array([
        [matrix[0][0] - 1, matrix[1][0], matrix[2][0]],
        [matrix[0][1], matrix[1][1] - 1, matrix[2][1]],
        [1, 1, 1]
    ])
    B = np.array([0, 0, 1])
    C = linalg.solve(A, B)
    B = B.T
    A = linalg.inv(A)  # обратная матрица
    X = A * B
    print(X)
    return X

def practice(T, matrix):
    mt = matrix # название покороче
    setState0 = 1 # начальное состояние
    setState1 = 0
    setState2 = 0
    N_0 = 0.
    N_1 = 0.
    N_2 = 0.
    for i in range(T - 1):
        rnum = rnd.random()
        if(setState0):
            # переход в 1
            if ((rnum > mt[0][0]) and (rnum <= mt[0][0] + mt[0][1])):
                setState1 = 1
                setState0, setState2 = 0, 0
                N_1 += 1
            # переход в 2
            elif(rnum > mt[0][0] + mt[0][1]):
                setState2 = 1
                setState0, setState1 = 0, 0
                N_2 += 1
                # остался в 0
            elif(rnum <= mt[0][0]):
                setState0 = 1
                N_0 += 1
        elif(setState1):
            # переход в 0
            if(rnum < mt[1][0]):
                setState0 = 1
                setState1, setState2 = 0, 0
                N_0 += 1
            # переход в 2
            elif(rnum > (mt[1][1] + mt[1][0])):
                setState2 = 1
                setState0, setState1 = 0, 0
                N_2 += 1
                # остался в 1
            elif((rnum >= mt[1][0]) and (rnum <= mt[1][0] + mt[1][1])):
                setState1 = 1
                setState0, setState2 = 0, 0
                N_1 += 1
        elif(setState2):
            # переход в 1
            if(rnum > (mt[2][0] + mt[2][1])):
                setState1 = 1
                setState2, setState0 = 0, 0
                N_1 += 1
            # остался в 2
            elif((rnum >= mt[2][0]) and (rnum <= mt[2][0] + mt[2][1])):
                setState2 = 1
                setState1, setState0 = 0, 0
                N_2 += 1
            # переход в 0
            if(rnum < mt[2][0]):
                setState0 = 1
                setState1, setState2 = 0, 0
                N_0 += 1
    print(N_0/T)
    print(N_1/T)
    print(N_2/T)
    return 1

theorValue(m)
practice(T, m)
