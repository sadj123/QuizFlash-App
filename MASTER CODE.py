# FLASHCARD AND QUIZ APP FOR COMPUTER PROGRAMMING PROJECT 

import FlashcardModule                                                                                                     #Como ya se creo el modulo "FlashcardModule" entonces se importarán funciones definidas dentro de dicho modulo
                                                                                                                           #Las lineas de 4 a 9 imprimen la introduccion al codigo, dandole la bienvenida al usuario y mostrandole las opciones que puede escoger
print("Bienvenido a la aplicacion de Flashcards y Quizzes")
print("------------------------------------- \n")
print("Las opciones son las siguientes:")
print("\n A: Crear una baraja de Flashcards \n B: Crear o tomar un Quiz \n C: Si ya tienes una baraja de flashcards y deseas repasarla(No adimte la opción con un quiz)")
option_question = input("Que opcion desearía ejecutar?: ")                                                                 

if option_question == "A" or option_question == "a":                                                                       # El programa ejecuta el bloque de codigo que se encuentra entre las lineas 11 a 47
    file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ")                                 # Dentro de las lineas 11 a 21, se le pregunta al ususario el nombre del archivo con el cual lo quiere salvaro 
    new_file = open(file_name + ".txt", "w")                                                                               # Despues se abre el archivo donde el programa va escribir las preguntas y respuestas de las cartas 
    from string import ascii_letters                                                                                       # Se le pregunta al usuario cuantas cartas quiere hacer y si el usuario ingresa un entero negativo o una letra, le saldrá los error en las lineas 18 y 21
    h= ascii_letters                                                                                                       
    ncards= input("¿Cuantas cartas desea crear?: ")                                                                        
    if ncards in h:                                                                                                        
        raise ValueError("Solo se puede recibir numeros positivos, {0} ni siquiera es un numero.".format(ncards))
    num_of_cards = int(ncards)                                                                                             
    if num_of_cards <= 0:                                                                                                  
        raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo.".format(num_of_cards))
        
    for i in range(num_of_cards):                                                                                          # El bloque de codigo entre las lineas 23 y 34 crea el numero de cartas que el usuario ingreso 
        print("\nFlashcard",i + 1)                                                                                         # Tambien, si es que la pregunta tiene mas de una respuesta, el usuario la puede ingresar
        Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ")                                # Al mismo tiempo, la inforamcion se va guardando dentro del archivo, que se cierra cuando se termien de crear las cartas 
        A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ")                                      
        A = A.lower()                                                                                                       
        new_file.write(Q + ":" + A)                                                                                        
        c= input("\tSi la pregunta tiene otra respuesta ingresela aqui, sino solo presione ENTER: ")                       
        while c != "":                                                                                                     
            new_file.write(";" + c)                                                                                        
            c= input("\tSi la pregunta tiene otra respuesta ingresela aqui, sino solo presione ENTER: ")                   
        new_file.write("\n")                                                                                               
    new_file.close()                                                                                                       
    
    q2 = input("¿Desea tomar un repaso de las cartas?: ")                                                                  #Aqui se pregunta si el usuario quiere repazar las cartas ahora mismo o si desea repazarlas mas tarde (que se vuelve la opcion C mas adelante)
    q2= q2.upper()                                                                                                         #Vuelve el input del usuario a letras mayusculas para que el codigo entienda y no haya confusiones

    if q2 == "SI":                                                                                                         #Si la respuesta es "si" se ejecutan las lineas 40-41 acceden a una funcion dentro del modulo definido antes que permite revisar las cartas  
        FlashcardModule.Flashcard_Review(file_name)                                                                        
        print("\nHas terminado de repasar las cartas")                                                                     

    elif q2 == "NO":                                                                                                       #Si la respuesta es "no", entonces se termina el programa e imprime el mensaje en la linea 44
        print("Gracias por usar nuestra app. Tus cartas se salvaron bajo el nombre que le asignaste al archivo para usarlas en otro tiempo.")
        
    elif q2 != "SI" or q2 != "NO":                                                                                         #Si el usuario responde algo que no sea "si" o "no", entonces se le presenta el error expresado en la linea 47 
        raise ValueError("Solo se admiten respuestas: si o no")

