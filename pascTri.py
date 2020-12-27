from variables import *  # type: ignore

def triangleGen(x):
    global pascTriangle
    triangle = pascTriangle  # type: ignore
    x = abs(x)
    for i in range(len(triangle)-1, x):
        newRow = [1]*(i+2)
        if len(newRow) > 2:
            for j in range(1, len(newRow)-1):
                newRow[j] = triangle[i][j]+triangle[i][j-1]
        triangle += [newRow]

def visualize():
    global pascTriangle
    for i in enumerate(pascTriangle):
        print((len(str(pascTriangle[-1]))//2-len(str(i[1]))//2)*" "+str(i[1]))

