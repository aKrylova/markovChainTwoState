# Допуск к лабораторной работе 1
# Описание задачи:
# Смоделировать работу Марковской цепи с двумя состояниями за t шагов.
# Оценить вероятность того, что она окажется в i-ом состоянии на шаге t.
# Также произвести теоретический расчет данной вероятности.

# подключаем библиотеки:
# numpty для работы с матрицами и векторами
# random генерация псевдо-случ числа
# для графиков
import numpy as np
import random as rnd
import matplotlib.pyplot as plt

# матрица переходов
m = np.array([
    [0.8, 0.2],
    [0.6, 0.4]
])


def practice(N, time, startState):
    if startState and time == 0 :
        return 0
    # количетсво экспериментов сколько раз были в заданном состоянии
    Nt = 0
    # начальное состояние
    setState = startState
    # вероятности перехода из 0 в 0
    p00 = m[0][0]
    # из в 1 в 1
    p11 = m[1][1]
    for n in range(0, N):
        for t in range(0, time):
            rnum = rnd.random()
            # стартуем из 0
            if setState:
                # если выполнится, то переход
                if rnum > p11:
                    setState = 0
            else:
                if rnum > p00:
                    setState = 1
            # проверим если МЦ осталась в нужном состоянии
        if setState == startState:
            Nt += 1
    return Nt / N


# время
T = 100
# количество экспериментов
N = 5000

arrayT = []
arrayState0 = []
arrayState1 = []

# цикл по оси x (время)
for t in range(0, T):
    arrayT.append(t)
    result = practice(N, t, 0)
    print('state 0 = ')
    print(result)
    arrayState0.append(result)
    print('state 1 = ')
    result = practice(N, t, 1)
    arrayState1.append(result)
    print(result)

plt.plot(arrayT, arrayState0)
plt.plot(arrayT, arrayState1)
plt.grid(True)
plt.show()
