# Промоделировать работу Марковской цепи с одним поглощающим состоянием из трех.
# Путем моделирования оценить среднее время достижения поглощающего
# состояния и вычислить его теоретически.

import random as rnd
import numpy as np
from scipy import linalg

# матрица переходов
m = np.array([
    [0.03, 0.07, 0.9],
    [0.9, 0.02, 0.08]
])

N = 1000000

def theorValue(matrix):
    A = np.array([
        [1 - matrix[0][0], -matrix[0][1]],
        [-matrix[1][0], 1 - matrix[1][1]]
    ])

    B = np.array([1, 1]) # вектор столбец
    X = np.linalg.inv(A).dot(B)
    print(X)
    return 1

def practice(N, mt):
    T = 0  # время до поглощ состояния
    # count = 0
    # N эксперементов
    for i in range(N - 1):
        setState0 = 0  # нач сост
        setState1 = 1
        setState2 = 0
        i = 0
        count = 0
        while 1:
            rnum = rnd.random()
            if (i == 0):
                if (setState0):
                    count += 1
                elif (setState1):
                    count += 1
                elif (setState2):
                    count += 1
                    break
            i += 1
            if (setState0):
                # остался в 0
                if (rnum <= mt[0][0]):
                    count += 1
                # переход в 1
                elif ((rnum > mt[0][0]) and (rnum <= (mt[0][0] + mt[0][1]))):
                    setState0 = 0
                    setState1 = 1
                    count += 1
                # перешли в 2
                elif (rnum > (mt[0][0] + mt[0][1])):
                    # count += 1 ???
                    break
            elif (setState1):
                # переход в 0
                if (rnum < mt[1][0]):
                    setState1 = 0
                    setState0 = 1
                    count += 1
                # остался в 1
                elif ((rnum >= mt[1][0]) and (rnum <= (mt[1][0] + mt[1][1]))):
                    setState0 = 0
                    setState1 = 1
                    count += 1
                # переход в 2
                elif (rnum > (mt[1][1] + mt[1][0])):
                    # count += 1 ???
                    break
            elif (setState2):
                # остаёмся в нём
                # count += 1 ???
                break
        T += count
    print(T / N)
    return 1

theorValue(m)
practice(N, m)