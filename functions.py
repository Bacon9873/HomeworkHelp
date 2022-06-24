import math

# A function for the calculator that returns the final product (if possible)


class Functions():
    class Calculator():
        def solve(equation: str):
            new = equation
            for i in range(len(equation)):
                # Factorials
                if equation[i] == "!":
                    x = i
                    try:
                        if equation[i+1].isdigit():
                            return "Error"
                    except:
                        pass
                    while equation[i-1].isdigit() and x > 0 or x == 1:
                        x -= 1
                    newSubString = ""
                    for j in range(i - x):
                        newSubString += equation[x + j]
                    new = new.replace(newSubString + '!',
                                      str(math.factorial(int(newSubString))))

            # Exponents
            new = new.replace('^', '**')

            # Pi
            new = new.replace('π', '3.14159265359')

            return eval(new)

        def squareRoot(equation: str):
            new = float(Functions.Calculator.solve(equation))
            try:
                return math.sqrt(int(new))
            except:
                return "Error"

        # Solves the sine function for the equation given
        def sine(equation: str, isRadians: bool):
            new = float(Functions.Calculator.solve(equation))
            try:
                if isRadians:
                    answer = math.sin(int(new))
                else:
                    answer = math.sin(math.radians(int(new)))
            except:
                answer = "Error"
            return answer

        def cosine(equation: str, isRadians: bool):
            new = float(Functions.Calculator.solve(equation))
            try:
                if isRadians:
                    answer = math.cos(new)
                else:
                    answer = math.cos(math.radians(new))
            except:
                answer = "Error"

            return answer

        def tan(equation: str, isRadians: bool):
            new = float(Functions.Calculator.solve(equation))
            try:
                if isRadians:
                    answer = math.tan(new)
                else:
                    answer = math.tan(math.radians(new))
            except:
                answer = "Error"

            return answer

        def arcsine(equation: str, isRadians: bool):
            new = float(Functions.Calculator.solve(equation))
            try:
                if isRadians:
                    answer = math.asin(new)
                else:
                    answer = math.degrees(math.asin(new))
            except:
                answer = "Error"

            return answer

        def arccos(equation: str, isRadians: bool):
            new = float(Functions.Calculator.solve(equation))
            try:
                if isRadians:
                    print(new)
                else:
                    print(new)
                    answer = math.degrees(math.acos(new))
            except:
                answer = "Error"

            return answer

        def arctan(equation: str, isRadians: bool):
            new = float(Functions.Calculator.solve(equation))
            try:
                if isRadians:
                    answer = math.atan(new)
                else:
                    answer = math.degrees(math.atan(new))
            except:
                answer = "Error"

            return answer

    class Pythag():
        def solveForA(b, c):
            try:
                a = math.sqrt(float(c)**2 - float(b)**2)
            except:
                a = "Error"
            return a

        def solveForB(a, c):
            try:
                b = math.sqrt(float(c)**2 - float(a)**2)
            except:
                b = "Error"
            return b

        def solveForC(a, b):
            try:
                c = math.sqrt(float(a)**2 + float(b)**2)
            except:
                c = "Error"
            return c
