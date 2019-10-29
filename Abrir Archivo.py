from tkinter import *
from tkinter import filedialog

root=Tk()
root.config(height=200)

def abreFichero():
    fichero= filedialog.askopenfilename(title="Abrir", initialdir="/", filetypes=(("Ficheros de Excel","*xlsx"),("Ficheros de texto","*txt"),("Todos los ficheros","*.*")))
    print(fichero)

Button(root,text="Abrir fichero", command=abreFichero). pack()

root.mainloop()