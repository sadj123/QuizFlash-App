from tkinter import *
from tkinter import filedialog

raizPrincipal=Tk()                                                              #Se crea la raíz que es la ventana principal
raizPrincipal.config(bg="#F7444E")
raizPrincipal.title("FlashQuiz App")
                     
framePrincipal=Frame()                                                            #Se crea un frame que es donde se colocan todos los widgets que queremos
framePrincipal.pack(expand=True, fill="both")
framePrincipal.config(bg="#F7444E")
                      
ancho = raizPrincipal.winfo_screenwidth()
altura = raizPrincipal.winfo_screenheight()
raizPrincipal.geometry("%dx%d+0+0" % (ancho,altura))                            #Esto nos permite que se ejecute por defecto en pantalla completa



def crearVentana(numerolineas):
    vacio = Label(framePrincipal, text= "",anchor="center", bg="#F7444E")        #Creamos etiquetas vacias arriba y abajo de todo para dejar márgenes.
    vacio.grid(row=int(numerolineas+1),column=1,padx=20,pady=20)
    vacio1 = Label(framePrincipal, text= "",anchor="center", bg="#F7444E")
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
global contador
contador=1

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

def volver_inicio():
    global contador
    contador=1
    ventana_inicial()

def ultimaFlashcard(pregunta,respuesta):
    global archivo                                                              #Esta función guarda en el archivo de texto, la pregunta y seguido de dos puntos la repuesta.
    question = pregunta.get()                                                   #El .get nos permite recolectar la información que el usuario ha puesto en la entrada
    answer = respuesta.get()
    answer.lower()
    archivo.write(question + ":" + answer)
    clear()
    crearVentana(3)
    mensaje_final=Label(framePrincipal, text = "Gracias por utilizar FlashQuiz App",bg ="#F7444E",fg ="#F7F8F3", pady = 20)
    mensaje_final.grid(row=1,column=1)
    mensaje_final.config(font=("",20))
    archivo.close()                                                            #Aquí se cierra el archivo
    cerrar_programa=Button(framePrincipal,text= "Cerrar", command = lambda:raizPrincipal.destroy(),bg="#002C3E", fg ="#F7F8F3")
    cerrar_programa.grid(row=2,column=1,ipadx=55)
    cerrar_programa.config(font=("",18))
    inicio=Button(framePrincipal,text= "Pantalla de inicio", command = lambda:volver_inicio(),bg="#002C3E", fg ="#F7F8F3")
    inicio.grid(row=3,column=1, pady=10)
    inicio.config(font=("",18))                                            
    
def hacer_flashcards(numero_flashcards):                                        #Esta función crea la pantalla donde va a estar la pregunta y la respuesta de la flashcard
    global contador                                                             #La única diferencia en los if es que si todavía no es la última flashcard, el botón dice "Continuar" y cuando es la última el botón dice "Finalizar" y cierra el archivo.
    clear()
    if contador < int(numero_flashcards):
        crearVentana(6)
        textosuperior = StringVar()
        textosuperior.set("Flashcard "+ str(contador))
        arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#F7444E", fg ="#002C3E") 
        arriba.grid(row=1,column=1)
        arriba.config(font=("",25))
        pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#F7444E", fg ="#F7F8F3")
        pregunta.grid(row=2,column=1)
        pregunta.config(font=("",18))
        entrada_pregunta = Entry(framePrincipal)
        entrada_pregunta.grid(row=3,column=1, pady=20)
        respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",bg ="#F7444E", fg ="#F7F8F3", height=-1)
        respuesta_correcta.grid(row=4,column=1)
        respuesta_correcta.config(font=("",18))
        entrada_respuesta = Entry(framePrincipal)
        entrada_respuesta.grid(row=5,column=1,pady=20)       
        boton_continuar = Button(framePrincipal, text="Continuar", command=lambda:guardarFlashcard(entrada_pregunta,entrada_respuesta,int(numero_flashcards)),bg="#002C3E",fg ="#F7F8F3")
        boton_continuar.grid(row=6,column=1)
        boton_continuar.config(font=("",16))
        
    if contador == int(numero_flashcards):
        crearVentana(6)
        pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#F7444E",fg ="#F7F8F3")
        pregunta.grid(row=2,column=1)
        pregunta.config(font=("",18))
        entrada_pregunta = Entry(framePrincipal)
        entrada_pregunta.grid(row=3,column=1, pady=20)
        respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",bg ="#F7444E", fg ="#F7F8F3")
        respuesta_correcta.grid(row=4,column=1)
        respuesta_correcta.config(font=("",18))
        entrada_respuesta = Entry(framePrincipal)
        entrada_respuesta.grid(row=5,column=1, pady=20)
        textosuperior = StringVar()
        textosuperior.set("Flashcard "+ str(contador))
        arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#F7444E",fg ="#002C3E") 
        arriba.grid(row=1,column=1)
        arriba.config(font=("",25))
        boton_finalizar = Button(framePrincipal, text="Finalizar", command=lambda:ultimaFlashcard(entrada_pregunta,entrada_respuesta),bg="#002C3E",fg ="#F7F8F3")
        boton_finalizar.grid(row=6,column=1)
        boton_finalizar.config(font=("",16))
        
        

