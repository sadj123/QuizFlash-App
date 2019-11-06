# FLASHCARD AND QUIZ APP FOR COMPUTER PROGRAMMING PROJECT 

import FlashcardModule #Como ya se creo el modulo "FlashcardModule" entonces, dentro de este codigo, se importara este modulo para usar funciones definidas alla
#Las siguientes 4 lineas solamente imprime la introduccion al codigo, dandole la bienvenida al usuario y mostrandole las opciones que puede escoger
print("Bienvenido a la aplicacion de Flashcards y Quizzes")
print("------------------------------------- \n")
print("Las opciones son las siguientes:")
print("\n A: Crear una baraja de Flashcards \n B: Crear o tomar un Quiz \n C: Si ya tienes una baraja de flashcards y deseas repasarla(No adimte la opción con un quiz)")
option_question = input("Que opcion desearía ejecutar?: ") # El codigo le pregunta al usuario cual de las opciones desea implementar y la guarda dentro de la variable "option_question"

if option_question == "A" or option_question == "a": #Si el usuario escoge la opcion A (independientemente si lo escribe con mayuscila o minuscula) entonces entre a este tramo de codigo
    file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ") #Aqui se le pide que el suuraio nombre el archivo donde se salvara la informacion para asi volver a usar la misma informacion despues 
    new_file = open(file_name + ".txt", "w")#Se abre el archivo con el nombre que le coloco el usuario y es un archivo en el cual se escribe (si el nombre del archivo ya existe, entonces editara ese archivo)
    from string import ascii_letters # Se importa la libreria string y solo se accede a la funcion de ascii_letters
    h= ascii_letters #h se vuelve entonces cualquier letra que se encuentra en la libreria importada
    ncards= input("¿Cuantas cartas desea crear?: ")#Se le pregunta al usuario cuantas cartas quiere hacer y se guarda a la variable "ncacrds"
    if ncards in h: #Entonces, si lo que ingreso el usuario no es un numero, el mensaje escrito en la proxima linea de codigo se muestra
        raise ValueError("Solo se puede recibir numeros positivos, {0} ni siquiera es un numero.".format(ncards))
    num_of_cards = int(ncards) #El umero de cartas se guerda en una nueva variable para evitar confusion y mejorar la legibilidad del codigo
    
    
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
        FlashcardModule.Flashcard_Review(file_name)
        print("\nHas terminado de repasar las cartas")

    elif q2 == "NO":
        print("Gracias por usar nuestro app. Tus cartas se salvaron bajo el nombre que le asignaste al archivo para usarlas en otro tiempo.")
        
    elif q2 != "SI" or q2 != "NO":
        raise ValueError("Solo se admiten respuestas: si o no")

elif option_question == "B" or option_question == "b":   
    print("\n B1: Crear un Quiz \n B2: Tomar un quiz")
    q3 = input("Que opcion desearía ejecutar?: ")
    if q3 == "B1" or q3 == "b1":
        file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ") 
        new_file = open(file_name + ".txt", "w") 
        from string import ascii_letters
        p= ascii_letters
        nquestions= input("¿Cuantas preguntas quieres crear?: ")
        if nquestions in p:
            raise ValueError("Solo se puede recibir numeros positivos, {0} ni siquiera es un numero.".format(nquestions))
        num_of_questions = int(nquestions) 
        if num_of_questions <= 0:
            raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo".format(num_of_questions))
    
        for i in range(num_of_questions):
            print("\nQuestion",i + 1)
            Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ")
            A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ")
            A2 = input("\tPor favor ingrese una respuesta incorrecta: ")
            A3 = input("\tPor favor ingrese una respuesta incorrecta: ")
            A4 = input("\tPor favor ingrese una respuesta incorrecta: ")
            A = A.lower()
            A2 = A2.lower()
            A3 = A3.lower()
            A4 = A4.lower()
            new_file.write(Q + ":" + A + ";" + A2 + ";" + A3 + ";" + A4 + "\n")
        new_file.close()
        
        q4 = input("La creación del quiz ha finalizado ¿Desea tomar un repaso del quiz?: ")
        q4 = q4.upper()
        
        if q4 == "SI":
            FlashcardModule.Quiz_Review(file_name)
            print("\nHas terminado el quiz")

        elif q4 == "NO":
            print("Gracias por usar nuestro app. Tu quiz se salvó bajo el nombre que le asignaste al archivo para usarlo o mandarlo en otro tiempo.")
        
        elif q4 != "SI" or q2 != "NO":
            raise ValueError("Solo se admiten respuestas: si o no")
        
    elif q3 == "B2" or q3 == "b2":
        #Aqui deberiamos crear otro modulo!
        chosen_file = input("Por favor Ingrese el nombre del archivo: ")
        FlashcardModule.Quiz_Review(chosen_file)
        print("\nHas terminado repasando las cartas")
    
    else: 
        raise ValueError(" Solo hay dos opciones: B1 & B2, {0} no es una de ellas".format(q3))
     
# Y la otra que es un archivo ojala ENCRIPTADO  para que los estudiantes no hagan trampa!!!!!!!!!!!! 
        
elif option_question == "C" or option_question =="c":
    chosen_file = input("Por favor Ingrese el nombre del archivo: ")
    FlashcardModule.Flashcard_Review(chosen_file)
    print("\nHas terminado de repasar las cartas")
else:
    raise ValueError(" Solo hay tres opciones: A, B o C, {0} no es una de ellas".format(option_question))
    
