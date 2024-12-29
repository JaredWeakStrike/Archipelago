# Imports will need to be changed accordingly
from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .Items import item_table
from .Locations import all_chests
from .Names import LocationName, ItemName, RegionName
from .Options import StartingCharacter
from worlds.generic.Rules import add_rule, forbid_items, add_item_rule

# I don't know what is going on here, but it works.
if TYPE_CHECKING:
    from . import Octopath2World
else:
    Octopath2World = object


# Shamelessly Stolen from Messanger


class OT2Rules:
    player: int
    world: Octopath2World
    # Those are copy-paste from kh2 I tried to mimic into categories, but currently makes no sense
    # Regions accesses to prevent recursions
    Winterlands1Access: int
    BrightlandsAccess: int
    CrestlandsAccess: int
    TotohahaAccess: int
    HarborlandsAccess: int
    Hinoeuma1Access: int
    Hinoeuma2Access: int
    LeaflandsAccess: int
    Wildlands1Access: int
    Wildlands2Access: int
    CapeColdAccess: int
    FlameChurchAccess: int
    NewDelstaAccess: int
    BeastingVillageAccess: int
    CanalbrineAccess: int
    RyuAccess: int
    OresrushAccess: int
    CropdaleAccess: int
    SeaAccess: int

    def __init__(self, world: Octopath2World) -> None:
        self.player = world.player
        self.world = world
        self.multiworld = world.multiworld
        
        self.Winterlands1Access=0
        self.BrightlandsAccess=0
        self.CrestlandsAccess=0
        self.TotohahaAccess=0
        self.HarborlandsAccess=0
        self.Hinoeuma1Access=0
        self.Hinoeuma2Access=0
        self.LeaflandsAccess=0
        self.Wildlands1Access=0
        self.Wildlands2Access=0
        self.CapeColdAccess=0
        self.FlameChurchAccess=0
        self.NewDelstaAccess=0
        self.BeastingVillageAccess=0
        self.CanalbrineAccess=0
        self.RyuAccess=0
        self.OresrushAccess=0
        self.CropdaleAccess=0
        self.SeaAccess=0

    def can_be_daytime(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TimeChange, self.player)
                or self.world.starting_time == "Day")

    def can_be_nighttime(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TimeChange, self.player)
                or self.world.starting_time == "Night")

    # Regions access, need to check if we already went through that requirement to avoid infinite loops

    def can_access_winterlands1(self, state: CollectionState) -> bool:
        if self.Winterlands1Access == 1:
            return True
        elif self.Winterlands1Access == -1:
            return False
        else:
            self.Winterlands1Access = -1
            tempvar = (state.has(ItemName.WinterlandsUnlock, self.player)
                                  and (self.can_access_brightlands(state)
                                       or self.can_access_crestlands(state))
                                  or self.world.options.StartingCharacter == StartingCharacter.option_osvald)
            self.Winterlands1Access = tempvar  
            return self.Winterlands1Access ==1
            

    def can_access_crestlands(self, state: CollectionState) -> bool:
        if self.CrestlandsAccess == 1:
            return True
        elif self.CrestlandsAccess == -1:
            return False
        else:
            self.CrestlandsAccess = -1
            tempvar = (state.has(ItemName.CrestlandsUnlock, self.player)
                        and (self.can_access_brightlands(state)
                            or self.can_access_winterlands1(state))
                        or self.world.options.StartingCharacter == StartingCharacter.option_temenos)
            self.CrestlandsAccess = tempvar  
            return self.CrestlandsAccess == 1

    def can_access_brightlands(self, state: CollectionState) -> bool:
        if self.BrightlandsAccess == 1:
            return True
        elif self.BrightlandsAccess == -1:
            return False
        else:
            self.BrightlandsAccess = -1
            tempvar = (state.has(ItemName.BrightlandsUnlock, self.player)
                        and (self.can_access_winterlands1(state)
                            or self.can_access_crestlands(state)
                            or self.can_access_totohaha(state)
                            or self.can_access_wildlands2(state))
                        or self.world.options.StartingCharacter == StartingCharacter.option_throne)
            self.BrightlandsAccess = tempvar  
            return self.BrightlandsAccess == 1

    def can_access_totohaha(self, state: CollectionState) -> bool:
        if self.TotohahaAccess == 1:
            return True
        elif self.TotohahaAccess == -1:
            return False
        else:
            self.TotohahaAccess = -1
            tempvar = (state.has(ItemName.TotohahaUnlock, self.player)
                        and (self.can_access_brightlands(state)
                            or self.can_access_wildlands2(state))
                        or self.world.options.StartingCharacter == StartingCharacter.option_ochette)
            self.TotohahaAccess = tempvar  
            return self.TotohahaAccess == 1

    def can_access_harborlands(self, state: CollectionState) -> bool:
        if self.HarborlandsAccess == 1:
            return True
        elif self.HarborlandsAccess == -1:
            return False
        else:
            self.HarborlandsAccess = -1
            tempvar = ((state.has(ItemName.HarborlandsUnlock, self.player)
                        and (self.can_access_brightlands(state)
                            or self.can_access_hinoeuma1(state)
                            or self.can_access_hinoeuma2(state)))
                        or self.world.options.StartingCharacter == StartingCharacter.option_castti)
            self.HarborlandsAccess = tempvar  
            return self.HarborlandsAccess == 1

    def can_access_hinoeuma1(self, state: CollectionState) -> bool:
        if self.Hinoeuma1Access == 1:
            return True
        elif self.Hinoeuma1Access == -1:
            return False
        else:
            self.Hinoeuma1Access = -1
            tempvar = (state.has(ItemName.HinoeumaUnlock, self.player)
                        and (self.can_access_harborlands(state)
                            or self.can_access_wildlands1(state))
                        or self.world.options.StartingCharacter == StartingCharacter.option_hikari)
            self.Hinoeuma1Access = tempvar  
            return self.Hinoeuma1Access == 1

    def can_access_leaflands(self, state: CollectionState) -> bool:
        if self.LeaflandsAccess == 1:
            return True
        elif self.LeaflandsAccess == -1:
            return False
        else:
            self.LeaflandsAccess = -1
            tempvar = ((state.has(ItemName.LeaflandsUnlock, self.player)
                        and (self.can_access_wildlands1(state)
                            or self.can_access_wildlands2(state)
                            or self.can_access_hinoeuma2(state)))
                        or self.world.options.StartingCharacter == StartingCharacter.option_agnea)
            self.LeaflandsAccess = tempvar  
            return self.LeaflandsAccess == 1

    def can_access_wildlands1(self, state: CollectionState) -> bool:
        if self.Wildlands1Access == 1:
            return True
        elif self.Wildlands1Access == -1:
            return False
        else:
            self.Wildlands1Access = -1
            tempvar = (state.has(ItemName.WildlandsUnlock, self.player)
                and (self.can_access_hinoeuma1(state)
                    or self.can_access_leaflands(state))
                or self.world.options.StartingCharacter == StartingCharacter.option_partitio)
            self.Wildlands1Access = tempvar  
            return self.Wildlands1Access == 1

    def can_access_winterlands2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.WinterlandsUnlock, self.player)
                and self.can_access_crestlands(state)
                and self.can_KO(state))

    def can_access_hinoeuma2(self, state: CollectionState) -> bool:
        if self.Hinoeuma2Access == 1:
            return True
        elif self.Hinoeuma2Access == -1:
            return False
        else:
            self.Hinoeuma2Access = -1
            tempvar = (state.has(ItemName.HinoeumaUnlock, self.player)
                        and (self.can_access_harborlands(state))
                        or self.can_access_leaflands(state))
            self.Hinoeuma2Access = tempvar  
            return self.Hinoeuma2Access == 1

    def can_access_wildlands2(self, state: CollectionState) -> bool:
        if self.Wildlands2Access == 1:
            return True
        elif self.Wildlands2Access == -1:
            return False
        else:
            self.Wildlands2Access = -1
            tempvar = (state.has(ItemName.WildlandsUnlock, self.player)
                        and (self.can_access_leaflands(state)
                            or self.can_access_totohaha(state)
                            or self.can_access_brightlands(state)))
            self.Wildlands2Access = tempvar  
            return self.Wildlands2Access == 1

    def can_access_sea(self, state: CollectionState) -> bool:
        if self.SeaAccess == 1:
            return True
        elif self.SeaAccess == -1:
            return False
        else:
            self.SeaAccess = -1
            tempvar = (state.has(ItemName.TheGrandTerry, self.player)
                        and (self.can_access_brightlands(state)
                            or self.can_access_totohaha(state)
                            or self.can_access_wildlands2(state)))
            self.SeaAccess = tempvar  
            return self.SeaAccess == 1

    # Individual Path Action access

    def can_hire(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_purchase(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and self.can_be_daytime(state))

    def can_allure(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and self.can_be_daytime(state))

    def can_entreat(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_befriend(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_provoke(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and self.can_be_daytime(state))

    def can_guide(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and self.can_be_daytime(state))

    def can_coerce(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_steal(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and self.can_be_daytime(state))

    def can_ambush(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_inquire(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and self.can_be_daytime(state))

    def can_soothe(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_challenge(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player)
                and self.can_be_daytime(state))

    def can_bribe(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player)
                and self.can_be_nighttime(state))

    def can_scrutinize(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and self.can_be_daytime(state))

    def can_mug(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and self.can_be_nighttime(state))

    # Path Actions results access. 3 types, splitting day and night, for when NPCs will be considered in logic.

    def can_have_followers_day(self, state: CollectionState) -> bool:
        return (self.can_guide(state)
                or self.can_allure(state))

    def can_have_followers_night(self, state: CollectionState) -> bool:
        return (self.can_hire(state)
                or self.can_befriend(state))

    def can_have_followers(self, state: CollectionState) -> bool:
        return (self.can_have_followers_day(state)
                or self.can_have_followers_night(state))

    def can_get_npcitems_day(self, state: CollectionState) -> bool:
        return (self.can_purchase(state)
                or self.can_steal(state))

    def can_get_npcitems_night(self, state: CollectionState) -> bool:
        return (self.can_entreat(state)
                or self.can_mug(state))

    def can_get_npcitems(self, state: CollectionState) -> bool:
        return (self.can_get_npcitems_day(state)
                or self.can_get_npcitems_night(state))

    def can_get_info_day(self, state: CollectionState) -> bool:
        return (self.can_scrutinize(state)
                or self.can_inquire(state))

    def can_get_info_night(self, state: CollectionState) -> bool:
        return (self.can_bribe(state)
                or self.can_coerce(state))

    def can_get_info(self, state: CollectionState) -> bool:
        return (self.can_get_info_day(state)
                or self.can_get_info_night(state))

    def can_KO_day(self, state: CollectionState) -> bool:
        return (self.can_provoke(state)
                or self.can_challenge(state))

    def can_KO_night(self, state: CollectionState) -> bool:
        return (self.can_ambush(state)
                or self.can_soothe(state))

    def can_KO(self, state: CollectionState) -> bool:
        return (self.can_KO_day(state)
                or self.can_KO_night(state))

    # Towns Unlocks

    def capecold_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.OsvaldCh1, self.player)
                or self.world.options.StartingCharacter == StartingCharacter.option_osvald)

    def winterbloom_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player)
                 and state.has(ItemName.ThroneCh2Father,self.player))
                or (state.has(ItemName.CasttiUnlock, self.player)
                    and state.has(ItemName.CasttiCh2Winterbloom,self.player))
                or (state.has(ItemName.PartitioUnlock, self.player)
                    and state.has(ItemName.PartitioWinterbloom, self.player)))

    def stormhail_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.HikariUnlock, self.player)
                 and state.has(ItemName.HikariCh4, self.player))
                or (state.has(ItemName.OchetteUnlock, self.player)
                    and state.has(ItemName.OchetteCh2Glacis,self.player))
                or (state.has(ItemName.TemenosUnlock, self.player)
                    and state.has(ItemName.TemenosCh3Stormhail,self.player)))

    def flamechurch_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.TemenosUnlock, self.player)
                 and state.has(ItemName.TemenosCh1, self.player))
                or (state.has(ItemName.TemenosUnlock, self.player)
                    and state.has(ItemName.ThroneUnlock,self.player)
                    and state.has(ItemName.TemenosThroneCh1, self.player))
                or self.world.options.StartingCharacter == StartingCharacter.option_temenos)

    def montwise_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player)
                 and state.has(ItemName.ThroneCh3Father, self.player))
                or (state.has(ItemName.HikariUnlock, self.player)
                    and state.has(ItemName.HikariCh4, self.player))
                or (state.has(ItemName.OsvaldUnlock, self.player)
                    and state.has(ItemName.OsvaldCh4, self.player))
                or (state.has(ItemName.OsvaldUnlock, self.player)
                    and state.has(ItemName.PartitioUnlock, self.player)
                    and state.has(ItemName.OsvaldPartitioCh2, self.player)))

    def merryhills_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.AgneaCh5, self.player))

    def newdelsta_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player)
                 and state.has(ItemName.ThroneCh1, self.player))
                or (state.has(ItemName.ThroneUnlock, self.player)
                    and state.has(ItemName.ThroneCh4, self.player))
                or (state.has(ItemName.AgneaUnlock, self.player)
                    and state.has(ItemName.AgneaCh2, self.player))
                or (state.has(ItemName.OsvaldUnlock, self.player)
                    and state.has(ItemName.PartitioUnlock,self.player)
                    and state.has(ItemName.OsvaldPartitioCh1, self.player))
                or self.world.options.StartingCharacter == StartingCharacter.option_throne)

    def abandonedvillage_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.CasttiCh3, self.player))

    def clockbank_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioCh2, self.player))

    def lostseed_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh4, self.player))

    def beasting_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.OchetteUnlock, self.player)
                 and state.has(ItemName.OchetteCh1, self.player))
                or (state.has(ItemName.OchetteUnlock, self.player)
                    and state.has(ItemName.OchetteCh3, self.player))
                or self.world.options.StartingCharacter == StartingCharacter.option_ochette)

    def tropuhopu_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.AgneaUnlock, self.player)
                 and state.has(ItemName.AgneaCh3, self.player))
                or (state.has(ItemName.PartitioUnlock, self.player)
                    and state.has(ItemName.PartitioTotohaha,self.player)))

    def nameless_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.TemenosCh4, self.player))

    def canalbrine_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.CasttiUnlock, self.player)
                 and state.has(ItemName.CasttiCh1, self.player))
                or (state.has(ItemName.TemenosUnlock, self.player)
                    and state.has(ItemName.TemenosCh2,self.player))
                or self.world.options.StartingCharacter == StartingCharacter.option_castti)

    def conningcreek_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.OchetteCh2Acta,self.player))
                or (state.has(ItemName.OsvaldUnlock, self.player)
                    and state.has(ItemName.OsvaldCh3, self.player))
                or (state.has(ItemName.ThroneUnlock, self.player)
                    and state.has(ItemName.TemenosUnlock,self.player)
                    and state.has(ItemName.TemenosThroneCh2, self.player)))

    def roqueisland_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioCh4, self.player))

    def ryu_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.HikariUnlock, self.player)
                 and state.has(ItemName.HikariCh1, self.player))
                or (state.has(ItemName.HikariUnlock, self.player)
                    and state.has(ItemName.AgneaUnlock,self.player)
                    and state.has(ItemName.HikariAgneaCh1, self.player))
                or self.world.options.StartingCharacter == StartingCharacter.option_hikari)

    def sai_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.CasttiUnlock, self.player)
                 and state.has(ItemName.CasttiCh2Sai, self.player))
                or (state.has(ItemName.AgneaUnlock, self.player)
                    and state.has(ItemName.AgneaCh4, self.player))
                or (state.has(ItemName.PartitioUnlock, self.player)
                    and state.has(ItemName.PartitioSai,self.player)))

    def ku_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.HikariUnlock, self.player)
                and state.has(ItemName.HikariCh5, self.player))
                or (state.has(ItemName.HikariUnlock, self.player)
                    and state.has(ItemName.AgneaUnlock,self.player)
                    and state.has(ItemName.HikariAgneaCh2, self.player)))

    def cropdale_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.AgneaUnlock, self.player)
                 and state.has(ItemName.AgneaCh1, self.player))
                or (state.has(ItemName.CasttiUnlock, self.player)
                    and state.has(ItemName.OchetteUnlock,self.player)
                    and (state.has(ItemName.CasttiOchetteCh1, self.player)
                         or state.has(ItemName.CasttiOchetteCh2, self.player)))
                or self.world.options.StartingCharacter == StartingCharacter.option_agnea)

    def wellgrove_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh3Mother,self.player))
                or (state.has(ItemName.HikariUnlock, self.player)
                    and state.has(ItemName.HikariCh3, self.player))
                or (state.has(ItemName.PartitioUnlock, self.player)
                    and state.has(ItemName.PartitioCh3,self.player)))

    def timberain_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.CasttiCh4, self.player))

    def oresrush_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.PartitioUnlock, self.player)
                 and state.has(ItemName.PartitioCh1, self.player))
                or (state.has(ItemName.ThroneUnlock, self.player)
                    and state.has(ItemName.ThroneCh2Mother, self.player))
        or self.world.options.StartingCharacter == StartingCharacter.option_partitio)

    def crackridge_unlock(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.TemenosUnlock, self.player)
                 and state.has(ItemName.TemenosCh3Crackridge,self.player))
                or (state.has(ItemName.OchetteUnlock, self.player)
                    and state.has(ItemName.OchetteCh2Tera, self.player)))

    def gravell_unlock(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.OsvaldCh5, self.player))

    # Towns Accesses

    def can_access_capecold(self, state: CollectionState) -> bool:
        return (self.capecold_unlock(state)
                and self.can_access_winterlands1(state))

    def can_access_winterbloom(self, state: CollectionState) -> bool:
        return (self.winterbloom_unlock(state)
                and self.can_access_winterlands1(state))

    def can_access_stormhail(self, state: CollectionState) -> bool:
        return (self.stormhail_unlock(state)
                and self.can_access_winterlands2(state))

    def can_access_flamechurch(self, state: CollectionState) -> bool:
        return (self.flamechurch_unlock(state)
                and self.can_access_crestlands(state))

    def can_access_montwise(self, state: CollectionState) -> bool:
        return (self.montwise_unlock(state)
                and self.can_access_crestlands(state))

    def can_access_merryhills(self, state: CollectionState) -> bool:
        return (self.merryhills_unlock(state)
                and self.can_access_crestlands(state))

    def can_access_newdelsta(self, state: CollectionState) -> bool:
        return (self.newdelsta_unlock(state)
                and self.can_access_brightlands(state))

    def can_access_clockbank(self, state: CollectionState) -> bool:
        return (self.clockbank_unlock(state)
                and self.can_access_brightlands(state))

    def can_access_abandonedvillage(self, state: CollectionState) -> bool:
        return (self.abandonedvillage_unlock(state)
                and self.can_access_brightlands(state))

    def can_access_lostseed(self, state: CollectionState) -> bool:
        return (self.lostseed_unlock(state)
                and self.can_access_brightlands(state))

    def can_access_beasting(self, state: CollectionState) -> bool:
        return (self.beasting_unlock(state)
                and self.can_access_totohaha(state))

    def can_access_tropuhopu(self, state: CollectionState) -> bool:
        return (self.tropuhopu_unlock(state)
                and self.can_access_totohaha(state))

    def can_access_nameless(self, state: CollectionState) -> bool:
        return (self.nameless_unlock(state)
                and self.can_access_totohaha(state)
                and state.has(ItemName.Boat, self.player))

    def can_access_canalbrine(self, state: CollectionState) -> bool:
        return (self.canalbrine_unlock(state)
                and self.can_access_harborlands(state))

    def can_access_conningcreek(self, state: CollectionState) -> bool:
        return (self.conningcreek_unlock(state)
                and self.can_access_harborlands(state))

    def can_access_roqueisland(self, state: CollectionState) -> bool:
        return (self.roqueisland_unlock(state)
                and self.can_access_sea(state))

    def can_access_ryu(self, state: CollectionState) -> bool:
        return (self.ryu_unlock(state)
                and self.can_access_hinoeuma1(state))

    def can_access_sai(self, state: CollectionState) -> bool:
        return (self.sai_unlock(state)
                and self.can_access_hinoeuma2(state))

    def can_access_ku(self, state: CollectionState) -> bool:
        return (self.ku_unlock(state)
                and self.can_access_hinoeuma2(state))

    def can_access_cropdale(self, state: CollectionState) -> bool:
        return (self.cropdale_unlock(state)
                and self.can_access_leaflands(state))

    def can_access_wellgrove(self, state: CollectionState) -> bool:
        return (self.wellgrove_unlock(state)
                and self.can_access_leaflands(state))

    def can_access_timberain(self, state: CollectionState) -> bool:
        return (self.timberain_unlock(state)
                and self.can_access_leaflands(state))

    def can_access_oresrush(self, state: CollectionState) -> bool:
        return (self.oresrush_unlock(state)
                and self.can_access_wildlands1(state))

    def can_access_crackridge(self, state: CollectionState) -> bool:
        return (self.crackridge_unlock(state)
                and self.can_access_wildlands2(state))

    def can_access_gravell(self, state: CollectionState) -> bool:
        return (self.gravell_unlock(state)
                and self.can_access_wildlands2(state))

    # Can Clear Story chapters, unfinished

    def can_clear_osvaldch1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.OsvaldCh1, self.player)
                and self.can_access_capecold(state) and self.can_mug(state)
                and self.can_scrutinize(state))

    def can_clear_osvaldch3(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.OsvaldCh3, self.player)
                and self.can_access_conningcreek(state) and self.can_scrutinize(state))

    def can_clear_osvaldch4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.OsvaldCh4, self.player)
                and self.can_access_montwise(state)
                and self.can_scrutinize(state))

    def can_clear_osvaldch5(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.OsvaldCh5, self.player)
                and self.can_access_gravell(state)
                and self.can_mug(state)
                and self.can_scrutinize(state))

    def can_clear_temenosch1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.TemenosCh1, self.player)
                and self.can_access_flamechurch(state)
                and self.can_guide(state)
                and self.can_coerce(state))

    def can_clear_temenosch2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.TemenosCh2, self.player)
                and self.can_access_canalbrine(state)
                and self.can_guide(state)
                and self.can_coerce(state))

    def can_clear_temenosch3crackridge(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.TemenosCh3Crackridge,self.player)
                and self.can_access_crackridge(state)
                and self.can_guide(state)
                and self.can_coerce(state))

    def can_clear_temenosch3stormhail(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.TemenosCh3Stormhail,self.player)
                and self.can_access_stormhail(state)
                and self.can_guide(state)
                and self.can_coerce(state))

    def can_clear_temenosch4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.TemenosCh4, self.player)
                and self.can_access_nameless(state)
                and self.can_guide(state))

    def can_clear_thronech1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh1, self.player)
                and self.can_access_newdelsta(state)
                and self.can_steal(state)
                and self.can_ambush(state))

    def can_clear_thronech2mother(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh2Mother,self.player)
                and self.can_access_oresrush(state)
                and self.can_steal(state)
                and self.can_ambush(state))

    def can_clear_thronech2father(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh2Father,self.player)
                and self.can_access_winterbloom(state)
                and self.can_ambush(state))

    def can_clear_thronech3mother(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh3Mother,self.player)
                and self.can_access_wellgrove(state)
                and self.can_steal(state)
                and self.can_ambush(state))

    def can_clear_thronech3father(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh3Father,self.player)
                and self.can_access_montwise(state))

    def can_clear_thronech4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.ThroneCh4, self.player)
                and self.can_access_newdelsta(state))

    def can_clear_ochettech1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.OchetteCh1, self.player)
                and self.can_access_beasting(state)
                and self.can_provoke(state)
                and self.can_befriend(state))

    def can_clear_ochettech2acta(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.OchetteCh2Acta,self.player)
                and self.can_access_conningcreek(state)
                and self.can_provoke(state)
                and state.has(ItemName.Boat, self.player))

    def can_clear_ochettech2tera(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.OchetteCh2Tera,self.player)
                and self.can_access_crackridge(state)
                and self.can_befriend(state))

    def can_clear_ochettech2glacis(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.OchetteCh2Glacis,self.player)
                and self.can_access_stormhail(state)
                and self.can_provoke(state))

    def can_clear_ochettech3(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.OchetteCh3, self.player)
                and self.can_access_beasting(state)
                and self.can_befriend(state))

    def can_clear_casttich1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.CasttiCh1, self.player)
                and self.can_access_canalbrine(state)
                and self.can_inquire(state)
                and self.can_soothe(state))

    def can_clear_casttich2sai(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.CasttiCh2Sai, self.player)
                and self.can_access_sai(state)
                and self.can_inquire(state)
                and self.can_soothe(state))

    def can_clear_casttich2winterbloom(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.CasttiCh2Winterbloom, self.player)
                and self.can_access_winterbloom(state)
                and self.can_inquire(state)
                and self.can_soothe(state))

    def can_clear_casttich3(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.CasttiCh3, self.player)
                and self.can_access_abandonedvillage(state)
                and self.can_inquire(state))

    def can_clear_casttich4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player) 
                and state.has(ItemName.CasttiCh4, self.player)
                and self.can_access_timberain(state) 
                and self.can_inquire(state) 
                and self.can_soothe(state))

    def can_clear_hikarich1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player) 
                and state.has(ItemName.HikariCh1, self.player)
                and self.can_access_ryu(state) 
                and self.can_bribe(state) 
                and self.can_challenge(state))

    def can_clear_hikarich2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player) 
                and state.has(ItemName.HikariCh2, self.player)
                and self.can_access_montwise(state) 
                and self.can_bribe(state) 
                and self.can_challenge(state))

    def can_clear_hikarich3(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player) 
                and state.has(ItemName.HikariCh3, self.player)
                and self.can_access_wellgrove(state) 
                and self.can_bribe(state) 
                and self.can_challenge(state))

    def can_clear_hikarich4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player) 
                and state.has(ItemName.HikariCh4, self.player)
                and self.can_access_stormhail(state) 
                and self.can_challenge(state)) # Challenge needed for the flashback duel

    def can_clear_hikarich5(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player) 
                and state.has(ItemName.HikariCh5, self.player)
                and self.can_access_ku(state)
                and self.can_challenge(state))

    def can_clear_partitioch1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player) 
                and state.has(ItemName.PartitioCh1, self.player)
                and self.can_access_oresrush(state) 
                and self.can_purchase(state) 
                and self.can_hire(state))

    def can_clear_partitioch2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioCh2, self.player)
                and self.can_access_clockbank(state)
                and self.can_purchase(state)
                and self.can_hire(state))

    def can_clear_partitioch3(self, state: CollectionState) -> bool:
        return ((state.has(ItemName.PartitioUnlock, self.player)
                 and state.has(ItemName.PartitioCh3, self.player)
                 and self.can_access_wellgrove(state)
                 and self.can_purchase(state)
                 and self.can_hire(state))
                and (self.can_clear_partitiowinterbloom(state) # You don't need to finish these?
                    or self.can_clear_partitiototohaha(state)       # You only need the item, afaik.
                    or self.can_clear_partitiosai(state)))

    def can_clear_partitioch4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioCh4, self.player)
                and self.can_access_roqueisland(state)
                and self.can_purchase(state)
                and self.can_hire(state))

    def can_clear_partitiowinterbloom(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioWinterbloom,self.player)
                and self.can_access_winterbloom(state)
                and self.can_access_canalbrine(state)
                and self.can_access_crackridge(state)
                and self.can_access_flamechurch(state)
                and (self.can_have_followers_night(state)  # Canalbrine is Night Follower, Flamechurch is both
                     or self.can_have_followers_day(state)))  # Crackrdige is Day Follower

    def can_clear_partitiototohaha(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioTotohaha,self.player)
                and self.can_access_tropuhopu(state)
                and self.can_purchase(state))


    def can_clear_partitiosai(self, state: CollectionState) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.PartitioSai,self.player)
                and self.can_access_sai(state)
                and self.can_hire(state))

    def can_clear_agneach1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.AgneaCh1, self.player)
                and self.can_access_cropdale(state)
                and self.can_allure(state)
                and self.can_entreat(state))

    def can_clear_agneach2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.AgneaCh2, self.player)
                and self.can_access_newdelsta(state)
                and self.can_entreat(state)
                and self.can_allure(state))

    def can_clear_agneach3(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.AgneaCh3, self.player)
                and self.can_access_tropuhopu(state)
                and self.can_allure(state)
                and self.can_entreat(state))

    def can_clear_agneach4(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.AgneaCh4, self.player)
                and self.can_access_sai(state)
                and self.can_entreat(state))

    def can_clear_agneach5(self, state: CollectionState) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.AgneaCh5, self.player)
                and self.can_access_merryhills(state)
                and self.can_allure(state))

        # Can Clear Full stories

    def can_clear_osvaldstory(self, state: CollectionState) -> bool:
        return (self.can_clear_osvaldch1(state)
                and self.can_clear_osvaldch3(state)
                and self.can_clear_osvaldch4(state)
                and self.can_clear_osvaldch5(state))

    def can_clear_temenosstory(self, state: CollectionState) -> bool:
        return (self.can_clear_temenosch1(state)
                and self.can_clear_temenosch2(state)
                and self.can_clear_temenosch3crackridge(state)
                and self.can_clear_temenosch3stormhail(state)
                and self.can_clear_temenosch4(state))

    def can_clear_thronestory(self, state: CollectionState) -> bool:
        return (self.can_clear_thronech1(state)
                and self.can_clear_thronech2mother(state)
                and self.can_clear_thronech2father(state)
                and self.can_clear_thronech3mother(state)
                and self.can_clear_thronech3father(state)
                and self.can_clear_thronech4(state))

    def can_clear_ochettestory(self, state: CollectionState) -> bool:
        return (self.can_clear_ochettech1(state)
                and self.can_clear_ochettech2acta(state)
                and self.can_clear_ochettech2tera(state)
                and self.can_clear_ochettech2glacis(state)
                and self.can_clear_ochettech3(state))

    def can_clear_casttistory(self, state: CollectionState) -> bool:
        return (self.can_clear_casttich1(state)
                and self.can_clear_casttich2sai(state)
                and self.can_clear_casttich2winterbloom(state)
                and self.can_clear_casttich3(state)
                and self.can_clear_casttich4(state))

    def can_clear_hikaristory(self, state: CollectionState) -> bool:
        return (self.can_clear_hikarich1(state)
                and self.can_clear_hikarich2(state)
                and self.can_clear_hikarich3(state)
                and self.can_clear_hikarich4(state)
                and self.can_clear_hikarich5(state))

    def can_clear_partitiostory(self, state: CollectionState) -> bool:
        return (self.can_clear_partitioch1(state)
                and self.can_clear_partitioch2(state)
                and self.can_clear_partitioch3(state)
                and self.can_clear_partitioch4(state))

    def can_clear_agneastory(self, state: CollectionState) -> bool:
        return (self.can_clear_agneach1(state)
                and self.can_clear_agneach2(state)
                and self.can_clear_agneach3(state)
                and self.can_clear_agneach4(state)
                and self.can_clear_agneach5(state))

    # Can Clear Dual-Stories
    def can_clear_temenosthronech1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.TemenosThroneCh1, self.player)
                and self.can_access_flamechurch(state)
                and self.can_coerce(state)
                and self.can_guide(state))

    def can_clear_temenosthronech2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player)
                and state.has(ItemName.ThroneUnlock, self.player)
                and state.has(ItemName.TemenosThroneCh2, self.player)
                and self.can_access_conningcreek(state)
                and self.can_access_harborlands(state)
                and self.can_ambush(state)
                and self.can_steal(state))

    def can_clear_hikariagneach1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player)
                and state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.HikariAgneaCh1, self.player)
                and self.can_access_ryu(state)
                and self.can_bribe(state)
            and self.can_entreat(state))

    def can_clear_hikariagneach2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player)
                and state.has(ItemName.AgneaUnlock, self.player)
                and state.has(ItemName.HikariAgneaCh2, self.player)
                and self.can_access_ku(state)
                and self.can_access_hinoeuma2(state)
                and self.can_challenge(state)
                and self.can_entreat(state))

    # Unsure on the Path Actions required for both castti-ochette dual quests, so I put all of them.
        # A: Only Provoke is needed for CasttiOchette2

    def can_clear_casttiochettech1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.CasttiOchetteCh1, self.player)
                and self.can_access_cropdale(state))

    def can_clear_casttiochettech2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player)
                and state.has(ItemName.OchetteUnlock, self.player)
                and state.has(ItemName.CasttiOchetteCh2, self.player)
                and self.can_access_cropdale(state)
                and self.can_provoke(state))

    def can_clear_osvaldpartitioch1(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.PartitioUnlock, self.player)
                and state.has(ItemName.OsvaldPartitioCh1, self.player)
                and self.can_access_newdelsta(state)
                and self.can_purchase(state))  # Only need Purchase for pt1

    def can_clear_osvaldpartitioch2(self, state: CollectionState) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player)
                and state.has(ItemName.PartitioUnlock,self.player)
                and state.has(ItemName.OsvaldPartitioCh2, self.player)
                and self.can_access_montwise(state)
                and self.can_mug(state))  # Only need Mug for pt2





