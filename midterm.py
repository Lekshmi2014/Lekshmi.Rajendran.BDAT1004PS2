from tkinter import *
   
expression = "" 
  
class Calculator:
    def press(num): 
        global expression 
  
        expression = expression + str(num) 
  
        equation.set(expression) 
  
# Function to evaluate the final expression 
    def equalpress(): 
 
        try: 
  
            global expression 

            total = str(eval(expression)) 
  
            equation.set(total) 

            expression = "" 

        except: 
  
            equation.set(" error ") 
            expression = "" 

    def clear(): 
        global expression 
        expression = "" 
        equation.set("") 
 
    if __name__ == "__main__": 
        # create a GUI window 
        gui = Tk() 
  
        gui.configure(background="light green") 
  
        gui.title("Simple Calculator") 

        gui.geometry("700x178") 
        equation = StringVar() 
        expression_field = Entry(gui, textvariable=equation) 
 
        expression_field.grid(columnspan=4, ipadx=60) 
  
        equation.set('enter your expression') 
  
        # create a Buttons and place at a particular 
        # location inside the root window . 
        # when user press the button, the command or 
        # function affiliated to that button is executed . 
        buttonMC = Button(gui, text=' MC ', fg='black', 
                     command=lambda: press('MC'), height=1, width=7) 
        buttonMC.grid(row=2, column=0) 
  
        buttonM = Button(gui, text=' M+ ', fg='black', 
                     command=lambda: press('M+'), height=1, width=7) 
        buttonM.grid(row=2, column=1) 
  
        buttonm = Button(gui, text=' M- ', fg='black', 
                     command=lambda: press('M-'), height=1, width=7) 
        buttonm.grid(row=2, column=2) 
  
        clear = Button(gui, text=' C ', fg='black', 
                   command=clear, height=1, width=7)
        clear.grid(row=3, column=0) 
  
        buttonroot = Button(gui, text=' √ ', fg='black', 
                     command=lambda: press('√'), height=1, width=7) 
        buttonroot.grid(row=3, column=1) 
  
        buttonSq = Button(gui, text=' x^2', fg='black', 
                     command=lambda: press('x^2'), height=1, width=7) 
        buttonSq.grid(row=3, column=2) 
  
        button7 = Button(gui, text=' 7 ', fg='black', 
                     command=lambda: press(7), height=1, width=7) 
        button7.grid(row=4, column=0) 
  
        button8 = Button(gui, text=' 8 ', fg='black', 
                     command=lambda: press(8), height=1, width=7) 
        button8.grid(row=4, column=1) 
  
        button9 = Button(gui, text=' 9 ', fg='black', 
                     command=lambda: press(9), height=1, width=7) 
        button9.grid(row=4, column=2) 
  
        button4 = Button(gui, text=' 4 ', fg='black', 
                     command=lambda: press(4), height=1, width=7) 
        button4.grid(row=5, column=0) 
  
        MR = Button(gui, text=' MR ', fg='black', 
                  command=lambda: press("MR"), height=1, width=7) 
        MR.grid(row=2, column=3) 
  
        plus = Button(gui, text=' + ', fg='black', 
                   command=lambda: press("+"), height=1, width=7) 
        plus.grid(row=3, column=3) 
  
        minus = Button(gui, text=' - ', fg='black', 
                      command=lambda: press("-"), height=1, width=7) 
        minus.grid(row=4, column=3) 
  
        multi = Button(gui, text=' * ', fg='black', 
                    command=lambda: press("*"), height=1, width=7) 
        multi.grid(row=5, column=3) 
  
        button6 = Button(gui, text=' 6 ', fg='black', 
                     command=lambda: press(6), height=1, width=7) 
        button6.grid(row=5, column=2) 
  
        button5 = Button(gui, text=' 5 ', fg='black', 
                     command=lambda: press(5), height=1, width=7) 
        button5.grid(row=5, column='1') 
  
        Button1= Button(gui, text='1', fg='black', 
                    command=lambda: press(1), height=1, width=7) 
        Button1.grid(row=6, column=0) 
        Button2= Button(gui, text='2', fg='black', 
                    command=lambda: press(2), height=1, width=7) 
        Button2.grid(row=6, column=1) 
        Button3= Button(gui, text='3', fg='black', 
                    command=lambda: press(3), height=1, width=7) 
        Button3.grid(row=6, column=2) 
        Divide= Button(gui, text='/', fg='black', 
                    command=lambda: press('/'), height=1, width=7) 
        Divide.grid(row=6, column=3) 
        Button0= Button(gui, text='0', fg='black', 
                    command=lambda: press(0), height=1, width=7) 
        Button0.grid(row=7, column=0) 
        Point= Button(gui, text='.', fg='black', 
                    command=lambda: press('.'), height=1, width=7) 
        Point.grid(row=7, column=1) 
        ButtonPM= Button(gui, text='+-', fg='black', 
                    command=lambda: press('+-'), height=1, width=7) 
        ButtonPM.grid(row=7, column=2) 
        ButtonEQ= Button(gui, text='=', fg='black', 
                    command=lambda: press('='), height=1, width=7) 
        ButtonEQ.grid(row=7, column=3) 
    
        # start the GUI 
        gui.mainloop() 
        
code = Calculator()