# FLASHCARD AND QUIZ APP FOR COMPUTER PROGRAMMING PROJECT 

import FlashcardModule #Como ya se creo el modulo "FlashcardModule" entonces, dentro de este codigo, se importara este modulo para usar funciones definidas alla
#Las siguientes 4 lineas solamente imprime la introduccion al codigo, dandole la bienvenida al usuario y mostrandole las opciones que puede escoger
print("Bienvenido a la aplicacion de Flashcards y Quizzes")
print("------------------------------------- \n")
print("Las opciones son las siguientes:")
print("\n A: Crear una baraja de Flashcards \n B: Crear o tomar un Quiz \n C: Si ya tienes una baraja de flashcards y deseas repasarla(No adimte la opción con un quiz)")
option_question = input("Que opcion desearía ejecutar?: ") # El codigo le pregunta al usuario cual de las opciones desea implementar y la guarda dentro de la variable "option_question"

if option_question == "A" or option_question == "a": #Si el usuario escoge la opcion A (independientemente si lo escribe con mayuscula o minuscula) entonces entra a este tramo de codigo
    file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ") #Aqui se le pide que el suuraio nombre el archivo donde se salvara la informacion para asi volver a usar la misma informacion despues 
    new_file = open(file_name + ".txt", "w")#Se abre el archivo con el nombre que le coloco el usuario y es un archivo en el cual se escribe (si el nombre del archivo ya existe, entonces editara ese archivo)
    from string import ascii_letters # Se importa la libreria string y solo se accede a la funcion de ascii_letters
    h= ascii_letters #h se vuelve entonces cualquier letra que se encuentra en la libreria importada
    ncards= input("¿Cuantas cartas desea crear?: ")#Se le pregunta al usuario cuantas cartas quiere hacer y se guarda a la variable "ncacrds"
    if ncards in h: #Entonces, si lo que ingreso el usuario no es un numero sino una letra, el mensaje escrito en la proxima linea de codigo se muestra
        raise ValueError("Solo se puede recibir numeros positivos, {0} ni siquiera es un numero.".format(ncards))
    num_of_cards = int(ncards) #El numero de cartas se guerda en una nueva variable para evitar confusion y mejorar la legibilidad del codigo
    if num_of_cards <= 0:#Si el usuario ingresa un numero negativo al tiempo de crear cartas, se presentara el mensaje en la proxima linea de codigo
        raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo.".format(num_of_cards))
        
    for i in range(num_of_cards): #Por cada numero de cartas que el usuario desee crear, el codigo dentro del for loop se va a ejecutar
        print("\nFlashcard",i + 1)
        Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ") #El usuario ingresa la pregunta
        A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ") #El usuario entra la respuesta correspondiente 
        A = A.lower() #Para evitar confusion con letras mayusculas o minusculas, la respuesta que ingreso es estudiante se convierte toda a minuscula 
        new_file.write(Q + ":" + A) #Dentro de nuestro archivo, se escribira la pregunta y la respuesta separados por un ":"
        c= input("\tSi la pregunta tiene otra respuesta ingresela aqui, sino solo presione ENTER: ")
        while c != "":
            new_file.write(";" + c)
            c= input("\tSi la pregunta tiene otra respuesta ingresela aqui, sino solo presione ENTER: ")
        new_file.write("\n")
    new_file.close() #Ya que toda la informacion se ha escrito dentro del archivo, el archivo se cierra con .close()
    
    q2 = input("¿Desea tomar un repaso de las cartas?: ") #Aqui se pregunta si es que el usuario quiere repazar las cartas que creo ahora mismo o si desea usarlas mas tarde (que se vuelve la opcion C mas adelante)
    q2= q2.upper() #Vuelve el input del usuario a letras mayusculas

    if q2 == "SI": 
        FlashcardModule.Flashcard_Review(file_name) #Si la respuesta es si, entonces usa una funcion definida en el modulo importado al principio del codigo. Esta funcion repasa las cartas en un orden aleatorio
        print("\nHas terminado de repasar las cartas")#Despues de haber terminado el repaso, se imprime este mensaje y termina el codigo

    elif q2 == "NO": #Si la respuesta es no, entonces se termina el programa e imprime el siguente mensaje
        print("Gracias por usar nuestro app. Tus cartas se salvaron bajo el nombre que le asignaste al archivo para usarlas en otro tiempo.")
        
    elif q2 != "SI" or q2 != "NO": #Si el usuario responde algo que no sea si o no, entonces se le presenta el error expresado en la siguente linea
        raise ValueError("Solo se admiten respuestas: si o no")

