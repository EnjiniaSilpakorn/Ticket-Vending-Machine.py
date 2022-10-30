from ast import While
from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.title('Program Ticket vending machine')
GUI.geometry('500x650')
Stationcodes = ('จตุจักร', 'เสมียนนารี', 'บางเขน', 'ทุ่งสองห้อง', 'หลักสี่', 'การเคหะ', 'ดอนเมือง', 'หลักหก', 'รังสิต')
StationList=('สถานีจตุจักร','สถานีวัดเสมียนนารี','สถานีบางเขน','สถานีทุ่งสองห้อง','สถานีหลักสี่','สถานีการเคหะ','สถานีดอนเมือง','สถานีหลักหก','สถานีรังสิต')
Snames = StringVar(value=StationList)
price_ticket = {'จตุจักร':16, 'เสมียนนารี':19, 'บางเขน':20, 'ทุ่งสองห้อง':23, \
        'หลักสี่':27, 'การเคหะ':30, 'ดอนเมือง':33, 'หลักหก':42, 'รังสิต':45}

# Names of the gifts we can send
tickets = { 'around':'ตั๋วไปกลับ', 'oneway':'ตั๋วไปอย่างเดียว'}

# State variables
ticket = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()


def showPrice(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = Stationcodes[idx]
        name = StationList[idx]
        price = price_ticket[code]
        statusmsg.set("ราคาตั๋วไป %s (%s) คือ %d บาท" % (name, code, price))
    sentmsg.set('')


def selectticket(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = StationList[idx]
        sentmsg.set("ท่านเลือก %s ไปที่ %s" % (tickets[ticket.get()], name))


c = ttk.Frame(GUI, padding=(5, 5, 10, 200))
c.grid(column=0, row=0, sticky=(N,W,E,S))
GUI.grid_columnconfigure(0, weight=1)
GUI.grid_rowconfigure(0,weight=1)


lbox = Listbox(c, listvariable=Snames, height=0)
lbl = ttk.Label(c, text="เลือกชนิดตั๋วที่ต้องการ:")
g1 = ttk.Radiobutton(c, text=tickets['around'], variable=ticket, value='around')
g2 = ttk.Radiobutton(c, text=tickets['oneway'], variable=ticket, value='oneway')

selected = ttk.Button(c, text='Select ticket', command=selectticket, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=10, pady=0)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)

selected.grid(column=2, row=3, sticky=E)
sentlbl.grid(column=1, row=4, columnspan=2, sticky=N, pady=0, padx=5)
status.grid(column=0, row=5, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(0, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', showPrice)
lbox.bind('<Double-1>', selectticket)
GUI.bind('<Return>', selectticket)

# Colorize alternating lines of the listbox
for i in range(0,len(StationList),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# fired when users makes a change, we explicitly call showPopulation.
ticket.set('around')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
showPrice()
d = ttk.Frame(GUI, padding=(10, 0, 50, 120))
d.grid(column=0, row=1, sticky=(N,W,E,S))
GUI.grid_columnconfigure(1, weight=1)
GUI.grid_rowconfigure(1,weight=1)

L1=Label(d,text='โปรดเติมเงินตามช่องที่ต้องการ',font=(None,10)).grid(column=0, row=0,padx=10,pady=0, sticky=N)

L2=Label(d,text='เหรียญ 10 บาท จำนวน',font=(None,10)).grid(column=0, row=1,padx=10,pady=0, sticky=N)

C10=StringVar()
A0=ttk.Entry(d,textvariable=C10,font=(None,10)).grid(column=0, row=2,padx=10, sticky=N)

L3=Label(d,text='เหรียญ 5 บาท จำนวน',font=(None,10)).grid(column=0, row=3,padx=10, sticky=N)

C5=StringVar()
A1=ttk.Entry(d,textvariable=C5,font=(None,10)).grid(column=0, row=4,padx=10, sticky=N)

L4=Label(d,text='เหรียญ 1 บาท จำนวน',font=(None,10)).grid(column=0, row=5,padx=10, sticky=N)

C1=StringVar()
A2=ttk.Entry(d,textvariable=C1,font=(None,10)).grid(column=0, row=6,padx=10, sticky=N)
Tcoin=float()
Coin1=float()
Coin10=float()
Coin5=float()
Diff=float()
Diff1=float()
def coin():
    Coin10=float(C10.get())
    Coin5=float(C5.get())
    Coin1=float(C1.get())
    Tcoin=(Coin10*10)+(Coin5*5)+(Coin1*1)
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = Stationcodes[idx]
        price = price_ticket[code]

    messagebox.showinfo('จำนวนเงินของท่าน','จำนวนเงินของท่าน {} Bath'.format(Tcoin))
    messagebox.showinfo('ราคาตั๋วที่ท่านเลือก','ราคาตั๋วที่ท่านเลือก {} Bath'.format(price))
    Diff=price-Tcoin
    Diff1=Tcoin-price
    if Tcoin < price:
        messagebox.showinfo('กรุณาเพิ่มเงินให้เท่ากับราคาตั๋ว','กรุณาเพิ่มเงินจำนวน {} Bath'.format(Diff))
    elif Tcoin > price:
        messagebox.showinfo('กรุณายกเลิกเพื่อใส่เงินใหม่','ท่านใส่เงินเกินจำนวน {} Bath'.format(Diff1))
    else:
        messagebox.showinfo('รายการสำเร็จ','กรุณารับตั๋วเดินทาง ขอให้เดินทางโดยสวัสดิภาพ')

        
    
    
C0=ttk.Button(d,text='คำนวณ',command=coin).grid(column=1, row=0,padx=10,pady=0, sticky=N)


GUI.mainloop()