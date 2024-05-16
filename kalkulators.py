import numbers
from tkinter import*
Kalkulators=Tk()
import math
Kalkulators.title("Kalkulatora projekts")
Kalkulators.geometry("325x337")

def btnClick(number):
    current=e.get() #nolasa skaitli
    e.delete(0,END) 
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #  displejs
    return 0

def btnCommand(command):
    global number #skaitlis un darbība
    global num1 
    global mathOp
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

def Vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

btn0=Button(Kalkulators, text="0", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(0))
btn1=Button(Kalkulators, text="1", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(1))
btn2=Button(Kalkulators, text="2", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(2))
btn3=Button(Kalkulators, text="3", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(3))
btn4=Button(Kalkulators, text="4", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(4))
btn5=Button(Kalkulators, text="5", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(5))
btn6=Button(Kalkulators, text="6", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(6))
btn7=Button(Kalkulators, text="7", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(7))
btn8=Button(Kalkulators, text="8", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(8))
btn9=Button(Kalkulators, text="9", padx="30", pady="20",bg="aqua",bd=5,command=lambda:nospiestaPoga(9))

btnReiz=Button(Kalkulators, text="*", padx="30", pady="20", bg="blue",bd=5,command=lambda:btnCommand("*"))
btnSask=Button(Kalkulators, text="+", padx="30", pady="20",bg="blue",bd=5, command=lambda:btnCommand("+"))
btnDal=Button(Kalkulators, text="/", padx="30", pady="20",bg="blue",bd=5,command=lambda:btnCommand("/"))
btnMin=Button(Kalkulators, text="-", padx="30", pady="20",bg="blue",bd=5,command=lambda:btnCommand("-"))
btnC=Button(Kalkulators, text="C", padx="30", pady="20",bg="grey",bd=5,command=notirit)
btnVien=Button(Kalkulators, text="=", padx="30", pady="20",bg="grey",bd=5,command=Vienads)

btn0.grid(row=5, column=0)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btnReiz.grid(row=4, column=3)
btnSask.grid(row=3, column=3)
btnDal.grid(row=5, column=3)
btnMin.grid(row=1, column=3)
btnC.grid(row=5, column=1)
btnVien.grid(row=5, column=2)

e=Entry(Kalkulators, width=15, bd=10, font=("Arial Black",20), justify="center")
e.grid(row=0, column=0, columnspan=4)

Kalkulators.mainloop()