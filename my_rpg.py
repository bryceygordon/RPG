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
terrain = ["water", "fire", "grass"]
terrain_check = []
terrain_dump = [""]
water_story = storyline.storyline_dict["water"]
fire_story = storyline.storyline_dict["fire"]
grass_story = storyline.storyline_dict["grass"]
intro = storyline.storyline_dict["intro"]
secret_lair_storey = storyline.storyline_dict["secret_lair"]

class Monster(Room):

    pass

#new note
#another new note

def storeyline_checker(terrain_roll):

    for elem in map:


        if terrain_roll in terrain_check:
            return
        elif terrain_roll == "water":
            print(water_story)
            terrain_check.append(terrain_roll)
            return
        elif terrain_roll == "fire":
            print(fire_story)
            terrain_check.append(terrain_roll)
            return
        elif terrain_roll == "grass":
            print(grass_story)
            terrain_check.append(terrain_roll)
            return
        elif terrain_roll == 3:
            print(secret_lair_storey)
            terrain_check.append("secret_lair")
            return
        else:
            print("error with storeyline_checker")
            exit(0)


def terrain_generator():

    t_dice = randint(0,3)
    if t_dice < len(terrain):
        terrain_roll = terrain[t_dice]
        storeyline_checker(terrain_roll)
        return terrain_roll
    elif randint(0,5) == 5:
        print("rare executed")
        storeyline_checker(t_dice)
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
        pass

def start(room_number):

    direction = input(">>> ").lower()
    explorer(room_number, direction)

#print(intro)
#storeyline_checker()

start(0)
