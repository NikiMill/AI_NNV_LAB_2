#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Поиск кратчайшего пути в лабиринте.

from collections import deque

# Функция для поиска кратчайшего пути в лабиринте
def bfs(maze, start, goal):
    # Дирекции для перемещения (верх, низ, влево, вправо)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])
    visited = {start: None}  # Словарь для отслеживания предков

    while queue:
        current = queue.popleft()

        # Если достигли цели, строим путь
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Возвращаем путь в обратном порядке

        # Проверка соседних клеток
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if (0 <= neighbor[0] < len(maze) and
                    0 <= neighbor[1] < len(maze[0]) and
                    maze[neighbor[0]][neighbor[1]] == 1 and
                    neighbor not in visited):
                visited[neighbor] = current
                queue.append(neighbor)

    return None  # Если путь не найден

# Пример лабиринта
maze = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
]
initial = (0, 0)
goal = (4, 5)


path = bfs(maze, initial, goal)

if path:
    print("Кратчайший путь:", path)
    print("Длина пути:", len(path) - 1)
else:
    print("Путь не найден")
