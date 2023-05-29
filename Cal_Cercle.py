
from tkinter import*


root = Tk()
root.title("โปรแกรมคำนวณพื้นที่วงกลม")

#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400")
Label(text="รัสมี",font=30).grid(row=0,sticky=W)
redius = IntVar()
et1 = Entry(width=30,font=30,textvariable=redius)
et1.grid(row=0,column=1)

Label(text="พื้นที่วงกลม",font=30).grid(row=1,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=1,column=1)

def calculate():
    et2.delete(0,END)
    r = redius.get()
    area = 3.14*r*r
    et2.insert(0,area)
def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

btn1 = Button(text="คำนวณ",command=calculate).grid(row=2,column=1,sticky=W)
btn2 = Button(text="ล้างค่า",command=deleteText).grid(row=2,column=1,sticky=E)

root.mainloop()