def ventana_cartas(entradaNombreTexto):
    global archivo                                                              #Se define una variable globsl, ya que tenemos que usarla y modificarla en distintas funciones.
    archivo = open(entradaNombreTexto.get() + ".txt", "w")                      #Se crea un archivo con el nombre que el usuario especificó
    clear()
    crearVentana(3)
    pregunta1= Label(framePrincipal, text = "¿Cuántas cartas desea crear?",bg ="#F7444E", fg ="#F7F8F3")
    pregunta1.grid(row=1,column=1)                                              #Se le pregunta al usuario cuántas flashcards desea crear
    pregunta1.config(font=("",18))
    entradaCartas = Entry(framePrincipal)
    entradaCartas.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar", command=lambda:hacer_flashcards(entradaCartas.get()),bg="#002C3E",fg="#F7F8F3")
    continuar.grid(row=3,column=1)
    continuar.config(font=("",14))

          
def opcionFlashcards():                                                         #Esta es la función que se ejecuta cuando se pulsa "Hacer flashcards" en la ventana principal
    clear()
    crearVentana(3)
    pregunta= Label(framePrincipal, text = "Por favor ingrese el nombre con el cual desea guardar el archivo: ",bg ="#F7444E",fg = "#F7F8F3")
    pregunta.grid(row=1,column=1)
    pregunta.config(font=("", 18))
    entradaNombreTexto= Entry(framePrincipal)                                   #En esta función se le pregunta al usuario cómo quiere guardar el archivo.
    entradaNombreTexto.grid(row=2,column=1, pady=20)                            #Consta de una Label y una entrada de texto que se recopila para guardar el archivo con ese nombre más adelante
    continuar = Button(framePrincipal, text="Continuar",command=lambda:ventana_cartas(entradaNombreTexto),bg="#002C3E",fg="#F7F8F3")
    continuar.grid(row=3,column=1,pady=30)
    continuar.config(font=("",16))

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
    crearVentana(3)
    mensaje_final=Label(framePrincipal, text = "Gracias por utilizar FlashQuiz App",bg ="#F7444E")
    mensaje_final.grid(row=1,column=1)
    mensaje_final.config(font=("",20))
    cerrar_programa=Button(framePrincipal,text="Cerrar programa", command = lambda:raizPrincipal.destroy(), bg="#002C3E",fg="#F7F8F3")
    cerrar_programa.grid(row=2,column=1,pady=18)
    cerrar_programa.config(font=("",18))
    inicio=Button(framePrincipal,text= "Pantalla de inicio", command = lambda:ventana_inicial(),bg="#002C3E", fg ="#F7F8F3")
    inicio.grid(row=3,column=1, pady=10)
    inicio.config(font=("",18)) 
    
    
