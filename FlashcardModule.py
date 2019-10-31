import random 

def Flashcard_Review(file_name):
    file = open(str(file_name) + ".txt")
    lines = file.readlines()

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
        if pick not in lista:
            print("\nPregunta", count+1,": " + "¿" + str(pick) + "?")
            user_answer = str(input("Respuesta: "))
            answer = q_and_a[pick]
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
    
