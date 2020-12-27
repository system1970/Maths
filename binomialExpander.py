from pascTri import triangleGen  # type: ignore
from variables import *  # type: ignore
from alpha import superscript
from MathSyntax import Expression

def expander(eq,power):
    return f"{eq} + {superscript(str(power))} + \N{SUPERSCRIPT MINUS}" if power < 0 else eq + superscript(str(power)) if power > 1 else eq

def surround(string,c="("):
    return c+string+bracketPairs[c]

def solve(equation,terms,**kwargs):
    terms = list(map(str,terms))
    print(equation)
    print(kwargs['indent']*" ",end="= ")
    print(" + ".join(terms))
    print(kwargs['indent']*" ",end="= ")
    print(eval(" + ".join(terms)))
    

def expansion(x=None,ve=0):
    global pascTriangle
    triangle = pascTriangle  # type: ignore
    start = 97
    if ve!=0:
        co_factor = -1
    else:
        co_factor = 1
    standardForm = [chr(start+i) for i in range(2)]
    symbols = [chr(start-54+i) for i in range(0,4,2)]
    order = []
    memX = x
    terms = []
    # cases = {
    #     "No Int": exec("")
    # }
    specials = {
        0: f"({standardForm[0]} + {standardForm[1]}){superscript(str(x))} = 1",
    }
    if not x:
        return "Null Argument"
    if x == 0:
        return specials[x] 
    if abs(x) > len(triangle)-1:
        triangleGen(x)
    x = abs(x)
    evaluatedTerms = [f"{standardForm[0]}**{triangle[x][1]}"]
    expanded = f"{expander(standardForm[0], triangle[x][1])} " if memX == x else f"({expander(standardForm[0], triangle[x][1])} {symbols[ve]} "
    # terms += [Expression(f"{standardForm[0]}**{triangle[x][1]}") if memX == x else Expression(f"({standardForm[0]}**{triangle[x][1]}")]
    if ve==0:
        for i in range(1, len(triangle[x])-1):
            expanded += f"{symbols[ve]} {str(triangle[x][i])}{expander(standardForm[0],x-i)}{expander(standardForm[1],i)} "
            # terms.append(lambda a,b: f"{str(triangle[x][i])}*({standardForm[0]}**{x-i})*({standardForm[1]}**{i})".replace("a",str(a)).replace("b",str(b)))
            evaluatedTerms.append(f"{symbols[ve]}{str(triangle[x][i])}*({standardForm[0]}**{x-i})*({standardForm[1]}**{i})")
        expanded += f"{symbols[ve]} {expander(standardForm[1], triangle[x][-2])}" if memX == x else f"{expander(standardForm[1], triangle[x][-2])})\N{SUPERSCRIPT MINUS}{superscript(str(1))}"
    else:
        for i in range(1, len(triangle[x])-1):
            expanded += f"{symbols[(ve+(i-1))%2]} {str(triangle[x][i])}{expander(standardForm[0],x-i)}{expander(standardForm[1],i)} "
            # terms.append(lambda a,b: f"{str(triangle[x][i])}*({standardForm[0]}**{x-i})*({standardForm[1]}**{i})".replace("a",str(a)).replace("b",str(b)))
            evaluatedTerms.append(f"{symbols[ve+i%2]}{str(triangle[x][i])}*({standardForm[0]}**{x-i})*({standardForm[1]}**{i})")
        expanded += f"{symbols[(ve+(len(triangle[x])))%2]} {expander(standardForm[1], triangle[x][-2])}" if memX == x else f"{expander(standardForm[1], triangle[x][-2])})\N{SUPERSCRIPT MINUS}{superscript(str(1))}"
    # terms+=[lambda a,b: f"{standardForm[1]}**{triangle[x][-2]}".replace("a",str(a)).replace("b",str(b))]
    evaluatedTerms.append(f"{symbols[ve]}{standardForm[1]}**{triangle[x][-2]}")
    print(evaluatedTerms)
    print(f"({standardForm[0]} + {standardForm[1]}){superscript(str(memX))} = {expanded}")
    return lambda a,b: solve( "({} + {}){} = {}".format(a,b*co_factor,superscript(str(memX)),expanded.replace("a",str(a),1).replace("a",surround(str(a))).replace("b",surround(str(b)),len(triangle[x])-2).replace("b",str(b))),[eval(i.replace("a",str(a)).replace("b",str(b))) for i in evaluatedTerms],indent=len("({} + {}){} ".format(a,b,superscript(str(memX)))),symbol=symbols[ve])
    

equation = expansion(2) # expansion(n) => (a + b)**n , expansion(n,-1) => (a - b)**n , expansion(-n) => ((a + b)**n)**-1 
equation(-5,2)
# TODO: ()