import queue

def createMaze():
    maze = []
    maze.append(["#", "O", "#", " ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "X", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"])

    return maze

def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
    
    i = start
    j = 0 
    pos = set ()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j,i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()

def valid(maze, moves):
    start = None  # Initialize start to None
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    if start is None:
        return False
    
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
        
    return True

def findEnd(maze, moves):
    start = None  # Initialize start to None
    for x, pos in enumerate(maze[0]):
        if pos == 'O':
            start = x

    if start is None:
        return False  # Return False or handle the error appropriately

    i = start
    j = 0
    for move in moves:
        if move == 'L':
            i -= 1

        elif move == 'R':
            i += 1

        elif move == 'U':
            j -= 1

        elif move == 'D':
            j += 1

    if maze[j][i] == 'X':
        print('Found: ' + moves)
        printMaze(maze, moves)
        return True

    return False

nums = queue.Queue( )
nums.put("")
add = ""
maze = createMaze()

while not findEnd(maze, add):
    if nums.empty():  # If the queue is empty, break the loop
        print("No valid path found.")
        break
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)