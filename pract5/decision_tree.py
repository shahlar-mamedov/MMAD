import numpy as np
import math

NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит

NUMERICAL = 0       # параметр числовой
CATEGORICAL = 1     # параметр категориальный


def decision_tree(X, Y, scale, level=0):

    if len(np.unique(Y)) == 1:
        print('class = %d' % Y[0])
        return

    print('')

    n = X.shape[1]  # количество признаков
    m = X.shape[0]  # количество примеров

    # энтропия до разбиения
    info = Info(Y)

    gain = []
    thresholds = np.zeros(n)

    # цикл вычисления информационного выигрыша
    # по каждому столбцу выборки
    for i in range(n):

        if scale[i] == CATEGORICAL:   # категориальный признак
            
            info_s = 0
            k = len(np.unique(X[:, i]))
            values, counts = np.unique(X[:, i], return_counts=True)
            for j in range(k):
                info_s += (counts[j] / m) * Info(Y[X[:, i] == values[j]])
            gain.append(info - info_s)

        else:  # непрерывный признак
            # сортируем столбец по возрастанию
            val = np.sort(X[:, i])

            local_gain = np.zeros(m - 1)

            # количество порогов на 1 меньше числа примеров
            for j in range(m - 1):
                threshold = val[j]
                less = sum(X[:, i] <= threshold)  # количество значений в столбце, <=, чем порог
                greater = m - less  # количество значений в столбце, >, чем порог

                # вычисляем информативность признака при данном пороге
                info_s = (less / m) * Info(Y[X[:, i] <= threshold]) + (greater / m) * Info(Y[X[:, i] > threshold])

                local_gain[j] = info - info_s

            gain.append(np.max(local_gain, axis=0))
            idx = np.argmax(local_gain, axis=0)

            thresholds[i] = val[idx]

    # теперь нужно выбрать столбец с максимальным приростом информации
    max_idx = np.argmax(gain)

    if scale[max_idx] == CATEGORICAL:
        # если этот столбец категориальный
        # запускаем цикл по всем уникальным значениям этого столбца
        categories = np.unique(X[:, max_idx])

        for category in categories:
            # рекурсивно вызываем функцию decision_tree с параметрами:
            sub_x = X[X[:, max_idx] == category, :]
            sub_y = Y[X[:, max_idx] == category]

            print_indent(level)
            print('column %d == %f, ' % (max_idx, category), end='')

            decision_tree(sub_x, sub_y, scale, level + 1)
    else:
        # столбец числовой
        # рекурсивно вызываем decision_tree для значений, меньше порога, и значений, больше порога
        threshold = thresholds[max_idx]

        sub_x = X[X[:, max_idx] <= threshold, :]
        sub_y = Y[X[:, max_idx] <= threshold]

        print_indent(level)
        print('column %d <= %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)

        sub_x = X[X[:, max_idx] > threshold, :]
        sub_y = Y[X[:, max_idx] > threshold]

        print_indent(level)
        print('column %d >  %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)


# вычисление энтропии множества set
def Info(set):
    m = len(set)
    info = 0

    unique, counts =np.unique(set,return_counts=True)
    for i in range(len(np.unique(set))):
        p = counts[i]/m
        info += (p * np.log2(p))

    info = -info
    return info


# печать отступа (дня наглядности)
def print_indent(level):
    print(level * '  ', end='')
