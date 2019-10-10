import Decision_Tree as dt
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import pandas as pd
import numpy as np
import Association as ap

window = Tk()
window.geometry("1000x600")
window.title('Asscoiation')

#fn = StringVar()
# Catch event choose of OptionMenu
var = StringVar()
var1 = StringVar()
var2 = StringVar()
filename = 'null'
a, c, d = [], [], []


def prints():
    global a, c, d, filename, var1, var2
    filename = filename.replace('/', '\\')
    a, c, d = ap.association(filename, float(var1.get()), float(var2.get()))
    file = open("D:\\Work_Space\\Machine_Learning\\Decision_Tree\\plc.txt", "w")
    file.write('Tap pho bien :\n')
    for i in a:
        file.write(str(i)+'\n')
    file.write('\n=============================================\n')
    file.write('Tap pho bien toi dai :\n')
    for j in c:
        file.write(str(j)+'\n')
    file.write('\n=============================================\n')
    file.write('Tap luat : \n')
    for k in d:
        file.write(str(k)+'\n')
    file.write('\n=============================================\n')
    configfile = Text(window, wrap=WORD, width=45, height=40)
    configfile.place(x=0, y=0)
    file.close()
    with open('D:\\Work_Space\\Machine_Learning\\Decision_Tree\\plc.txt', 'r') as f:
        configfile.insert(INSERT, f.read())
    # print(a)
    # print(c)
    # print(d)
    # def predict():
    # def prints_get(event):
    #    print(var.get())


def upload_File():
    global filename
    filename = filedialog.askopenfilename()
    # print(type(filename))


    # Label
label = Label(window, text='Association Rule', fg='blue',
              bg='yellow', font=('arial', 16, 'bold')).pack()
# Entry
#entry = Entry(window, textvar=fn).place(x=240, y=242)

b1 = Button(window, text='Upload Data Train', width=20, bg='red', fg='white', command=upload_File)
b1.place(x=600, y=200)

b1 = Button(window, text='Train', width=10, bg='red', fg='white', command=prints)
b1.place(x=800, y=200)

label1 = Label(window, text='Min Support : ', font=('arial', 16, 'bold')).place(x=500, y=300)
entry1 = Entry(window, textvar=var1).place(x=700, y=305)
label2 = Label(window, text='Min Confidence : ', font=('arial', 16, 'bold')).place(x=500, y=350)
entry2 = Entry(window, textvar=var2).place(x=700, y=355)

# label1 = Label(window, text='Min Support : ', font=('arial', 16, 'bold')).place(x=500, y=300)
# entry1 = Entry(window, textvar=var1).place(x=700, y=305)
# label2 = Label(window, text='Min Confidence : ', font=('arial', 16, 'bold')).place(x=500, y=350)
# entry2 = Entry(window, textvar=var2).place(x=700, y=355)
# Drop List
window.mainloop()
