from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Lynx import Lynx
from Organisms.Antelope import Antelope
from WorldRender import WorldRenderer
from TurnManager import TurnManager
import os

if __name__ == '__main__':
    WORLD_WIDTH = 5
    WORLD_HEIGHT = 5
    TOTAL_TURNS = 30

    ORGANISM_TYPES = {
        Grass.SIGN: Grass,
        Sheep.SIGN: Sheep,
        Lynx.SIGN: Lynx,
        Antelope.SIGN: Antelope
    }

    world = World(WORLD_WIDTH, WORLD_HEIGHT)
    renderer = WorldRenderer()
    turnManager = TurnManager(world)

    world.addOrganism(Grass(position=Position(xPosition=0, yPosition=0), world=world))
    world.addOrganism(Grass(position=Position(xPosition=4, yPosition=4), world=world))
    world.addOrganism(Sheep(position=Position(xPosition=2, yPosition=2), world=world))
    world.addOrganism(Lynx(position=Position(xPosition=1, yPosition=1), world=world))
    world.addOrganism(Antelope(position=Position(xPosition=2, yPosition=1), world=world))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(renderer.render(world))

    for _ in range(0, TOTAL_TURNS):
        turn_advanced = False
        
        while not turn_advanced:
            prompt_msg = 'ENTER: kolejna tura | "p": plaga | "dodaj [Znak] [X] [Y]" (np. dodaj S 3 3): '
            user_input = input(prompt_msg).strip().split()
            
            if not user_input:
                turn_advanced = True
                
            elif user_input[0].lower() == 'p':
                turnManager.activatePlague()
                turn_advanced = True
                
            elif user_input[0].isalpha() and len(user_input) == 3:
                sign = user_input[0].upper()
                try:
                    x = int(user_input[1])
                    y = int(user_input[2])
                    target_position = Position(xPosition=x, yPosition=y)
                    
                    if sign in ORGANISM_TYPES:
                
                        if world.positionOnBoard(target_position) and world.getOrganismFromPosition(target_position) is None:
                            new_organism = ORGANISM_TYPES[sign](position=target_position, world=world)
                            world.addOrganism(new_organism)
                            
                            
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(renderer.render(world))
                            print(f"Sukces! Dodano {sign} na polu ({x}, {y}).")
                        else:
                            print("Błąd: Pole znajduje się poza planszą lub jest już zajęte!")
                    else:
                        print(f"Błąd: Nieznany znak organizmu '{sign}'. Dostępne: {list(ORGANISM_TYPES.keys())}")
                        
                except ValueError:
                    print("Błąd: Współrzędne X i Y muszą być liczbami całkowitymi!")
            else:
                print("Błąd: Nierozpoznana komenda lub zła liczba argumentów.")
        os.system('cls' if os.name == 'nt' else 'clear')
        turnManager.makeTurn()
        print(renderer.render(world))
  
  
  