def crear_quizzes(numero_quizzes):
    global counter_quiz                                                         #Se tiene una variable global que  nos permite saber en qué pregunta vamos.
    clear()
    if counter_quiz < int(numero_quizzes):                                      #Se crea la pantalla con una entrada para la pregunta, una entrada para la pregunta correcta y tres entradas para las respuestas incorrectas.
        crearVentana(10)
        textosuperior = StringVar()                                            #Se declara una variable de texto
        textosuperior.set("Pregunta "+ str(counter_quiz))
        arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#F7444E", fg ="#002C3E") 
        arriba.grid(row=1,column=1)
        arriba.config(font=("",25))
        pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#F7444E",fg ="#F7F8F3")
        pregunta.grid(row=2,column=1)
        pregunta.config(font=("",18))
        entrada_pregunta = Entry(framePrincipal)
        entrada_pregunta.grid(row=3, column=1)
        respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",pady=25,bg ="#F7444E",fg ="#F7F8F3")
        respuesta_correcta.grid(row=4,column=1)
        respuesta_correcta.config(font=("",18))
        entrada_rcorrecta = Entry(framePrincipal)
        entrada_rcorrecta.grid(row=5,column=1)
        respuestas_incorrectas = Label(framePrincipal, text = "Ingrese 3 respuestas incorrectas",pady=25,bg ="#F7444E",fg ="#F7F8F3")
        respuestas_incorrectas.grid(row=6,column=1)
        respuestas_incorrectas.config(font=("",18))
        entrada_rincorrecta1 = Entry(framePrincipal)
        entrada_rincorrecta1.grid(row=7,column=1)
        entrada_rincorrecta2 = Entry(framePrincipal)
        entrada_rincorrecta2.grid(row=8,column=1)
        entrada_rincorrecta3 = Entry(framePrincipal)
        entrada_rincorrecta3.grid(row=9,column=1,pady = 10)
        boton_continuar = Button(framePrincipal, text="Continuar", command=lambda:guardarQuiz(entrada_pregunta,entrada_rcorrecta,entrada_rincorrecta1,entrada_rincorrecta2,entrada_rincorrecta3,int(numero_quizzes)),bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=10,column=1)
        boton_continuar.config(font=("",16))
        
    if counter_quiz == int(numero_quizzes):                                     #Para la última pregunta el botón de "Continuar" se cambia por el de "Finalizar" y la función que ejecuta cambia también.
       crearVentana(10)
       textosuperior = StringVar()                                            #Se declara una variable de texto
       textosuperior.set("Pregunta "+ str(counter_quiz))
       arriba = Label(framePrincipal, textvariable=textosuperior,pady = 30,bg ="#F7444E") 
       arriba.grid(row=1,column=1)
       arriba.config(font=("",25))
       pregunta = Label(framePrincipal, text = "Ingrese la pregunta",bg ="#F7444E",fg ="#F7F8F3")
       pregunta.grid(row=2,column=1)
       pregunta.config(font=("",18))
       entrada_pregunta = Entry(framePrincipal)
       entrada_pregunta.grid(row=3, column=1)
       respuesta_correcta = Label(framePrincipal, text = "Ingrese la respuesta correcta",pady=25,bg ="#F7444E",fg ="#F7F8F3")
       respuesta_correcta.grid(row=4,column=1)
       respuesta_correcta.config(font=("",18))
       entrada_rcorrecta = Entry(framePrincipal)
       entrada_rcorrecta.grid(row=5,column=1)
       respuestas_incorrectas = Label(framePrincipal, text = "Ingrese 3 respuestas incorrectas",pady=25,bg ="#F7444E",fg ="#F7F8F3")
       respuestas_incorrectas.grid(row=6,column=1)
       respuestas_incorrectas.config(font=("",18))
       entrada_rincorrecta1 = Entry(framePrincipal)
       entrada_rincorrecta1.grid(row=7,column=1,pady=10)
       entrada_rincorrecta2 = Entry(framePrincipal)
       entrada_rincorrecta2.grid(row=8,column=1)
       entrada_rincorrecta3 = Entry(framePrincipal)
       entrada_rincorrecta3.grid(row=9,column=1,pady = 10)
       boton_continuar = Button(framePrincipal, text="Finalizar", command=lambda:ultimoQuiz(entrada_pregunta,entrada_rcorrecta,entrada_rincorrecta1,entrada_rincorrecta2,entrada_rincorrecta3),bg="#002C3E",fg="#F7F8F3")
       boton_continuar.grid(row=10,column=1)
       boton_continuar.config(font=("",16))
       
