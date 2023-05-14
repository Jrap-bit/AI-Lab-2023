# def solve_8_puzzle(board):
#     def is_valid(x, y):
#         return 0 <= x < 3 and 0 <= y < 3
#
#     def find_empty_cell():
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == 0:
#                     return i, j
#         return None
#
#     def solve(board):
#         empty_cell = find_empty_cell()
#         if not empty_cell:
#             return True
#         row, col = empty_cell
#         moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         for move in moves:
#             new_row, new_col = row + move[0], col + move[1]
#             if is_valid(new_row, new_col):
#                 board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
#                 if solve(board):
#                     return True
#                 board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
#         return False
#
#     if solve(board):
#         return board
#     return None
#
#
# if __name__ == '__main__':
#     initial_board = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
#     solved_board = solve_8_puzzle(initial_board)
#     if solved_board:
#         for row in solved_board:
#             print(row)
#     else:
#         print("No solution found.")

def is_solvable(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversions += 1
    return inversions % 2 == 0


def find_zero(state):
    for i in range(len(state)):
        if state[i] == 0:
            return (i // 3, i % 3)


def move_up(state, row, col):
    if row == 0:
        return None
    new_state = state.copy()
    new_state[row * 3 + col], new_state[(row - 1) * 3 + col] = new_state[(row - 1) * 3 + col], new_state[row * 3 + col]
    return new_state


def move_down(state, row, col):
    if row == 2:
        return None
    new_state = state.copy()
    new_state[row * 3 + col], new_state[(row + 1) * 3 + col] = new_state[(row + 1) * 3 + col], new_state[row * 3 + col]
    return new_state


def move_left(state, row, col):
    if col == 0:
        return None
    new_state = state.copy()
    new_state[row * 3 + col], new_state[row * 3 + col - 1] = new_state[row * 3 + col - 1], new_state[row * 3 + col]
    return new_state


def move_right(state, row, col):
    if col == 2:
        return None
    new_state = state.copy()
    new_state[row * 3 + col], new_state[row * 3 + col + 1] = new_state[row * 3 + col + 1], new_state[row * 3 + col]
    return new_state


def children(state):
    row, col = find_zero(state)
    children = []
    for move, new_pos in [(move_up, (row - 1, col)), (move_down, (row + 1, col)), (move_left, (row, col - 1)),
                          (move_right, (row, col + 1))]:
        child = move(state, row, col)
        if child is not None:
            children.append(child)
    return children


def solve_puzzle(start, end, seen, visited):
    print(seen)
    if start == end:
        return True
    if tuple(start) in visited:
        return False
    seen.add(tuple(start))
    visited.add(tuple(start))
    for child in children(start):
        if solve_puzzle(child, end, seen, visited):
            return True
    return False


if __name__ == '__main__':
    start = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    end = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    seen = set()
    visited = set()
    print(solve_puzzle(start, end, seen, visited))
