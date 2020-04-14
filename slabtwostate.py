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
    # вероятности перехода из 0 в 0
    p00 = m[0][0]
    # из в 1 в 1
    p11 = m[1][1]
    inState0 = []
    inState1 = []
    stateRes = []
    for n in range(0, N):
        setState = 0
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
            inState0.append(setState)
        else:
            inState1.append(setState)
    stateRes = [np.size(inState0)/N, np.size(inState1)/N]
    return stateRes


def theorValue(vectP0, time):
    prTh = []
    prTh.append(np.transpose(vectP0))

    for k in range(0, time - 1):
        vectP0 = vectP0.dot(m)
        prTh.append(np.transpose(vectP0))

    return prTh

# время
T = 10
# количество экспериментов
N = 100000

arrayT = []
arrayState0 = []
arrayState1 = []
thArrayState0 = []
thArrayState1 = []

vP0 = np.array([1, 0])

# цикл по оси x (время)
for t in range(0, T):
    arrayT.append(t)
    result = practice(N, t, 0)
    print('state 0 = ')
    print(result)
    arrayState0.append(result)
    # print('state 1 = ')
    # result = practice(N, t, 1)
    # arrayState1.append(result)
    # print(result)


plt.plot(arrayT, arrayState0, label = 'practice0')
# plt.plot(arrayT, arrayState1, label = 'practice1')
plt.plot(arrayT, theorValue(vP0, T), label = 'theor')
# plt.plot(arrayT, thArrayState1)
plt.xlabel('Time')
plt.ylabel('Pr')
plt.legend()
plt.grid(True)
plt.show()

print(theorValue(vP0, T))
# print(arrayState0)

# plt.plot(arrayT, theorValue(1, T))