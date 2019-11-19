import random                                                                    #Se importa la librearia Random 

def Flashcard_Review(file_name):                                                 #Se define la funcion Flashcard_Review. La funcion recibibe el nombre del archivo y ejecute las lineas de codigo 3 hasta 50  
    file = open(str(file_name) + ".txt")                                         #El programa abre el archivo y lo lee lina por linea 
    lines = file.readlines()                                                      

    q_and_a = {}                                                                 #Se crea un diccionario vacio 
    lista=[]                                                                     #Se crea una lista vacia 
    count = 0                                                                    #De la linea 9 a 11 se crean 3 contadores, uno en general y los otros dos que cuentas las preguntas acertadas y las preguntas incorrectas
    count_right = 0                                                              
    count_wrong = 0                                                              

    for i in lines:                                                              #Por cada linea en el archivo, el codigo ejecutará las lineas 13 a 21
        (Q,A)=i.split(":")                                                       # el metodo split logra separa la pregunta y la respuesta correcta por ":" 
        p= A.split(";")                                                          # y si hay mas de una respuesta, se separan con ";"    
        z= len(p)                                                                # Z el la cantidad de respuestas que hay y k es el ultimo elemento de la lista
        k= p[z-1]                                                                # Para evitar confusion, el metodo split logra quitar cualquier espacio o enter 
        k= k.strip()                                                             # A La lista de respuestas, se elimina el ultimo elemento y se le agrega la ultima respuesta modificada
        p.pop()                                                                  # En la linea 21 Las preguntas y sus respuestas van siendo agregadas al diccionario
        p.append(k)                                                             
        q_and_a[Q] = p                                                            

    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")
    while count < len(lines):                                                    # Mientras el contador es menor que el numero de lineas, las lineas 24 a 47 se ejecutan      
        pick = random.choice(list(q_and_a.keys()))                               #El random.choice elige un elemento aleatoriamente dentro de la lista de las llaves del diccionarios (las preguntas)
        if pick not in lista:                                                    # y para prevenir que la misma pregunta sea escogida al azar, las preguntas se van agregando a una lista
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?")
            user_answer = str(input("Respuesta: "))                              
            answer = q_and_a[pick]                                               #La respuesta de la pregunta escogida se encuentra dentro del diccionario y se va compara con la respuesta del usuario 
            user_answer = user_answer.lower()                                               

            if user_answer in answer:                                            #Si la respuesta del usuario concuerda con la respuesta que tiene el codigo, entonces ejecta las lineas 32 a 36 
                print("¡Muy bien! Esa es la respuesta correcta ")                #Donde se agrega la pregunta a la lista para evitar repeticion, se incrementa el numero de erspuestas y de respuestas correctas 
                lista.append(pick)                                                
                count += 1                                                       
                count_right += 1                                                 

            elif user_answer == "":                                              #Si el usuario presiona enter (no responde), se incrementa el numero de pregutnas y el de respuesta incorrectas. Tambien sale del loop  
                count += 1                                                        
                count_wrong += 1                                                  
                break                                                             
            
            else:                                                                #Si la respuesta es incorrecta, se ejectun las lineas 44 a 47  
                print("La respuesta es incorrecta. La respuesta correcta es:", str(answer))  
                lista.append(pick)                                               # Donde se agreaga la pregutna a la lista para evitar repeticion y tambien le dice al usuario la respuesta correcta 
                count += 1                                                       # Se incrementa el contador de preguntas y el contador de respuestas incorrectas 
                count_wrong += 1                                                 

    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
    #La linea 49 imprime los resultados   
   
    
