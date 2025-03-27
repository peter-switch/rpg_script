import random #importa la libreria random para poder generar numeros aleatorios para el dado
import time  # Para hacer pausas entre turnos

class Heroe:
    def __init__(self, nombre,nombre_ataque01,nombre_ataque02):
        self.nombre = nombre
        self.ataque01=nombre_ataque01
        self.ataque02=nombre_ataque02
        self.valor_ataque01=2
        self.valor_ataque02=3        
        self.vida=10
        self.turno=False

    def saludar(self):
        print(f'Hola, soy {self.nombre}')


    def dado_rojo(self):
        print(f'{self.nombre} lanza dado rojo')
        return random.randint(1,20)
    
    def  pausa_dramatica(self):
            
            print(".", end="")
            time.sleep(1.5)
            print(".", end="")
            time.sleep(1.5)
            print(".")  

    def ataca_a(self, Enemigo):
        print(f"\nTurno de {self.nombre}. ¡Elige tu ataque!")
        print(f"1.{self.ataque01}:{self.valor_ataque01} de daño. Dado +5")
        print(f"2.{self.ataque02}:{self.valor_ataque02} de daño. Dado +12")
        ataque_seleccionado=int(input("Selecciona un ataque: "))

        tirada=self.dado_rojo() #Tirada del dado rojo y almacenamiento en la variable en 1tirada

        self.pausa_dramatica() #Pausa dramática

        if ataque_seleccionado==1 and tirada>5:
            Enemigo.vida-=self.valor_ataque01
            print(f"Has atacado a {Enemigo.nombre} con {self.ataque01}.")
            print(f"{Enemigo.nombre} ha perdido {self.valor_ataque01} puntos de vida. Aún le quedan {Enemigo.vida} puntos de vida.")
         

        elif ataque_seleccionado==2 and tirada>12:

            Enemigo.vida-=self.valor_ataque02
            print(f"Has atacado a {Enemigo.nombre} con {self.ataque02}.")
            print(f"{Enemigo.nombre} ha perdido {self.valor_ataque02} puntos de vida. Aún le quedan {Enemigo.vida} puntos de vida.")
            #Pausa dramática
            print(".", end="")
            time.sleep(1.5)
            print(".", end="")
            time.sleep(1.5)
            print(".")
        else:
            print(f"Has fallado en tu ataque a {Enemigo.nombre}")  
           

class Enemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida=20
        self.ataque01="Golpe al aire"
        self.ataque02="Puño de la muerte"
        self.ataque03="Golpe de la desesperación"
        self.ataque04="Bola de fuego"
        self.valor_ataque01=0
        self.valor_ataque02=1   
        self.valor_ataque03=2
        self.valor_ataque04=4   
        self.turno=False     

    def saludar(self):
        print(f'Hola, soy {self.nombre}')

    def dado_negro(self):
        print(f'{self.nombre} lanza dado negro')
        return random.randint(1,10)
    

    def ataca_a(self, Heroe):
        print(f"{self.nombre} ataca a {Heroe.nombre}")
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
#Cambios de turno EN EL JUEGO#Cambios de turno EN EL JUEGO
    if dado_p01>dado_p02:
        player01.turno = True
        player02.turno = False
        print(f"Es el turno de ataque de {player01.nombre}.")
        
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


nombre_player01=str(input("Nombre de tu héroe: "))
ataque01_player01=str(input("Nombre de tu ataque +2: "))
ataque02_player01=str(input("Nombre de tu ataque +4: "))

player01=Heroe(nombre_player01,ataque01_player01,ataque02_player01)

nombre_player02=str(input("Nombre de tu enemigo: "))
player02=Enemigo(nombre_player02)

combate(player01,player02)
