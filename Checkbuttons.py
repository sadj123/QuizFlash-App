from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
mountain=IntVar()
turismo=IntVar()

def opcionesViaje():
    opcionEscogida=""
    
    if playa.get()==1:
        opcionEscogida+="playa"
    if mountain.get()==1:
        opcionEscogida+="montaña"
    if turismo.get()==1:
        opcionEscogida+="Turismo rural"
    
    textoFinal.config(text=opcionEscogida)
    
    


frame =Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50). pack()

Checkbutton(root, text = "Playa", variable = playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text = "Montaña",variable = mountain, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text = "Turismo rural", variable = turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()


root.mainloop()