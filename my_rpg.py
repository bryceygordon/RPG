from random import randint
from textwrap import dedent
import storyline
from sys import exit

### What do i want to do
### i want to created a new minted version of a class and store it in a dictionary

class Room(object):

    def __init__(self, level, terrain):
        self.level = level
        self.terrain = terrain


map = [Room(0,"town")]
terrain = ["water", "fire", "earth"]
terrain_check = []
water_story = storyline.storyline_dict["water"]
fire_story = storyline.storyline_dict["fire"]
earth_story = storyline.storyline_dict["earth"]
intro = storyline.storyline_dict["intro"]
secret_lair_storey = storyline.storyline_dict["secret_lair"]
controls = storyline.storyline_dict["controls"]

class Monster(Room):

    pass

#new note
#another new note

def hunt():
    print("the hunt option has not been developed yet")
    print("you are still in the same zone")
    return

def abyss_fight():
    print("this monster encounter hasn't been developed yet.")
    print("returning to town")
    return


def storyline_checker(terrain_roll):

        if terrain_roll in terrain_check:
            print(f"You discover a new {terrain_roll} zone.\n")
        elif terrain_roll == "water":
            print(water_story)
            terrain_check.append(terrain_roll)
            return
        elif terrain_roll == "fire":
            print(fire_story)
            terrain_check.append(terrain_roll)
            return
        elif terrain_roll == "earth":
            print(earth_story)
            terrain_check.append(terrain_roll)
            return
        elif terrain_roll == 3:
            print(secret_lair_storey)
            terrain_check.append("secret_lair")
            return
        else:
            print("error with storyline_checker")
            exit(0)


def terrain_generator():

    t_dice = randint(0,3)
    if t_dice < len(terrain):
        terrain_roll = terrain[t_dice]
        storyline_checker(terrain_roll)
        return terrain_roll
    elif randint(0,5) == 5:
        print("rare executed")
        storyline_checker(t_dice)
        return "Secret Lair"
    else:
        print("rolling again")
        return terrain_generator()


def explorer(room_number):

    direction = input("\n>>> ").lower()
    print("\n")
    
    if direction == "forward" and len(map) == room_number+1:
        room_number += 1
        map.append(Room(room_number, terrain_generator()))
        current_room = map[room_number]
        print(f"I am in a level {current_room.level}", end=" ")
        print(f"{current_room.terrain} zone.")
        print(f"Map range length is {len(map)}")
        explorer(room_number)
    elif direction == "backward" and room_number != 0:
        room_number -= 1
        current_room = map[room_number]
        print("Moving back to previous zone.\n")
        print(f"I am in a level {current_room.level}", end=" ")
        print(f"{current_room.terrain} zone.")
        print(f"Map range length is {len(map)}")
        explorer(room_number)
    elif direction == "forward" and len(map) > room_number+1:
        room_number += 1
        current_room = map[room_number]
        print("Moving forward to previously discovered zone.\n")
        print(f"I am in a level {current_room.level}", end=" ")
        print(f"{current_room.terrain} zone.")
        print(len(map))
        explorer(room_number)
    elif direction == "down" and room_number == 0:
         print("Entered the abyss")
         abyss_fight()
         explorer(room_number)
    elif direction == "backward" and room_number == 0:
        print("There's no going back from town. only forward")
        explorer(room_number)
    elif direction == "hunt":
        print("program is now moving to hunt function")
        hunt()
        explorer(room_number)
    elif direction == "hunt" and room_number == 0:
        print("Cannot hunt in town. Heading back to town")
        explorer(room_number)
    elif direction == "help":
        print(controls)
        input("Press any key to return to zone\n")
        explorer(room_number)
    else:
        print("""Cannot recognise this input,
        please enter help if you need a list of controls
        returning to zone""")
        explorer(room_number)




#print(intro)


explorer(0)