def ventana_nopreguntas(entradaNombreTexto):
    global archivo_quiz
    archivo_quiz = open(entradaNombreTexto.get() + ".txt", "w")
    clear()
    crearVentana(3)
    pregunta1= Label(framePrincipal, text = "¿Cuántas preguntas desea crear?",bg ="#F7444E",fg ="#F7F8F3")
    pregunta1.grid(row=1,column=1)                                             #Se le pregunta al usuario cuántas preguntas desea hacer
    pregunta1.config(font=("",20))
    nquestions = Entry(framePrincipal)
    nquestions.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar", command=lambda:crear_quizzes(nquestions.get()),bg="#002C3E",fg="#F7F8F3")
    continuar.grid(row=3,column=1)
    continuar.config(font=("",16))

def opcionQuiz():
    clear()                                                                     
    crearVentana(3)
    pregunta= Label(framePrincipal, text = "Por favor ingrese el nombre con el cual desea guardar el archivo: ",bg ="#F7444E",fg="#F7F8F3")
    pregunta.grid(row=1,column=1)
    pregunta.config(font=("",20))
    entradaNombreTexto= Entry(framePrincipal)                                   #Por medio de un Entry se le pide al usuario el nombre con el cual desea guardar el archivo
    entradaNombreTexto.grid(row=2,column=1, pady=20)
    continuar = Button(framePrincipal, text="Continuar",command=lambda:ventana_nopreguntas(entradaNombreTexto),bg="#002C3E",fg="#F7F8F3")
    continuar.grid(row=3,column=1,pady=30)
    continuar.config(font=("",16))

#-------------------------------------Repaso de flashcards----------------------------------------
import random
global count
count = 1
global count_right
count_right = 0
global count_wrong
count_wrong = 0  



def abrirArchivo():
    global archivoRepasoF
    archivoRepasoF = filedialog.askopenfilename(title= "Abra el archivo que contenga las Flashcards", filetypes = (("Archivos de texto","*.txt"),("Todos los archivos","*.*")))                                  
    archivoRepasoF.open()

def leerRespuesta(respuesta_usuario,respuesta_correcta,no_flashcards):
    global count
    global count_right
    global count_wrong
    r_usuario = respuesta_usuario
    r_usuario.lower()
    clear()
    if r_usuario in str(respuesta_correcta):
        crearVentana(2)
        correcta = Label(framePrincipal, text="Muy bien. Respuesta correcta",pady= 30, bg ="#F7444E",fg="#F7F8F3")
        correcta.grid(row=1,column=1)
        correcta.config(font=("",20))
        boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:pantallaRepasoFlashcards(no_flashcards),bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=2,column=1)
        boton_continuar.config(font=("",16))
        count += 1                                                   
        count_right += 1
       
    
    else:
        crearVentana(2)
        a=","
        a=a.join(respuesta_correcta)
        wrong = StringVar()
        wrong.set("La respuesta es incorrecta. La respuesta correcta era: " + str(a) )
        incorrecta = Label(framePrincipal, textvariable = wrong ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        incorrecta.grid(row=1,column=1)
        incorrecta.config(font=("",20))
        boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:pantallaRepasoFlashcards(no_flashcards),bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=2,column=1)
        boton_continuar.config(font=("",16))
        count +=1
        count_wrong +=1
    

