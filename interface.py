from tkinter import *
import math
class Calculator:
    '''Class to define the calculator and its layout'''
    def get_and_replace(self):
        ''' Replaces printable operators with machine readable ones'''
        self.expression = self.e.get()
        TRANS = self.expression.maketrans({
            '÷':'/','x':'*'
        })
        self.expression.translate(TRANS)

    def compute(self):
        ''' Compute equation on pressing the equals button'''
        self.get_and_replace()
        try:
            #Use built in function eval() to evaluate function
            self.value = eval(self.expression)
        except:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

    def square_root(self):
        ''' Method to find square-root '''
        self.get_and_replace()
        try:
            # USe build in function to evaluate the expression
            self.value = eval(self.expression)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.sqrt_val = math.sqrt(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.sqrt_val)

    def __init__(self,master):
        """ Constructor method """
        master.title('Calculator')
        master.geometry()
        self.e = Entry(master) # Input Field
        self.e.grid(row=0,column=0,columnspan=6,pady=3)
        self.e.focus_set() #Sets focus on the input field

        #Generating buttons
        Button(master,text='=',width=11,height=3).grid(row=4,column=4,columnspan=2)
        Button(master,text='AC',width=5,height=3).grid(row=1,column=4)
        Button(master,text='C',width=5,height=3).grid(row=1, column=4)

root = Tk()
obj = Calculator(root)
root.mainloop()

