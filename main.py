# Constants
BOARD_SIZE = 19
WIN_LENGTH = 5

# Напрямки перевірки: праворуч, вниз, діагональ вниз-право, діагональ вниз-ліво
DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]

def is_valid(x, y):
    """
    Перевіряє, чи координати (x, y) лежать у межах поля 19x19.
    """
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def check_win(board, color):
    """
    Перевіряє, чи є у гравця color п’ять каменів поспіль у будь-якому з допустимих напрямків.

    Повертає:
        - (color, i + 1, j + 1), якщо знайдено точку початку виграшної послідовності.
        - (0, ), якщо переможної послідовності не знайдено.
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != color:
                continue  # ця клітинка не належить гравцю, пропускаємо
            for dx, dy in DIRECTIONS:
                ni, nj = i - dx, j - dy
                if is_valid(ni, nj) and board[ni][nj] == color:
                    continue  # не початок послідовності
                
                count = 0
                x, y = i, j
                while is_valid(x, y) and board[x][y] == color:
                    count += 1
                    if count > WIN_LENGTH:
                        break  # понад 5 — не виграшна послідовність
                    x += dx
                    y += dy
                if count == WIN_LENGTH:
                    return (color, i + 1, j + 1)
    return (0, )

def main():
    """
    Основна функція:
    - Зчитує кількість тестів та ігрові дошки з файлу input.txt.
    - Для кожного тесту визначає, чи є переможець.
    - Записує результат у файл output.txt у форматі:
        * 0 — якщо немає переможця;
        * color\nx y — якщо виграв color і перший камінь послідовності в (x, y).
    """
    with open("input.txt", "r") as f:
        lines = f.read().split()

    idx = 0
    T = int(lines[idx])
    idx += 1

    output = []

    for test_num in range(T):
        board = []
        for row_num in range(BOARD_SIZE):
            if idx + BOARD_SIZE > len(lines):
                raise ValueError(f"Недостатньо даних для зчитування {row_num+1}-го рядка {test_num+1}-го тесту.")
            row = list(map(int, lines[idx:idx + BOARD_SIZE]))
            if len(row) != BOARD_SIZE:
                raise ValueError(f"Рядок {row_num + 1} не містить {BOARD_SIZE} елементів у {test_num+1}-му тесті.")
            board.append(row)
            idx += BOARD_SIZE

        if len(board) != BOARD_SIZE:
            raise ValueError(f"Дошка {test_num+1} не містить {BOARD_SIZE} рядків")

        # Перевірка виграшу спочатку для чорного (1), потім для білого (2)
        for color in [1, 2]:
            result = check_win(board, color)
            if result[0] != 0:
                output.append(str(result[0]))
                output.append(f"{result[1]} {result[2]}")
                break
        else:
            output.append("0")

    with open("output.txt", "w") as f:
        f.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()
