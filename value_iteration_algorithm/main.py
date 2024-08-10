grid = [
    [0, 0, 0, 1],
    [0, 'X', 0, -1],
    [0, 0, 0, 0]
]

value = [
    [0, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, 0, 0]
]

GAMMA = 0.9
step_cost = 0.1

def can_move(row, col):
    if (col >= 0 and col < 4 and row >= 0 and row < 3 and grid[row][col] != 'X'):
        return True
    return False

if __name__ == '__main__':
    start = (2, 0)

    for i in range(2):
        for row in range(3):
            for col in range(4):
                state_reward = 0
                for action in range(4):
                    if (action == 0 and (row == 0 or grid[row - 1][col] == 'X')) or \
                            (action == 1 and (col == 3 or grid[row][col + 1] == 'X')) or \
                            (action == 2 and (row == 2 or grid[row + 1][col] == 'X')) or \
                            (action == 3 and (col == 0 or grid[row][col - 1] == 'X')) or \
                            (row == 0 and col == 3) or \
                            (row == 1 and col == 3):
                        continue

                    if (action == 0):
                        if (can_move(row-1, col)): state_reward += 0.8 * (0 + GAMMA * value[row-1][col])
                        if (can_move(row, col-1)): state_reward += 0.1 * (0 + GAMMA * value[row][col-1])
                        if (can_move(row, col+1)): state_reward += 0.1 * (0 + GAMMA * value[row][col+1])
                    elif (action == 1):
                        if (can_move(row, col+1)): state_reward += 0.8 * (0 + GAMMA * value[row][col+1])
                        if (can_move(row-1, col)): state_reward += 0.1 * (0 + GAMMA * value[row-1][col])
                        if (can_move(row+1, col)): state_reward += 0.1 * (0 + GAMMA * value[row+1][col])
                    elif (action == 2):
                        if (can_move(row+1, col)): state_reward += 0.8 * (0 + GAMMA * value[row+1][col])
                        if (can_move(row, col-1)): state_reward += 0.1 * (0 + GAMMA * value[row][col-1])
                        if (can_move(row, col+1)): state_reward += 0.1 * (0 + GAMMA * value[row][col+1])
                    elif (action == 3):
                        if (can_move(row, col-1)): state_reward += 0.8 * (0 + GAMMA * value[row][col-1])
                        if (can_move(row-1, col)): state_reward += 0.1 * (0 + GAMMA * value[row-1][col])
                        if (can_move(row+1, col)): state_reward += 0.1 * (0 + GAMMA * value[row+1][col])

                    value[row][col] = max(0, state_reward)

for i in range(3):
    for j in range(4):
        print(value[i][j], end=" ")
    print()