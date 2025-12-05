file_path = "roll_matrix.txt"
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]
print((grid))
# Clean the input diagram into a list of strings (rows)
#this is a math problem using Moore neighbourhood : https://en.wikipedia.org/wiki/Moore_neighborhood

ROWS = len(grid)
COLS = len(grid[0])
ROLL = '@'

def count_accessible_rolls(grid):
    accessible_count = 0
    
    # Offsets for the 8 adjacent neighbors (dr, dc)
    # (-1,-1) to (1,1), excluding (0,0)
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    for r in range(ROWS):
        for c in range(COLS):
            # 1. Check if the current cell is a roll of paper
            if grid[r][c] == ROLL:
                #print(type(grid[r][c]))
                neighbor_rolls = 0 # this is first condition that the forklift works only at the roll position                
                # 2. Count adjacent rolls
                for dr, dc in neighbor_offsets:
                    nr, nc = r + dr, c + dc # Neighbor Row, Neighbor Column
                    
                    # 3. Check boundaries
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        
                        # 4. Check if the neighbor cell is also a roll
                        if grid[nr][nc] == ROLL:
                            neighbor_rolls += 1
                
                # 5. Check Access: Must have FEWER THAN FOUR rolls adjacent
                if neighbor_rolls < 4:
                    accessible_count += 1
                    
    return accessible_count

# Calculate the result for the example
example_result = count_accessible_rolls(grid)
print(f"The number of accessible rolls in the example is: {example_result}")