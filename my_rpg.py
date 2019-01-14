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


class Monster(object):

    def __init__(self, current_room):
        type = current_room.terrain
        level = current_room.level
        evade_chance = 0.1
        hitpoints = 100
        damage_type = type
        damage = level * 1.3
        regen = 1
        movement = 20
        self.evade_chance = evade_chance
        self.hitpoints = hitpoints
        self.damage_type = damage_type
        self.damage = damage
        self.current_room = current_room
        self.level = level
        self.type = type
        self.regen = regen


class Elemental(Monster):
    pass


class Giant(Monster):
    def __init__(self, current_room):
        super().__init__(current_room)
        hitpoints = hitpoints * 2

class Fairy(Monster):
    pass


class Goblin(Monster):
    pass




# there is surely a way to hide all of this variable assignment on another
# module but I don't yet know how.
map = [Room(0,"town")]
terrain = ["water", "fire", "earth"]
terrain_check = []
water_story = storyline.storyline_dict["water"]
fire_story = storyline.storyline_dict["fire"]
earth_story = storyline.storyline_dict["earth"]
intro = storyline.storyline_dict["intro"]
secret_lair_storey = storyline.storyline_dict["secret_lair"]
controls = storyline.storyline_dict["controls"]








# I am thinking a timer here to look for monsters
def hunt(current_room):
    #print("the hunt option has not been developed yet")
    #print("you are still in the same zone")
    monster1 = Giant(current_room)
    print(monster1.level)
    print(monster1.regen)
    print(monster1.hitpoints)
    return

def abyss_fight():
    print("this monster encounter hasn't been developed yet.")
    print("returning to town")
    return

# As new rooms are generated for the first time I wanted a way to keep track
# so I could ensure an opening message for a room is only explained on first
# occurence, and then a generic after that. I am not sure if using a list is the
# only way to do this. I also tried a for loop looking to see if the terrain
# attribute of Room instances exist, but could not get this to work, so I have
# created another separate list especially to keep track.
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

# I wanted a way to generate new rooms as the runner moves further into the
# dungeon. I have created a variable for room number to keep track of what
# room the player is currently in. I am still trying to figure out whether
# a global variable will be better for this purpose. Also I have level as an
# attribute of Room. I am thinking this will come in handy but may just be a
# double up.
def explorer(room_number):

    current_room = map[room_number]

    if room_number != 0:
        print(f"I am in a level {current_room.level}", end=" ")
        print(f"{current_room.terrain} zone.")
        print(f"Map range length is {len(map)}")
    else:
        print("\nI'm in town")

    direction = input("\n>>> ").lower()
    print("\n")

    if direction == "forward" and len(map) == room_number+1:
        room_number += 1
        map.append(Room(room_number, terrain_generator()))
        explorer(room_number)
    elif direction == "backward" and room_number != 0:
        room_number -= 1
        print("Moving back to previous zone.\n")
        explorer(room_number)
    elif direction == "forward" and len(map) > room_number+1:
        room_number += 1
        print("Moving forward to previously discovered zone.\n")
        explorer(room_number)
    elif direction == "down" and room_number == 0:
         print("Entered the abyss")
         abyss_fight()
         explorer(room_number)
    elif direction == "backward" and room_number == 0:
        print("There's no going back from town. only forward")
        explorer(room_number)
    elif direction == "hunt":
        #print("program is now moving to hunt function")
        hunt(current_room)
        #explorer(room_number)
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
