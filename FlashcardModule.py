import random #Se importa la librearia Random ya que la usaremos a lo largo de nuestro modulo y por ende el codigo

def Flashcard_Review(file_name): #Se define la funcion llamada "Flashcard_Review" que después será incovacada en el master code. Lo que se será ingresado en la funcion es el nombre del archivo  
    file = open(str(file_name) + ".txt") #Ya teniendo el nombre del codigo, el programa habrerá el archivo
    lines = file.readlines() #El codigo lee el archivo linea por linea 

    q_and_a = {} #Se crea un diccionario vacio asignado a la variable "q_and_a"
    lista=[] #Se crea una lista vacia asignada a la variable "lista"
    count = 0 #Se crea un contador que va incrementando cada vez que el codigo pasa por el while loop en la linea 24
    count_right = 0 #Se crea un contador que incrementa cada vez que el usuario acierta la pregunta
    count_wrong = 0 #Se crea un contador que incrementa cada vez que el usuraio tenga una pregunta mala

    for i in lines: #Por cada linea que se encuentre en el archivo, el codigo ejecutará este ciclo for
        (Q,A)=i.split(":") #Dentro del archivo, la pregunta y la respuesta estan separadas por ":" entonces el metodo split logra separarlo
        p= A.split(";") #El codigo tiene la opcion de que la pregunta tiene mas de una respuesta entonces las otras respuestas esta separadas por ";" entonces el metodo split cumple la funcion de separlas 
        z= len(p) 
        k= p[z-1]
        k= k.strip()
        p.pop()
        p.append(k)
        q_and_a[Q] = p # Aqui las preguntas y sus respuestas van siendo agregadas al diccionario creado en la linea 7. La pregutnas se vuelve la llave y la respuesta el valor 

    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")
    while count < len(lines): #Como count = 0, el codigo entra dentro de este ciclo while. Solo saldra de este ciclo cuando count iguala al numero de lineas     
        pick = random.choice(list(q_and_a.keys())) #El random.choice elige una valor dentro de la lista de las llaves del diccionarios. Por ende escoge una pregunta al azar
        if pick not in lista: #Para prevenir que la misma pregunta se escogida al azar, las preguntas se van agregando a una lsita. El codigo va ejecutar los siguente siempre y cuando la pregunta no se repita
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?")
            user_answer = str(input("Respuesta: ")) #La respuesta que escriba el usuario se salva dentro de la variable "user_answer" 
            answer = q_and_a[pick] #La respuesta se encuentra dentro del diccionario que se crea en la linea 21 
            answer = answer[0] #Como hay la oportudinad de que haya mas de una respuesta, la respuesta se encuentra en el espacio 0 de la lista dentro de la llave del diccionario
            user_answer = user_answer.lower() #El answer.lower() cambia todas las letras a minusculas para asi evitar confusiones con mayusculas             

            if user_answer == answer: #Si la respuesta del usuario concuerda con la respuesta que tiene el codigo, entonces ejecta el proximo codigo 
                print("¡Muy bien! Esa es la respuesta correcta ")
                lista.append(pick) #Esta pregunta entonces se agrega a la lista para asegurar no vuelve a ser escogida aleatoreamente 
                count += 1 #El count se encrementa por 1
                count_right += 1 #Como la respuesta fue la corercta, el count_right tambien incrementa por 1

            elif user_answer == "": #El codigo tambien tiene en cuenta si el usuario no responde y presiona enter 
                count += 1 #Aun se encrementa el contador ya que la pregutnas fue mostrada al usuario 
                count_wrong += 1 #El codigo luego toma en cuenta la respuesta nula como una uncorrecta y por ende se incremente el contador count_wrong 
                break #Cuando se presiona entre como respuesta, el codigo se usa el break para salir del loop y ejecutar la primera linea afuera de el 
            
            else: #Esta es la opcion si la respuesta del usuario sea incorrecta 
                print("La respuesta es incorrecta. La respuesta correcta es:", answer[0]) #No solo le imprime el mensaje de que esta incorrecta pero tambien logra mostrarle al usuario la respuesta acertada 
                lista.append(pick) #Esta pregunta entonces se agrega a la lista para asegurar no vuelve a ser escogida aleatoreamente
                count += 1 #Aun se encrementa el contador ya que la pregutnas fue mostrada al usuario
                count_wrong += 1 #El codigo luego toma en cuenta la respuesta nula como una uncorrecta y por ende se incremente el contador count_wrong 

    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
    #La linea de arriba despues imprime los resultados de las preguntas correctas, incorrectas, y el porcentaje de efectividad 
   
    
