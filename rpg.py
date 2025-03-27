import random #Importa la libreria random para poder generar numeros aleatorios para el dado
import time  #Importa libreria time para hacer pausas de tiempo entre turnos


#Creamos la clase Heroe con sus atributos y métodos
class Heroe:
    def __init__(self, nombre,nombre_ataque01,nombre_ataque02):
        self.nombre = nombre
        self.ataque01=nombre_ataque01
        self.ataque02=nombre_ataque02
        self.valor_ataque01=2
        self.valor_ataque02=3        
        self.vida=10
        self.turno=False #El turno comienza en falso para luego ir rotando a verdadero según corresponda

    def saludar(self):
        print(f'Hola, soy el legendario héroe conocido como {self.nombre}')

    #Método para lanzar el dado rojo de 20 caras
    def dado_rojo(self):
        print(f'🎲 {self.nombre} lanza el dado rojo...')
        return random.randint(1,20)
    
    def  pausa_dramatica(self):#Método para hacer una pausa dramática de unos segundos
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")  

    def ataca_a(self, Enemigo):
        
        while True: #Bucle infinito que se rompe si la selección coincide con el número 1 o 2
            # Imprimir en color rojo
            print(f"\033[31m\n¡Vamos {self.nombre}! ¡Elige tu ataque!\n\033[0m")
    
            # Imprimir en color verde usando código ANSI
            print(f"\033[32m🏹 1.{self.ataque01}: -{self.valor_ataque01} de daño. Dado +5\033[0m")
            print(f"\033[32m🏹 2.{self.ataque02}: -{self.valor_ataque02} de daño. Dado +12\033[0m")
            
            ataque_seleccionado=int(input("\n> Ataco con: \n"))
            
            if ataque_seleccionado in (1,2):#Si el ataque coincide con los valores de la tupla salimos del bucle
                break
            else:#Si no coinde, imprime advertencia y continua el bucle
                print("\n\033[31mDebes seleccionar el número de ataque de deseas.(1 o 2)\033[0m\n")
                
                

        tirada=self.dado_rojo() #Tirada del dado rojo y almacenamiento en la variable en 1tirada

        self.pausa_dramatica() #Pausa dramática

        if ataque_seleccionado==1 and tirada>5:
            Enemigo.vida-=self.valor_ataque01
            print(f"Has atacado a {Enemigo.nombre} con {self.ataque01}.")
            self.pausa_dramatica() #Pausa dramática
            print(f"{Enemigo.nombre} ha perdido {self.valor_ataque01} puntos de vida. Aún le quedan {Enemigo.vida} puntos de vida.")
            self.pausa_dramatica() #Pausa dramática

        elif ataque_seleccionado==2 and tirada>12:

            Enemigo.vida-=self.valor_ataque02
            print(f"Has atacado a {Enemigo.nombre} con {self.ataque02}.")
            self.pausa_dramatica() #Pausa dramática
            print(f"{Enemigo.nombre} ha perdido {self.valor_ataque02} puntos de vida. Aún le quedan {Enemigo.vida} puntos de vida.")
            self.pausa_dramatica() #Pausa dramática
        else:
            print(f"Has fallado en tu ataque a {Enemigo.nombre}. Recuerda que debes introducir el número del ataque y superar la tirada de tu dado. Escribe 1 o 2 para atacar.")  
            self.pausa_dramatica() #Pausa dramática

class Enemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida=20
        self.ataque01="GOLPE AL AIRE"
        self.ataque02="FURIA DESCARNADA"
        self.ataque03="BOLAS DE FUEGO"
        self.ataque04="IRA DE DIOS"
        self.valor_ataque01=0
        self.valor_ataque02=1   
        self.valor_ataque03=2
        self.valor_ataque04=4   
        self.turno=False     

    def saludar(self):
        print(f'Hola, soy {self.nombre}')

    def dado_negro(self):
        print(f'\n🎲 {self.nombre} lanza el dado negro.\n')
        
        return random.randint(1,10)
    

    def ataca_a(self, Heroe):
        print(f"\n{self.nombre} ataca a {Heroe.nombre}")
        valor=self.dado_negro()
        if valor==10:
            Heroe.vida-=4   
            print(f"{Heroe.nombre} ha recibido {self.ataque04} y ha perdido {self.valor_ataque04} puntos de vida.")

        if 9 >= valor >=6:
            Heroe.vida-=2
            print(f"{Heroe.nombre} ha recibido {self.ataque03} y ha perdido {self.valor_ataque03} puntos de vida.")
        

        if 3 <= valor <= 5:
            Heroe.vida-=1
            print(f"{Heroe.nombre} ha recibido {self.ataque02} y ha perdido {self.valor_ataque02} puntos de vida.")

        
        if valor <= 2:
        
            print(f"¡{Heroe.nombre} ha esquivado el ataque de {self.nombre}!")


       
def combate(player01,player02):
    dado_p01=random.randint(1,12)
    dado_p02=random.randint(1,12)
#El siguiente condicional estable quién comienza atacando primero y lo alterna a lo largo del juego
    if dado_p01>dado_p02:
        player01.turno = True
        player02.turno = False
        print(f"\nEs el turno de ataque es de {player01.nombre}.")
        
    else:
        player01.turno = False
        player02.turno = True

    while player01.vida>0 and player02.vida>0:
        if player01.turno==True:
            player01.ataca_a(player02)
            player01.turno=False
            player02.turno=True
        else:
            player02.ataca_a(player01)
            player01.turno=True
            player02.turno=False
    
    # Determinar ganador
    if player01.vida > 0:
        print(f"¡{player01.nombre} ha ganado el combate!")
    else:
        print(f"¡{player02.nombre} ha ganado el combate!")

print("\n🏹 ¡Bienvenidos a Duelo Épico! 🏰\n")

nombre_player01=(input("> Nombre de tu héroe: ").upper())
ataque01_player01=(input("> Nombre de tu ataque +2: ").upper())
ataque02_player01=(input("> Nombre de tu ataque +4: ").upper())

nombre_player02=(input("> Nombre de tu enemigo: ").upper())

player01=Heroe(nombre_player01,ataque01_player01,ataque02_player01)
player02=Enemigo(nombre_player02)

combate(player01,player02) #Llama ala función combate() con contendientes como parámetro