# Допуск 4
# Промоделировать работу системы массового обслуживания с ограниченной очередью
# размеров b. Оценить путем моделирования среднее количество заявок в системе E[N] и
# среднюю задержку E[D]. Также произвести теоретический расчет двух данных величин.

import numpy as np
import math
# для построения графика
import pylab
import matplotlib.pyplot as plt

# размер очереди
b = 5
# время работы системы (кол-во эксперементов)
T = 100000
# лямбда задаются
lambdaUser = np.linspace(0.1, 2, 19)

En_model = []  # количество заявок (практ)
Ed_model = []  # задержка (практ)
En_theor = []  # средняя количетсво заявок (теор)
Ed_theor = []  # средняя задержка (теор)
lOut_theor = []  # средняя задержка (теор)

# генерация матрицы переходов
def generate_matrix(b, λ):
     matrix = np.zeros((b + 1, b + 1))
     for i in range(b + 1):
          matrix[0][i] = poisson(λ, i)
     if(sum(matrix[0]) != 1):
        matrix[0][b] += 1 - sum(matrix[0])
     for i in range(b + 1):
          for j in range(b + 1):
               if(j + i < b + 1 and i + 1 < b + 1):
                    if(j + 1 == b + 1 - i):
                         # matrix[i + 1][j + i - 1] += 1 - sum(matrix[0][j:b+1])
                         matrix[i + 1][j + i - 1] += sum(matrix[0][j:b+1])
                        # 1 - sum(matrix[])
                    else:
                         matrix[i + 1][j + i] = matrix[0][j]

     matrix[-1][-2] = 1
     print(matrix)
     return matrix


# пуассон (кол-во заявок в окне будем считаеть по нему)
def poisson(lmb, i):
    return (lmb ** i) / (math.factorial(i)) * (math.exp(-lmb))


# практика
for ind in range(len(lambdaUser)):
    countEn = 0
    countEd = []
    buf = []
    for time in range(T):
        # заяка
        req = np.random.poisson(lambdaUser[ind], 1)
        # увеличиваем количетсво заявок
        addLen = len(buf)
        qBuf = len(buf)
        for r in range(req[0]):
            addLen = len(buf)
            if (addLen < b):
                buf.append(time)
        # пока заявка не ушла из системы, она в буфере
        # очередь не пустая, обрабатываем заявку
        if (qBuf != 0):
            timeStart = buf.pop(0)
            # time = timeEnd
            sub = time - timeStart
            countEd.append(sub) # задержка
        countEn += len(buf) # суммир всех заявок
    En_model.append(countEn / (T)) # sum(D)/M среднее кол-во заявок
    Ed_model.append(sum(countEd) / len(countEd))  # средняя задержка

    # генерируем матрицу переходов
    A = np.transpose(generate_matrix(b, lambdaUser[ind])) - np.eye(b + 1)
    A[-1] = np.ones(b + 1)
    vect = np.zeros(b + 1)
    vect[-1] = 1
    x = np.linalg.solve(A, vect)
    # среднее количество заявок в системе
    N = [i * x[i] for i in range(len(x))]
    s = sum(N)

    lambdaOut = 1 - x[0] # сред число заявок покидающее систему в 1 времени
    lOut_theor.append(lambdaOut)
    En_theor.append(round(s, 4))
    Ed_theor.append(round(s / lambdaOut, 4)) # по т Литтла


pylab.plot(lambdaUser, En_model, label='model E[N]')
print("En_model: ", En_model)
print()
pylab.plot(lambdaUser, En_theor, label='theor E[N]_t')
print("En_model_t: ", En_theor)
print()
pylab.plot(lambdaUser, Ed_model, label='model E[D]')
print("Ed_model: ", Ed_model)
pylab.legend(('model E[N]', 'model E[D]'))
pylab.plot(lambdaUser, Ed_theor, label='model E[D]_t')
print("Ed_model_t: ", Ed_theor)
# pylab.plot( lambdaUser, lOut_theor, label='lOut(lIn)')
pylab.legend(('model E[N]', 'model E[N]_t', 'model E[D]', 'model E[D]_t'))
pylab.show()