def Quiz_Review(file_name):                                                      #Se defina la funcion llamada Quiz_Review. La funcion recibibe el nombre del archivo y ejecute las lineas de codigo 53 hasta 124  
    file = open(str(file_name) + ".txt")                                         #El programa abre el archivo y lo lee lina por linea   
    lines = file.readlines()                                                         
    
    rng = random.Random()                                                        #Creamos nuestro propio elemento random llamado rng 
    q_and_a = {}                                                                 #Se crea un diccionario vacio
    lista=[]                                                                     #Se crea una lista vacia 
    count = 0                                                                    #De la linea 60 a 62 se crean 3 contadores, uno en general y los otros dos que cuentas las preguntas acertadas y las preguntas incorrectas
    count_right = 0                                                              
    count_wrong = 0                                                              
    
    for i in lines:                                                              #Por cada linea en el archivo, el codigo ejecutará las lineas 65 a 72
        (Q,A)=i.split(":")                                                       # el metodo split logra separa la pregunta y la respuesta correcta por ":" y las otras opciones del quiz con ";" 
        p= A.split(";")                                                          # Z el la cantidad de respuestas que hay y k es el ultimo elemento de la lista 
        z= len(p)                                                                # Para evitar confusion, el metodo split logra quitar cualquier espacio o enter 
        k= p[z-1]                                                                # A La lista de respuestas, se elimina el ultimo elemento y se le agrega la ultima respuesta modificada
        k= k.strip()                                                             # En la linea 72 Las preguntas y sus respuestas van siendo agregadas al diccionario
        p.pop()                                                                  
        p.append(k)                                                              
        q_and_a[Q] = p                                                           

        
    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")    
    while count < len(lines):                                                    #Mientras el contador es menor que el numero de lineas, las lineas 76 a 124 se ejecutan         
        pick = random.choice(list(q_and_a.keys()))                               #El random.choice elige un elemento aleatoriamente dentro de la lista de las llaves del diccionarios (las preguntas)
        quiz_questions = q_and_a[pick]                                           #Esta variable contiene las diferentes opciones de respuestas para la pregunta. Se clona para facilitar que las opciones se muestren en un orde aleatorio  
        quiz_questions_2 = quiz_questions[:]                                      
        dicto = {}                                                               #Se crea un nuevo diccionario 
        
        if pick not in lista:                                                    #Para prevenir que la misma pregunta sea escogida al azar, las preguntas se van agregando a una lista
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?")
                  
             
            choice_A = str((quiz_questions_2[rng.randrange(4)]))                 #De la linea 86 a 107, de la lista "quiz_questions_2" que contiene las 4 opciones de respuesta, una de ella se escoge aleatoriamente 
            print("    A: " + choice_A.capitalize())                             #Para evitar repeticiones, la pregunta que se escogió se remueve de la lista y por ende se le resta 1 al numero de opciones
            quiz_questions_2.remove(choice_A)                                    #Se agraga la pregunta como la clave y la opcion correspondiente (A,B,C o D) como el valor en el diccionario "dicto" 
            dicto[choice_A] = "A"                                                #Este proceso se repite hasta que todas las opciones tengan respuesta  
            
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
            
            quiz_answer = dicto[quiz_questions[0]]                               #El codigo guarda en la variable "quiz_answer" la respuesta correcta 
            user_quiz_answer = input("Respuesta entre A, B, C, o D: ")
            user_quiz_answer = user_quiz_answer.upper()                          
            
            if user_quiz_answer == quiz_answer:                                  #Si la respuesta del usuario es correcta, entonces ejecuta las lineas 109 a 113  
                print("¡Muy bien! Esa es la respuesta correcta. ")
                lista.append(pick)                                               #La pregunta se agrega a la lista para evitar repeticiones y se incrementa el contador de preguntas y respuesta correctas  
                count += 1                                                       
                count_right += 1                                                  
                
            elif user_quiz_answer == "":                                         #Si el usuario no responde y presiona enter, se incrementa el numero de preguntas y el de respuestas incorrectas. Tambien sale del loop 
                count += 1                                                       
                count_wrong += 1                                                  
                break                                                            
            
            else:                                                                #Esta es la opcion si la respuesta del usuario es incorrecta 
                print("La respuesta es incorrecta. La respuesta correcta es: ", quiz_answer)  
                lista.append(pick)                                               #Donde se agreaga la pregutna a la lista para evitar repeticion y tambien le dice al usuario la respuesta correcta 
                count += 1                                                       #Se incrementa el contador de preguntas y el contador de respuestas incorrectas
                count_wrong += 1                                                 
                
    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
    #La linea 126 imprime los resultados 
