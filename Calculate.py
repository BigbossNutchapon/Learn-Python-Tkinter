from tkinter import*
from tkinter.font import BOLD

root = Tk()
root.title("เครื่องคิดเลข")
img = PhotoImage(file='C:\\Users\\nutch\\OneDrive\\เอกสาร\\summer sf210\\Midterm\\calculator.png')
root.iconphoto(False,img)
root.configure(bg="#fff")
root.geometry("485x690+500+30")
#content เก็บสมการ
content = ""
#txt นำสมการมาใช้งานหรือแสดงผล และผูกกับวิดเจต
txt_input = StringVar(value="0")


def btn(number):
    global content
    content = content +str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = (eval(content))
    if type(calculate) == float:
        txt_input.set(float(calculate))
    elif type(calculate) == int:
        txt_input.set(int(calculate))
    content = ""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")

# แสดงผล 5*4
display = Entry(font=('arial',32,BOLD),textvariable=txt_input,justify="right")
display.grid(columnspan=4,pady=15)

#รับค่าผ่านปุ่ม
#row1
btn7 = Button(text="7",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(7))
btn7.grid(row=1,column=0)
btn8 = Button(text="8",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(8))
btn8.grid(row=1,column=1)
btn9 = Button(text="9",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(9))
btn9.grid(row=1,column=2)
btnC = Button(text="C",fg="black",font=('arial',30,BOLD),padx=28,pady=19,command=clear)
btnC.grid(row=1,column=3,pady=1)

#row2
btn4 = Button(text="4",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(4))
btn4.grid(row=2,column=0)
btn5 = Button(text="5",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(5))
btn5.grid(row=2,column=1)
btn6 = Button(text="6",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(6))
btn6.grid(row=2,column=2)
btnPlus = Button(text="+",fg="black",font=('arial',30,BOLD),padx=31,pady=19,command=lambda:btn("+"))
btnPlus.grid(row=2,column=3,pady=3)

#row3
btn1 = Button(text="1",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(1))
btn1.grid(row=3,column=0)
btn2 = Button(text="2",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(2))
btn2.grid(row=3,column=1)
btn3 = Button(text="3",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn(3))
btn3.grid(row=3,column=2)
btnMinus = Button(text="-",fg="black",font=('arial',30,BOLD),padx=36,pady=19,command=lambda:btn("-"))
btnMinus.grid(row=3,column=3,pady=3)

#row4
btn0 = Button(text="0",fg="black",font=('arial',30,BOLD),padx=33,pady=19,command=lambda:btn(0))
btn0.grid(row=4,column=1)
btndot = Button(text=".",fg="black",font=('arial',30,BOLD),padx=37,pady=19,command=lambda:btn("."))
btndot.grid(row=4,column=0)
btndivision = Button(text="\u00F7",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn("/"))
btndivision.grid(row=4,column=2)
btnmultiply = Button(text="\u00D7",fg="black",font=('arial',30,BOLD),padx=32,pady=19,command=lambda:btn("*"))
btnmultiply.grid(row=4,column=3,pady=3)

#row5
btnequal = Button(text="=",fg="black",font=('arial',30,BOLD),padx=90,pady=15,command=equal)
btnequal.grid(row=5,column=2,columnspan=2)
btnopen = Button(text="(",fg="black",font=('arial',30,BOLD),padx=35,pady=15,command=lambda:btn("("))
btnopen.grid(row=5,column=0)
btnclose = Button(text=")",fg="black",font=('arial',30,BOLD),padx=38,pady=15,command=lambda:btn(")"))
btnclose.grid(row=5,column=1,pady=3)
root.mainloop()