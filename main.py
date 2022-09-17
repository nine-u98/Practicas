from functions import *

if __name__ == '__main__':
    print(f"""
{BLUE}Bienvenido a la trivia del Señor de los anillos
¿Quieres realizar este reto?
La trivia consta de 10 preguntas
{RESET}""")
    while True:
        inpt = input(RED+"\n¿Quieres iniciar? [Presiona (s/n)] "+RESET).lower().strip()
        if inpt:
            if inpt == 's' or inpt == 'si':
                for i in range(1,4):
                    print(i)
                    time.sleep(1)
                while True:
                    nom = input(MAGENTA + "Ingresa tu usuario : " +
                                RESET).lower().capitalize().strip()
                    if nom and len(nom) < 12:
                        banners()
                        trivia(data(), nom, aleatorynumber(data()))
                    else:
                        print(RED+"Valor muy largo"+RESET)
            elif inpt == 'n' or inpt == 'no':
                break
            else:
                print(RED+"\nValor ingresado incorrecto"+RESET)
