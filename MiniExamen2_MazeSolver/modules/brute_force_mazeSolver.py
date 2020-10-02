from PIL import Image
from .mazeToGif import makeGIF #pylint: disable=relative-beyond-top-level

def make_step(k:int):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
          m[i-1][j] = k + 1
        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
          m[i][j-1] = k + 1
        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
          m[i+1][j] = k + 1
        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
           m[i][j+1] = k + 1

def runSolver(mazeMatrix:list, startCoord:tuple, endCoord:tuple, fileNameGif:str):
    global a, m
    images = []
    a = mazeMatrix
    start = startCoord
    end = endCoord
    m = []

    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1

    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k)
        images = makeGIF(start,end,a,m,[],images)

    i, j = end
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1
    images = makeGIF(start,end,a,m,the_path,images)

    for i in range(10):
        if i % 2 == 0:
            images = makeGIF(start,end,a,m,the_path,images)
        else:
            images = makeGIF(start,end,a,m,[],images)

    images[0].save(fileNameGif,
                save_all=True, append_images=images[1:],
                optimize=False, duration=0.5, loop=0)