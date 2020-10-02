from PIL import Image
from simpleai.search import SearchProblem, astar
from .modules.brute_force_mazeSolver import runSolver #pylint: disable=relative-beyond-top-level
from .modules.a_star_mazeSolver import MazeSolver #pylint: disable=relative-beyond-top-level
from .modules.mazeToGif import makeGIF #pylint: disable=relative-beyond-top-level


def get_start_end(mazeMatrix:list):
    start = (1,1)
    end = (len(mazeMatrix)-2,len(mazeMatrix[0])-2)
    if mazeMatrix[start[0]][start[1]] == 1:
        s1 = (start[0],start[1]+1)
        s2 = (start[0]+1,start[1])
        s3 = (start[0]+1,start[1]+1)
        start = s1 if mazeMatrix[s1[0]][s1[1]] != 1 else s2 \
            if mazeMatrix[s2[0]][s2[1]] != 1 else s3
    if mazeMatrix[end[0]][end[1]] == 1:
        e1 = (end[0],end[1]-1)
        e2 = (end[0]-1,end[1])
        e3 = (end[0]-1,end[1]-1)
        end = e1 if mazeMatrix[e1[0]][e1[1]] != 1 else e2 \
            if mazeMatrix[e2[0]][e2[1]] != 1 else e3
    return start, end
    

def brute_force(mazeMatrix:list):
    start,end = get_start_end(mazeMatrix)
    runSolver(mazeMatrix,start,end,"./static/brute.gif")

def mazeMatrix_for_astar(mazeMatrix:list):
    start,end = get_start_end(mazeMatrix)
    mazeConverted = []
    for y in range(len(mazeMatrix)):
        tempRow = []
        for x in range(len(mazeMatrix[y])):
            if (y,x) == start:
                tempRow.append("o")
            elif (y,x) == end:
                tempRow.append("x")
            elif x == 0 or x == len(mazeMatrix[0])-1 or \
                y == 0 or y == len(mazeMatrix)-1 or mazeMatrix[y][x] == 1:
                tempRow.append("#")
            elif mazeMatrix[y][x] == 0:
                tempRow.append(" ")
        mazeConverted.append(tempRow)
    return mazeConverted

def a_star(mazeMatrix:list):
    images = []
    fileNameGif = "./static/a.gif"
    MAP = mazeMatrix_for_astar(mazeMatrix)
    cost_regular = 1.0

    # Create the cost dictionary
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular
    }

    # Create maze solver object
    problem = MazeSolver(MAP,COSTS)

    # Run the solver
    result = astar(problem, graph_search=True)

    # Extract the path
    path = [x[1] for x in result.path()]

    # Print the result
    print()
    start = (0,0)
    end = (0,0)
    maze = []
    for y in range(len(MAP)):
        tempRow = []
        for x in range(len(MAP[y])):
            if (x, y) == problem.initial:
                start = problem.initial[::-1]
            elif (x, y) == problem.goal:
                end = problem.goal[::-1]
            if MAP[y][x] == '#':
                tempRow.append(1)
            elif MAP[y][x] == ' ' or MAP[y][x] == 'o' or MAP[y][x] == 'x':
                tempRow.append(0)
        maze.append(tempRow)

    path = [item[::-1] for item in path]
    for i in range(len(path)):
        tempPath = path[:i+1]
        mazeWithSteps = []
        for y in range(len(maze)):
            tempRow = []
            for x in range(len(maze[y])):
                if (y,x) in tempPath:
                    tempRow.append(tempPath.index((y,x)))
                else:
                    tempRow.append(0)
            mazeWithSteps.append(tempRow)
        images = makeGIF(start,end,maze,mazeWithSteps,[], images)
    path = path[::-1]
    for i in range(10):
        if i % 2 == 0:
            images = makeGIF(start,end,maze,mazeWithSteps,path,images)
        else:
            images = makeGIF(start,end,maze,mazeWithSteps,[],images)
    images[0].save(fileNameGif,
                save_all=True, append_images=images[1:],
                optimize=False, duration=0.5, loop=0)

# def main():
#     maze = generator(30,10)
#     a_star(maze)
#     print("Done A*")
#     brute_force(maze)
#     print("DONE Brute_Force")
# main()