from tkinter import *

raizPrincipal=Tk()                                      #Se crea la raíz que es la ventana principal.
raizPrincipal.config(bg="#e7593b")
                     
framePrincipal=Frame()                                  #Se crea un frame que es donde se colocan todos los widgets que queremos
framePrincipal.pack(expand=True, fill="both")
framePrincipal.config(bg="#83EB53")

global contador
contador=1


def crearVentana(numerolineas):
    vacio = Label(framePrincipal, text= "",anchor="center", bg="#83EB53")    #Creamos etiquetas vacias arriba y abajo de todo para dejar márgenes.
    vacio.grid(row=int(numerolineas+1),column=1,padx=20,pady=20)
    vacio1 = Label(framePrincipal, text= "",anchor="center", bg="#83EB53")
    vacio1.grid(row=0,column=1,padx=20,pady=20)
    framePrincipal.grid_columnconfigure(1,weight = 1)      #Hacemos esto para que al expandir la pantalla los elementos se mantengan centrados.
    framePrincipal.grid_rowconfigure(int(numerolineas+1),weight = 1)
    framePrincipal.grid_rowconfigure(0,weight = 1)

    
def clear():                                        #Definimos una función para borrar todo lo que haya en pantalla
    list = framePrincipal.grid_slaves()             #Buscamos todos los elementos que están ordenados en el grid
    for l in list:  
        l.destroy()                                 #Los destruimos
    
#def guardar_archivo(entradaNombreTexto):
#    new_file = open(entradaNombreTexto.get() + ".txt", "w")
def guardarFlashcard(pregunta,respuesta,boton):
    global contador
    global archivo
    question = pregunta.get()
    answer = respuesta.get()
    answer.lower()
    archivo.write(question + ":" + answer+"\n")
    contador += 1
    pregunta.delete(0,1000)
    respuesta.delete(0,1000)
    boton.destroy()
        
    

def ultimaFlashcard(pregunta,respuesta):
    global archivo
    question = pregunta.get()
    answer = respuesta.get()
    answer.lower()
    archivo.write(question + ":" + answer)
    clear()
    crearVentana(1)
    mensaje_final=Label(framePrincipal, text = "Gracias por usar nuestro programa")
    mensaje_final.grid(row=1,column=1)
    archivo.close()
    
    
        

def hacer_flashcards(entradaCartas):
    global contador
    numero = entradaCartas.get()
    clear()
    crearVentana(5)
    pregunta = Label(framePrincipal, text = "Ingrese la pregunta")
    pregunta.grid(row=1,column=1)
    entrada_pregunta = Entry(framePrincipal)
    entrada_pregunta.grid(row=2,column=1, pady=20)
    respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta")
    respuesta_correcta.grid(row=3,column=1)
    entrada_respuesta = Entry(framePrincipal)
    entrada_respuesta.grid(row=4,column=1, pady=20)
    
    for i in range (1,int(numero)+1): #contador < int(numero):
        boton_continuar = Button(framePrincipal, text="Continuar", command=lambda:guardarFlashcard(entrada_pregunta,entrada_respuesta,boton_continuar))
        boton_continuar.grid(row=5,column=1)
        
        
        
#        if 
#        contador += 1
    if contador == int(numero):
        list = framePrincipal.grid_slaves(5,1)             #Buscamos todos los elementos que están ordenados en el grid
        for l in list:  
            l.destroy()
            boton_finalizar = Button(framePrincipal, text="Finalizar", command=lambda:ultimaFlashcard(entrada_pregunta,entrada_respuesta))
            boton_finalizar.grid(row=5,column=1)
        
        
        
    

def ventana_cartas(entradaNombreTexto):
    global archivo
    archivo = open(entradaNombreTexto.get() + ".txt", "w")
    clear()
    crearVentana(3)
    pregunta1= Label(framePrincipal, text = "¿Cuántas cartas desea crear?")
    pregunta1.grid(row=1,column=1)
#    numeroflashcards= IntVar()
#    numeroflashcards=""
    entradaCartas = Entry(framePrincipal)#)
#    a = numeroflashcards
    entradaCartas.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar", command=lambda:hacer_flashcards(entradaCartas))
    continuar.grid(row=3,column=1)
#    if int(entradaCartas.get()) <0:
#        raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo".format(num_of_cards))
#    for i in range(entradaCartas.get()):

          

def guardar_nombre_texto():
    clear()
    crearVentana(3)
    pregunta= Label(framePrincipal, text = "Por favor ingrese el nombre con el cual desea guardar el archivo: ")
    pregunta.grid(row=1,column=1)
    entradaNombreTexto= Entry(framePrincipal)
    entradaNombreTexto.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar",command=lambda:ventana_cartas(entradaNombreTexto))
    continuar.grid(row=3,column=1,pady=30)

def opcionFlashcards():
    guardar_nombre_texto()
    

def aver():
    clear()
#    guardar_nombre_texto()

    
def ventana_inicial():  
    crearVentana(5)
    saludo = Label(framePrincipal, text= "Bienvenidos a nuestro programa", cursor="dot")      
    saludo.grid(row=1,column=1,padx=20,pady=5)              #Creamos los textos que queremos mostrar y los ubicamos en la interfaz.
    saludo.config(font=("Comic Sans MS", 44))
    
    saludo1 = saludo = Label(framePrincipal, text= "Elige la opción que quieres usar")
    saludo1.grid(row=2,column=1, padx=10, pady=40,)
    saludo1.grid_columnconfigure(1,weight = 1)
    saludo1.grid_rowconfigure(1,weight = 1)
    
    botonFlashcard=Button(framePrincipal, text="Crear Flashcards",bg="black",fg="white",command=lambda: opcionFlashcards())    
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