class OT2WorldRules(OT2Rules):
    def __init__(self, ot2world: Octopath2World) -> None:
        # These Rules are Always in effect
        super().__init__(ot2world)
        self.region_rules = {
            # Winterlands regions
            RegionName.Winterlands1: lambda state: self.can_access_winterlands1(state),
            RegionName.Ruffians: lambda state: (self.can_access_winterlands1(state) and (state.has(ItemName.Boat, self.player) or self.can_KO(state))),
            RegionName.RuffiansBoss: lambda state: (self.can_access_winterlands1(state) and state.has(ItemName.Boat, self.player)),
            RegionName.CapeCold: lambda state: self.can_access_capecold(state),
            RegionName.OsvaldCh1: lambda state: self.can_clear_osvaldch1(state),
            RegionName.Winterbloom: lambda state: self.can_access_winterbloom(state),
            RegionName.WinterbloomKO: lambda state: (self.can_access_winterbloom(state) and self.can_KO(state)),
            RegionName.ThroneCh2Father: lambda state: self.can_clear_thronech2father(state),
            RegionName.Winterlands2: lambda state: self.can_access_winterlands2(state),
            RegionName.InfernalCastle: lambda state: (self.can_access_winterlands2(state) and self.can_hire(state) and self.can_guide(state) and self.can_befriend(state) and self.can_allure(state)),
            RegionName.Stormhail: lambda state: self.can_access_stormhail(state),
            RegionName.StormhailKO: lambda state: (self.can_access_stormhail(state) and self.can_KO(state)),
            RegionName.TemenosCh3Stormhail: lambda state: self.can_clear_temenosch3stormhail(state),
            RegionName.HikariCh4: lambda state: self.can_clear_hikarich4(state),
            RegionName.OchetteCh2Glacis: lambda state: self.can_clear_ochettech2glacis(state),
            RegionName.CasttiCh2Winterbloom: lambda state: self.can_clear_casttich2winterbloom(state),
            RegionName.PartitioWinterbloom: lambda state: self.can_clear_partitiowinterbloom(state),
            
            # Crestlands regions
            RegionName.Crestlands: lambda state: self.can_access_crestlands(state),
            RegionName.CrestlandsPass: lambda state: (self.can_access_crestlands(state) and self.can_KO(state)),
            RegionName.SpriteCave: lambda state: (self.can_access_crestlands(state) and state.has(ItemName.Boat, self.player)),
            RegionName.Flamechurch: lambda state: self.can_access_flamechurch(state),
            RegionName.FlamechurchKO: lambda state: (self.can_access_flamechurch(state) and self.can_KO(state)),
            RegionName.TemenosCh1: lambda state: self.can_clear_temenosch1(state),
            RegionName.Montwise: lambda state: self.can_access_montwise(state),
            RegionName.MontwiseKO: lambda state: (self.can_access_montwise(state) and self.can_KO(state)),
            RegionName.HikariCh2: lambda state: self.can_clear_hikarich2(state),
            RegionName.OsvaldCh4: lambda state: self.can_clear_osvaldch4(state),
            RegionName.MerryHills: lambda state: self.can_access_merryhills(state),
            RegionName.AgneaCh5: lambda state: self.can_clear_agneach5(state),
            RegionName.ThroneCh3Father: lambda state: self.can_clear_thronech3father(state),
            RegionName.AgneaClear: lambda state: self.can_clear_agneastory(state),
            
            #Brightlands regions
            RegionName.Brightlands: lambda state: self.can_access_brightlands(state),
            RegionName.Waterway: lambda state: self.can_access_brightlands(state),
            RegionName.SunkenMaw: lambda state: (self.can_access_brightlands(state) and state.has(ItemName.Boat, self.player)),
            RegionName.AbandonedVillage: lambda state: self.can_access_abandonedvillage(state),
            RegionName.NewDelsta: lambda state: self.can_access_newdelsta(state),
            RegionName.NewDelstaAmbush: lambda state: (self.can_access_newdelsta(state) and self.can_ambush(state)),
            RegionName.NewDelstaKO: lambda state: (self.can_access_newdelsta(state) and self.can_KO(state)),
            RegionName.AgneaCh2: lambda state: self.can_clear_agneach2(state),
            RegionName.Clockbank: lambda state: self.can_access_clockbank(state),
            RegionName.PartitioCh2: lambda state: self.can_clear_partitioch2(state),
            RegionName.Clocktower: lambda state: (self.can_access_clockbank(state) and state.has(ItemName.Boat, self.player)),
            RegionName.LostseedPass: lambda state: self.can_access_lostseed(state),
            RegionName.Lostseed: lambda state: self.can_access_lostseed(state),
            RegionName.ThroneCh1: lambda state: self.can_clear_thronech1(state),
            RegionName.ThroneClear: lambda state: self.can_clear_thronestory(state),
            RegionName.CasttiCh3: lambda state: self.can_clear_casttich3(state),
            
            # Totohaha regions
            RegionName.Totohaha: lambda state: self.can_access_totohaha(state),
            RegionName.BeastingVillage: lambda state: self.can_access_beasting(state),
            RegionName.BeastingVillageKO: lambda state: (self.can_access_beasting(state) and self.can_KO(state)),
            RegionName.OchetteCh3: lambda state: self.can_clear_ochettech3(state),
            RegionName.Tropuhopu: lambda state: self.can_access_tropuhopu(state),
            RegionName.TropuhopuKO: lambda state: (self.can_access_tropuhopu(state) and self.can_KO(state)),
            RegionName.TropuhopuKOBoat: lambda state: (self.can_access_winterlands1(state) and self.can_KO(state) and state.has(ItemName.Boat, self.player)),
            RegionName.CavernOfWaves: lambda state: (self.can_access_totohaha(state) and state.has(ItemName.Boat, self.player)),
            RegionName.TotohahaPass: lambda state: (self.can_access_totohaha(state) and state.has(ItemName.Boat, self.player)),
            RegionName.SinkingRuins: lambda state: (self.can_access_totohaha(state) and state.has(ItemName.Boat, self.player)),
            RegionName.NamelessVillage: lambda state: self.can_access_nameless(state),
            RegionName.NamelessVillageKO: lambda state: (self.can_access_nameless(state) and self.can_KO(state)),
            RegionName.TemenosCh4: lambda state: self.can_clear_temenosch4(state),
            RegionName.TemenosClear: lambda state: self.can_clear_temenosstory(state),
            RegionName.OchetteCh1: lambda state: self.can_clear_ochettech1(state),
            RegionName.OchetteClear: lambda state: self.can_clear_ochettestory(state),
            RegionName.PartitioTropuhopu: lambda state: self.can_clear_partitiototohaha(state),
            RegionName.AgneaCh3: lambda state: self.can_clear_agneach3(state),
            
            #Harborlands
            RegionName.Harborlands: lambda state: self.can_access_harborlands(state),
            RegionName.HarborlandsBoat: lambda state: (self.can_access_harborlands(state) and state.has(ItemName.Boat, self.player)),
            RegionName.HarborlandsKO: lambda state: (self.can_access_totohaha(state) and self.can_KO(state)),
            RegionName.SunMoonCave: lambda state: (self.can_access_harborlands(state) and self.can_be_daytime(state) and self.can_be_nighttime(state)),
            RegionName.Canalbrine: lambda state: self.can_access_canalbrine(state),
            RegionName.CanalbrineBoat: lambda state: (self.can_access_canalbrine(state) and state.has(ItemName.Boat, self.player)),            
            RegionName.CanalbrineBoatKO: lambda state: (self.can_access_totohaha(state) and state.has(ItemName.Boat, self.player) and self.can_KO(state)),
            RegionName.TemenosCh2: lambda state: self.can_clear_temenosch2(state),
            RegionName.ConningCreek: lambda state: self.can_access_conningcreek(state),
            RegionName.OsvaldCh3: lambda state: self.can_clear_osvaldch3(state),
            RegionName.OchetteCh2Acta: lambda state: self.can_clear_ochettech2acta(state),
            RegionName.RoqueIsland: lambda state: self.can_access_roqueisland(state),
            RegionName.RoqueIslandKO: lambda state: (self.can_access_roqueisland(state) and self.can_KO(state)),
            RegionName.PartitioCh4: lambda state: self.can_clear_partitioch4(state),
            RegionName.CasttiCh1: lambda state: self.can_clear_casttich1(state),
            RegionName.PartitioClear: lambda state: self.can_clear_partitiostory(state),
            
            # Hinoeuma Regions
            RegionName.Hinoeuma1: lambda state: self.can_access_hinoeuma1(state),
            RegionName.Ryu: lambda state: self.can_access_ryu(state),
            RegionName.Hinoeuma2: lambda state: self.can_access_hinoeuma2(state),
            RegionName.Sai: lambda state: self.can_access_sai(state),
            RegionName.SaiRuins: lambda state: self.can_access_sai(state), # Must add requirements for ruins sidequest here
            RegionName.SaiKO: lambda state: (self.can_access_sai(state) and self.can_KO(state)),
            RegionName.CasttiCh2Sai: lambda state: self.can_clear_casttich2sai(state),
            RegionName.CasttiCh2SaiKO: lambda state: (self.can_clear_casttich2sai(state) and self.can_KO(state)),
            RegionName.Ku: lambda state: self.can_access_ku(state),
            RegionName.HikariCh5: lambda state: self.can_clear_hikarich5(state),
            RegionName.HikariCh1: lambda state: self.can_clear_hikarich1(state),
            RegionName.HikariClear: lambda state: self.can_clear_hikaristory(state),
            RegionName.PartitioSai: lambda state: self.can_clear_partitiosai(state),
            RegionName.AgneaCh4: lambda state: self.can_clear_agneach4(state),
            
            # Leaflands regions
            RegionName.Leaflands: lambda state: self.can_access_leaflands(state),
            RegionName.LeaflandsBoat: lambda state: (self.can_access_leaflands(state) and state.has(ItemName.Boat, self.player)),
            RegionName.Spring: lambda state: (self.can_access_leaflands(state) and state.has(ItemName.Boat, self.player)),
            RegionName.Cropdale: lambda state: self.can_access_cropdale(state),
            RegionName.CropdaleBoat: lambda state: (self.can_access_cropdale(state) and state.has(ItemName.Boat, self.player)),
            RegionName.Wellgrove: lambda state: self.can_access_wellgrove(state),
            RegionName.ThroneCh3Mother: lambda state: self.can_clear_thronech3mother(state),
            RegionName.Timberain: lambda state: self.can_access_timberain(state),
            RegionName.TimberainKO: lambda state: (self.can_access_timberain(state) and self.can_KO(state)),
            RegionName.CasttiCh4: lambda state: self.can_clear_casttich4(state),
            RegionName.CasttiClear: lambda state: self.can_clear_casttistory(state),
            RegionName.HikariCh3: lambda state: self.can_clear_hikarich3(state),
            RegionName.PartitioCh3: lambda state: self.can_clear_partitioch3(state),
            RegionName.AgneaCh1: lambda state: self.can_clear_agneach1(state),
            RegionName.ThroneCh2Mother: lambda state: self.can_clear_thronech2mother(state),
            
            # Wildlands Regions
            RegionName.Wildlands1: lambda state: self.can_access_wildlands1(state),
            RegionName.Oresrush: lambda state: self.can_access_oresrush(state),
            RegionName.OresrushKO: lambda state: (self.can_access_oresrush(state) and self.can_KO(state)),
            RegionName.PartitioCh1: lambda state: self.can_clear_partitioch1(state),
            RegionName.Wildlands2: lambda state: self.can_access_wildlands2(state),
            RegionName.Tunnels: lambda state: (self.can_access_wildlands2(state) and self.can_KO(state)),
            RegionName.Crackridge: lambda state: self.can_access_crackridge(state),
            RegionName.CrackridgeKO: lambda state: (self.can_access_crackridge(state) and self.can_KO(state)),
            RegionName.TemenosCh3Crackridge: lambda state: self.can_clear_temenosch3crackridge(state),
            RegionName.OchetteCh2Tera: lambda state: self.can_clear_ochettech2tera(state),
            RegionName.Gravell: lambda state: self.can_access_gravell(state),
            RegionName.OsvaldCh5: lambda state: self.can_clear_osvaldch5(state),
            RegionName.OsvaldClear: lambda state: self.can_clear_osvaldstory(state),
            
            
            # Sea Regions
            RegionName.SunderingSea: lambda state: self.can_access_sea(state),
            RegionName.SeaBehindScourge: lambda state: self.can_access_sea(state),
            RegionName.SeaIslands: lambda state: self.can_access_sea(state),
            RegionName.SeaBehindShark: lambda state: self.can_access_sea(state),
            RegionName.TyranodrakesLair: lambda state: (self.can_access_sea(state) and state.has(ItemName.Boat, self.player)),
            
            #Side-Stories
            RegionName.ThroneTemenosCh2: lambda state: self.can_clear_temenosthronech2(state),
            RegionName.AgneaHikariCh1: lambda state: self.can_clear_hikariagneach1(state),
            RegionName.AgneaHikariCh2: lambda state: self.can_clear_hikariagneach2(state),
            RegionName.PartitioOsvaldCh1: lambda state: self.can_clear_osvaldpartitioch1(state),
            RegionName.PartitioOsvaldCh2: lambda state: self.can_clear_osvaldpartitioch2(state),
            RegionName.OchetteCasttiCh1: lambda state: self.can_clear_casttiochettech1(state),
            RegionName.OchetteCasttiCh2: lambda state: self.can_clear_casttiochettech2(state),
            
            #Endbosses quests, quests requirements are borked
            RegionName.Vide: lambda state: (self.can_clear_casttiochettech2(state) and self.can_clear_temenosthronech2(state) and self.can_clear_hikariagneach2(state) and self.can_clear_osvaldpartitioch2(state)),
            RegionName.TravelersBag: lambda state: (self.can_clear_casttiochettech2(state) and self.can_clear_temenosthronech2(state) and self.can_clear_hikariagneach2(state) and self.can_clear_osvaldpartitioch2(state)),
            RegionName.PeculiarTomes: lambda state: (self.can_clear_casttiochettech2(state) and self.can_clear_temenosthronech2(state) and self.can_clear_hikariagneach2(state) and self.can_clear_osvaldpartitioch2(state)),
            RegionName.ReachesOfHell: lambda state: (self.can_clear_casttiochettech2(state) and self.can_clear_temenosthronech2(state) and self.can_clear_hikariagneach2(state) and self.can_clear_osvaldpartitioch2(state)),
            RegionName.Galdera: lambda state: (self.can_clear_casttiochettech2(state) and self.can_clear_temenosthronech2(state) and self.can_clear_hikariagneach2(state) and self.can_clear_osvaldpartitioch2(state)),
        }
