#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Расширенный подсчет количества островов в бинарной матрице.

from collections import deque

# Ниже перечислены все восемь возможных перемещений из ячейки.
# (верхний, правый, нижний, левый и четыре диагональных хода)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# Функция проверки безопасного перехода в позицию (x, y)
# с текущей позиции. Функция возвращает false, если (x, y)
# недействительные матричные координаты или (x, y) представляет воду или
# Позиция # (x, y) уже обработана.

def isSafe(mat, x, y, processed):
    return (x >= 0 and x < len(processed)) and (y >= 0 and y < len(processed[0])) and \
        mat[x][y] == 1 and not processed[x][y]


def BFS(mat, processed, i, j):
    # создает пустую queue и ставит в queue исходный узел
    q = deque()
    q.append((i, j))

    # пометить исходный узел как обработанный
    processed[i][j] = True

    # Цикл # до тех пор, пока queue не станет пустой
    while q:
        # удаляет передний узел из очереди и обрабатывает его
        x, y = q.popleft()

        # проверяет все восемь возможных перемещений из текущей ячейки
        # и ставить в queue каждое допустимое движение
        for k in range(len(row)):
            # пропустить, если локация недействительна, уже обработана или содержит воду
            if isSafe(mat, x + row[k], y + col[k], processed):
                # пропустить, если местоположение неверно или уже
                # обработан или состоит из воды
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))


def countIslands(mat):
    # Базовый вариант
    if not mat or not len(mat):
        return 0

    # Матрица `M × N`
    (M, N) = (len(mat), len(mat[0]))

    # запоминает, обработана ячейка или нет
    processed = [[False for x in range(N)] for y in range(M)]

    island = 0
    for i in range(M):
        for j in range(N):
            # запускает BFS с каждого необработанного узла и увеличивает количество островов
            if mat[i][j] == 1 and not processed[i][j]:
                BFS(mat, processed, i, j)
                island = island + 1

    return island


if __name__ == '__main__':
    mat = [
        [1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0]
    ]

    print('Общее количество островов:', countIslands(mat))
