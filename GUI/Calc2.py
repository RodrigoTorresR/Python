
from Tkinter import *
import Pmw
class SLabel(Frame):
    """ SLabel defines a 2.sided label within a Frame. The left hand label has blue letters; the right
        has white letters.
    """
    def __init__(self, master, left1, right1):
        Frame.__init__(self, master,bg='gray40')
        self.pack(side=LEFT, expand=YES,fill=BOTH)
        Label(self,text=left1, fg='steelblue1',
              font=("arial",6,"bold"), width=5,bg='gray40').pack(side=LEFT,expand=YES,fill=BOTH)
        Label(self,text=right1,fg='white',font=("arial",6,"bold"),width=1,bg='gray40').pack(side=RIGHT,
              expand=YES,fill=BOTH)
class Key(Button):
    def __init__(self,master,font=('arial',8,'bold'),
                 fg='white',width=5,borderwidth=5, **kw):
        kw['font']=font
        kw['fg']=fg
        kw['width']=width
        kw['borderwidth']=borderwidth
        apply(Button.__init__, (self, master), kw)
        self.pack(side=LEFT, expand=NO, fill=NONE)
class Calculator(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,bg='gray40')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Tkinter Toolkit TT-42')
        self.mater.iconname('Tk-42')
        self.calcu=Evaluator()      #This is our evaluator
        self.buildCalculator()      #Build the widgets
        #This is an incomplete dictionary - a goo excercise!
        self.actionDict={'second':self.doThis, 'mode':self.doThis,
                         'delete':self.doThis, 'alpha':self.doThis,
                         'stat':self.doThis, 'math':self.doThis,
                         'matrix':self.doThis, 'program':self.doThis,
                         'vars':self.doThis, '':self.doThis,
                         'sin':self.doThis, 'program':self.doThis,
                         'tan':self.doThis, 'up':self.doThis,
                         'X1':self.doThis, 'X2':self.doThis,
                         'log':self.doThis, 'ln':self.doThis,
                         'store':self.doThis, 'off':self.doThis,
                         'neg':self.doThis, 'enter':self.doThis,
                         }
        self.current=" "
    def doThis(self,action):
        print ('"%s" has not been impmented' % action)
    def tunoff(self, *args):
        self.quit()
    def clearall(self, *args):
        self.current=" "
        self.display.component('text').delete(1.0,END)
    def doEnter(self, *args):
        self.display.insert(END, '\n')
        result=self.calc.runpython(self.current)
        if result:
            self.display.insert(END, '%s\n', % result, 'ans')
        self.current=" "
    def dokeypress(self, event):
        key=event.char
        if key != '\b':
            self.current=self.current+key
        else:
            self.current=self.current[:-1]
    def keyAction(self, key):
        self.display.insert(END, key)
        self.current=self.current+key
    def evalAction(self,action):
        try:
            self.actionDict[action](action)
        except keyError:
            pass
        
