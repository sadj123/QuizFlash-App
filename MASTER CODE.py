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

    if q2 == "SI":                                                                                                         #Si la respuesta es "si" se ejecutan las lineas 40-41 que acceden a la funcion Flashcard_Review   
        FlashcardModule.Flashcard_Review(file_name)                                                                        
        print("\nHas terminado de repasar las cartas")                                                                     

    elif q2 == "NO":                                                                                                       #Si la respuesta es "no", entonces se termina el programa e imprime el mensaje en la linea 44
        print("Gracias por usar nuestra app. Tus cartas se salvaron bajo el nombre que le asignaste al archivo para usarlas en otro tiempo.")
        
    elif q2 != "SI" or q2 != "NO":                                                                                         #Si el usuario responde algo que no sea "si" o "no", entonces se le presenta el error expresado en la linea 47 
        raise ValueError("Solo se admiten respuestas: si o no")

elif option_question == "B" or option_question == "b":                                                                     #Si el usuario escoge la opcion B entonces se ejecuta el bloque de codigo de la linea 50 hasta 98   
    print("\n B1: Crear un Quiz \n B2: Tomar un quiz")                                                                     
    q3 = input("Que opcion desearía ejecutar?: ")                                                                          
    
    if q3 == "B1" or q3 == "b1":                                                                                           # Si la opcion que escogio el usuario es b1 entonces el programa ejecuta el bloque de codigo de la linea 53 hasta la 90 
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
    
        for i in range(num_of_questions):                                                                                  #Por cada numero de preguntas, se ejecutan las lineas 65 hasta 77 
            print("\nQuestion",i + 1)                                                                                      # Que le pregunta al usuario ingresar la pregunta y las cuatro posibles respuestas del quiz
            Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ")                            # Teniendo en cuenta de que la primera res´puesta es la correcta mientras las otras tres son incorrectas y actuan como distractoras  
            A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ")                                  # Al final, todo lo que ingrese el usuario se salva dentro del archivo, y el archivo se cierra
            A2 = input("\tPor favor ingrese una respuesta incorrecta: ")                                                    
            A3 = input("\tPor favor ingrese una respuesta incorrecta: ")                                                    
            A4 = input("\tPor favor ingrese una respuesta incorrecta: ")                                                    
            A = A.lower()                                                                                                  
            A2 = A2.lower()                                                                                                
            A3 = A3.lower()                                                                                                
            A4 = A4.lower()                                                                                                
            new_file.write(Q + ":" + A + ";" + A2 + ";" + A3 + ";" + A4 + "\n")                                            
        new_file.close()                                                                                                   
        
        q4 = input("La creación del quiz ha finalizado ¿Desea tomar un repaso del quiz?: ")                                #Se le pregunta al usuario si quiere realizar un repaso del quiz para ver como quedo
        q4 = q4.upper()                                                                                                     
        
        if q4 == "SI":                                                                                                     #Si la respuesta es "si", se ejecutaran las lineas 83 a 84, donde se accede a la funcion Quiz_Review 
            FlashcardModule.Quiz_Review(file_name)                                                                         
            print("\nHas terminado el quiz")                                                                                

        elif q4 == "NO":                                                                                                   #Si la respuesta es "no" se imprime el mensaje en la linea 87
            print("Gracias por usar nuestro app. Tu quiz se salvó bajo el nombre que le asignaste al archivo para usarlo o mandarlo en otro tiempo.")
        
        elif q4 != "SI" or q2 != "NO":                                                                                     #Si el usuario no responde con un "si" o "no" entonces se muestra el error escrito en la linea 90 
            raise ValueError("Solo se admiten respuestas: si o no")
        
    elif q3 == "B2" or q3 == "b2":                                                                                         #Si la opcion que escogió el usuario es b2 entonces el programa ejecuta el bloque de codigo encontrado de la lina 92 hasta la 98 
        chosen_file = input("Por favor Ingrese el nombre del archivo: ")                                                   #Como la informacion se salvó en un archivo, entonces  el nombre de dicho archivo se usa en la funcion Quiz_Review 
        FlashcardModule.Quiz_Review(chosen_file)                                                                            
        print("\nHas terminado repasando las cartas")                                                                      
    
    else:                                                                                                                  #Si el usuario no responde con una de las dos opciones "b1" o "b2", se presenta el error en la linea 98  
        raise ValueError(" Solo hay dos opciones: B1 & B2, {0} no es una de ellas".format(q3))
        
elif option_question == "C" or option_question =="c":                                                                      #Si el usuario escoge la opcion C entonces ejecuta las lineas 100 hasta 105  
    chosen_file = input("Por favor Ingrese el nombre del archivo: ")                                                       # Donde se acceden a las cartas guardadas en un archivo. Cuyo nombre entra a la funcion Flashcard_Review
    FlashcardModule.Flashcard_Review(chosen_file)                                                                          
    print("\nHas terminado de repasar las cartas")                                                                         
else:                                                                                                                      #Si el usuario pone una opcion que no sea A, B, C entonces se imprime el error en la linea 105 
    raise ValueError(" Solo hay tres opciones: A, B o C, {0} no es una de ellas".format(option_question))
    