elif option_question == "B" or option_question == "b": #Si el usuario escoge la opcion B (independientemente si lo escribe con mayuscula o minuscula) entonces entra a este tramo de codigo   
    print("\n B1: Crear un Quiz \n B2: Tomar un quiz") #Como la parte B del programa consiste en dos sub partes, se imprimen las 2 opciones para que asi el usuario escoge si hacer un quiz o tomarlo
    q3 = input("Que opcion desearía ejecutar?: ") #la opcion que escoge el usuario se guarda en la variable "q3"
    
    if q3 == "B1" or q3 == "b1": #Si la opcion que escogio el usuario es b1 (independiente de mayuscula o minuscula, entonces entra en el tramo de codigo indentado)
        file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ") #Aqui se le pide que el suuraio nombre el archivo donde se salvara la informacion para asi volver a usar la misma informacion despues  
        new_file = open(file_name + ".txt", "w") #Se abre el archivo con el nombre que le coloco el usuario y es un archivo en el cual se escribe (si el nombre del archivo ya existe, entonces editara ese archivo) 
        from string import ascii_letters # Se importa la libreria string y solo se accede a la funcion de ascii_letters
        p= ascii_letters #p se vuelve entonces cualquier letra que se encuentra en la libreria importada
        nquestions= input("¿Cuantas preguntas quieres crear?: ") #Se le pregunta al usuario cuantas preguntas del quiz quiere hacer y se guarda a la variable "nquestions"
        if nquestions in p: #Entonces, si lo que ingreso el usuario no es un numero sino una letra, el mensaje escrito en la proxima linea de codigo se muestra
            raise ValueError("Solo se puede recibir numeros positivos, {0} ni siquiera es un numero.".format(nquestions))
        num_of_questions = int(nquestions) #El numero de preguntas se guerda en una nueva variable para evitar confusion y mejorar la legibilidad del codigo 
        if num_of_questions <= 0: #Si el usuario ingresa un numero negativo al tiempo de crear cartas, se presentara el mensaje en la proxima linea de codigo
            raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo".format(num_of_questions))
    
        for i in range(num_of_questions): #Por cada pregunta que el usuario quiere crear, se ejecuta este for loop
            print("\nQuestion",i + 1)
            Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ") #Aqui el usuario escribe la pregunta
            A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ") #Aqui ingresa la respuesta CORRECTA a la pregunta
            A2 = input("\tPor favor ingrese una respuesta incorrecta: ") #Como un quiz tiene diferentes opciones de que escoger, aqui se ingresa una respuesta INCORRECTA 
            A3 = input("\tPor favor ingrese una respuesta incorrecta: ") #Aqui se ingresa una respuesta INCORRECTA 
            A4 = input("\tPor favor ingrese una respuesta incorrecta: ") #Aqui se ingresa una respuesta INCORRECTA 
            A = A.lower() #La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa 
            A2 = A2.lower()#La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa
            A3 = A3.lower()#La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa
            A4 = A4.lower()#La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa
            new_file.write(Q + ":" + A + ";" + A2 + ";" + A3 + ";" + A4 + "\n") #Dentro del archivo, la pregunta y la respuesta correcta se separa via un ":" mientras que las respuesta incorrectas se separan por un ";"
        new_file.close() #Cuando todas las preguntas con sus respuestas fueron escritas, entonces se cierra el archivo
        
        q4 = input("La creación del quiz ha finalizado ¿Desea tomar un repaso del quiz?: ") #Se le pregunta al usuario si quiere realizar un repaso del quiz para ver como quedo
        q4 = q4.upper() #La respuesta se cambia a mayusculas para evitar confusion 
        
        if q4 == "SI":
            FlashcardModule.Quiz_Review(file_name) #Si la respuesta guardada en la variable "q4" es "si" entonces se implementa una funcion dentro del modulo importado al principio del codigo
            print("\nHas terminado el quiz") #Al terminar el repaso se imprime esta linea de codigo 

        elif q4 == "NO": #Si la respuesta es "no" se imprime el proximo mensaje
            print("Gracias por usar nuestro app. Tu quiz se salvó bajo el nombre que le asignaste al archivo para usarlo o mandarlo en otro tiempo.")
        
        elif q4 != "SI" or q2 != "NO": #Si el usuario no responde con un "si" o con un "no" entonces se muestra el error escrito en la siguiente linea de codigo 
            raise ValueError("Solo se admiten respuestas: si o no")
        
    elif q3 == "B2" or q3 == "b2": #Si la opcion que escogio el usuario es b2 (independiente de mayuscula o minuscula, entonces entra en el tramo de codigo indentado)
        chosen_file = input("Por favor Ingrese el nombre del archivo: ")#Como la informacion se salvó en un archivo, entonces se le pide el nombre del archivo al usuario
        FlashcardModule.Quiz_Review(chosen_file) #Siempre cuando exista el archivo que el usuario ingreso, el nombre se usa un una funcion dentro del modulo para tomar el quiz
        print("\nHas terminado repasando las cartas") #Al terminar el quiz, se imprime esta linea de codigo 
    
    else: #Si el usuario no responde con una de las dos opciones, se presenta el siguiente error  
        raise ValueError(" Solo hay dos opciones: B1 & B2, {0} no es una de ellas".format(q3))
        
elif option_question == "C" or option_question =="c": #Si el usuario escoge la opcion C (independientemente si lo escribe con mayuscula o minuscula) entonces entra a este tramo de codigo   
    chosen_file = input("Por favor Ingrese el nombre del archivo: ") #Como las cartas se guardaron dentro de un archivo, entonces se le pide al usuario el nombre de dicho archivo para acceder a la informacion 
    FlashcardModule.Flashcard_Review(chosen_file) #Siempre cuando exista el archivo que el usuario ingreso, el nombre se usa un una funcion dentro del modulo para tomar el repaso de las cartas
    print("\nHas terminado de repasar las cartas") #Al terminar el quiz, se imprime esta linea de codigo 
else: #Si el usuario pone una opcion que no sea A, B, C entocnes se imprime el error en la siguiente linea y termina el codigo 
    raise ValueError(" Solo hay tres opciones: A, B o C, {0} no es una de ellas".format(option_question))
    
