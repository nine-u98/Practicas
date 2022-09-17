import random
import time
from colors import *
from data import *


# Funcion random me retorna una lista con numeros random agregados sin repetirse

def aleatorynumber(data):
    i, lista = 0, []
    while i < len(data):
        L = random.randint(0, len(data))
        if L not in lista:
            lista.append(L)
            i += 1
    return lista

# Funcion trivia contiene toda la logica de la trivia


def trivia(data, nombre, aleatory):
    count, incorrectos, score = 0, 0, 0
    """ Creo un ciclo que recorra mi lista de numeros aleatorios sin repeticion"""
    for num in aleatory:
        for item in data[num]:  # Recorre los elementos que esten en data[i]
            if isinstance(item, dict):  # Si el elemento e es de tipo dict entonces ejecuta el bloque
                # recorre el diccionario en busca de las opciones - la key result
                for key in item:
                    if key != 'result':  # Si es diferente a result ejecuta el codigo
                        # Imprime la key y la pregunta item[key]
                        print(
                            f"{GREEN}{key}){RESET} {MAGENTA}{item[key]}{RESET}")
                    else:
                        # Evalua la respuesta
                        while True:
                            opcion = input(f"{YELLOW}>>> {RESET}").lower().strip()

                            if opcion == 'x':  # Opcion especial
                                while True:  # Valide el input
                                    inpt = input(
                                        CYAN+"Deseas ver las respuestas [Presiona (s/n)] "+RESET).lower().strip()
                                    if inpt:
                                        if inpt == 's':
                                            # number al rango de (0, len(data) retorna 10 - 9 )
                                            for number in range(len(data)):
                                                print(
                                                    f"{BLUE}{''.join(data[number][0])}{RESET}" + f" respuesta : {GREEN}{data[number][1]['result']}{RESET}")  # Imprime la key y la pregunta uso join para convertir la lista a str
                                            exit()
                                        elif inpt == 'n':
                                            exit()
                                        else:
                                            print(
                                                RED+"Valor ingresado incorrecto"+RESET)

                            elif opcion == 'exit' or opcion == 'salir':  # Opcion exit
                                exit()
                            # recorre la opcion ingresada este en las opciones establecidas en data
                            # Tambien se puede poner >> n in ['a', 'b', 'c', 'd']
                            elif opcion in list(item.keys())[:-1]:
                                # Se compara la opcion con el item[key]
                                if opcion == item[key]:
                                    count += 1
                                    score += 10
                                    print(GREEN+'Correcto'+RESET)
                                    time.sleep(1.0)
                                    break
                                else:
                                    incorrectos += 1
                                    score -= 10
                                    print(RED+"Incorrecto"+RESET)
                                    time.sleep(1.0)
                                    break
                            else:  # En el caso que no sea una opcion establecida en data ni en las opciones te pedira volver a ingresar ya que el bucle es while True y solo en las opciones tiene un break
                                print(
                                    RED+"Valor ingresado incorrecto vuelve ingresar un valor"+RESET)
            else:  # Imprime todo lo que no sea diccionario
                # join convierte una lista a str
                print(f'\n{YELLOW}{"".join(item)}{RESET}')
                time.sleep(1.0)
    # Imprime los resultado
    print(f"""

{RED}{'*' * 5} Resultados : de {RESET}{YELLOW}{nombre}{RESET}
\n{GREEN}correcto' :{RESET} {YELLOW}{count}{RESET}
{GREEN}incorrecto' :{RESET} {YELLOW}{incorrectos}{RESET}
{BLUE}{nombre} {RESET}{WHITE}tu puntuacion es :{RESET} {YELLOW}{score}{RESET}
""")
    # Condicional evalua si se desea volver a ejecutar la trivia
    #trivia(data, nombre, aleatory) if input(CYAN+"¿Deseas volver intentar la trivia? [s]  "+RESET)  == 's' else print(WHITE+"\nEspero que lo hayas pasado muy bien, hasta pronto."+RESET)

    while True:  # Valide el input
        inpt = input(
            CYAN+"¿Deseas volver intentar la trivia? [Presiona (s/n)] "+RESET).lower().strip()
        if inpt:
            if inpt == 's':
                trivia(data, nombre, aleatory)
            elif inpt == 'n':
                print(WHITE+"\nEspero que lo hayas pasado muy bien, hasta pronto."+RESET)
                exit()
            else:
                print(RED+"Valor ingresado incorrecto"+RESET)


# La funcion banners recorre banner.txt, lo uso como inicio a la trivia
def banners():
    banners = ['./resources/banner.txt']
    for i in banners:
        with open(i) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                print(MAGENTA+line+RESET)
            time.sleep(1.0)