# I didn't change that one much, need to review it
    def set_ot2_rules(self) -> None:
        for region_name, rules in self.region_rules.items():
            region = self.multiworld.get_region(region_name, self.player)
            for entrance in region.entrances:
                entrance.access_rule = rules
        self.set_ot2_goal()

    def set_ot2_goal(self):
        vide_location = self.multiworld.get_location(LocationName.DefeatVide, self.player)

# We might want to add some fighting rules to split Chapters in tiers (lvl1-10, 11-20, 21-30, 31-40 and final chapters).

        # Old KH2 logic down there


"""
    def set_kh2_rules(self) -> None:
        for region_name, rules in self.region_rules.items():
            region = self.multiworld.get_region(region_name, self.player)
            for entrance in region.entrances:
                entrance.access_rule = rules

        self.set_kh2_goal()

        weapon_region = self.multiworld.get_region(RegionName.Keyblade, self.player)
        for location in weapon_region.locations:
            add_rule(location, lambda state: state.has(exclusion_table["WeaponSlots"][location.name], self.player))
            if location.name in Goofy_Checks:
                add_item_rule(location,
                              lambda item: item.player == self.player and item.name in GoofyAbility_Table.keys())
            elif location.name in Donald_Checks:
                add_item_rule(location,
                              lambda item: item.player == self.player and item.name in DonaldAbility_Table.keys())

    def set_kh2_goal(self):

        final_xemnas_location = self.multiworld.get_location(LocationName.FinalXemnas, self.player)
        if self.multiworld.Goal[self.player] == "three_proofs":
            final_xemnas_location.access_rule = lambda state: self.kh2_has_all(three_proofs, state)
            if self.multiworld.FinalXemnas[self.player]:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Victory,
                                                                                            self.player)
            else:
                self.multiworld.completion_condition[self.player] = lambda state: self.kh2_has_all(three_proofs, state)
        # lucky emblem hunt
        elif self.multiworld.Goal[self.player] == "lucky_emblem_hunt":
            final_xemnas_location.access_rule = lambda state: state.has(ItemName.LuckyEmblem, self.player,
                                                                        self.multiworld.LuckyEmblemsRequired[
                                                                            self.player].value)
            if self.multiworld.FinalXemnas[self.player]:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Victory,
                                                                                            self.player)
            else:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.LuckyEmblem,
                                                                                            self.player,
                                                                                            self.multiworld.LuckyEmblemsRequired[
                                                                                                self.player].value)
        # hitlist if == 2
        elif self.multiworld.Goal[self.player] == "hitlist":
            final_xemnas_location.access_rule = lambda state: state.has(ItemName.Bounty, self.player,
                                                                        self.multiworld.BountyRequired[
                                                                            self.player].value)
            if self.multiworld.FinalXemnas[self.player]:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Victory,
                                                                                            self.player)
            else:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Bounty,
                                                                                            self.player,
                                                                                            self.multiworld.BountyRequired[
                                                                                                self.player].value)
        else:
            final_xemnas_location.access_rule = lambda state: state.has(ItemName.Bounty, self.player,
                                                                        self.multiworld.BountyRequired[
                                                                            self.player].value) and \
                                                              state.has(ItemName.LuckyEmblem, self.player,
                                                                        self.multiworld.LuckyEmblemsRequired[
                                                                            self.player].value)
            if self.multiworld.FinalXemnas[self.player]:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Victory,
                                                                                            self.player)
            else:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Bounty,
                                                                                            self.player,
                                                                                            self.multiworld.BountyRequired[
                                                                                                self.player].value) and \
                                                                                  state.has(ItemName.LuckyEmblem,
                                                                                            self.player,
                                                                                            self.multiworld.LuckyEmblemsRequired[
                                                                                                self.player].value)

"""
