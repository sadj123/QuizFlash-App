from tkinter import *
from tkinter import filedialog

raizPrincipal=Tk()                                                              #Se crea la raíz que es la ventana principal
raizPrincipal.config(bg="#e7593b")
raizPrincipal.title("FlashQuiz App")
                     
framePrincipal=Frame()                                                            #Se crea un frame que es donde se colocan todos los widgets que queremos
framePrincipal.pack(expand=True, fill="both")
framePrincipal.config(bg="#83EB53", height=800)

global contador
contador=1


def crearVentana(numerolineas):
    vacio = Label(framePrincipal, text= "",anchor="center", bg="#83EB53")        #Creamos etiquetas vacias arriba y abajo de todo para dejar márgenes.
    vacio.grid(row=int(numerolineas+1),column=1,padx=20,pady=20)
    vacio1 = Label(framePrincipal, text= "",anchor="center", bg="#83EB53")
    vacio1.grid(row=0,column=1,padx=20,pady=20)
    framePrincipal.grid_columnconfigure(1,weight = 1)                           #Hacemos esto para que al expandir la pantalla los elementos se mantengan centrados.
    framePrincipal.grid_rowconfigure(int(numerolineas+1),weight = 1)
    framePrincipal.grid_rowconfigure(0,weight = 1)

    
def clear():                                        #Definimos una función para borrar todo lo que haya en pantalla
    list = framePrincipal.grid_slaves()             #Buscamos todos los elementos que están ordenados en el grid
    for l in list:  
        l.destroy()                                 #Los destruimos
    
# A partir de aquí, el coódigo se lee de abajo hacia arriba, ya que como Python
# lee de abajo hacia arriba, al pulsar un botón, la función que va a ejecutar
# debe estar definida antes     
        
#En todos botones se utiliza siempre "lambda" para que la función que se quiera 
# ejcutar únicamente lo haga cuando se pulse el botón.
#---------------------- Hacer flashcards-----------------------------------------------------------
def guardarFlashcard(pregunta,respuesta,numero):
    global contador                                                             #La variable global contador que definimos en la función "Hacer F
    global archivo
    question = pregunta.get()
    answer = respuesta.get()
    answer.lower()
    archivo.write(question + ":" + answer+"\n")
    clear()
    contador += 1
    hacer_flashcards(numero)

def ultimaFlashcard(pregunta,respuesta):
    global archivo                                                              #Esta función guarda en el archivo de texto, la pregunta y seguido de dos puntos la repuesta.
    question = pregunta.get()                                                   #El .get nos permite recolectar la información que el usuario ha puesto en la entrada
    answer = respuesta.get()
    answer.lower()
    archivo.write(question + ":" + answer)
    clear()
    crearVentana(2)
    mensaje_final=Label(framePrincipal, text = "Gracias por usar nuestro programa",bg ="#83EB53")
    mensaje_final.grid(row=1,column=1)
    archivo.close()                                                            #Aquí se cierra el archivo
    cerrar_programa=Button(framePrincipal,text= "Cerrar", command = lambda:raizPrincipal.destroy())
    cerrar_programa.grid(row=2,column=1)                                        
    
def hacer_flashcards(numero_flashcards):                                        #Esta función crea la pantalla donde va a estar la pregunta y la respuesta de la flashcard
    global contador                                                             #La única diferencia en los if es que si todavía no es la última flashcard, el botón dice "Continuar" y cuando es la última el botón dice "Finalizar" y cierra el archivo.
    clear()
    if contador < int(numero_flashcards):
        crearVentana(6)
        textosuperior = StringVar()
        textosuperior.set("Flashcard "+ str(contador))
        arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#83EB53") 
        arriba.grid(row=1,column=1)
        pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#83EB53")
        pregunta.grid(row=2,column=1)
        entrada_pregunta = Entry(framePrincipal)
        entrada_pregunta.grid(row=3,column=1, pady=20)
        respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",bg ="#83EB53")
        respuesta_correcta.grid(row=4,column=1)
        entrada_respuesta = Entry(framePrincipal)
        entrada_respuesta.grid(row=5,column=1, pady=20)       
        boton_continuar = Button(framePrincipal, text="Continuar", command=lambda:guardarFlashcard(entrada_pregunta,entrada_respuesta,int(numero_flashcards)))
        boton_continuar.grid(row=6,column=1)
        
    if contador == int(numero_flashcards):
        crearVentana(6)
        pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#83EB53")
        pregunta.grid(row=2,column=1)
        entrada_pregunta = Entry(framePrincipal)
        entrada_pregunta.grid(row=3,column=1, pady=20)
        respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",bg ="#83EB53")
        respuesta_correcta.grid(row=4,column=1)
        entrada_respuesta = Entry(framePrincipal)
        entrada_respuesta.grid(row=5,column=1, pady=20)
        textosuperior = StringVar()
        textosuperior.set("Flashcard "+ str(contador))
        arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#83EB53") 
        arriba.grid(row=1,column=1)
        boton_finalizar = Button(framePrincipal, text="Finalizar", command=lambda:ultimaFlashcard(entrada_pregunta,entrada_respuesta))
        boton_finalizar.grid(row=6,column=1)
        
        

