# Промоделировать работу системы массового обслуживания с ограниченной очередью
# размеров b. Оценить путем моделирования среднее количество заявок в системе E[N] и
# среднюю задержку E[D]. Также произвести теоретический расчет двух данных величин.

import numpy as np
import math
# для построения графика
import pylab
import matplotlib.pyplot as plt

# размер очереди
b = 3
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

