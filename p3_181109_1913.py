from tkinter import *
 
def addItem():
    lbox.insert(END, entry.get())
    entry.delete(0, END)
 
def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)
 
def saveList():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(lbox.get(0, END)))
    f.close()
 
root = Tk()
 
lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)
 
f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
badd = Button(f, text="Add", command=addItem)
badd.pack(fill=X)
bdel = Button(f, text="Delete", command=delList)
bdel.pack(fill=X)
bsave = Button(f, text="Save", command=saveList)
bsave.pack(fill=X)
 
root.mainloop()