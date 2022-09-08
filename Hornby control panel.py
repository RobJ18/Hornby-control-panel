from tkinter import *

background=Tk()

## Setting background parameters
background.title('Hornby control panel')
background.geometry("600x250")
c=Canvas(background, bg='black', height=480,width=270)
filename=PhotoImage(file="IMG_20200130_145200.png")
background_label=Label(background,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

## Display and setting parameters for the text at the top of the window
lbl=Label(background, text="Hornby control panel", fg='#FFF700', bg='Red', font=('arial', 20))
lbl.pack(side=TOP, anchor=NW)

Entry_Frame = Frame(background, bg='green')
Entry_Frame.pack(side=BOTTOM, anchor=SW, pady=15, padx=15)

##Point functions
def clickp1():
    print('P1')
def clickp2():
    print('P2')
def clickp3():
    print('P3')
def clickp4():
    print('P4')

##Lighting functions
def clickl1():
    print('l1')
def clickl2():
    print('l2')
def clickl3():
    print('l3')
def clickl4():
    print('l4')

##Sidings live, true ot false
def clicks1():
    print('s1')
def clicks2():
    print('s2')
def clicks3():
    print('s3')
def clicks4():
    print('s4')

#Buttons for switching points
lbl1=Label(Entry_Frame, text="Points", fg='Black', bg='green', font=('arial', 13))
btnp1=Button(Entry_Frame, text='Points 1', bg='gray', fg='#000000', command=clickp1)
btnp2=Button(Entry_Frame, text='Points 2', bg='gray', fg='#000000', command=clickp2)
btnp3=Button(Entry_Frame, text='Points 3', bg='gray', fg='#000000', command=clickp3)
btnp4=Button(Entry_Frame, text='Points 4', bg='gray', fg='#000000', command=clickp4)

#Buttons for switching lights
lbl2=Label(Entry_Frame, text="Lights", fg='Black', bg='green', font=('arial', 13))
btnl1=Button(Entry_Frame, text='Lights 1', bg='gray', fg='#000000', command=clickl1)
btnl2=Button(Entry_Frame, text='Lights 2', bg='gray', fg='#000000', command=clickl2)
btnl3=Button(Entry_Frame, text='Lights 3', bg='gray', fg='#000000', command=clickl3)
btnl4=Button(Entry_Frame, text='Lights 4', bg='gray', fg='#000000', command=clickl4)

#Buttons for making sidings live
lbl3=Label(Entry_Frame, text="Sidings", fg='Black', bg='green', font=('arial', 13))
btns1=Button(Entry_Frame, text='Siding 1', bg='gray', fg='#000000', command=clicks1)
btns2=Button(Entry_Frame, text='Siding 2', bg='gray', fg='#000000', command=clicks2)
btns3=Button(Entry_Frame, text='Siding 3', bg='gray', fg='#000000', command=clicks3)
btns4=Button(Entry_Frame, text='Siding 4', bg='gray', fg='#000000', command=clicks4)

#Adding points buttons to grid
lbl1.grid(row=0, column=1, pady=3, padx=20)
btnp1.grid(row=1, column=1, pady=1, padx=5)
btnp2.grid(row=2, column=1, pady=1, padx=5)
btnp3.grid(row=3, column=1, pady=1, padx=5)
btnp4.grid(row=4, column=1, pady=1, padx=5)

#Adding lights buttons to grid
lbl2.grid(row=0, column=2, pady=3, padx=20)
btnl1.grid(row=1, column=2, pady=1, padx=5)
btnl2.grid(row=2, column=2, pady=1, padx=5)
btnl3.grid(row=3, column=2, pady=1, padx=5)
btnl4.grid(row=4, column=2, pady=1, padx=5)

#Make sidings live
lbl3.grid(row=0, column=3, pady=3, padx=20)
btns1.grid(row=1, column=3, pady=1, padx=5)
btns2.grid(row=2, column=3, pady=1, padx=5)
btns3.grid(row=3, column=3, pady=1, padx=5)
btns4.grid(row=4, column=3, pady=1, padx=5)

background.mainloop()