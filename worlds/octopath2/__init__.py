import logging
from typing import List, Any

from BaseClasses import Tutorial, ItemClassification
from Fill import fill_restrictive
from Options import StartInventory
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from .Items import *
from .Locations import *
from .Names import ItemName, LocationName, RegionName
from .Options import Octopath2Options, StartingCharacter, LockedTime, RandomizeCanoe
from .Regions import create_regions, connect_regions
from .Rules import *
#from .Logic import *


class Octopath2Web(WebWorld):
    setup_en = Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Octopath Traveler 2 with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Probably HappyArtea"]
    )
    
    setup_fr = Tutorial(
        setup_en.tutorial_name,
        setup_en.description,
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Probably HappyArtea"]
        )
        
    tutorials = [setup_en, setup_fr]


class Octopath2World(World):
    """
    Octopath Traveler 2 is a turn-based role-playing game developed and published by Square Enix and released in 2023.
    """
    game = "Octopath Traveler 2"
    topology_present = True
    web = Octopath2Web()

    #required_client_version = (0, 5, 1)
    options_dataclass = Octopath2Options
    options: Octopath2Options
    item_name_to_id = {item: item_id
                       for item_id, item in enumerate(item_table.keys(), 0x88888888)}
    location_name_to_id = {item: location
                           for location, item in enumerate(all_chests.keys(), 0x88888888)}
    for location, id in location_name_to_id.items():
        print(f"[{id}] = \"{location}\",")
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

        starting_items = []

        if self.options.StartingCharacter == StartingCharacter.option_osvald:
            starting_items = [ItemName.OsvaldUnlock, ItemName.OsvaldCh1, ItemName.WinterlandsUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_castti:
            starting_items = [ItemName.CasttiUnlock, ItemName.CasttiCh1, ItemName.HarborlandsUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_temenos:
            starting_items = [ItemName.TemenosUnlock, ItemName.TemenosCh1, ItemName.CrestlandsUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_ochette:
            starting_items = [ItemName.OchetteUnlock, ItemName.OchetteCh1, ItemName.TotohahaUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_partitio:
            starting_items = [ItemName.PartitioUnlock, ItemName.PartitioCh1, ItemName.WildlandsUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_agnea:
            starting_items = [ItemName.AgneaUnlock, ItemName.AgneaCh1, ItemName.LeaflandsUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_throne:
            starting_items = [ItemName.ThroneUnlock, ItemName.ThroneCh1, ItemName.BrightlandsUnlock]

        elif self.options.StartingCharacter == StartingCharacter.option_hikari:
            starting_items = [ItemName.HikariUnlock, ItemName.HikariCh1, ItemName.HinoeumaUnlock]

        for item in starting_items:
            self.push_precollected(self.create_item(item))

        non_fillers=0
        
        for name, data in item_table.items():
            if name not in self.exclude:
                for i in range(data.quantity):
                    item = self.create_item(name)
                    self.multiworld.itempool.append(item)
                    non_fillers = non_fillers+1
                    
        itempool = []
                    
        # Creating fillers for unfilled locations
        size = len(all_chests) - non_fillers-2
        for i in range(size):
            filler = self.random.choice(list(filler_items)) 
            itempool += [self.create_item(filler)]

        self.multiworld.itempool += itempool


    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict(
                "Goal",
                #"StartingCharacter"
        )
        return slot_data
        

    def generate_early(self) -> None:
        """
        Determines the quantity of items and maps plando locations to items.
        """
        
        if self.options.LockedTime == False:
          self.exclude.append(ItemName.TimeChange)
          self.multiworld.push_precollected(self.create_item(ItemName.TimeChange))
        if self.options.RandomizeCanoe == False:
          self.exclude.append(ItemName.Boat)
          self.multiworld.push_precollected(self.create_item(ItemName.Boat))
            
        #pass

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
