import random #Se importa la librearia Random la cual usaremos a lo largo de nuestro modulo y por ende el codigo

def Flashcard_Review(file_name): #Se define la funcion llamada "Flashcard_Review" que después será incovacada en el master code. La funcion recibirá el nombre del archivo  
    file = open(str(file_name) + ".txt") #Ya teniendo el nombre del archivo, el programa habrerá para después leer el contenido
    lines = file.readlines() #El codigo lee el archivo linea por linea 

    q_and_a = {} #Se crea un diccionario vacio asignado a la variable "q_and_a"
    lista=[] #Se crea una lista vacia asignada a la variable "lista"
    count = 0 #Se crea un contador que va incrementando cada vez que el codigo pasa por el while loop en la linea 24
    count_right = 0 #Se crea un contador que incrementa cada vez que el usuario acierta la pregunta
    count_wrong = 0 #Se crea un contador que incrementa cada vez que el usuraio tenga una pregunta mala

    for i in lines: #Como el codigo recorre todo el archivo, por cada linea en el archivo, el codigo ejecutará este ciclo for
        (Q,A)=i.split(":") #Dentro del archivo, la pregunta y la respuesta estan separadas por ":" entonces el metodo split logra que el codigo entienda cual es la pregutna y cual es la respuesta de las cartas 
        p= A.split(";") #El codigo tiene la opcion de que la pregunta tenga mas de una respuesta, entonces las otras respuestas estan separadas por ";" de nuevo el metodo split cumple la funcion de separlas 
        z= len(p)### 
        k= p[z-1]###
        k= k.strip()###
        p.pop()###
        p.append(k)###
        q_and_a[Q] = p # Aqui las preguntas y sus respuestas van siendo agregadas al diccionario creado en la linea 7. La pregutnas se vuelve la llave y la respuesta el valor del diccionario 

    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")
    while count < len(lines): #Como count = 0 al principio del codigo, el codigo entra dentro de este ciclo while siempre cuando el count sea menor que el numero de lineas en el archivo. Solo saldra de este ciclo cuando count iguala al numero de lineas     
        pick = random.choice(list(q_and_a.keys())) #El random.choice elige una valor dentro de la lista de las llaves del diccionarios. Por ende escoge una preguntade las cartas al azar
        if pick not in lista: #Para prevenir que la misma pregunta sea escogida al azar, las preguntas se van agregando a una lista. El codigo va ejecutar las siguentes lineas siempre y cuando la pregunta no se repita cuando se escoge
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?")
            user_answer = str(input("Respuesta: ")) #La respuesta que escriba el usuario se salva dentro de la variable "user_answer" 
            answer = q_and_a[pick] #La respuesta de la pregunta escogida se encuentra dentro del diccionario que se crea en la linea 21 
            answer = answer[0] #Como hay la oportudinad de que haya mas de una respuesta, la respuesta se encuentra en el espacio 0 de la lista
            user_answer = user_answer.lower() #Se cambian todas las letras a minusculas para evitar confusiones con mayusculas             

            if user_answer == answer: #Si la respuesta del usuario concuerda con la respuesta que tiene el codigo, entonces ejecta el codigo dentro del if statment 
                print("¡Muy bien! Esa es la respuesta correcta ")
                lista.append(pick) #Esta pregunta entonces se agrega a la lista para asegurar no vuelve a ser escogida aleatoreamente a la hora de repasar 
                count += 1 #El count se encrementa por 1
                count_right += 1 #Como la respuesta fue la corercta, el count_right tambien incrementa por 1

            elif user_answer == "": #El codigo tambien tiene en cuenta si el usuario presiona enter (no responde) 
                count += 1 #Se encrementa el contador ya que el codigo aun le muestra la pregunta al usuario, solo que el usuario decide no responder 
                count_wrong += 1 #El codigo luego toma en cuenta la respuesta nula como una incorrecta y por ende se incremente el contador count_wrong por 1 
                break #Cuando se presiona entre como respuesta, el codigo ejecuta el break para salir del loop. Despues de salir del loop, se ejecuta la primera linea afuera 
            
            else: #Si la respuesta es incorrecta, se ejectua este tramo de codigo 
                print("La respuesta es incorrecta. La respuesta correcta es:", answer[0]) #No solo le imprime el mensaje de que esta incorrecta la respuesta pero tambien logra mostrarle al usuario la respuesta acertada 
                lista.append(pick) #Esta pregunta entonces se agrega a la lista para asegurar de que no vuelve a ser escogida aleatoreamente en la linea 25
                count += 1 #El count se incrementa
                count_wrong += 1 #Como la respuesta estuvo incorrecta se incremente el contador count_wrong 

    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
    #La linea de arriba imprime los resultados de las preguntascorrectas, incorrectas, y el porcentaje de efectividad despues de haber tomado el repaso de cartas  
   
    
