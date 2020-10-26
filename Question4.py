from tkinter import *
class Mortgage(Frame):
    '''GUI for Mortgage class'''

    def __init__(self, parent = None):
        '''Thsi is to set the labels and entiers for Mortgage GUI'''
        Frame.__init__(self, parent)
        
        self.loanAmount = Label(self, font=('Times New Roman', 10, 'bold'), text='Loan Amount').grid(row=1, column=0)
        self.loanAmountEntry = Entry(self).grid(row=1, column=1, ipadx= 25, padx = 20)
        
        self.interestRate = Label(self, font=('Times New Roman', 10, 'bold'), text='Interest Rate').grid(row=2, column=0)
        self.interestRateEntry = Entry(self).grid(row=2, column=1, ipadx= 25, padx = 20)
        
        self.loanTerms = Label(self, font=('Times New Roman', 10, 'bold'), text='Loan Terms').grid(row=3, column=0)
        self.loanTermsEntry = Entry(self).grid(row=3, column=1, ipadx= 25, padx = 20)
        
        self.computeMortgage = Button(self, font=('Times New Roman', 10, 'bold'), text='Compute Mortgage').grid(row=4, column=0)
        self.computeMortgageEntry = Entry(self).grid(row=4, column=1, ipadx= 25, padx = 20)
        
class Calculator(Frame):
    '''GUI for Calculator class'''
    
    def __init__(self, parent = None):
        '''This sets up the calculator buttons'''
        Frame.__init__(self, parent)
        self.text = [['MC', 'M', 'M-', 'MR'],
                      ['C', '\u221a', 'x\u00b2', '+'],
                      ['1', '2', '3', '-'],
                      ['4', '5', '6', '*'],
                      ['7', '8', '9', '/'],
                      ['0', '.', '+-', '=']]
        #The number of rows
        for r in range(6):   
            #The number of columns
            for c in range(4):  
                #Button so users can feel like they are pressing buttons
                self.label = Button(self, relief=RAISED,    
                                    padx=15,
                                    text=self.text[r] [c], 
                                    font=('Times New Roman', 11), 
                                    width = 3, 
                                    bg = 'white')
                self.label.grid(row=r, column=c)

class Cscreen(Frame):
    '''Class for the screen above the calculator'''
    
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.screen = Text(self, width = 30, height = 2, bg = 'grey').grid(row=0)
        


class FullApp(Frame):
    '''Class to gather all the class into one'''
    
    def __init__(self, master):
        Frame.__init__(self, master)
        call1 = Mortgage(self)
        
        #align GUI to the left side
        call1.pack(side = LEFT)    
        call2 = Calculator(self)
        call2.pack(side = BOTTOM) 
        screen = Cscreen(self)
        screen.pack(side=TOP)

#root is an object of tkinter module 
tk = Tk() 
combineClass = FullApp(tk)
combineClass.pack()
#display the App
tk.mainloop()