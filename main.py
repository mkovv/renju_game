DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]

def is_valid(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def check_win(board, color):
    for i in range(19):
        for j in range(19):
            if board[i][j] != color:
                continue
            for dx, dy in DIRECTIONS:
                ni, nj = i - dx, j - dy
                if is_valid(ni, nj) and board[ni][nj] == color:
                    continue  # не початок послідовності
                count = 0
                x, y = i, j
                while is_valid(x, y) and board[x][y] == color:
                    count += 1
                    if count > 5:
                        break
                    x += dx
                    y += dy
                if count == 5:
                    return (color, i + 1, j + 1)
    return (0, )

def main():
    with open("input.txt", "r") as f:
        lines = f.read().split()

    idx = 0
    T = int(lines[idx])
    idx += 1

    output = []

    for _ in range(T):
        board = []
        for _ in range(19):
            row = list(map(int, lines[idx:idx + 19]))
            board.append(row)
            idx += 19

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