def ventana_cartas(entradaNombreTexto):
    global archivo                                                              #Se define una variable globsl, ya que tenemos que usarla y modificarla en distintas funciones.
    archivo = open(entradaNombreTexto.get() + ".txt", "w")                      #Se crea un archivo con el nombre que el usuario especificó
    clear()
    crearVentana(3)
    pregunta1= Label(framePrincipal, text = "¿Cuántas cartas desea crear?",bg ="#83EB53")
    pregunta1.grid(row=1,column=1)                                              #Se le pregunta al usuario cuántas flashcards desea crear
    entradaCartas = Entry(framePrincipal)
    entradaCartas.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar", command=lambda:hacer_flashcards(entradaCartas.get()))
    continuar.grid(row=3,column=1)

          
def opcionFlashcards():                                                         #Esta es la función que se ejecuta cuando se pulsa "Hacer flashcards" en la ventana principal
    clear()
    crearVentana(3)
    pregunta= Label(framePrincipal, text = "Por favor ingrese el nombre con el cual desea guardar el archivo: ",bg ="#83EB53")
    pregunta.grid(row=1,column=1)
    entradaNombreTexto= Entry(framePrincipal)                                   #En esta función se le pregunta al usuario cómo quiere guardar el archivo.
    entradaNombreTexto.grid(row=2,column=1, pady=20)                            #Consta de una Label y una entrada de texto que se recopila para guardar el archivo con ese nombre más adelante
    continuar = Button(framePrincipal, text="Continuar",command=lambda:ventana_cartas(entradaNombreTexto))
    continuar.grid(row=3,column=1,pady=30)

#-------------------------------Quiz-------------------------------------------------------
global counter_quiz                                                             #Se crea la variable global que nos ayudará a saber en que pregunta vamos
counter_quiz = 1

def guardarQuiz(pregunta,rc,ri_1,ri_2,ri_3,numero):                             #Esta función recolecta la información de las entradas y guarda la información en un archivo de texto.
    global counter_quiz
    global archivo_quiz
    question = pregunta.get()
    correcta = rc.get()
    incorrecta1 = ri_1.get()
    incorrecta2 = ri_2.get()
    incorrecta3 = ri_3.get()
    correcta.lower()                                                           # Con el .lower(), evitamos que haya problemas con las mayúsculas y minúsculas.
    incorrecta1.lower()
    incorrecta2.lower()
    incorrecta3.lower()
    archivo_quiz.write(question + ":" + correcta + ";" + incorrecta1 + ";" + incorrecta2 + ";" +incorrecta3 + "\n") 
    clear()
    counter_quiz += 1
    crear_quizzes(numero)
    
def ultimoQuiz(pregunta,rc,ri_1,ri_2,ri_3):                                     #Esta función recolecta la información de las entradas y las guarda en un archivo de texto.
    global archivo_quiz
    question = pregunta.get()
    correcta = rc.get()
    incorrecta1 = ri_1.get()
    incorrecta2 = ri_2.get()
    incorrecta3 = ri_3.get()
    correcta.lower()
    incorrecta1.lower()
    incorrecta2.lower()
    incorrecta3.lower()
    archivo_quiz.write(question + ":" + correcta + ";" + incorrecta1 + ";" + incorrecta2 + ";" +incorrecta3 + "\n")
    archivo_quiz.close()
    clear()
    crearVentana(2)
    mensaje_final=Label(framePrincipal, text = "Gracias por usar nuestro programa",bg ="#83EB53")
    mensaje_final.grid(row=1,column=1)
    cerrar_programa(framePrincipal,text="Cerrar programa", command = raizPrincipal.destroy())
    cerrr_programa.grid(row=2,column=1)
    
    
