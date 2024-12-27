from collections import deque


def bfs_min_distance(distance_matrix, start, end):
    """Поиск минимального расстояния с помощью алгоритма BFS."""

    # Количество городов
    num_cities = len(distance_matrix)

    # Очередь для BFS
    queue = deque([start])

    # Список для хранения расстояний
    distances = [float('inf')] * num_cities
    distances[start] = 0

    # Массив для отслеживания посещенных узлов
    visited = [False] * num_cities
    visited[start] = True

    while queue:
        current = queue.popleft()

        for neighbor in range(num_cities):
            if distance_matrix[current][neighbor] > 0 and not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + distance_matrix[current][neighbor]
                queue.append(neighbor)

    return distances[end] if distances[end] != float('inf') else -1  # -1 если путь не найден


# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами
    distance_matrix = [
        [0, 634, 246, 420, 98, 181, 853, 462, 457, 199],
        [634, 0, 719, 545, 732, 815, 1487, 1096, 983, 833],
        [246, 719, 0, 174, 183, 100, 938, 708, 703, 284],
        [420, 545, 174, 0, 357, 274, 1112, 882, 877, 458],
        [98, 732, 183, 357, 0, 83, 755, 560, 555, 101],
        [181, 815, 100, 274, 83, 0, 838, 643, 638, 184],
        [853, 1487, 938, 1112, 755, 838, 0, 462, 674, 654],
        [462, 1096, 708, 882, 560, 643, 462, 0, 212, 661],
        [457, 983, 703, 877, 555, 638, 674, 212, 0, 656],
        [199, 833, 284, 458, 101, 184, 654, 661, 656, 0],
    ]

    start_city = 0  # Начальный город (индекс)
    end_city = 3  # Конечный город (индекс)

    min_distance = bfs_min_distance(distance_matrix, start_city, end_city)

    if min_distance != -1:
        print(f"Минимальное расстояние между городами {start_city} и {end_city}: {min_distance}")
    else:
        print(f"Путь между городами {start_city} и {end_city} не найден.")
