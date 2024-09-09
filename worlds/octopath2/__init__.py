import logging
from typing import List

from BaseClasses import Tutorial, ItemClassification
from Fill import fill_restrictive
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from worlds.AutoWorld import World, WebWorld
from .Items import *
from .Locations import *
from .Names import ItemName, LocationName, RegionName
from .Options import Octopath2Options
from .Regions import create_regions, connect_regions
from .Rules import *


class Octopath2Web(WebWorld):
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Kingdom Hearts 2 Final Mix with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["JaredWeakStrike"]
    )]


class Octopath2World(World):
    """
    Octopath is an action role-playing game developed and published by Square Enix and released in 2005.
    It is the sequel to Kingdom Hearts and Kingdom Hearts: Chain of Memories, and like the two previous games,
    focuses on Sora and his friends' continued battle against the Darkness.
    """
    game = "Octopath Traveler 2"
    web = Octopath2Web()

    #required_client_version = (0, 4, 4)
    options_dataclass = Octopath2Options
    options: Octopath2Options
    item_name_to_id = {item: item_id
                       for item_id, item in enumerate(item_table.keys(), 0x88888888)}
    location_name_to_id = {item: location
                           for location, item in enumerate(all_locations.keys(), 0x88888888)}
    item_name_groups = item_groups
    total_locations: int
    # growth_list: list[str]

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        # random_super_boss_list List[str]
        # has to be in __init__ or else other players affect each other's bounties
        pass

    def fill_slot_data(self) -> dict:

        return

    def create_item(self, name: str) -> Item:
        """
        Returns created OT2Item
        """
        data = item_table[name]
        created_item = OT2Item(name, name.classification, self.item_name_to_id[name], self.player)

        return created_item

    def create_event_item(self, name: str) -> Item:
        item_classification = ItemClassification.progression
        created_item = OT2Item(name, item_classification, None, self.player)
        return created_item

    def create_items(self) -> None:
        """
        Fills ItemPool and manages schmovement, random growth, visit locking and random starting visit locking.
        """

        itempool = [self.create_item(item) for item, data in self.item_quantity_dict.items() for _ in range(data)]

        # Creating filler for unfilled locations
        itempool += [self.create_filler() for _ in range(self.total_locations - len(itempool))]

        self.multiworld.itempool += itempool

        pass

    def generate_early(self) -> None:
        """
        Determines the quantity of items and maps plando locations to items.
        """
        pass

    def pre_fill(self):
        """
        Plandoing Events and Fill_Restrictive for donald,goofy and sora
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

    def generate_output(self, output_directory: str):
        """
        Generates the .zip for OpenKH (The KH Mod Manager)
        """
        pass


    def get_filler_item_name(self) -> str:
        """
        Returns random filler item name.
        """
        return self.random.choice(filler_items)
