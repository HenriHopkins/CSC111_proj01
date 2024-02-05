"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
import time
from typing import Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - num:
            @TODO
        - name:
            The name of the place, such as the building name, "street", or "sidewalk"
        - s_desc:
            The short description of the place. Will include a short description, entry requirements, and possible paths
            from that location in cardinal directions.
        - l_desc:
            The long description of the place. Includes everything listed in the short description but will be more
            descriptive in what the building is and what may be inside the building as well as directions that are a
            include what buildings may be close to them.
        - cmds:
            A list of all possible commands that you can do at this location with the current items in a players
            selected inventory.
        - side:
            A integer for the side something is one, 0 if it isn't on a side, 1 if it is on the left side, 2 if it's on
            the right side.

    Representation Invariants:
        - self.num @TODO
        - self.name != ''
        - s_desc != ''
        - l_desc != ''
        - cmds != []
    """

    def __init__(self, num: int, name: str, s_desc: str, l_desc: str, cmds: list, side: bool) -> None:
        """Initialize a new location.

        Since the player hasn't entered the building by default, we will set visited to False.
        """
        self.num = num
        self.name = name
        self.s_desc = s_desc
        self.l_desc = l_desc
        self.cmds = cmds
        self.side = side

    def available_actions(self) -> list:
        """
        Return the available actions in this location.
        """
        return self.cmds


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name:
            The name of the item
        - usage:
            Vague description of an item and uses for it at certain locations
        - points:
            How many points this item gives you at the end

    Representation Invariants:
        - self.name != ''
        - self.usage != ''
        - self.points >= 0
    """
    name: str
    usage: str
    points: int

    def __init__(self, name: str, usage: str, points: int) -> None:
        """Initialize a new item.
        """
        self.name = name
        self.usage = usage
        self.points = points


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x:
            x-coordinate of the players location, starting at 6 (x-coordinate of exam center)
        - y:
            y-coordinate of the players location, starting at 15 (y-coordinate of exam center)
        - inventory:
            A list of the current items that a player currently has and is carrying
        - victory:
            Boolean for whether the player has finished the game or not, when True, it will calculate players score
        - money:
            The amount of money a player has.

    Representation Invariants:
        - 0 <= self.x <= 7
        - 0 <= self.y <= 16
    """

    def __init__(self, money: int) -> None:
        """
        Initializes a new Player at position (2, 5) which is outside Robart's Library.
        """
        self.x = 2
        self.y = 4
        self.inventory = []
        self.victory = False
        self.money = money

    def move(self, x: int, y: int) -> None:
        """
        Moves the player according to the x and y corrdinates by adding them to the players current location
        """
        self.x += x
        self.y += y

    def score(self, move: int, fail: bool, places: set) -> int:
        """
        Returns the current score of the player based on 100/(number of moves), items in inventory affected by a scalar
        depending on if they failed or passed/still playing and the places they have visited also affected by the pass
        fail.
        """
        if fail:
            return len(places) + (len(self.inventory) * 2) + (100 / move)
        else:
            score = 0
            for item in self.inventory:
                score += item.points + 1
        return score + (len(places) * 5) + 100 / move + 10

    def show_inventory(self) -> list:
        """
        Returns a list of all items in a player's inventory with their name only
        """
        inventory = []
        for item in self.inventory:
            inventory.append(item.name)
        return inventory

    def drop_item(self, item: Item) -> None:
        """
        Removes an item from the inventory, but it is probably not a good idea to do this.
        """
        choice = input('Are you sure you want to drop this item (Y|N): ')
        while choice.upper() != 'Y' or choice.upper() != 'N':
            print('That is not a valid option!')
            choice = input('Are you sure you want to drop this item (Y|N): ')
        if choice == 'Y':
            self.inventory.remove(item)
            print(f'Dropped {item.name}!')

    def print_inventory(self) -> str:
        """
        Prints out the names and descriptions of items in a player's inventory
        """
        if len(self.inventory) == 0:
            print('You currently have no items in your inventory, they will be added here once you find them!')
        else:
            while True:
                print('These are the items currently in your inventory:')
                for item in self.inventory:
                    print(f'{item.name} ')
                choice = input('Inspect an item or LEAVE: ')
                while choice.upper() != 'LEAVE' and choice.upper() not in [x.upper() for x in self.show_inventory()]:
                    print('That is not a valid option!')
                    print('These are the items currently in your inventory:')
                    for item in self.inventory:
                        print(f'{item.name} ')
                    choice = input('Inspect an item or LEAVE: ')
                if choice.upper() in [x.upper() for x in self.show_inventory()]:
                    for item in self.inventory:
                        if item.name.upper() == choice.upper():
                            print(item.usage)
                            time.sleep(1)
                else:
                    break




class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map

    Representation Invariants:
        - map != []
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """
        self.map = self.load_map(map_data)
        self.location = self.load_location(location_data)
        self.item = self.load_items(items_data)

    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        map_list = []
        with open(map_data) as file:
            for line in file:
                map_list.append([int(num) for num in line.split()])
        return map_list

    def load_location(self, loc_data: TextIO) -> list[int, list[str], bool, str]:
        """
        Store location from open file loc_data as the location attribute of this object as a nested list of integers,
        strings, and booleans like so:

        If loc_data is a file containing the following text:
            1
            LOCATION: EXAMPLE
            short description
            A B C D
            False
            long
            description
            long
            description
            END
            STOP
        then load_location should assign this World object's location to be [1, 'LOCATION: EXAMPLE',
                                                                             'short description', ['A', 'B', 'C', 'D'],
                                                                             False, 'long description long description']
        return this list representation of the location
        """
        location_list = []
        with open(loc_data) as file:
            a = file.readline().strip()
            while a != 'STOP':
                curr = [int(a), file.readline().strip(), file.readline().strip()]
                cmds = []
                for word in file.readline().strip().split(','):
                    cmds.append(word)
                curr.append(cmds)
                curr.append((file.readline().strip() == 'True'))
                long = ''
                b = file.readline().strip()
                while b != 'END':
                    long += b + '\n'
                    b = file.readline().strip()
                curr.append(long)
                location_list.append(curr)
                a = file.readline().strip()
        return location_list

    def load_items(self, item_data: TextIO) -> list[str, int]:
        """
        Store Item from open file item_data as the item attribute of this object, as a nested list of strings like so:

        If item_data is a file containing the following text:
            0,ItemName,ItemDesc,200
            1,Item Name1,Item Desc1,2001
        then load_items should assign this World object's items to be [[0,'ItemName','ItemDesc',200],[ 1,'Item Name1',
                                                                        'Item Desc1',2001]]
        """
        item_list = []
        with open(item_data) as file:
            for line in file:
                parts = line.strip().split(',')
                part_list = [int(parts[0]), parts[1], parts[2], int(parts[3])]
                item_list.append(part_list)
        return item_list

    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        number = self.map[y][x]
        loc = self.location
        for i in range(len(loc)):
            if loc[i][0] == number:
                return Location(loc[i][0], loc[i][1], loc[i][2], loc[i][5], loc[i][3], loc[i][4])
        return None

    def get_item(self, play: Player, num: int) -> Optional[Item]:
        """Append the Item object whose unique ID is num to a player's inventory. If it is not a valid unique ID, return
        None (Doesn't append anything).
        """
        items = self.item
        for i in range(len(items)):
            if items[i][0] == num:
                choice = input(f'Do you wish to pick up {items[i][1]} (Y|N):')
                while choice.upper() != 'Y' and choice.upper() != 'N':
                    print('Sorry that is not a valid option!')
                    time.sleep(1)
                    choice = input(f'Do you wish to pick up {items[i][1]} (Y|N):')
                if choice.upper() == 'Y':
                    play.inventory.append(Item(items[i][1], items[i][2], items[i][3]))
                    print(f'You have obtained {items[i][1]}!')
                    time.sleep(1)
                else:
                    print('You can always return to get this item!')
                    time.sleep(1)
        return None