elif option_question == "B" or option_question == "b":                                                                     #Si el usuario escoge la opcion B entonces se ejecuta el bloque de codigo de la linea 50 hasta 98   
    print("\n B1: Crear un Quiz \n B2: Tomar un quiz")                                                                     
    q3 = input("Que opcion desearía ejecutar?: ")                                                                          
    
    if q3 == "B1" or q3 == "b1":                                                                                           # Si la opcion que escogio el usuario es b1 entonces el programa ejecuta el bloque de codigo de la linea 53 hasta la 63 
        file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ")                             # Donde se le pregunta al usuario el nombre con el cual quiere slavar el archivo donde la infroamcion se guardara   
        new_file = open(file_name + ".txt", "w")                                                                           # Despues se abre el archivo donde el programa va escribir las preguntas  
        from string import ascii_letters                                                                                   # Se le pregunta al usuario cuantas cartas quiere hacer y si el usuario ingresa un entero negativo o una letra, le saldrá los error en las lineas 60 y 63
        p= ascii_letters                                                                                                   
        nquestions= input("¿Cuantas preguntas quieres crear?: ")                                                           
        if nquestions in p:                                                                                                
            raise ValueError("Solo se puede recibir numeros positivos, {0} ni siquiera es un numero.".format(nquestions))
        num_of_questions = int(nquestions)                                                                                  
        if num_of_questions <= 0:                                                                                          
            raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo".format(num_of_questions))
    
        for i in range(num_of_questions):                                                                                  #Por cada pregunta, se ejecuta este for loop
            print("\nQuestion",i + 1)
            Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ")                            #Aqui el usuario escribe la pregunta
            A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ")                                  #Aqui ingresa la respuesta CORRECTA a la pregunta
            A2 = input("\tPor favor ingrese una respuesta incorrecta: ")                                                   #Como un quiz tiene diferentes opciones de que escoger, aqui se ingresa una respuesta INCORRECTA que actuará como distractora 
            A3 = input("\tPor favor ingrese una respuesta incorrecta: ")                                                   #Aqui se ingresa la segeunda respuesta INCORRECTA 
            A4 = input("\tPor favor ingrese una respuesta incorrecta: ")                                                   #Aqui se ingresa la tercera respuesta INCORRECTA 
            A = A.lower()                                                                                                  #La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa 
            A2 = A2.lower()                                                                                                #La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa
            A3 = A3.lower()                                                                                                #La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa
            A4 = A4.lower()                                                                                                #La respuesta ingresada se cambia a minuscula para evitar confusion entra letra mayusculas y minusculas dentro del programa
            new_file.write(Q + ":" + A + ";" + A2 + ";" + A3 + ";" + A4 + "\n")                                            #Dentro del archivo, la pregunta y la respuesta correcta se separa via un ":" mientras que las respuesta incorrectas se separan por un ";"
        new_file.close()                                                                                                   #Cuando todas las preguntas con sus opciones de respuestas hayan sido escritas, entonces se cierra el archivo
        
        q4 = input("La creación del quiz ha finalizado ¿Desea tomar un repaso del quiz?: ")                                #Se le pregunta al usuario si quiere realizar un repaso del quiz para ver como quedo
        q4 = q4.upper()                                                                                                    #La respuesta se cambia a mayusculas para que el codigo entienda y evitar confusiones 
        
        if q4 == "SI":                                                                                                     #Si la respuesta guardada en la variable "q4" es "si", se ejecutaran las proximas 2 lineas de codigo
            FlashcardModule.Quiz_Review(file_name)                                                                         #Se implementa la funcion "Quiz_Review" que se encuentra dentro del modulo importado al principio del codigo
            print("\nHas terminado el quiz")                                                                               #Al terminar el repaso se imprime esta linea de codigo y el codigo termina 

        elif q4 == "NO":                                                                                                   #Si la respuesta es "no" se imprime el proximo mensaje
            print("Gracias por usar nuestro app. Tu quiz se salvó bajo el nombre que le asignaste al archivo para usarlo o mandarlo en otro tiempo.")
        
        elif q4 != "SI" or q2 != "NO":                                                                                     #Si el usuario no responde con un "si" o "no" entonces se muestra el error escrito en la siguiente linea 
            raise ValueError("Solo se admiten respuestas: si o no")
        
    elif q3 == "B2" or q3 == "b2":                                                                                         #Si la opcion que escogió el usuario es b2 (independiente de mayuscula o minuscula) entonces entra en el tramo de codigo indentado
        chosen_file = input("Por favor Ingrese el nombre del archivo: ")                                                   #Como la informacion se salvó en un archivo, entonces para accederlo, el codigo le pide al ususario que ingrese el nombre de dicho archivo
        FlashcardModule.Quiz_Review(chosen_file)                                                                           #Siempre cuando exista el archivo que el usuario ingresa, el nombre se ingresa en la funcion "Quiz_Review" 
        print("\nHas terminado repasando las cartas")                                                                      #Al terminar el quiz, se imprime esta linea de codigo y el codigo termina 
    
    else:                                                                                                                  #Si el usuario no responde con una de las dos opciones "b1" o "b2", se presenta el siguiente error  
        raise ValueError(" Solo hay dos opciones: B1 & B2, {0} no es una de ellas".format(q3))
        
elif option_question == "C" or option_question =="c":                                                                      #Si el usuario escoge la opcion C (independientemente si lo escribe con mayuscula o minuscula) entonces entra a este tramo de codigo   
    chosen_file = input("Por favor Ingrese el nombre del archivo: ")                                                       #Como las cartas se guardaron dentro de un archivo, entonces se le pide al usuario el nombre de dicho archivo para acceder a la informacion 
    FlashcardModule.Flashcard_Review(chosen_file)                                                                          #Siempre y cuando exista el archivo ingresado, el nombre se usa en la funcion "Flashcard_Review" 
    print("\nHas terminado de repasar las cartas")                                                                         #Al terminar el quiz, se imprime esta linea de codigo terminando el codigo
else:                                                                                                                      #Si el usuario pone una opcion que no sea A, B, C entocnes se imprime el error en la siguiente linea y termina el codigo 
    raise ValueError(" Solo hay tres opciones: A, B o C, {0} no es una de ellas".format(option_question))
    
