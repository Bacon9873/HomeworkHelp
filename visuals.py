from tkinter import *  # Needed
from functions import Functions  # Needed
from pyglet import font  # Needed
import random  # Needed

# Adds the various fonts to our library
font.add_file('./Assets/Digital Dream.ttf')
font.add_file('./Assets/Mukta-Regular.ttf')
font.add_file('./Assets/Anton-Regular.ttf')

# Create a class to store all of the dimentions we plan to use for the future


class Dimentions():
    # A class to store all dimentions that have to do with the window
    class window():
        width = 700
        height = 550

    class Buttons():
        borderThickness = 3
        font = ("Mukta", 13)

    class Text():
        class Title():
            font = ("Anton", 18)

        class Body():
            font = ("Mukta", 14)

    class Calculator():
        class View():
            width = 17
            font = ("Digital Dream", 20)

        class Buttons():
            width = 2
            height = 1


class Visuals():
    class Window():
        def start():
            # Create a tkinter window
            global window
            window = Tk()

            # Open window having dimensions of the variables below. Also adds header and all other perameters
            window.geometry(str(Dimentions.window.width) +
                            'x' + str(Dimentions.window.height))
            window.title("HomeworkHelp")
            window.iconbitmap('./Assets/Icon.ico')
            window.resizable(False, False)

        def clearWindow():
            for widgets in window.winfo_children():
                widgets.destroy()

    class Pages():
        def homePage():
            # Make a homepage using tkinter that has a prompt for users to choose one of the HomeworkHelp options.
            Visuals.Window.clearWindow()

            # Adds a title to the window
            title = Label(window, text="Welcome! Please select one of the options to get started.",
                          font=Dimentions.Text.Title.font)
            title.pack()

            # Create a Button for the mathematics section
            mathButton = Button(window, text='Mathematics', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=Visuals.Pages.mathematics)
            historyButton = Button(window, text='History', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=Visuals.Pages.inProgress)

            # Instantiate the button with given peramiters
            mathButton.pack(pady=50)
            historyButton.pack()
            # Loop the window
            window.mainloop()

        def mathematics():
            Visuals.Window.clearWindow()
            # Open window having dimensions of the variables below. Also adds header and all other perameters

            # Creating a button that takes you back home
            homeButton = Button(window, text='Home', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.homePage))
            homeButton.pack(side="top", anchor=NW)

            # Adds a title to the window
            title = Label(window, text="Mathematics",
                          font=Dimentions.Text.Title.font)
            title.pack()

            # Create a Button for opening Factors Finder
            factorsFinderButton = Button(window, text='Factors Finder', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.inProgress))

            # Create a button for opening the calculator
            calculatorButton = Button(window, text='Calculator', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.calculator))

            pythagButton = Button(window, text='Pythagorean Theorem', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.pythag))

            # Instantiate the buttons with given perameters
            factorsFinderButton.pack(pady=50)
            calculatorButton.pack()
            pythagButton.pack(pady=50)

            # Loop the window
            window.mainloop()

        def inProgress():
            Visuals.Window.clearWindow()
            # Creating a button that takes you back home
            homeButton = Button(window, text='Home', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.homePage))
            homeButton.pack(side="top", anchor=NW)

            # Adds a title to the window
            title = Label(window, text="In Progress!",
                          font=Dimentions.Text.Title.font)
            title.pack()

        def calculator():
            Visuals.Window.clearWindow()

            # Functions for the calculator

            # Adds a character to the end of the view
            def addCharacter(character):
                view.config(state="normal")
                if not (len(view.get()) >= 16):
                    view.insert('end', character)
                view.config(state="readonly")

            # Clears any view (there's two clear functions because I'm too lazy to get rid of the other one)
            def clearAnyView(view):
                view.config(state='normal')
                view.delete(0, 'end')
                view.config(state="readonly")

            # Clears the view
            def clear():
                view.config(state="normal")
                view.delete(0, 'end')
                view.config(state="readonly")
                if answerView1.get() != '':
                    addStringToAView(answerView2, answerView1.get())
                clearAnyView(answerView1)

            # Makes sure that trig functions use radians or degrees
            isRadians = False

            def radiansOrDegrees(button: any):
                nonlocal isRadians

                if not isRadians:
                    button.config(text='Rad')
                    button.grid()
                    isRadians = True
                else:
                    button.config(text='Deg')
                    button.grid()
                    isRadians = False

            # Adds any string to any view
            def addStringToAView(view, itemToAdd: str):
                view.config(state='normal')
                view.delete(0, 'end')
                view.insert('end', itemToAdd)
                view.config(state='readonly')

            def addNewAnswer(answer):
                allowedLengthOfAnswer = 13
                answer = str(answer)
                if len(answer) > allowedLengthOfAnswer:
                    answer = answer[0:11] + "..."
                if not answerView1.get() == '':
                    addStringToAView(answerView2, answerView1.get())
                addStringToAView(answerView1, answer)

            def solveSimplifier(func, isRadians):
                try:
                    answer = func(view.get(), isRadians)
                except:
                    answer = "Error"

                return answer
            # Different ways of anwering

            class GetAnswer():
                # Equals is most optimized, works for most things
                def equals():
                    try:
                        answer = Functions.Calculator.solve(view.get())
                    except:
                        answer = "Error"
                    addNewAnswer(answer)
                # EqualsSqrt works well. Returns the sqrt of the equation in the view

                def equalsSqrt():
                    try:
                        answer = Functions.Calculator.squareRoot(view.get())
                    except:
                        answer = "Error"

                    # Moves the old answer to the view memory and adds the new answer
                    addNewAnswer(answer)

                # Returns the equation in the view to the sine function
                def equalsSine():
                    nonlocal isRadians
                    try:
                        answer = Functions.Calculator.sine(
                            view.get(), isRadians)
                    except:
                        answer = "Error"

                    # Moves the old answer to the view memory and adds the new answer
                    addNewAnswer(answer)

                def equalsCos():
                    nonlocal isRadians
                    answer = solveSimplifier(
                        Functions.Calculator.cosine, isRadians)

                    addNewAnswer(answer)

                def equalsTan():
                    nonlocal isRadians
                    answer = solveSimplifier(
                        Functions.Calculator.tan, isRadians)

                    addNewAnswer(answer)

                def equalsArcTan():
                    nonlocal isRadians
                    answer = solveSimplifier(
                        Functions.Calculator.arctan, isRadians)

                    addNewAnswer(answer)

                def equalsArcCos():
                    nonlocal isRadians
                    answer = solveSimplifier(
                        Functions.Calculator.arccos, isRadians)

                    addNewAnswer(answer)

                def equalsArcSin():
                    nonlocal isRadians
                    answer = solveSimplifier(
                        Functions.Calculator.arcsine, isRadians)

                    addNewAnswer(answer)

            # Deletes the last entered character on the view
            def delLast():
                view.config(state="normal")
                view.delete(len(view.get()) - 1, 'end')
                view.config(state="readonly")
                if answerView1.get() != '':
                    addStringToAView(answerView2, answerView1.get())
                clearAnyView(answerView1)

            # Changes the next entered character to either positive or negative

            def changePositiveNegative():
                view.config(state="normal")
                if len(view.get()) > 0:
                    last = view.get()[len(view.get()) - 1]
                else:
                    last = 'does not exist'
                if last == 'does not exist':
                    addCharacter('-')
                elif last == '-':
                    delLast()
                else:
                    addCharacter('(-')
                view.config(state="readonly")

            # Scientific calculator function
            isScientificCalcOn = False
            scientificCalcItems = []

            def scientificCalculator():
                nonlocal isScientificCalcOn
                nonlocal scientificCalcItems

                if not isScientificCalcOn:
                    # Defining buttons on the scientific calculator
                    exponentButton = Button(window, text='^', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('^')))
                    exponentButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    exponentButton.grid(row=6, column=5, sticky=NSEW)
                    scientificCalcItems.append(exponentButton)

                    factorialButton = Button(window, text='!', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('!')))
                    factorialButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    factorialButton.grid(row=7, column=5, sticky=NSEW)
                    scientificCalcItems.append(factorialButton)

                    sqrtButton = Button(window, text='√', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsSqrt))
                    sqrtButton.config(width=Dimentions.Calculator.Buttons.width,
                                      height=Dimentions.Calculator.Buttons.height)
                    sqrtButton.grid(row=6, column=4, sticky=NSEW)
                    scientificCalcItems.append(sqrtButton)

                    radiansDegreesButton = Button(window, text='Deg', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(lambda: radiansOrDegrees(radiansDegreesButton)))
                    radiansDegreesButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    radiansDegreesButton.grid(row=6, column=0, sticky=NSEW)
                    scientificCalcItems.append(radiansDegreesButton)

                    sineButton = Button(window, text='sin', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsSine))
                    sineButton.config(width=Dimentions.Calculator.Buttons.width,
                                      height=Dimentions.Calculator.Buttons.height)
                    sineButton.grid(row=6, column=1, sticky=NSEW)
                    scientificCalcItems.append(sineButton)

                    cosButton = Button(window, text='cos', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsCos))
                    cosButton.config(width=Dimentions.Calculator.Buttons.width,
                                     height=Dimentions.Calculator.Buttons.height)
                    cosButton.grid(row=6, column=2, sticky=NSEW)
                    scientificCalcItems.append(cosButton)

                    tanButton = Button(window, text='tan', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsTan))
                    tanButton.config(width=Dimentions.Calculator.Buttons.width,
                                     height=Dimentions.Calculator.Buttons.height)
                    tanButton.grid(row=6, column=3, sticky=NSEW)
                    scientificCalcItems.append(tanButton)

                    piButton = Button(window, text='π', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('π')))
                    piButton.config(width=Dimentions.Calculator.Buttons.width,
                                    height=Dimentions.Calculator.Buttons.height)
                    piButton.grid(row=7, column=4, sticky=NSEW)
                    scientificCalcItems.append(piButton)

                    arctanButton = Button(window, text='tan⁻¹', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsArcTan))
                    arctanButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    arctanButton.grid(row=7, column=3, sticky=NSEW)
                    scientificCalcItems.append(arctanButton)

                    arccosButton = Button(window, text='cos⁻¹', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsArcCos))
                    arccosButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    arccosButton.grid(row=7, column=2, sticky=NSEW)
                    scientificCalcItems.append(arccosButton)

                    arcsinButton = Button(window, text='sin⁻¹', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(GetAnswer.equalsArcSin))
                    arcsinButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    arcsinButton.grid(row=7, column=1, sticky=NSEW)
                    scientificCalcItems.append(arcsinButton)

                    infoButton = Button(window, text='Info', font=Dimentions.Buttons.font, bd=str(
                        Dimentions.Buttons.borderThickness), command=(Visuals.Pages.info))
                    infoButton.config(
                        width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
                    infoButton.grid(row=7, column=0, sticky=NSEW)
                    scientificCalcItems.append(infoButton)

                    isScientificCalcOn = True
                else:
                    isScientificCalcOn = False
                    Visuals.Pages.calculator()

            # Title
            title = Label(window, text="Calculator",
                          font=Dimentions.Text.Title.font)
            title.grid(row=0, column=5, sticky=NSEW, columnspan=3)
            # Back to previous page
            backButton = Button(window, text='Back', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.mathematics))
            backButton.grid(column=0, row=0, sticky=NW, pady=30)

            # View wherein you will type your numbers
            view = Entry(window, width=Dimentions.Calculator.View.width,
                         font=Dimentions.Calculator.View.font, justify='right')
            view.config(state="readonly")
            view.grid(row=1, column=0, columnspan=6, sticky=NSEW)

            equalsSign = Label(window, text="=", font=Dimentions.Buttons.font)
            equalsSign.grid(row=1, column=6, columnspan=1, sticky=NSEW)

            # View that shows the answer after clicking the equals sign
            answerView1 = Entry(window, width=Dimentions.Calculator.View.width,
                                font=Dimentions.Calculator.View.font, justify='left')
            answerView1.config(state="readonly")
            answerView1.grid(row=1, column=7, columnspan=6, sticky=NSEW)

            # Showing the past answers
            pastLabel = Label(window, text='Past Answer',
                              font=Dimentions.Buttons.font, justify='center')
            pastLabel.grid(row=2, column=9)

            answerView2 = Entry(window, width=Dimentions.Calculator.View.width,
                                font=Dimentions.Calculator.View.font, justify='left')
            answerView2.config(state="readonly")
            answerView2.grid(row=3, column=7, columnspan=6, sticky=NSEW)

            # Buttons for the calculator
            solveButton = Button(window, text='=', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(GetAnswer.equals))
            solveButton.config(width=Dimentions.Calculator.Buttons.width,
                               height=Dimentions.Calculator.Buttons.height*2)
            solveButton.grid(row=5, column=4, columnspan=2,
                             rowspan=1, sticky=NSEW)

            sciButton = Button(window, text='Sci', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(scientificCalculator))
            sciButton.config(width=Dimentions.Calculator.Buttons.width,
                             height=Dimentions.Calculator.Buttons.height*2)
            sciButton.grid(row=3, column=0, rowspan=2, sticky=NSEW)

            delButton = Button(window, text='Del', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(delLast))
            delButton.config(width=Dimentions.Calculator.Buttons.width,
                             height=Dimentions.Calculator.Buttons.height)
            delButton.grid(row=5, column=0, rowspan=1, sticky=NSEW)

            clearButton = Button(window, text='C', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(clear))
            clearButton.config(width=Dimentions.Calculator.Buttons.width,
                               height=Dimentions.Calculator.Buttons.height)
            clearButton.grid(row=2, column=0, columnspan=1, sticky=NSEW)

            oneButton = Button(window, text='1', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(1)))
            oneButton.config(width=Dimentions.Calculator.Buttons.width,
                             height=Dimentions.Calculator.Buttons.height)
            oneButton.grid(row=2, column=1, columnspan=1, sticky=NSEW)

            twoButton = Button(window, text='2', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(2)))
            twoButton.config(width=Dimentions.Calculator.Buttons.width,
                             height=Dimentions.Calculator.Buttons.height)
            twoButton.grid(row=2, column=2, sticky=NSEW)

            threeButton = Button(window, text='3', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(3)))
            threeButton.config(width=Dimentions.Calculator.Buttons.width,
                               height=Dimentions.Calculator.Buttons.height)
            threeButton.grid(row=2, column=3, sticky=NSEW)

            fourButton = Button(window, text='4', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(4)))
            fourButton.config(width=Dimentions.Calculator.Buttons.width,
                              height=Dimentions.Calculator.Buttons.height)
            fourButton.grid(row=3, column=1, sticky=NSEW)

            fiveButton = Button(window, text='5', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(5)))
            fiveButton.config(width=Dimentions.Calculator.Buttons.width,
                              height=Dimentions.Calculator.Buttons.height)
            fiveButton.grid(row=3, column=2, sticky=NSEW)

            sixButton = Button(window, text='6', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(6)))
            sixButton.config(width=Dimentions.Calculator.Buttons.width,
                             height=Dimentions.Calculator.Buttons.height)
            sixButton.grid(row=3, column=3, sticky=NSEW)

            sevenButton = Button(window, text='7', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(7)))
            sevenButton.config(width=Dimentions.Calculator.Buttons.width,
                               height=Dimentions.Calculator.Buttons.height)
            sevenButton.grid(row=4, column=1, sticky=NSEW)

            eightButton = Button(window, text='8', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(8)))
            eightButton.config(width=Dimentions.Calculator.Buttons.width,
                               height=Dimentions.Calculator.Buttons.height)
            eightButton.grid(row=4, column=2, sticky=NSEW)

            nineButton = Button(window, text='9', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(9)))
            nineButton.config(width=Dimentions.Calculator.Buttons.width,
                              height=Dimentions.Calculator.Buttons.height)
            nineButton.grid(row=4, column=3, sticky=NSEW)

            zeroButton = Button(window, text='0', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(0)))
            zeroButton.config(width=Dimentions.Calculator.Buttons.width,
                              height=Dimentions.Calculator.Buttons.height)
            zeroButton.grid(row=5, column=1, sticky=NSEW)

            decimalButton = Button(window, text='.', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('.')))
            decimalButton.config(width=Dimentions.Calculator.Buttons.width,
                                 height=Dimentions.Calculator.Buttons.height)
            decimalButton.grid(row=5, column=2, sticky=NSEW)

            changePositiveNegativeButton = Button(window, text='+/-', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(changePositiveNegative))
            changePositiveNegativeButton.config(
                width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
            changePositiveNegativeButton.grid(row=5, column=3, sticky=NSEW)

            openBracketButton = Button(window, text='(', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('(')))
            openBracketButton.config(
                width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
            openBracketButton.grid(row=2, column=4, sticky=NSEW)

            closedBracketButton = Button(window, text=')', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter(')')))
            closedBracketButton.config(
                width=Dimentions.Calculator.Buttons.width, height=Dimentions.Calculator.Buttons.height)
            closedBracketButton.grid(row=2, column=5, sticky=NSEW)

            addButton = Button(window, text='+', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('+')))
            addButton.config(width=Dimentions.Calculator.Buttons.width,
                             height=Dimentions.Calculator.Buttons.height)
            addButton.grid(row=3, column=4, sticky=NSEW)

            minusButton = Button(window, text='-', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('-')))
            minusButton.config(width=Dimentions.Calculator.Buttons.width,
                               height=Dimentions.Calculator.Buttons.height)
            minusButton.grid(row=4, column=4, sticky=NSEW)

            multiplyButton = Button(window, text='×', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('*')))
            multiplyButton.config(width=Dimentions.Calculator.Buttons.width,
                                  height=Dimentions.Calculator.Buttons.height)
            multiplyButton.grid(row=3, column=5, sticky=NSEW)

            divideButton = Button(window, text='÷', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(lambda: addCharacter('/')))
            divideButton.config(width=Dimentions.Calculator.Buttons.width,
                                height=Dimentions.Calculator.Buttons.height)
            divideButton.grid(row=4, column=5, sticky=NSEW)

            window.mainloop()

        def info():
            Visuals.Window.clearWindow()
            backButton = Button(window, text='Back', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.calculator))
            backButton.pack(side="top", anchor=W)

            titleLabel = Label(window, text='Info',
                               font=Dimentions.Text.Title.font)
            titleLabel.pack(side="top")

            infoText = """
            Scientific buttons may be more prone to errors. Trig functions and square roots 
            are done on the items inside the view after they are evaluated. For 
            example, if you pressed the 'square root' button while '6 + 3' was inside the 
            view, your answer would be 3. This is because 6 + 3 is nine, and the square 
            root of nine is 3.\n\n
             - Daniel Markusson
            """

            infoLabel = Label(window, text=infoText,
                              font=Dimentions.Text.Body.font, justify="center")
            infoLabel.pack(padx=10)
            window.mainloop()

        def pythag():
            Visuals.Window.clearWindow()
            # A page that helps you solve for the Pythagorean theorem

            # Title for page
            title = Label(window, text="Solve Pythagorean Theorem",
                          font=Dimentions.Text.Title.font)
            title.grid(row=0, column=5, sticky=NSEW, columnspan=5)

            # Label showing the equation you plan on using
            equationLabel = Label(
                window, font=Dimentions.Buttons.font, text="Equation")
            equationLabel.grid(row=20, column=20, sticky=NSEW)
            # Functions

            # Clears any view
            def clearAnyView(view):
                view.config(state='normal')
                view.delete(0, 'end')
                view.config(state="readonly")

            # Showing which equation user plans on using
            _sideToSolveFor = 'a'

            def showEquation(sideToSolveFor):
                nonlocal aEntry
                nonlocal bEntry
                nonlocal cEntry
                nonlocal _sideToSolveFor
                # Variations
                if sideToSolveFor == 'a':
                    clearAnyView(aEntry)
                    clearAnyView(bEntry)
                    clearAnyView(cEntry)
                    # c^2 - b^2 = a^2
                    equationLabel.config(text="c² - b² = a²")
                    aEntry.config(state="readonly")
                    bEntry.config(state="normal")
                    cEntry.config(state="normal")

                    _sideToSolveFor = 'a'
                elif sideToSolveFor == 'b':
                    clearAnyView(aEntry)
                    clearAnyView(bEntry)
                    clearAnyView(cEntry)
                    # c² - a² = b²
                    equationLabel.config(text="c² - a² = b²")
                    aEntry.config(state="normal")
                    bEntry.config(state="readonly")
                    cEntry.config(state="normal")

                    _sideToSolveFor = 'b'
                else:
                    clearAnyView(aEntry)
                    clearAnyView(bEntry)
                    clearAnyView(cEntry)
                    # a² + b² = c²
                    equationLabel.config(text="a² + b² = c²")
                    aEntry.config(state="normal")
                    bEntry.config(state="normal")
                    cEntry.config(state="readonly")

                    _sideToSolveFor = 'c'

            def addStringToAView(view, itemToAdd: str):
                view.config(state='normal')
                view.delete(0, 'end')
                view.insert('end', itemToAdd)
                view.config(state='readonly')

            def solve(sideToSolveFor: str):
                nonlocal aEntry
                nonlocal bEntry
                nonlocal cEntry

                aEntry.config(state="normal")
                bEntry.config(state="normal")
                cEntry.config(state="normal")
                if sideToSolveFor == 'a':
                    answer = Functions.Pythag.solveForA(
                        bEntry.get(), cEntry.get())
                    addStringToAView(aEntry, answer)
                elif sideToSolveFor == 'b':
                    answer = Functions.Pythag.solveForB(
                        aEntry.get(), cEntry.get())
                    addStringToAView(bEntry, answer)
                else:
                    answer = Functions.Pythag.solveForC(
                        aEntry.get(), bEntry.get())
                    addStringToAView(cEntry, answer)
                aEntry.config(state="readonly")
                bEntry.config(state="readonly")
                cEntry.config(state="readonly")
            # Back to previous page
            backButton = Button(window, text='Back', font=Dimentions.Buttons.font, bd=str(
                Dimentions.Buttons.borderThickness), command=(Visuals.Pages.mathematics))
            backButton.grid(column=0, row=0, sticky=NW, pady=10, padx=10)

            # Create a triangle in the center of the window to act as a visual for the function
            trianglePicture = PhotoImage(file='./Assets/Right Triangle.png')
            triangle = Label(window, image=trianglePicture,
                             width=250, height=250)
            triangle.grid(row=1, column=1, sticky=NSEW,
                          columnspan=10, rowspan=10)

            # a, b, and c labels for the user
            aLabel = Label(window, text='a', font=Dimentions.Buttons.font)
            aLabel.grid(row=7, column=0, sticky=E)

            bLabel = Label(window, text='b', font=Dimentions.Buttons.font)
            bLabel.grid(row=13, column=6, sticky=W, pady=7)

            cLabel = Label(window, text='c', font=Dimentions.Buttons.font)
            cLabel.grid(row=6, column=6, sticky=S)

            # Choosing which variant of the equation you plan on using
            solveForA = Button(window, text="Solve for a", font=Dimentions.Buttons.font, command=(
                lambda: showEquation('a')))
            solveForA.grid(row=19, column=5, sticky=NSEW)

            solveForB = Button(window, text="Solve for b", font=Dimentions.Buttons.font, command=(
                lambda: showEquation('b')))
            solveForB.grid(row=20, column=5, sticky=NSEW, pady=10)

            solveForC = Button(window, text="Solve for c", font=Dimentions.Buttons.font, command=(
                lambda: showEquation('c')))
            solveForC.grid(row=21, column=5, sticky=NSEW)

            # Entry points for the user to input their a, b, or c values
            entryWidth = 7

            # For a
            aEntryLabel = Label(window, text='a = ',
                                font=Dimentions.Buttons.font)
            aEntryLabel.grid(row=5, column=15, sticky=NSEW)

            aEntry = Entry(window, width=entryWidth,
                           font=Dimentions.Buttons.font)
            aEntry.config(state="readonly")
            aEntry.grid(column=16, row=5, sticky=NSEW)

            # For b
            bEntryLabel = Label(window, text='b = ',
                                font=Dimentions.Buttons.font)
            bEntryLabel.grid(row=6, column=15, sticky=NSEW)

            bEntry = Entry(window, width=entryWidth,
                           font=Dimentions.Buttons.font)
            bEntry.config(state="readonly")
            bEntry.grid(column=16, row=6, sticky=NSEW)

            # For c
            cEntryLabel = Label(window, text='c = ',
                                font=Dimentions.Buttons.font)
            cEntryLabel.grid(row=7, column=15, sticky=NSEW)

            cEntry = Entry(window, width=entryWidth,
                           font=Dimentions.Buttons.font)
            cEntry.config(state="readonly")
            cEntry.grid(column=16, row=7, sticky=NSEW)

            # Solve button
            solveButton = Button(window, text="Solve", font=Dimentions.Buttons.font, command=(
                lambda: solve(_sideToSolveFor)))
            solveButton.grid(column=16, row=8)

            window.mainloop()
