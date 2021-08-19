from tkinter import*

window = Tk()

window.title('Python Calculator')

window.geometry('355x475')

window.configure(bg = 'black')

window.iconbitmap('icon.ico')

#lock window size, window.resizable(width = False, height = False) or window.resizable(width = False, False) or window.resizable(False, False)
window.resizable(width = False, height = False)


#functions for special buttons (clear, equal...)

#when user press button
expression = ''

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():

    global expression
    
    try:

        total = str(eval(expression))

        equation.set(total)

        expression = ''

    except:

        equation.set('*lol* dividing by zero :)')

        expression = ''

#function for the clear button
def clear():
    
    global expression

    expression = ''

    equation.set('0')

#create a frame inside the window
button_frame = Frame(window, bg = '#ffffff')
button_frame.pack()

#add entry box into the button frame, get text from user into textvariable
equation = StringVar()

#show number zero in the right side of the textfield
equation.set('0')

#align numbers in field to the right
expression_field = Entry(button_frame, textvariable = equation, justify = 'right', font = ('arial', 20, 'bold'))

#pack it
#expression_field.pack()

#create buttons, locate them in the button frame
button1 = Button(button_frame, text = '1', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(1))

button2 = Button(button_frame, text = '2', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(2))

button3 = Button(button_frame, text = '3', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(3))

addition = Button(button_frame, text = '+', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press('+'))

button4 = Button(button_frame, text = '4', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(4))

button5 = Button(button_frame, text = '5', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(5))

button6 = Button(button_frame, text = '6', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(6))

subtract = Button(button_frame, text = '-', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press('-'))

button7 = Button(button_frame, text = '7', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(7))

button8 = Button(button_frame, text = '8', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(8))

button9 = Button(button_frame, text = '9', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(9))

multiplication = Button(button_frame, text = '*', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press('*'))

button0 = Button(button_frame, text = '0', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press(0))

decimal = Button(button_frame, text = '.', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press('.'))

clear = Button(button_frame, text = 'C', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = clear)

division = Button(button_frame, text = '/', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 8, height = 3, command = lambda:press('/'))

equal = Button(button_frame, text = '=', font = ('times new roman', 12), relief = 'ridge', borderwidth = 1, bg = '#ffffff', width = 34, height = 3, command = equalpress)

#place the grid - cordinates 0 and 0 is top left, create separations (paddings) between text field and buttons)
expression_field.grid(row = 0, column = 0, columnspan = 4, ipadx = 8, ipady = 25, pady = 15)

button1.grid(row = 1, column = 0)

button2.grid(row = 1, column = 1)

button3.grid(row = 1, column = 2)

addition.grid(row = 1, column = 3)

button4.grid(row = 2, column = 0)

button5.grid(row = 2, column = 1)

button6.grid(row = 2, column = 2)

subtract.grid(row = 2, column = 3)

button7.grid(row = 3, column = 0)

button8.grid(row = 3, column = 1)

button9.grid(row = 3, column = 2)

multiplication.grid(row = 3, column = 3)

button0.grid(row = 4, column = 0)

decimal.grid(row = 4, column = 1)

clear.grid(row = 4, column = 2)

division.grid(row = 4, column = 3)

equal.grid(row = 5, column = 0, columnspan = 4)

window.mainloop()