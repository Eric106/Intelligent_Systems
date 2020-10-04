import random

def generator(mx:int,my:int):
    maze = [[0 for x in range(mx)] for y in range(my)]
    dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze

    stack = [(random.randint(0, mx - 1), random.randint(0, my - 1))]

    while len(stack) > 0:
        (cx, cy) = stack[-1]
        maze[cy][cx] = 1
        # find a new cell to add
        nlst = [] # list of available neighbors
        for i in range(4):
            nx = cx + dx[i]; ny = cy + dy[i]
            if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                if maze[ny][nx] == 0:
                    # of occupied neighbors must be 1
                    ctr = 0
                    for j in range(4):
                        ex = nx + dx[j]; ey = ny + dy[j]
                        if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                            if maze[ey][ex] == 1: ctr += 1
                    if ctr == 1: nlst.append(i)
        # if 1 or more neighbors available then randomly select one and move
        if len(nlst) > 0:
            ir = nlst[random.randint(0, len(nlst) - 1)]
            cx += dx[ir]; cy += dy[ir]
            stack.append((cx, cy))
        else: stack.pop()

    mazeInvert = []
    for row in range(len(maze)):
        tempRow = []
        for col in range(len(maze[row])):
            if maze[row][col] == 0:
                tempRow.append(1)
            elif maze[row][col] == 1:
                tempRow.append(0)
        mazeInvert.append(tempRow)
    # mazeToPNG(maze,imgx,imgy,mx,my,color)
    finalMaze = []
    finalMaze.append([1]*(len(mazeInvert[0])+2))
    for row in range(len(mazeInvert)):
        tempRow = [1] + mazeInvert[row] + [1]
        finalMaze.append(tempRow)
    finalMaze.append([1]*(len(mazeInvert[0])+2))
    return finalMaze