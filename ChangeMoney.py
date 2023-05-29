# 1บาทไทย = 0.026 EUR (ยูโร)
# 1บาทไทย = 3.486 JPY (เยน)
# 1บาทไทย = 0.031 USD (ดอลล่า)
# 1บาทไทย = 0.023 GBP (ปอนด์)

from tkinter import*
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400")
#ป้อนจำนวนเงินมา
money = IntVar()
Label(text="จำนวนเงิน",padx=10,font=30).grid(row=0,sticky=W)
et1 = Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

#เลือกว่าจะแปลงไปสกุลไหน
Label(text="เลือกสกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
choice = StringVar(value="โปรดเลือกสกุลเงิน")
combo = ttk.Combobox(width=28,font=30,textvariable=choice)
combo["values"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

#คำนวณผลรับออกมา
Label(text="ผลการคำนวณ",padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(font=30,width=30)
et2.grid(row=2,column=1)

#ปุ่มคำนวณ
def calculate():
    amount = money.get()
    currency = choice.get()

    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR(ยูโร)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*3.486),"JPY(เยน)")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = ((amount*0.031),"USD(ดอลล่า)")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount*0.023),"GBP(ปอนด์)")
        et2.insert(0,result)
    else:
        et2.delete(0,END)
        result = ("ไม่พบข้อมูล")
        et2.insert(0,result)
def deleteText():
    combo.delete(0,END)
    et1.delete(0,END)
    et2.delete(0,END)
Button(text="คำนวณ",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้างค่า",font=30,width=15,command=deleteText).grid(row=3,column=1,sticky=E)

root.mainloop()