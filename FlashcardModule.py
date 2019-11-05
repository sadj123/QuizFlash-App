import random #Se importa la librearia Random ya que la usaremos a lo largo de nuestro modulo y por ende el codigo

def Flashcard_Review(file_name): #Se define la funcion llamada "Flashcard_Review" que después será incovacada en el master code. Lo que se será ingresado en la funcion es el nombre del archivo  
    file = open(str(file_name) + ".txt") #Ya teniendo el nombre del codigo, el programa habrerá el archivo
    lines = file.readlines() #El codigo lee el archivo linea por linea 

    q_and_a = {} #Se crea un diccionario vacio asignado a la variable "q_and_a"
    lista=[] #Se crea una lista vacia asignada a la variable "lista"
    count = 0 #Se crea un contador que va incrementando cada vez que el codigo pasa por el while loop en la linea 24
    count_right = 0 #Se crea un contador que incrementa cada vez que el usuario acerta la pregunta
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
            answer = q_and_a[pick] #La respuestase encuentra dentro de es 
            answer = answer[0]
            user_answer = user_answer.lower()            

            if user_answer == answer:
                print("¡Muy bien! Esa es la respuesta correcta ")
                lista.append(pick)
                count += 1
                count_right += 1

            elif user_answer == "":
                count += 1
                count_wrong += 1
                break
            
            else:
                print("La respuesta es incorrecta. La respuesta correcta es:", answer[0])
                lista.append(pick)
                count += 1
                count_wrong += 1

    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
   
    
def Quiz_Review(file_name): 
    file = open(str(file_name) + ".txt")
    lines = file.readlines()   
    
    rng = random.Random()
    q_and_a = {}
    lista=[]
    count = 0
    count_right = 0
    count_wrong = 0
    
    for i in lines:
        (Q,A)=i.split(":")
        p= A.split(";")
        z= len(p)
        k= p[z-1]
        k= k.strip()
        p.pop()
        p.append(k)
        q_and_a[Q] = p
        
    print("\nRecuerde que si quiere terminar, presiones ENTER. Al hacerlo, la respuesta automaticamente será incorrecta...")    
    while count < len(lines):    
        pick = random.choice(list(q_and_a.keys()))
        quiz_questions = q_and_a[pick]
        quiz_questions_2 = quiz_questions[:]
        dicto = {}
        
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
    
