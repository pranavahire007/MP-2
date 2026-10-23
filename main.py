from collections import deque

def snake_and_ladder():
    # Board size
    N = 30

    # Dictionary representing snakes and ladders
    # Key = starting position, Value = ending position
    jumps = {
        3: 22,    # Ladder
        5: 8,     # Ladder
        11: 26,   # Ladder
        20: 29,   # Ladder
        17: 4,    # Snake
        19: 7,    # Snake
        21: 9,    # Snake
        27: 1     # Snake
    }

    # BFS queue stores (position, number of dice throws)
    queue = deque([(1, 0)])

    # Track visited positions
    visited = [False] * (N + 1)
    visited[1] = True
    
    # BFS traversal
    while queue:
        position, throws = queue.popleft()
    
        # Destination reached
        if position == N:
            print("\nDestination reached!")
            print("Minimum dice throws required:", throws)
            return

        # Try all possible dice outcomes (1 to 6)
        for dice in range(1, 7):
            next_position = position + dice

            # Do not move beyond the board
            if next_position > N:
                continue

            # Apply snake or ladder
            if next_position in jumps:
                next_position = jumps[next_position]

            # Visit each position only once
            if not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, throws + 1))

    print("Destination cannot be reached.")


# Main program
print("================================")
print("     SNAKE AND LADDER USING BFS")
print("================================")
print("Starting position: 1")
print("Destination position: 30")

snake_and_ladder()
