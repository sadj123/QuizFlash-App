# FLASHCARD AND QUIZ APP FOR COMPUTER PROGRAMMING PROJECT 

import FlashcardModule
print("Bienvenido a la aplicacion de Flashcards y Quizzes")
print("------------------------------------- \n")
print("Las opciones son las siguientes:")
print("\n A: Crear una baraja de Flashcards \n B: Crear o tomar un Quiz \n C: Si ya tienes una baraja de flashcards y deseas repasarla(No adimte la opción con un quiz)")
option_question = input("Que opcion desearía ejecutar?: ")

if option_question == "A" or option_question == "a":
    file_name = input("Por favor ingrese el nombre con el cual desea salvar el archivo: ") 
    new_file = open(file_name + ".txt", "w") 
    num_of_cards = int(input("¿Cuantas cartas desea crear?: ")) 
    if num_of_cards < 0:
        raise ValueError("Solo se puede recibir numeros positivos, {0} no es positivo".format(num_of_cards))
        
    for i in range(num_of_cards):
        print("\nFlashcard",i + 1)
        Q = input("\tPor favor ingrese la pregunta (No utilice signos de interrogación): ")
        A = input("\tPor favor ingrese la respuesta correspondiente a la pregunta: ")
        A = A.lower()
        new_file.write(Q + ":" + A)
        c= input("\tSi la pregunta tiene otra respuesta ingresela aqui, sino solo presione ENTER: ")
        while c != "":
            new_file.write(";" + c)
            c= input("\tSi la pregunta tiene otra respuesta ingresela aqui, sino solo presione ENTER: ")
        new_file.write("\n")
    new_file.close()
    
    q2 = input("¿Desea tomar un repaso de las cartas?: ")
    q2= q2.upper()

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
        num_of_questions = int(input("¿Cuantas preguntas quieres crear?: ")) 
        if num_of_questions < 0:
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
    