def crear_quizzes(numero_quizzes):
    global counter_quiz                                                         #Se tiene una variable global que  nos permite saber en qué pregunta vamos.
    clear()
    if counter_quiz < int(numero_quizzes):                                      #Se crea la pantalla con una entrada para la pregunta, una entrada para la pregunta correcta y tres entradas para las respuestas incorrectas.
        crearVentana(10)
        textosuperior = StringVar()                                            #Se declara una variable de texto
        textosuperior.set("Pregunta "+ str(counter_quiz))
        arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#83EB53") 
        arriba.grid(row=1,column=1)
        pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#83EB53")
        pregunta.grid(row=2,column=1)
        entrada_pregunta = Entry(framePrincipal)
        entrada_pregunta.grid(row=3, column=1)
        respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",pady=25,bg ="#83EB53")
        respuesta_correcta.grid(row=4,column=1)
        entrada_rcorrecta = Entry(framePrincipal)
        entrada_rcorrecta.grid(row=5,column=1)
        respuestas_incorrectas = Label(framePrincipal, text = "Ingrese 3 respuestas incorrectas",pady=25,bg ="#83EB53")
        respuestas_incorrectas.grid(row=6,column=1)
        entrada_rincorrecta1 = Entry(framePrincipal)
        entrada_rincorrecta1.grid(row=7,column=1,pady=10)
        entrada_rincorrecta2 = Entry(framePrincipal)
        entrada_rincorrecta2.grid(row=8,column=1)
        entrada_rincorrecta3 = Entry(framePrincipal)
        entrada_rincorrecta3.grid(row=9,column=1,pady = 10)
        boton_continuar = Button(framePrincipal, text="Continuar", command=lambda:guardarQuiz(entrada_pregunta,entrada_rcorrecta,entrada_rincorrecta1,entrada_rincorrecta2,entrada_rincorrecta3,int(numero_quizzes)))
        boton_continuar.grid(row=10,column=1)
        
    if counter_quiz == int(numero_quizzes):                                     #Para la última pregunta el botón de "Continuar" se cambia por el de "Finalizar" y la funci´n que ejecuta cambia también.
       crearVentana(10)
       textosuperior = StringVar()                                            #Se declara una variable de texto
       textosuperior.set("Pregunta "+ str(counter_quiz))
       arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#83EB53") 
       arriba.grid(row=1,column=1)
       pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#83EB53")
       pregunta.grid(row=2,column=1)
       entrada_pregunta = Entry(framePrincipal)
       entrada_pregunta.grid(row=3, column=1)
       respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",pady=25,bg ="#83EB53")
       respuesta_correcta.grid(row=4,column=1)
       entrada_rcorrecta = Entry(framePrincipal)
       entrada_rcorrecta.grid(row=5,column=1)
       respuestas_incorrectas = Label(framePrincipal, text = "Ingrese 3 respuestas incorrectas",pady=25,bg ="#83EB53")
       respuestas_incorrectas.grid(row=6,column=1)
       entrada_rincorrecta1 = Entry(framePrincipal)
       entrada_rincorrecta1.grid(row=7,column=1,pady=10)
       entrada_rincorrecta2 = Entry(framePrincipal)
       entrada_rincorrecta2.grid(row=8,column=1)
       entrada_rincorrecta3 = Entry(framePrincipal)
       entrada_rincorrecta3.grid(row=9,column=1,pady = 10)
       boton_continuar = Button(framePrincipal, text="Finalizar", command=lambda:ultimoQuiz(entrada_pregunta,entrada_rcorrecta,entrada_rincorrecta1,entrada_rincorrecta2,entrada_rincorrecta3))
       boton_continuar.grid(row=10,column=1)
        
def ventana_nopreguntas(entradaNombreTexto):
    global archivo_quiz
    archivo_quiz = open(entradaNombreTexto.get() + ".txt", "w")
    clear()
    crearVentana(3)
    pregunta1= Label(framePrincipal, text = "¿Cuántas preguntas desea crear?",bg ="#83EB53")
    pregunta1.grid(row=1,column=1)                                              #Se le pregunta al usuario cuántas preguntas desea hacer
    nquestions = Entry(framePrincipal)
    nquestions.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar", command=lambda:crear_quizzes(nquestions.get()))
    continuar.grid(row=3,column=1)

def opcionQuiz():
    clear()                                                                     
    crearVentana(3)
    pregunta= Label(framePrincipal, text = "Por favor ingrese el nombre con el cual desea guardar el archivo: ",bg ="#83EB53")
    pregunta.grid(row=1,column=1)
    entradaNombreTexto= Entry(framePrincipal)                                   #Por medio de un Entry se le pide al usuario el nombre con el cual desea guardar el archivo
    entradaNombreTexto.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar",command=lambda:ventana_nopreguntas(entradaNombreTexto))
    continuar.grid(row=3,column=1,pady=30)