def Quiz_Review(file_name): #Se defina la funcion llamada "Quiz_Review" que se innvoca desde el master code. El nombre del archivo es el que se ingresa a la funcion 
    file = open(str(file_name) + ".txt") #Ya teniendo el nombre del archivo, el programa habrerá para después leer el contenido   
    lines = file.readlines() #El codigo lee el archivo linea por linea    
    
    rng = random.Random() #Creamos nuestro propio elemento random llamado rng usando el constructor random.Random(). Se crea para facilitar el uso de los metodos de la libreria random
    q_and_a = {} #Se crea un diccionario vacio asignado a la variable "q_and_a"
    lista=[] #Se crea una lista vacia asignada a la variable "lista"
    count = 0 #Se crea un contador que va incrementando cada vez que el codigo pasa por el while loop en la linea 76
    count_right = 0 #Se crea un contador que incrementa cada vez que el usuario acierta la pregunta
    count_wrong = 0 #Se crea un contador que incrementa cada vez que el usuraio tenga una pregunta mala
    
    for i in lines:
        (Q,A)=i.split(":") #Dentro del archivo, la pregunta y la respuesta estan separadas por ":" entonces el metodo split logra separarlos en las dos partes respectivamente
        p= A.split(";") #Como esta parte es de quizzes, entonces obligatoriamente tiene una respuesta correcta y tres malas que actuan como discractoras que se separan por ";" 
        z= len(p)### 
        k= p[z-1]###
        k= k.strip()###
        p.pop()###
        p.append(k)###
        q_and_a[Q] = p # Aqui las preguntas y sus respuestas van siendo agregadas al diccionario creado en la linea 59. La pregunta se vuelve la llave y la respuesta el valor del diccionario

        
    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")    
    while count < len(lines): #Como count = 0, el codigo entra dentro de este ciclo while siempre y cuando count sea menor que el numero de lineas. Solo saldra de este ciclo cuando count iguala al numero de lineas         
        pick = random.choice(list(q_and_a.keys())) #El random.choice elige una valor dentro de la lista de las llaves del diccionarios. Por ende escoge una pregunta al azar
        quiz_questions = q_and_a[pick] # Esta variable contiene las diferentes opciones de respuestas para la pregunta 
        quiz_questions_2 = quiz_questions[:] # Esta varaible es un clon de la anterior, por ende el uso de "[:]" ya que se usará para que las respuestas siempre se muestren en orden aleatoriamente 
        dicto = {} #Se crea un nuevo diccionario vacio que se llama "dicto"
        
        if pick not in lista: #Para prevenir que la misma pregunta se escogida al azar, las preguntas se van agregando a una lista. El codigo va ejecutar las siguentes lineas siempre y cuando la pregunta no se repita
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?"
                  
            #Como van haber cuatro opciones,entonces el siguente tramo de codigo mustra como las respuestas se asignan aleatoriamente a las letras A,B,C o D para asi conformar el quiz y que cada vez, la respusta se encuentra en una diferente letra 
            choice_A = str((quiz_questions_2[rng.randrange(4)])) #De la lista "quiz_questions_2" que contiene las 4 opciones de respuesta, una se escogera via el uso del randrange ya que escoge un numero aleatorio en el rango 4 (porque hay 4 opciones) y el numer escogido corresponde al espacio en la lista 
            print("    A: " + choice_A.capitalize())
            quiz_questions_2.remove(choice_A) #Para evitar repeticiones, la pregunta que se escogió se remueve de la lista
            dicto[choice_A] = "A" #se agraga la pregunta como la clave y la opcion "A" como el valor en el diccionario "dicto" 
            
            choice_B = str((quiz_questions_2[rng.randrange(3)])) #la segunda opcion se obtiene denuevo de la lista, como ahora tiene 3 elementos, se escogera un numero del rango de 3
            print("    B: " + choice_B.capitalize())
            quiz_questions_2.remove(choice_B) #Para evitar repeticiones, la pregunta que se escogio se remueve de la lista
            dicto[choice_B] = "B" #se agraga la pregunta como la clave y la opcion "B" como el valor en el diccionario "dicto"
            
            choice_C = str((quiz_questions_2[rng.randrange(2)])) #La tercera opcion se obtiene de la lista que ahora contiene 2 elementos entonces se escoge un numero en el rango de 2
            print("    C: " + choice_C.capitalize())
            quiz_questions_2.remove(choice_C) #Para evitar repeticiones, la pregunta que se escogio se remueve de la lista
            dicto[choice_C] = "C" #se agraga la pregunta como la clave y la opcion "C" como el valor en el diccionario "dicto"
            
            choice_D = str((quiz_questions_2[rng.randrange(1)])) #Como solo queda un elemento dentro de la lista, entonces este se vuevlve la ultima opcion de las respuestas 
            print("    D: " + choice_D.capitalize())
            dicto[choice_D] = "D" #se agraga la pregunta como la clave y la opcion "D" como el valor en el diccionario "dicto"
            
            quiz_answer = dicto[quiz_questions[0]] #El codigo guarda en la variable "quiz_answer" la respuesta correcta. tiene [0] porque un quiz esta conformado por 4 opciones de respuestas pero solo la primera respuesta dada es correcta 
            user_quiz_answer = input("Respuesta entre A, B, C, o D: ")
            user_quiz_answer = user_quiz_answer.upper() #Como las respuestas son A,B,C o D, entonces usamos el .upper() para que siempran sean mayusculas. Si el usuario ingresa b minuscula como opcion, entonces el codigo automaticamente lo cambiara a mayuscula para asi evita problemas
            
            if user_quiz_answer == quiz_answer: #Si la respuesta del usuario es correcta, entonces ejecuta el siguente codigo  
                print("¡Muy bien! Esa es la respuesta correcta. ")
                lista.append(pick) #La pregunta se agrega a la lista para evitar repeticiones 
                count += 1 #Se incrementa por 1 ya que se respondio la pregunta
                count_right += 1 #Como el usuario acerto, entonces se incrementa por 1 el numero de preguntas correctas 
                
            elif user_quiz_answer == "": #El codigo tambien tiene en cuenta si el usuario no responde y presiona enter 
                count += 1 #Aun se encrementa el contador ya que la pregutnas fue mostrada al usuario 
                count_wrong += 1 #El codigo luego toma en cuenta la respuesta nula como una incorrecta y por ende se incremente el contador count_wrong 
                break #Cuando se presiona entre como respuesta, el codigo ejecuta el break para salir del loop y ejecutar la primera linea de codigo afuera
            
            else: #Esta es la opcion si la respuesta del usuario es incorrecta 
                print("La respuesta es incorrecta. La respuesta correcta es: ", quiz_answer) #No solo le imprime el mensaje de que esta incorrecta pero tambien logra mostrarle al usuario la respuesta acertada (muestra que opcion era, es decir si fue A,B,C, o D) 
                lista.append(pick) #Esta pregunta entonces se agrega a la lista para asegurar no vuelve a ser escogida aleatoreamente
                count += 1 #Aun se encrementa el contador ya que la pregutnas fue mostrada al usuario
                count_wrong += 1 #El codigo incremente el contador count_wrong por 1 
                
    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
    #La linea de arriba despues imprime los resultados de las preguntas correctas, incorrectas, y el porcentaje de efectividad despues de haber tomado el quiz
