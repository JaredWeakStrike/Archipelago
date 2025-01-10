import logging
from typing import List, Any

from BaseClasses import Tutorial, ItemClassification
from Fill import fill_restrictive
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from .Items import *
from .Locations import *
from .Names import ItemName, LocationName, RegionName
from .Options import Octopath2Options, StartingCharacter
from .Regions import create_regions, connect_regions
from .Rules import *
from .Logic import *


class Octopath2Web(WebWorld):
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Octopath Traveler 2 with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Probably HappyArtea"]
    )]


class Octopath2World(World):
    """
    Octopath Traveler 2 is a turn-based role-playing game developed and published by Square Enix and released in 2023.
    """
    game = "Octopath Traveler 2"
    web = Octopath2Web()

    #required_client_version = (0, 5, 1)
    options_dataclass = Octopath2Options
    options: Octopath2Options
    item_name_to_id = {item: item_id
                       for item_id, item in enumerate(item_table.keys(), 0x88888888)}
    location_name_to_id = {item: location
                           for location, item in enumerate(all_chests.keys(), 0x88888888)}
    total_locations: int
    exclude: List[str]
    starting_character: str
    starting_time: str

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.exclude = []
        self.starting_character = ""
        self.starting_time = "Day"


    def create_item(self, name: str) -> Item:
        """
        Returns created OT2Item
        """
        data = item_table[name]
        if data.type == ItemType.progression:
            data_classification = ItemClassification.progression
        elif data.type == ItemType.useful:
            data_classification = ItemClassification.useful
        else:
            data_classification = ItemClassification.filler
        created_item = OT2Item(name, data_classification, self.item_name_to_id[name], self.player)

        return created_item

    def create_event_item(self, name: str) -> Item:
        """
        Returns created events "items"
        """
        item_classification = ItemClassification.progression
        created_item = OT2Item(name, item_classification, None, self.player)
        return created_item

    def __pre_fill_item(self, item_name: str, location_name: str, precollected) -> None:
        """Pre-assign an item to a location"""
        if item_name not in precollected:
            self.exclude.append(item_name)
            data = item_table[item_name]
            if data.type == ItemType.progression:
                data_classification = ItemClassification.progression
            elif data.type == ItemType.useful:
                data_classification = ItemClassification.useful
            else:
                data_classification = ItemClassification.filler
            item = OT2Item(item_name, data_classification, self.item_name_to_id[item_name], self.player)
            self.multiworld.get_location(location_name, self.player).place_locked_item(item)

    def create_items(self) -> None:
        """Create every item in the world"""
        precollected = [item.name for item in self.multiworld.precollected_items[self.player]]
        # That's horrible code but it'll have to do for now
        # Need to handle a add_location on game start for the starter char unlock, and then
        if self.options.StartingCharacter == StartingCharacter.option_osvald:
            self.__pre_fill_item("Osvald Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Osvald Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Winterlands Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Osvald"
        elif self.options.StartingCharacter == StartingCharacter.option_castti:
            self.__pre_fill_item("Castti Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Castti Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Harborlands Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Castti"
        elif self.options.StartingCharacter == StartingCharacter.option_temenos:
            self.__pre_fill_item("Temenos Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Temenos Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Crestlands Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Temenos"
        elif self.options.StartingCharacter == StartingCharacter.option_ochette:
            self.__pre_fill_item("Ochette Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Ochette Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Totohaha Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Ochette"
        elif self.options.StartingCharacter == StartingCharacter.option_partitio:
            self.__pre_fill_item("Partitio Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Partitio Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("WildlandsUnlock", "Game Start Region", precollected)
            self.starting_character = "Partitio"
        elif self.options.StartingCharacter == StartingCharacter.option_agnea:
            self.__pre_fill_item("Agnea Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Agnea Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Leaflands Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Agnea"
        elif self.options.StartingCharacter == StartingCharacter.option_throne:
            self.__pre_fill_item("Throne Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Throne Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Brightlands Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Throne"
        elif self.options.StartingCharacter == StartingCharacter.option_hikari:
            self.__pre_fill_item("Hikari Unlock", "Game Start Character", precollected)
            self.__pre_fill_item("Hikari Chapter1 Unlock", "Game Start Chapter", precollected)
            self.__pre_fill_item("Hinoeuma Region Unlock", "Game Start Region", precollected)
            self.starting_character = "Hikari"
        
        non_fillers=0
        
        for name, data in item_table.items():
            if name not in self.exclude:
                for i in range(data.quantity):
                    item = self.create_item(name)
                    self.multiworld.itempool.append(item)
                    non_fillers = non_fillers+1
                    
        itempool = []
                    
        # Creating fillers for unfilled locations
        size = len(all_chests) - non_fillers-3
        for i in range(size):
            filler = self.random.choice(list(filler_items)) 
            itempool += [self.create_item(filler)]

        self.multiworld.itempool += itempool


    def fill_slot_data(self) -> Dict[str, Any]:
        pass
        

    def generate_early(self) -> None:
        """
        Determines the quantity of items and maps plando locations to items.
        """
        pass

    def create_regions(self):
        """
        Creates the Regions and Connects them.
        """
        create_regions(self)
        connect_regions(self)

    def set_rules(self):
        """
        Sets the Logic for the Regions and Locations.
        """
        universal_logic = Rules.OT2WorldRules(self)
        universal_logic.set_ot2_rules()
