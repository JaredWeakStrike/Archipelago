from dataclasses import dataclass

from Options import Choice, Range, Toggle, ItemDict, PerGameCommonOptions, StartInventoryPool


#class EXPScaling(Range):
#    """Exp Multiplier for all available characters"""
#    display_name = "EXP multiplier"
#    range_start = 1
#    range_end = 10
#    default = 5

#class AvailableChars(Choice):
#    """Amount of available recruitable characters"""
#    display_name = "Amount of available characters"
#    range_start = 1
#    range_end = 8
#    default = 8

#class OpenMode(Toggle):
#    """Makes the world more open by removing some virtual barriers between regions"""
#    display_name = "Open Wolrd Mode"
#    default = false

#class IncludeChests(Toggle):
#    """Allows Archipelago items to be in any treasure chest"""
#    display_name = "Include Chests"
#    default = 1

#class IncludeMainQuests(Toggle):
#    """Allows Archipelago items to be rewards for ending main story chapters"""
#    display_name = "Include Main Quests"
#    default = 1

#class IncludeSideQuests(Toggle):
#    """Allows Archipelago items to be in side quests"""
#    display_name = "Include Side Quests"
#    default = 0

#class IncludeNPCInfo(Toggle):
#    """Allows Archipelago items to be rewards for getting information from NPCs. Also includes all hidden items."""
#    display_name = "Include NPC Information"
#    default = 0

#class IncludeNPCItems(Toggle):
#    """Allows Archipelago items to be from NPC possessions"""
#    display_name = "Include NPC Items"
#    default = 0

#class RandomizedTime(Choice):
#    """Locks the player in a specific time, with a progression item being the ability to change day/night."""
#    display_name = "Include NPC Items"
#    default = 0

class StartingCharacter(Choice):
    """Sets which character you will start with and is gonna be locked as your main character"""
    display_name = "Starting Character"
    option_osvald = 1
    option_castti = 2
    option_temenos = 3
    option_ochette = 4
    option_partitio = 5
    option_agnea = 6
    option_throne = 7
    option_hikari = 8
    default = 2

#class Difficulty(Choice):
#    """Sets up what is expected for later regions. Easy forces later regions to be later in logic, while hard may force you to go through hard regions early."""
#    display_name = "Difficulty"
#    option_easy = 0
#    option_normal = 1
#    option_hard = 2
#    option_no_logic = 3
#    default = 1

#class ShuffleSkills(Choice):
#    """Shuffles which job has which active abilities (job commands)
#    split_regular_and_divine shuffle abilities, but only shuffles regular skills between themselves and divine skills between themselves."""
#    display_name = "Shuffle Skills"
#    option_vanilla = 0
#    option_split_regular_and_divine = 1
#    option_everything =2
#    default = 0

#class ShuffleSupports(Toggle):
#    """Shuffles which job has which support skills (passive abilities)"""
#    display_name = "Shuffle Support Skills"
#    default = 0

#class RandomizeProficiencies(Choice):
#    """Randomizes jobs weapon proficiencies. Shuffled only shuffles proficiencies around. Balanced keeps the vanilla amount of prociency the job had in vanilla but randomizes each proficiency. Full_no_logic randomizes everything and full forces every weapon type to be usable by at least one job."""
#    display_name = "Randomize Proficiencies"
#    option_vanilla = 0
#    option_shuffled = 1
#    option_balanced = 2
#    option_full = 3
#    option_full_no_logic = 4
#    default = 0

#class TierEquipment(Choice):
#    """Puts tiers into equipment received from items and shops. There are more chance that early checks will have worse equipment and later checks better equipment"""
#    display_name = "TierEquipment"
#    option_no_tiering = 0
#    option_basic_tiering = 1
#    option_harsh_tiering = 2
#    option_no_equips_in_items = 3
#    default = 0

class Goal(Choice):
    """Win Condition
    main: clear main character's story
    main_with_vide: Clear main character's story, then kill vide.
    all: clear all available travelers story
    vide: kill vide
    galdera : defeat Galdera    
    """
    display_name = "Goal"
    option_vide = 0
#    option_main = 1
#    option_all = 2
#    option_main_with_vide = 3
#    option_galdera = 4
    default = 0


# shamelessly stolen from the messenger
@dataclass
class Octopath2Options(PerGameCommonOptions):
    start_inventory: StartInventoryPool
    Goal: Goal
#    EXPScaling: EXPScaling
#    Available_Chars: AvailableChars
#    Open_Mode: OpenMode
#    Include_Chests: IncludeChests
#    IncludeMainQuests: IncludeMainQuests
#    IncludeSideQuests: IncludeSideQuests
#    IncludeNPCInfo: IncludeNPCInfo
#    IncludeNPCItems: IncludeNPCItems
    StartingCharacter: StartingCharacter
#    Difficulty: Difficulty
#    ShuffleSkills: ShuffleSkills
#    ShuffleSupports: ShuffleSupports
#    RandomizeProficiencies: RandomizeProficiencies