def Quiz_Review(file_name): #Se defina la funcion llamada "Quiz_Review" que se innvoca desde el master code. Se ingresa el nombre del archivo
    file = open(str(file_name) + ".txt") #Ya teniendo el nombre del codigo, el programa habrerá el archivo
    lines = file.readlines() #El codigo lee el archivo linea por linea    
    
    rng = random.Random() #Creamos nuestro propio elemento random llamado rng y usando el constructor random.Random()
    q_and_a = {} #Se crea un diccionario vacio asignado a la variable "q_and_a"
    lista=[] #Se crea una lista vacia asignada a la variable "lista"
    count = 0 #Se crea un contador que va incrementando cada vez que el codigo pasa por el while loop en la linea 76
    count_right = 0 #Se crea un contador que incrementa cada vez que el usuario acierta la pregunta
    count_wrong = 0 #Se crea un contador que incrementa cada vez que el usuraio tenga una pregunta mala
    
    for i in lines:
        (Q,A)=i.split(":") #Dentro del archivo, la pregunta y la respuesta estan separadas por ":" entonces el metodo split logra separarlo
        p= A.split(";") #Como esta parte es de quizzes, entonces obligatoriamente tiene una respuesta correcta y tres malas que se separan por ";" 
        z= len(p) 
        k= p[z-1]
        k= k.strip()
        p.pop()
        p.append(k)
        q_and_a[Q] = p # Aqui las preguntas y sus respuestas van siendo agregadas al diccionario creado en la linea 59d. La pregutnas se vuelve la llave y la respuesta el valor 

        
    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")    
    while count < len(lines): #Como count = 0, el codigo entra dentro de este ciclo while. Solo saldra de este ciclo cuando count iguala al numero de lineas         
        pick = random.choice(list(q_and_a.keys()))  pick = random.choice(list(q_and_a.keys())) #El random.choice elige una valor dentro de la lista de las llaves del diccionarios. Por ende escoge una pregunta al azar
        quiz_questions = q_and_a[pick] # Esta variable entonces contiene las diferentes respuestas para la pregunta 
        quiz_questions_2 = quiz_questions[:] # Esta varaible entonces es un clon de la anteriori, por ende el uso de "[:]" ya que se usara para que las respuestas se muestren en orden aleatoriamente 
        dicto = {} #Se crea un nuevo diccionario vacio que se llama "dicto"
        
        if pick not in lista:
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?")
            
            choice_A = str((quiz_questions_2[rng.randrange(4)]))
            print("    A: " + choice_A.capitalize())
            quiz_questions_2.remove(choice_A)
            dicto[choice_A] = "A"
            
            choice_B = str((quiz_questions_2[rng.randrange(3)]))
            print("    B: " + choice_B.capitalize())
            quiz_questions_2.remove(choice_B)
            dicto[choice_B] = "B"
            
            choice_C = str((quiz_questions_2[rng.randrange(2)]))
            print("    C: " + choice_C.capitalize())
            quiz_questions_2.remove(choice_C)
            dicto[choice_C] = "C"
            
            choice_D = str((quiz_questions_2[rng.randrange(1)]))
            print("    D: " + choice_D.capitalize())
            dicto[choice_D] = "D"
            
            quiz_answer = dicto[quiz_questions[0]]
            user_quiz_answer = input("Respuesta entre A, B, C, o D: ")
            user_quiz_answer = user_quiz_answer.upper()
            
            if user_quiz_answer == quiz_answer:
                print("¡Muy bien! Esa es la respuesta correcta. ")
                lista.append(pick)
                count += 1
                count_right += 1
                
            elif user_quiz_answer == "":
                count += 1
                count_wrong += 1
                break
            
            else:
                print("La respuesta es incorrecta. La respuesta correcta es: ", quiz_answer)
                lista.append(pick)
                count += 1
                count_wrong += 1
                
    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
    
