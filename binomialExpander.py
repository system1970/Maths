from alpha import superscript  # type: ignore
from pascTri import triangleGen  # type: ignore
from variables import *  # type: ignore

def expander(eq,power):
    return f"{eq} + {superscript(str(power))} + \N{SUPERSCRIPT MINUS}" if power < 0 else eq + superscript(str(power)) if power > 1 else eq
    

def expansion(x):
    global pascTriangle
    triangle = pascTriangle  # type: ignore
    standardForm = ["a", "b"]
    memX = x
    specials = {
        0: f"({standardForm[0]} + {standardForm[1]}){superscript(str(x))} = 1",
    }
    if x == 0:
        return specials[x] 
    if abs(x) > len(triangle)-1:
        triangleGen(x)
    x = abs(x)
    expanded = f"{expander(standardForm[0], triangle[x][1])} + " if memX == x else f"({expander(standardForm[0], triangle[x][1])} + "
    for i in range(1, len(triangle[x])-1):
        expanded += f"{str(triangle[x][i])}{expander(standardForm[0],x-i)}{expander(standardForm[1],i)} + "
    expanded += f"{expander(standardForm[1], triangle[x][-2])}" if memX == x else f"{expander(standardForm[1], triangle[x][-2])})\N{SUPERSCRIPT MINUS}{superscript(str(1))}"
    return f"({standardForm[0]} + {standardForm[1]}){superscript(str(memX))} = {expanded}" 

print(expansion(-5))
