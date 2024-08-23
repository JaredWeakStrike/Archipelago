from dataclasses import dataclass

from Options import Choice, Range, Toggle, ItemDict, PerGameCommonOptions, StartInventoryPool



class Goal(Choice):
    """Win Condition
    vide: kill vide
    """
    display_name = "Goal"
    option_vide = 0
    default = 0


# shamelessly stolen from the messanger
@dataclass
class Octopath2Options(PerGameCommonOptions):
    Goal: Goal
