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
terrain_dump = [""]
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

def storyline_checker(terrain_roll):

        if terrain_roll in terrain_check:
            print(f"Generic {terrain_roll} message")
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


def explorer(room_number, direction):


    if direction == "forward" and len(map) == room_number+1:
        room_number += 1
        map.append(Room(room_number, terrain_generator()))
        current_room = map[room_number]
        print(f"My current room is {current_room.level}")
        print(f"My current terrain is {current_room.terrain}")
        print(f"Map range length is {len(map)}")
        start(room_number)
    elif direction == "backward" and room_number != 0:
        room_number -= 1
        current_room = map[room_number]
        print(f"My current room is {current_room.level}")
        print(f"My current terrain is {current_room.terrain}")
        print(len(map))
        start(room_number)
    elif direction == "forward" and len(map) > room_number+1:
        room_number += 1
        current_room = map[room_number]
        print(f"My current room is {current_room.level}")
        print(f"My current terrain is {current_room.terrain}")
        print(len(map))
        start(room_number)
    else:
        print("""Cannot recognise this input,
        please enter help if you need a list of controls""")
        start(room_number)

def start(room_number):

    direction = input(">>> ").lower()
    if direction == "help":
        print(controls)
        input("Press any key to return to zone\n")
        start(room_number)
    elif direction == "forward" or "backward":
        explorer(room_number, direction)

#print(intro)
#storyline_checker()

start(0)
