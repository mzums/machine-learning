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

possible_moves = {
    'up': [(-1, 0), (0, 1), (0, -1)],
    'down': [(1, 0), (0, 1), (0, -1)],
    'left': [(0, -1), (1, 0), (-1, 0)],
    'right': [(0, 1), (1, 0), (-1, 0)]
}

GAMMA = 0.9
THETA = 0.0001
step_cost = -0.1

def can_move(row, col):
    return 0 <= row < 3 and 0 <= col < 4 and grid[row][col] != 'X'

if __name__ == '__main__':
    max_change = float('inf')
    while max_change >= THETA:
        max_change = 0
        new_value = [row[:] for row in value]
        for row in range(3):
            for col in range(4):
                if grid[row][col] in ['X', 1, -1]:
                    continue
                
                max_action_reward = float('-inf')
                for action, moves in possible_moves.items():
                    next_state_reward = 0
                    for i, move in enumerate(moves):
                        next_row = row + move[0]
                        next_col = col + move[1]
                        if can_move(next_row, next_col):
                            next_state_reward += (0.8 if i == 0 else 0.1) * value[next_row][next_col]
                        else:
                            next_state_reward += (0.8 if i == 0 else 0.1) * value[row][col]
                    
                    max_action_reward = max(max_action_reward, next_state_reward)

                new_value[row][col] = step_cost + GAMMA * max_action_reward
                max_change = max(max_change, abs(new_value[row][col] - value[row][col]))
        
        value = new_value

    for i in range(3):
        for j in range(4):
            print(f"{value[i][j]:.2f}", end=" ")
        print()
