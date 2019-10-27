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

    while count < len(lines):    
        pick = random.choice(list(q_and_a.keys()))
        if pick not in lista:
            print("\nPregunta", count+1, ": " + "¿" + str(pick) + "?")
            user_answer = str(input("Respuesta: "))
            answer = q_and_a[pick]
            user_answer = user_answer.lower()            

            if user_answer in answer:
                print("¡Muy bien! Esa es la respuesta correcta ")
                lista.append(pick)
                count += 1
                count_right += 1

            elif user_answer == "":
                break
            
            else:
                print("La respuesta es incorrecta. La respuesta correcta es:", answer)
                lista.append(pick)
                count += 1
                count_wrong += 1

    print("\nTus resultados son los siguientes:\n\n Respuestas correctas: {0}\n Respuestas incorrectas: {1}\n Puntuación: {2}/{3}\n Porcentaje: {4}% de las preguntas bien".format(count_right, count_wrong, count_right,count,int((count_right/count)*100)))