#-------------------------------------Repaso de flashcards----------------------------------------
import random
# No hemos podido terminar la implementación del repaso de flashcards y quizzes, pero los tendremos listos para la presentación.
#def pantallaRepasoFlashcards(numero_flashcards):
#    
#
#def abrirArchivo():
#    archivoRepasoF = filedialog.askopenfilename(title= "Abra el archivo que contenga las Flashcards", filetypes = (("Archivos de texto","*.txt"),("Todos los archivos","*.*")))                                  
#    archivoRepasoF.ope
#def opcionRepasoFlashcards():
#    global archivoRepaso_f
#    lines = file.readlines()                                                     #El codigo lee el archivo linea por linea 
#    q_and_a = {}                                                                 #Se crea un diccionario vacio asignado a la variable "q_and_a"
#    lista=[]                                                                     #Se crea una lista vacia asignada a la variable "lista"
#    count = 0                                                                    #Se crea un contador que va incrementando cada vez que el codigo pasa por el while loop en la linea 24
#    count_right = 0                                                              #Se crea un contador que incrementa cada vez que el usuario acierta la pregunta
#    count_wrong = 0                                                             #Se crea un contador que incrementa cada vez que el usuraio tenga una pregunta mala
#
#    for i in lines:                                                              #Como el codigo recorre todo el archivo, por cada linea en el archivo, el codigo ejecutará este ciclo for
#        (Q,A)=i.split(":")                                                       #Dentro del archivo, la pregunta y la respuesta estan separadas por ":" entonces el metodo split logra que el codigo entienda cual es la pregutna y cual es la respuesta de las cartas 
#        p= A.split(";")                                                          #El codigo tiene la opcion de que la pregunta tenga mas de una respuesta, entonces las otras respuestas estan separadas por ";" de nuevo el metodo split cumple la funcion de separlas 
#        z= len(p)                                                                ### 
#        k= p[z-1]                                                                ###
#        k= k.strip()                                                             ###
#        p.pop()                                                                  ###
#        p.append(k)                                                              ###
#        q_and_a[Q] = p                                                           #Aqui las preguntas y sus respuestas van siendo agregadas al diccionario creado en la linea 7. La pregutnas se vuelve la llave y la respuesta el valor del diccionario 
#
#    clear()
#    crearVentana(3)
#    texto = Label(framePrincipal, text = "Seleccione el archivo en el cual están las flashcards", pady = 40,bg ="#83EB53")
#    texto.grid(row=1, column=1)
#    seleccionar_archivo = Button(framePrincipal,text= "Seleccionar archivo", command = lambda: filedialog.askopenfilename(title= "Abra el archivo que contenga las Flashcards", filetypes = (("Archivos de texto","*.txt"),("Todos los archivos","*.*"))))
#    seleccionar_archivo.grid(row=2,column=1)
#    boton_continuar = Button(framePrincipa, text = Continuar, command = lambda:pantallaRepasoFlashcards(len(lineas)))
#    boton_continuar.grid(row=3,column=1)
#     
    
    
    
    
    
    
    
def ventana_inicial():  
    crearVentana(5)
    saludo = Label(framePrincipal, text= "Bienvenidos a FlashQuiz", cursor="dot",bg ="#83EB53")      
    saludo.grid(row=1,column=1,padx=20,pady=5)              #Creamos los textos que queremos mostrar y los ubicamos en la interfaz.
    saludo.config(font=("Comic Sans MS", 44))
    
    saludo1 = saludo = Label(framePrincipal, text= "Elige la opción que quieres usar",bg ="#83EB53")
    saludo1.grid(row=2,column=1, padx=10, pady=40)
    saludo.config(font=("Comic Sans MS", 25))
   
    
    botonFlashcard=Button(framePrincipal, text="Crear Flashcards",relief = "groove",command=lambda: opcionFlashcards())    
    botonFlashcard.grid(row=3,column=1,pady=8)              #Creamos los botones para que al pulsarlos el programa realice lo pertienente.
    
    botonQuiz=Button(framePrincipal, text="Crear un Quiz",relief = "groove", command = lambda:opcionQuiz())
    botonQuiz.grid(row=4,column=1,pady=8)
    
    botonRepasar=Button(framePrincipal, text="Repasar flashcards",relief = "groove", command = lambda:opcionRepasoFlashcards())
    botonRepasar.grid(row=5,column=1,pady=8)


    

ventana_inicial()                                                               #Se comienza a ejecutar esta función que según el botón que oprimamos nos llevará a otras funciones.
raizPrincipal.mainloop()                                                        #Se necesita el mainloop para que la interfaz esté siempre encendida y preparada para escuchar los eventos.            
