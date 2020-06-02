# Промоделировать работу системы массового обслуживания с ограниченной очередью
# размеров b. Оценить путем моделирования среднее количество заявок в системе E[N] и
# среднюю задержку E[D]. Также произвести теоретический расчет двух данных величин.

import numpy as np
import math
# для построения графика
import pylab
import matplotlib.pyplot as plt

# размер очереди
b = 4
# время работы системы (кол-во эксперементов)
T = 100000
# лямбда задаются
lambdaUser = np.linspace(0.1, 3, 25)

En_model = []  # количество заявок (практ)
Ed_model = []  # задержка (практ)
En_theor = []  # средняя количетсво заявок (теор)
Ed_theor = []  # средняя задержка (теор)


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
        countEn += len(buf) # время
    En_model.append(countEn / T) # sum(D)/M
    Ed_model.append(sum(countEd) / (len(countEd) + 1))

pylab.plot(lambdaUser, En_model, label='model E[N]')
print("En_model: ", En_model)
print()
pylab.plot(lambdaUser, Ed_model, label='model E[D]')
print("Ed_model: ", Ed_model)
pylab.legend(('model E[N]', 'model E[D]'))
pylab.show()
