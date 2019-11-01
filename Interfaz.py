from tkinter import *

raizPrincipal=Tk()                                      #Se crea la raíz que es la ventana principal.
raizPrincipal.config(bg="#e7593b")
                     
framePrincipal=Frame()                                  #Se crea un frame que es donde se colocan todos los widgets que queremos
framePrincipal.pack(expand=True, fill="both")
framePrincipal.config(bg="orange")

def crearVentana(numerolineas):
    vacio = Label(framePrincipal, text= "",anchor="center", bg="orange")    #Creamos etiquetas vacias arriba y abajo de todo para dejar márgenes.
    vacio.grid(row=int(numerolineas),column=1,padx=20,pady=20)
    vacio1 = Label(framePrincipal, text= "",anchor="center", bg="orange")
    vacio1.grid(row=0,column=1,padx=20,pady=20)
    framePrincipal.grid_columnconfigure(1,weight = 1)      #Hacemos esto para que al expandir la pantalla los elementos se mantengan centrados.
    framePrincipal.grid_rowconfigure(int(numerolineas),weight = 1)
    framePrincipal.grid_rowconfigure(0,weight = 1)

    
def clear():
    list = framePrincipal.grid_slaves()
    for l in list:
        l.destroy()
    
#def guardar_archivo(entradaNombreTexto):
#    new_file = open(entradaNombreTexto.get() + ".txt", "w")
    
def ventana_cartas(entradaNombreTexto,pregunta,continuar):
    new_file = open(entradaNombreTexto.get() + ".txt", "w")
    pregunta.destroy()
    entradaNombreTexto.destroy()
    continuar.destroy()
    pregunta1= Label(framePrincipal, text = "¿Cuántas cartas desea crear?")
    pregunta1.grid(row=1,column=1)
    entradaCartas = Entry(framePrincipal)
    entradaCartas.grid(row=2,column=1, pady=20)
    if int(entradaCartas.get()) <0:
        raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo".format(num_of_cards))
#    for i in range(entradaCartas.get()):

          

def guardar_nombre_texto():
    pregunta= Label(framePrincipal, text = "Por favor ingrese el nombre con el cual desea guardar el archivo: ")
    pregunta.grid(row=1,column=1)
    entradaNombreTexto= Entry(framePrincipal)
    entradaNombreTexto.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar",command=ventana_cartas(entradaNombreTexto,pregunta,continuar))
    continuar.grid(row=3,column=1,pady=30)

def aver():
    clear()
#    guardar_nombre_texto()

    
def ventana_inicial():  
    crearVentana(6)
    saludo = Label(framePrincipal, text= "Bienvenidos a nuestro programa", cursor="dot")      
    saludo.grid(row=1,column=1,padx=20,pady=5)              #Creamos los textos que queremos mostrar y los ubicamos en la interfaz.

    saludo1 = saludo = Label(framePrincipal, text= "Elige la opción que quieres usar")
    saludo1.grid(row=2,column=1, padx=10, pady=40,)
    saludo1.grid_columnconfigure(1,weight = 1)
    saludo1.grid_rowconfigure(1,weight = 1)
    
    botonFlashcard=Button(framePrincipal, text="Crear Flashcards",bg="black",fg="white",command=aver)    
    botonFlashcard.grid(row=3,column=1,pady=8)              #Creamos los botones para que al pulsarlos el programa realice lo pertienente.
    
    botonQuiz=Button(framePrincipal, text="Crear un Quizz")
    botonQuiz.grid(row=4,column=1,pady=8)
    
    botonRepasar=Button(framePrincipal, text="Repasar flashcards")
    botonRepasar.grid(row=5,column=1,pady=8)

#vacio = Label(framePrincipal, text= "",anchor="center", bg="orange")    #Creamos etiquetas vacias arriba y abajo de todo para dejar márgenes.
#vacio.grid(row=6,column=1,padx=20,pady=20)
#
#vacio1 = Label(framePrincipal, text= "",anchor="center", bg="orange")
#vacio1.grid(row=0,column=1,padx=20,pady=20)
#
#framePrincipal.grid_columnconfigure(1,weight = 1)      #Hacemos esto para que al expandir la pantalla los elementos se mantengan centrados.
#framePrincipal.grid_rowconfigure(6,weight = 1)
#framePrincipal.grid_rowconfigure(0,weight = 1)

ventana_inicial()
raizPrincipal.mainloop()