def pantallaRepasoFlashcards(no_flashcards):
    global archivoFlashcards
    global count
    global count_right
    global count_wrong
    global q_and_a
    global lista
     
    if count <= no_flashcards:
        while True:
            pick = random.choice(list(q_and_a.keys()))
            if pick not in lista:
                pregunta = pick
                break
        r_correcta = q_and_a[pregunta] 
        print (r_correcta)
        lista.append(pregunta)
        clear()
        crearVentana(4)
        textosuperior = StringVar()                                            #Se declara una variable de texto
        textosuperior.set("Flashcard "+ str(count))
        arriba = Label(framePrincipal, textvariable = textosuperior,pady= 30, bg ="#F7444E",fg ="#002C3E")
        arriba.grid(row=1,column=1)
        arriba.config(font=("",20))
        preguntapantalla = Label(framePrincipal, text=pregunta, bg ="#F7444E",fg="#F7F8F3")
        preguntapantalla.grid(row=2, column = 1)
        preguntapantalla.config(font=("",18))
        respuesta = Entry(framePrincipal)
        respuesta.grid(row=3,column=1, pady=20)
        boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:leerRespuesta(respuesta.get(),r_correcta,no_flashcards), pady=10, bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=4,column=1)
        boton_continuar.config(font=("",16))
        
        
    else:
        clear()
        crearVentana(6)
        superior= Label(framePrincipal, text= "Tus resultados son" ,pady= 30, bg ="#F7444E",fg ="#002C3E")
        superior.grid(row=1,column=1)
        superior.config(font=("",20))
        correct_answers = StringVar()
        correct_answers.set( "Respuestas correctas: " + str(count_right))
        correctas = Label(framePrincipal, textvariable = correct_answers ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        correctas.grid(row=2,column=1)
        correctas.config(font=("",18))
        wrong_answers = StringVar()
        wrong_answers.set("Respuestas incorrectas: " + str(count_wrong))
        incorrectas = Label(framePrincipal, textvariable = wrong_answers ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        incorrectas.grid(row=3,column=1)
        incorrectas.config(font=("",18))
        puntuacion = StringVar()
        puntuacion.set("Tu puntaje total fue: " + str((count_right/(count-1))*5))
        puntaje = Label(framePrincipal, textvariable = puntuacion ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        puntaje.grid(row=4,column=1)
        puntaje.config(font=("",18))
        porcentaje = StringVar()
        porcentaje.set("Tu porcentaje de aciertos fue: " + str((count_right/(count-1))*100) +"%")
        percentage = Label(framePrincipal, textvariable = porcentaje ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        percentage.grid(row=5,column=1)
        percentage.config(font=("",18))
        
def configuracionArchivo():
    global archivoFlashcards
    global count
    global count_right
    global count_wrong
    global q_and_a
    q_and_a = {}  
    global lista
    lista=[] 
    lines = archivoFlashcards.readlines()                                                                                                                                                                                    
    for i in lines:                                                             
        (Q,A)=i.split(":")                                                       
        p= A.split(";")                                                           
        z= len(p)                                                               
        k= p[z-1]                                                                
        k= k.strip()                                                             
        p.pop()                                                                  
        p.append(k)                                                              
        q_and_a[Q] = p
    pantallaRepasoFlashcards(len(lines))
            
                                                     
def elegirArchivo():
    global archivoFlashcards
    archivoF = filedialog.askopenfilename(title= "Abra el archivo que contenga las Flashcards", filetypes = (("Archivos de texto","*.txt"),("Todos los archivos","*.*")))
    archivoFlashcards = open(archivoF,"r")
    
def opcionRepasoFlashcards():
    clear()
    crearVentana(4)
    texto = Label(framePrincipal, text = "Seleccione el archivo en el cual están las flashcards", pady = 40,bg ="#F7444E",fg="#F7F8F3")
    texto.grid(row=1, column=1)
    texto.config(font=("",20))
    seleccionar_archivo = Button(framePrincipal,text= "Seleccionar archivo", command = lambda: elegirArchivo(),bg="#002C3E",fg="#F7F8F3")
    seleccionar_archivo.grid(row=2,column=1)
    seleccionar_archivo.config(font=("",16))
    vacio = Label(framePrincipal, text= "",anchor="center", bg="#F7444E")
    vacio.grid(row=3,column=1,padx=20,pady=20)
    boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:configuracionArchivo(),bg="#002C3E",fg="#F7F8F3")
    boton_continuar.grid(row=4,column=1)
    boton_continuar.config(font=("",16))
     
        
 #-----------------------Opción Repaso de Quizzes---------------------------------------------   
rng = random.Random()
global countQ
countQ = 0 
global count_right_Q
count_right_Q = 0
global count_wrong_Q
count_wrong_Q = 0
global q_and_a_Q
q_and_a_Q = {}
global listaQ
listaQ =[]


def revisarRespuestas(opcion,no_preguntas,pregunta):
    global countQ
    global count_right_Q
    global count_wrong_Q
    global quiz_questions
    global listaQ
    clear()
    listaQ.append(pregunta)
    if opcion.get() == 1:
        crearVentana(2)
        correcta = Label(framePrincipal, text="Muy bien. Respuesta correcta",pady= 30, bg ="#F7444E",fg="#F7F8F3")
        correcta.grid(row=1,column=1) 
        correcta.config(font=("",22))
        boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:pantallaQuiz(no_preguntas),bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=2,column=1)
        boton_continuar.config(font=("",16))
        countQ += 1                                                   
        count_right_Q += 1
    else:
        crearVentana(2)
        wrong = StringVar()
        wrong.set("La respuesta es incorrecta. La respuesta correcta era: " + str(quiz_questions[0]))
        incorrecta = Label(framePrincipal, textvariable = wrong ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        incorrecta.grid(row=1,column=1)
        incorrecta.config(font=("",22))
        boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:pantallaQuiz(no_preguntas),bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=2,column=1)
        boton_continuar.config(font=("",16))
        countQ +=1
        count_wrong_Q +=1
    
    

    
       

def pantallaQuiz(no_preguntas):
    clear()
    global archivoQuiz
    global countQ
    global count_right_Q
    global count_wrong_Q
    global q_and_a_Q
    global listaQ
    global quiz_questions
    if countQ < no_preguntas:
        while True:
            pick = random.choice(list(q_and_a_Q.keys()))
            if pick not in listaQ:
                pregunta = pick
                break
        x = rng.randint(3,6)
        while True:
            t = rng.randint(3,6)
            if t != x:
                y = t
                break
        while True:
            t = rng.randint(3,6)
            if t != x and t!= y:
                w = t
                break
        while True:
            t = rng.randint(3,6)
            if t != x and t!= y and t!= w:
                z = t
                break
        def seleccionarse():
            if opcion.get() == 1:
                opcion_correcta.select()
                
            elif opcion.get() == 2:
                opcion_incorrecta1.select()
            
            elif opcion.get() == 3:
                opcion_incorrecta2.select()
            
            elif opcion.get() == 4:
                opcion_incorrecta3.select()
            
        quiz_questions = q_and_a_Q[pregunta]                                           
        quiz_questions_2 = quiz_questions[:]                                     
        dicto = {}
        crearVentana(7)
        textosuperior = StringVar()                                            
        textosuperior.set("Pregunta "+ str(countQ+1))
        arriba = Label(framePrincipal, textvariable = textosuperior,pady= 30, bg ="#F7444E",fg ="#002C3E")
        arriba.grid(row=1,column=1)
        arriba.config(font=("",20))
        escoja_pregunta = Label(framePrincipal, text = str(pregunta), pady = 20, bg ="#F7444E",fg="#F7F8F3")
        escoja_pregunta.grid(row=2,column=1)
        escoja_pregunta.config(font=("",18))
        opcion = IntVar()
        r_correcta = StringVar()
        r_correcta.set(str(quiz_questions[0]))
        opcion_correcta = Radiobutton(framePrincipal,textvariable =r_correcta, variable = opcion, value=1,bg="#F7444E",fg="#F7F8F3",command=seleccionarse(),highlightcolor="blue")
        opcion_correcta.grid(row=x,column=1)
        opcion_correcta.config(font=("",18))
        r_incorrecta_1 = StringVar()
        r_incorrecta_1.set(quiz_questions_2[1])
        opcion_incorrecta1 = Radiobutton(framePrincipal,textvariable =r_incorrecta_1, variable = opcion, value=2,bg="#F7444E",fg="#F7F8F3",command=seleccionarse(),highlightcolor="blue")
        opcion_incorrecta1.grid(row=y,column=1)
        opcion_incorrecta1.config(font=("",18))
        r_incorrecta_2 = StringVar()
        r_incorrecta_2.set(quiz_questions_2[2])
        opcion_incorrecta2 = Radiobutton(framePrincipal,textvariable =r_incorrecta_2, variable = opcion, value=3,bg="#F7444E",fg="#F7F8F3",command=seleccionarse(),highlightcolor="blue")
        opcion_incorrecta2.grid(row=w,column=1)
        opcion_incorrecta2.config(font=("",18))
        r_incorrecta_3 = StringVar()
        r_incorrecta_3.set(quiz_questions_2[3])
        opcion_incorrecta3 = Radiobutton(framePrincipal,textvariable =r_incorrecta_3, variable = opcion, value=4,bg="#F7444E",fg="#F7F8F3",command=seleccionarse(),highlightcolor="blue")
        opcion_incorrecta3.grid(row=z,column=1)
        opcion_incorrecta3.config(font=("",18))
        vacio = Label(framePrincipal, text= "",anchor="center", bg="#F7444E")       
        vacio.grid(row=7,column=7,padx=20,pady=20)
        boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:revisarRespuestas(opcion,no_preguntas,pregunta),bg="#002C3E",fg="#F7F8F3")
        boton_continuar.grid(row=8,column=1)
        boton_continuar.config(font=("",16))
  
    else:
        clear()
        crearVentana(6)
        superior= Label(framePrincipal, text= "Tus resultados son" ,pady= 30, bg ="#F7444E",fg ="#002C3E")
        superior.grid(row=1,column=1)
        superior.config(font=("",30))
        correct_answers = StringVar()
        correct_answers.set( "Respuestas correctas: " + str(count_right_Q))
        correctas = Label(framePrincipal, textvariable = correct_answers ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        correctas.grid(row=2,column=1)
        correctas.config(font=("",25))
        wrong_answers = StringVar()
        wrong_answers.set("Respuestas incorrectas: " + str(count_wrong_Q))
        incorrectas = Label(framePrincipal, textvariable = wrong_answers ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        incorrectas.grid(row=3,column=1)
        incorrectas.config(font=("",25))
        puntuacion = StringVar()
        puntuacion.set("Tu puntaje total fue: " + str((count_right_Q/(countQ))*5))
        puntaje = Label(framePrincipal, textvariable = puntuacion ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        puntaje.grid(row=4,column=1)
        puntaje.config(font=("",25))
        porcentaje = StringVar()
        porcentaje.set("Tu porcentaje de aciertos fue: " + str((count_right_Q/(countQ))*100) +"%")
        percentage = Label(framePrincipal, textvariable = porcentaje ,pady= 30, bg ="#F7444E",fg="#F7F8F3")
        percentage.grid(row=5,column=1)
        percentage.config(font=("",25))
        
        
        

def configurarArchivoQ():
    global archivoQuiz
    global countQ
    global count_right_Q
    global count_wrong_Q
    global q_and_a_Q
    global listaQ
    lines = archivoQuiz.readlines()                                                                                                                  
    for i in lines:
        (Q,A)=i.split(":")                                                       
        p= A.split(";")                                                           
        z= len(p)                                                                
        k= p[z-1]                                                                
        k= k.strip()
        p.pop()                                                                  
        p.append(k)                                                              
        q_and_a_Q[Q] = p
    pantallaQuiz(len(lines))
    
def elegirArchivoQ():
    global archivoQuiz
    archivoQ = filedialog.askopenfilename(title= "Abra el archivo que contenga el quiz", filetypes = (("Archivos de texto","*.txt"),("Todos los archivos","*.*")))
    archivoQuiz = open(archivoQ,"r")
    
def opcionRepasoQuiz():
    clear()
    crearVentana(4)
    texto = Label(framePrincipal, text = "Seleccione el archivo en el cual está el quiz", pady = 40,bg ="#F7444E",fg="#F7F8F3")            
    texto.grid(row=1, column=1)
    texto.config(font=("",20))
    seleccionar_archivo = Button(framePrincipal,text= "Seleccionar archivo", command = lambda: elegirArchivoQ(),bg="#002C3E",fg="#F7F8F3")
    seleccionar_archivo.grid(row=2,column=1)
    seleccionar_archivo.config(font=("",16))
    vacio = Label(framePrincipal, text= "",anchor="center", bg="#F7444E")
    vacio.grid(row=3,column=1,padx=20,pady=20)
    boton_continuar = Button(framePrincipal, text = "Continuar", command = lambda:configurarArchivoQ(),bg="#002C3E",fg="#F7F8F3")
    boton_continuar.grid(row=4,column=1)    
    boton_continuar.config(font=("",16))




 #----------------------------- Ventana inicial ---------------------------------------------------------------------   
def ventana_inicial():  
    clear()
    crearVentana(6)
    saludo = Label(framePrincipal, text= "Bienvenidos a FlashQuiz", cursor="dot",bg ="#F7444E", fg ="#F7F8F3")      
    saludo.grid(row=1,column=1,padx=20,pady=5)              #Creamos los textos que queremos mostrar y los ubicamos en la interfaz.
    saludo.config(font=("", 44))
    
    saludo1 = saludo = Label(framePrincipal, text= "Elige la opción que quieres usar",bg ="#F7444E",fg ="#F7F8F3")
    saludo1.grid(row=2,column=1, padx=10, pady=40)
    saludo.config(font=("", 25))
   
    
    botonFlashcard=Button(framePrincipal, text="Crear Flashcards",relief = "groove",command=lambda: opcionFlashcards(),bg="#002C3E",fg="#F7F8F3")    
    botonFlashcard.grid(row=3,column=1,pady=8,ipadx=25)             #Creamos los botones para que al pulsarlos el programa realice lo pertienente.
    botonFlashcard.config(font=("",16))
    
    botonQuiz=Button(framePrincipal, text="Crear un Quiz",relief = "groove", command = lambda:opcionQuiz(),bg="#002C3E",fg="#F7F8F3")
    botonQuiz.grid(row=4,column=1,pady=8,ipadx=41)
    botonQuiz.config(font=("",16))
    
    botonRepasar=Button(framePrincipal, text="Repasar Flashcards",relief = "groove", command = lambda:opcionRepasoFlashcards(),bg="#002C3E",fg="#F7F8F3")
    botonRepasar.grid(row=5,column=1,pady=8, ipadx=10)
    botonRepasar.config(font=("",16))
    
    botonRepasoQuiz = Button(framePrincipal,text="Repasar un Quiz",relief = "groove", command = lambda:opcionRepasoQuiz(),bg="#002C3E",fg="#F7F8F3")
    botonRepasoQuiz.grid(row=6,column=1,pady=8,ipadx=28)
    botonRepasoQuiz.config(font=("",16))


    

ventana_inicial()                                                               #Se comienza a ejecutar esta función que según el botón que oprimamos nos llevará a otras funciones.
raizPrincipal.mainloop() 
