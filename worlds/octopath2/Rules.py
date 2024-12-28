# Imports will need to be changed accordingly
from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .Items import item_table
from .Locations import all_chests
from .Names import LocationName, ItemName, RegionName
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

    def __init__(self, world: Octopath2World) -> None:
        self.player = world.player
        self.world = world
        self.multiworld = world.multiworld

    def can_be_daytime(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TimeChange, self.player, Amount)
                or self.multiworld.startingtime[self.player] == "Day")

    def can_be_nighttime(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TimeChange, self.player, Amount)
                or self.multiworld.startingtime[self.player] == "Night")

    # Regions access

    def can_access_winterlands1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.WinterlandsUnlock, self.player, Amount)
                and (self.can_access_brightlands(state, 1)
                     or self.can_access_crestlands(state, 1))
                or self.multiworld.startingcharacter[self.player] == "Osvald")

    def can_access_crestlands(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CrestlandsUnlock, self.player, Amount)
                and (self.can_access_brightlands(state, 1)
                     or self.can_access_winterlands1(state, 1))
                or self.multiworld.startingcharacter[self.player] == "Temenos")

    def can_access_brightlands(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.BrightlandsUnlock, self.player, Amount)
                and (self.can_access_winterlands1(state, 1)
                     or self.can_access_crestlands(state,1)
                     or self.can_access_totohaha(state, 1)
                     or self.can_access_wildlands2(state, 1))
                or self.multiworld.startingcharacter[self.player] == "Throne")

    def can_access_totohaha(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TotohahaUnlock, self.player, Amount)
                and (self.can_access_brightlands(state, 1)
                    or self.can_access_wildlands2(state, 1))
                or self.multiworld.startingcharacter[self.player] == "Ochette")

    def can_access_harborlands(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.HarborlandsUnlock, self.player, Amount)
                and (self.can_access_brightlands(state, 1)
                    or self.can_access_hinoeuma1(state,1)
                    or self.can_access_hinoeuma2(state, 1)))
                or self.multiworld.startingcharacter[self.player] == "Castti")

    def can_access_hinoeuma1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HinoeumaUnlock, self.player, Amount)
                and (self.can_access_harbolands(state, 1)
                    or self.can_access_wildlands1(state, 1))
                or self.multiworld.startingcharacter[self.player] == "Hikari")

    def can_access_leaflands(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.LeaflandsUnlock, self.player, Amount)
                and (self.can_access_wildlands1(state, 1)
                    or self.can_access_wildlands2(state,1)
                    or self.can_access_hinoeuma2(state, 1)))
                or self.multiworld.startingcharacter[self.player] == "Agnea")

    def can_access_wildlands1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.WildlandsUnlock, self.player, Amount)
                and (self.can_access_hinoeuma1(state, 1)
                    or self.can_access_leaflands(state, 1))
                or self.multiworld.startingcharacter[self.player] == "Partitio")

    def can_access_winterlands2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.WinterlandsUnlock, self.player, Amount)
                and self.can_access_crestlands(state,1)
                and self.can_KO(state, 1))

    def can_access_hinoeuma2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HinoeumaUnlock, self.player, Amount)
                and (self.can_access_harbolands(state, 1))
                or self.can_access_leaflands(state, 1))

    def can_access_wildlands2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.WildlandsUnlock, self.player, Amount)
                and (self.can_access_leaflands(state, 1)
                    or self.can_access_totohaha(state,1)
                    or self.can_access_brightlands(state, 1)))

    def can_access_sea(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TheGrandTerry, self.player, Amount)
                and (self.can_access_brightlands(state, 1)
                     or self.can_access_totohaha(state,1)
                     or self.can_access_wildlands2(state, 1)))

    # Individual Path Action access

    def can_hire(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_purchase(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_allure(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_entreat(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_befriend(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_provoke(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_guide(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_coerce(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_steal(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_ambush(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_inquire(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_soothe(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_challenge(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_bribe(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    def can_scrutinize(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and self.can_be_daytime(state, 1))

    def can_mug(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and self.can_be_nighttime(state, 1))

    # Path Actions results access. 3 types, splitting day and night, for when NPCs will be considered in logic.

    def can_have_followers_day(self, state: CollectionState, Amount) -> bool:
        return (self.can_guide(state, 1)
                or self.can_allure(state, 1))

    def can_have_followers_night(self, state: CollectionState, Amount) -> bool:
        return (self.can_hire(state, 1)
                or self.can_befriend(state, 1))

    def can_have_followers(self, state: CollectionState, Amount) -> bool:
        return (self.can_have_followers_day(state, 1)
                or self.can_have_followers_night(state, 1))

    def can_get_npcitems_day(self, state: CollectionState, Amount) -> bool:
        return (self.can_purchase(state, 1)
                or self.can_steal(state, 1))

    def can_get_npcitems_night(self, state: CollectionState, Amount) -> bool:
        return (self.can_entreat(state, 1)
                or self.can_mug(state, 1))

    def can_get_npcitems(self, state: CollectionState, Amount) -> bool:
        return (self.can_get_npcitems_day(state, 1)
                or self.can_get_npcitems_night(state, 1))

    def can_get_info_day(self, state: CollectionState, Amount) -> bool:
        return (self.can_scrutinize(state, 1)
                or self.can_inquire(state, 1))

    def can_get_info_night(self, state: CollectionState, Amount) -> bool:
        return (self.can_bribe(state, 1)
                or self.can_coerce(state, 1))

    def can_get_info(self, state: CollectionState, Amount) -> bool:
        return (self.can_get_info_day(state, 1)
                or self.can_get_info_night(state, 1))

    def can_KO_day(self, state: CollectionState, Amount) -> bool:
        return (self.can_provoke(state, 1)
                or self.can_challenge(state, 1))

    def can_KO_night(self, state: CollectionState, Amount) -> bool:
        return (self.can_ambush(state, 1)
                or self.can_soothe(state, 1))

    def can_KO(self, state: CollectionState, Amount) -> bool:
        return (self.can_KO_day(state, 1)
                or self.can_KO_night(state, 1))

    # Towns Unlocks

    def capecold_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldCh1, self.player,Amount)
                or self.multiworld.startingcharacter[self.player] == "Osvald")

    def winterbloom_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player, Amount)
                 and state.has(ItemName.ThroneCh2Father,self.player, Amount))
                or (state.has(ItemName.CasttiUnlock, self.player, Amount)
                    and state.has(ItemName.CasttiCh2Winterbloom,self.player, Amount))
                or (state.has(ItemName.PartitioUnlock, self.player, Amount)
                    and state.has(ItemName.PartitioWinterbloom, self.player, Amount)))

    def stormhail_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.HikariUnlock, self.player, Amount)
                 and state.has(ItemName.HikariCh4, self.player,Amount))
                or (state.has(ItemName.OchetteUnlock, self.player, Amount)
                    and state.has(ItemName.OchetteCh2Glacis,self.player, Amount))
                or (state.has(ItemName.TemenosUnlock, self.player, Amount)
                    and state.has(ItemName.TemenosCh3Stormhail,self.player, Amount)))

    def flamechurch_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.TemenosUnlock, self.player, Amount)
                 and state.has(ItemName.TemenosCh1, self.player,Amount))
                or (state.has(ItemName.TemenosUnlock, self.player, Amount)
                    and state.has(ItemName.ThroneUnlock,self.player,Amount)
                    and state.has(ItemName.TemenosThroneCh1, self.player, Amount))
                or self.multiworld.startingcharacter[self.player] == "Temenos")

    def montwise_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player, Amount)
                 and state.has(ItemName.ThroneCh3Father, self.player, Amount))
                or (state.has(ItemName.HikariUnlock, self.player, Amount)
                    and state.has(ItemName.HikariCh4, self.player,Amount))
                or (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                    and state.has(ItemName.OsvaldCh4, self.player,Amount))
                or (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                    and state.has(ItemName.PartitioUnlock, self.player,Amount)
                    and state.has(ItemName.PartitioOsvaldCh2, self.player, Amount)))

    def merryhills_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and state.has(ItemName.AgneaCh5, self.player,Amount))

    def newdelsta_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player, Amount)
                 and state.has(ItemName.ThroneCh1, self.player,Amount))
                or (state.has(ItemName.ThroneUnlock, self.player, Amount)
                    and state.has(ItemName.ThroneCh4, self.player,Amount))
                or (state.has(ItemName.AgneaUnlock, self.player, Amount)
                    and state.has(ItemName.AgneaCh2, self.player,Amount))
                or (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                    and state.has(ItemName.PartitioUnlock,self.player,Amount)
                    and state.has(ItemName.PartitioOsvaldCh1, self.player, Amount))
                or self.multiworld.startingcharacter[self.player] == "Throne")

    def abandonedvillage_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.CasttiCh3, self.player,Amount))

    def clockbank_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioCh2, self.player,Amount))

    def lostseed_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh4, self.player,Amount))

    def beasting_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.OchetteUnlock, self.player, Amount)
                 and state.has(ItemName.OchetteCh1, self.player,Amount))
                or (state.has(ItemName.OchetteUnlock, self.player, Amount)
                    and state.has(ItemName.OchetteCh3, self.player, Amount))
                or self.multiworld.startingcharacter[self.player] == "Ochette")

    def tropuhopu_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.AgneaUnlock, self.player, Amount)
                 and state.has(ItemName.AgneaCh3, self.player,Amount))
                or (state.has(ItemName.PartitioUnlock, self.player, Amount)
                    and state.has(ItemName.PartitioTotohaha,self.player, Amount)))

    def nameless_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.TemenosCh4, self.player, Amount))

    def canalbrine_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.CasttiUnlock, self.player, Amount)
                 and state.has(ItemName.CasttiCh1, self.player,Amount))
                or (state.has(ItemName.TemenosUnlock, self.player, Amount)
                    and state.has(ItemName.TemenosCh2,self.player, Amount))
                or self.multiworld.startingcharacter[self.player] == "Castti")

    def conningcreek_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.OchetteUnlock, self.player, Amount)
                and state.has(ItemName.OchetteCh2Acta,self.player, Amount))
                or (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                    and state.has(ItemName.OsvaldCh3, self.player,Amount))
                or (state.has(ItemName.ThroneUnlock, self.player, Amount)
                    and state.has(ItemName.TemenosUnlock,self.player,Amount)
                    and state.has(ItemName.TemenosThroneCh2, self.player, Amount)))

    def roqueisland_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioCh4, self.player, Amount))

    def ryu_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.HikariUnlock, self.player, Amount)
                 and state.has(ItemName.HikariCh1, self.player,Amount))
                or (state.has(ItemName.HikariUnlock, self.player, Amount)
                    and state.has(ItemName.AgneaUnlock,self.player,Amount)
                    and state.has(ItemName.HikariAgneaCh1, self.player, Amount))
                or self.multiworld.startingcharacter[self.player] == "Hikari")

    def sai_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.CasttiUnlock, self.player, Amount)
                 and state.has(ItemName.CasttiCh2Sai, self.player,Amount))
                or (state.has(ItemName.AgneaUnlock, self.player, Amount)
                    and state.has(ItemName.AgneaCh4, self.player,Amount))
                or (state.has(ItemName.PartitioUnlock, self.player, Amount)
                    and state.has(ItemName.PartitioSai,self.player, Amount)))

    def ku_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.HikariUnlock, self.player, Amount)
                and state.has(ItemName.HikariCh5, self.player,Amount))
                or (state.has(ItemName.HikariUnlock, self.player, Amount)
                    and state.has(ItemName.AgneaUnlock,self.player,Amount)
                    and state.has(ItemName.HikariAgneaCh2, self.player, Amount)))

    def cropdale_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.AgneaUnlock, self.player, Amount)
                 and state.has(ItemName.AgneaCh1, self.player, Amount))
                or (state.has(ItemName.CasttiUnlock, self.player, Amount)
                    and state.has(ItemName.OchetteUnlock,self.player, Amount)
                    and (state.has(ItemName.CasttiOchetteCh1, self.player, Amount)
                         or state.has(ItemName.CasttiOchetteCh2, self.player, Amount)))
                or self.multiworld.startingcharacter[self.player] == "Agnea")

    def wellgrove_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh3Mother,self.player, Amount))
                or (state.has(ItemName.HikariUnlock, self.player, Amount)
                    and state.has(ItemName.HikariCh3, self.player,Amount))
                or (state.has(ItemName.PartitioUnlock, self.player, Amount)
                    and state.has(ItemName.PartitioCh3,self.player, Amount)))

    def timberain_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.CasttiCh4, self.player,Amount))

    def oresrush_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.PartitioUnlock, self.player, Amount)
                 and state.has(ItemName.PartitioCh1, self.player,Amount))
                or (state.has(ItemName.ThroneUnlock, self.player, Amount)
                    and state.has(ItemName.ThroneCh2Mother, self.player, Amount))
        or self.multiworld.startingcharacter[self.player] == "Partitio")

    def crackridge_unlock(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.TemenosUnlock, self.player, Amount)
                 and state.has(ItemName.TemenosCh3Crackridge,self.player, Amount))
                or (state.has(ItemName.OchetteUnlock, self.player, Amount)
                    and state.has(ItemName.OchetteCh2Tera, self.player, Amount)))

    def gravell_unlock(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldCh5, self.player, Amount))

    # Towns Accesses

    def can_access_capecold(self, state: CollectionState, Amount) -> bool:
        return (self.capecold_unlock(state, 1)
                and self.can_access_winterlands1(state, 1))

    def can_access_winterbloom(self, state: CollectionState, Amount) -> bool:
        return (self.winterbloom_unlock(state, 1)
                and self.can_access_winterlands1(state, 1))

    def can_access_stormhail(self, state: CollectionState, Amount) -> bool:
        return (self.stormhail_unlock(state, 1)
                and self.can_access_winterlands2(state, 1))

    def can_access_flamechurch(self, state: CollectionState, Amount) -> bool:
        return (self.flamechurch_unlock(state, 1)
                and self.can_access_crestlands(state, 1))

    def can_access_montwise(self, state: CollectionState, Amount) -> bool:
        return (self.montwise_unlock(state, 1)
                and self.can_access_crestlands(state, 1))

    def can_access_merryhills(self, state: CollectionState, Amount) -> bool:
        return (self.merryhills_unlock(state, 1)
                and self.can_access_crestlands(state, 1))

    def can_access_newdelsta(self, state: CollectionState, Amount) -> bool:
        return (self.newdelsta_unlock(state, 1)
                and self.can_access_brightlands(state, 1))

    def can_access_clockbank(self, state: CollectionState, Amount) -> bool:
        return (self.clockbank_unlock(state, 1)
                and self.can_access_brightlands(state, 1))

    def can_access_abandonedvillage(self, state: CollectionState, Amount) -> bool:
        return (self.abandonedvillage_unlock(state, 1)
                and self.can_access_brightlands(state, 1))

    def can_access_lostseed(self, state: CollectionState, Amount) -> bool:
        return (self.lostseed_unlock(state, 1)
                and self.can_access_brightlands(state, 1))

    def can_access_beasting(self, state: CollectionState, Amount) -> bool:
        return (self.beasting_unlock(state, 1)
                and self.can_access_totohaha(state, 1))

    def can_access_tropuhopu(self, state: CollectionState, Amount) -> bool:
        return (self.tropuhopu_unlock(state, 1)
                and self.can_access_totohaha(state, 1))

    def can_access_nameless(self, state: CollectionState, Amount) -> bool:
        return (self.nameless_unlock(state, 1)
                and self.can_access_totohaha(state, 1)
                and state.has(ItemName.Boat, self.player, Amount))

    def can_access_canalbrine(self, state: CollectionState, Amount) -> bool:
        return (self.canalbrine_unlock(state, 1)
                and self.can_access_harborlands(state, 1))

    def can_access_conningcreek(self, state: CollectionState, Amount) -> bool:
        return (self.conningcreek_unlock(state, 1)
                and self.can_access_harborlands(state, 1))

    def can_access_roqueisland(self, state: CollectionState, Amount) -> bool:
        return (self.roqueisland_unlock(state, 1)
                and self.can_access_sea(state, 1))

    def can_access_ryu(self, state: CollectionState, Amount) -> bool:
        return (self.ryu_unlock(state, 1)
                and self.can_access_hinoeuma1(state, 1))

    def can_access_sai(self, state: CollectionState, Amount) -> bool:
        return (self.sai_unlock(state, 1)
                and self.can_access_hinoeuma2(state, 1))

    def can_access_ku(self, state: CollectionState, Amount) -> bool:
        return (self.ku_unlock(state, 1)
                and self.can_access_hinoeuma2(state, 1))

    def can_access_cropdale(self, state: CollectionState, Amount) -> bool:
        return (self.cropdale_unlock(state, 1)
                and self.can_access_leaflands(state, 1))

    def can_access_wellgrove(self, state: CollectionState, Amount) -> bool:
        return (self.wellgrove_unlock(state, 1)
                and self.can_access_leaflands(state, 1))

    def can_access_timberain(self, state: CollectionState, Amount) -> bool:
        return (self.timberain_unlock(state, 1)
                and self.can_access_leaflands(state, 1))

    def can_access_oresrush(self, state: CollectionState, Amount) -> bool:
        return (self.oresrush_unlock(state, 1)
                and self.can_access_wildlands1(state, 1))

    def can_access_crackridge(self, state: CollectionState, Amount) -> bool:
        return (self.crackridge_unlock(state, 1)
                and self.can_access_wildlands2(state, 1))

    def can_access_gravell(self, state: CollectionState, Amount) -> bool:
        return (self.gravell_unlock(state, 1)
                and self.can_access_wildlands2(state, 1))

    # Can Clear Story chapters, unfinished

    def can_clear_osvaldch1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldCh1, self.player,Amount)
                and self.can_access_capecold(state, 1) and self.can_mug(state, 1)
                and self.can_scrutinize(state, 1))

    def can_clear_osvaldch3(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldCh3, self.player,Amount)
                and self.can_access_conningcreek(state, 1) and self.can_scrutinize(state, 1))

    def can_clear_osvaldch4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldCh4, self.player,Amount)
                and self.can_access_montwise(state, 1)
                and self.can_scrutinize(state, 1))

    def can_clear_osvaldch5(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldCh5, self.player,Amount)
                and self.can_access_gravell(state, 1)
                and self.can_mug(state, 1)
                and self.can_scrutinize(state, 1))

    def can_clear_temenosch1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.TemenosCh1, self.player,Amount)
                and self.can_access_flamechurch(state, 1)
                and self.can_guide(state, 1)
                and self.can_coerce(state, 1))

    def can_clear_temenosch2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.TemenosCh2, self.player,Amount)
                and self.can_access_canalbrine(state, 1)
                and self.can_guide(state, 1)
                and self.can_coerce(state, 1))

    def can_clear_temenosch3crackridge(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.TemenosCh3Crackridge,self.player,Amount)
                and self.can_access_crackridge(state, 1)
                and self.can_guide(state, 1)
                and self.can_coerce(state, 1))

    def can_clear_temenosch3stormhail(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.TemenosCh3Stormhail,self.player,Amount)
                and self.can_access_stormhail(state, 1)
                and self.can_guide(state, 1)
                and self.can_coerce(state, 1))

    def can_clear_temenosch4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.TemenosCh4, self.player,Amount)
                and self.can_access_nameless(state, 1)
                and self.can_guide(state, 1))

    def can_clear_thronech1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh1, self.player,Amount)
                and self.can_access_newdelsta(state, 1)
                and self.can_steal(state, 1)
                and self.can_ambush(state, 1))

    def can_clear_thronech2mother(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh2Mother,self.player,Amount)
                and self.can_access_oresrush(state, 1)
                and self.can_steal(state, 1)
                and self.can_ambush(state, 1))

    def can_clear_thronech2father(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh2Father,self.player,Amount)
                and self.can_access_winterbloom(state, 1)
                and self.can_ambush(state, 1))

    def can_clear_thronech3mother(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh3Mother,self.player,Amount)
                and self.can_access_wellgrove(state, 1)
                and self.can_steal(state, 1)
                and self.can_ambush(state, 1))

    def can_clear_thronech3father(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh3Father,self.player,Amount)
                and self.can_access_montwise(state, 1))

    def can_clear_thronech4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.ThroneUnlock, self.player, Amount)
                and state.has(ItemName.ThroneCh4, self.player,Amount)
                and self.can_access_newdelsta(state, 1))

    def can_clear_ochettech1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and state.has(ItemName.OchetteCh1, self.player,Amount)
                and self.can_access_beasting(state, 1)
                and self.can_provoke(state, 1)
                and self.can_befriend(state, 1))

    def can_clear_ochettech2acta(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and state.has(ItemName.OchetteCh2Acta,self.player,Amount)
                and self.can_access_conningcreek(state, 1)
                and self.can_provoke(state, 1)
                and state.has(ItemName.Boat, self.player, Amount))

    def can_clear_ochettech2tera(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and state.has(ItemName.OchetteCh2Tera,self.player,Amount)
                and self.can_access_crackridge(state, 1)
                and self.can_befriend(state, 1))

    def can_clear_ochettech2glacis(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and state.has(ItemName.OchetteCh2Glacis,self.player,Amount)
                and self.can_access_stormhail(state, 1)
                and self.can_provoke(state, 1))

    def can_clear_ochettech3(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OchetteUnlock, self.player, Amount)
                and state.has(ItemName.OchetteCh3, self.player,Amount)
                and self.can_access_beasting(state, 1)
                and self.can_befriend(state, 1))

    def can_clear_casttich1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.CasttiCh1, self.player,Amount)
                and self.can_access_canalbrine(state, 1)
                and self.can_inquire(state, 1)
                and self.can_soothe(state, 1))

    def can_clear_casttich2sai(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.CasttiCh2sai, self.player,Amount)
                and self.can_access_sai(state, 1)
                and self.can_inquire(state, 1)
                and self.can_soothe(state, 1))

    def can_clear_casttich2winterbloom(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.CasttiCh2winterbloom, self.player,Amount)
                and self.can_access_winterbloom(state, 1)
                and self.can_inquire(state, 1)
                and self.can_soothe(state, 1))

    def can_clear_casttich3(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.CasttiCh3, self.player,Amount)
                and self.can_access_abandonnedvillage(state, 1)
                and self.can_inquire(state, 1))

    def can_clear_casttich4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount) 
                and state.has(ItemName.CasttiCh4, self.player,Amount) 
                and self.can_access_timberain(state, 1) 
                and self.can_inquire(state, 1) 
                and self.can_soothe(state, 1))

    def can_clear_hikarich1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount) 
                and state.has(ItemName.HikariCh1, self.player,Amount) 
                and self.can_access_ryu(state, 1) 
                and self.can_bribe(state, 1) 
                and self.can_challenge(state, 1))

    def can_clear_hikarich2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount) 
                and state.has(ItemName.HikariCh2, self.player,Amount) 
                and self.can_access_montwise(state, 1) 
                and self.can_bribe(state, 1) 
                and self.can_challenge(state, 1))

    def can_clear_hikarich3(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount) 
                and state.has(ItemName.HikariCh3, self.player,Amount) 
                and self.can_access_wellgrove(state, 1) 
                and self.can_bribe(state, 1) 
                and self.can_challenge(state, 1))

    def can_clear_hikarich4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount) 
                and state.has(ItemName.HikariCh4, self.player,Amount) 
                and self.can_access_stormhail(state, 1) 
                and self.can_challenge(state, 1)) # Challenge needed for the flashback duel

    def can_clear_hikarich5(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount) 
                and state.has(ItemName.HikariCh5, self.player,Amount) 
                and self.can_access_ku(state, 1)
                and self.can_challenge(state, 1))

    def can_clear_partitioch1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount) 
                and state.has(ItemName.PartitioCh1, self.player,Amount) 
                and self.can_access_oresrush(state, 1) 
                and self.can_purchase(state, 1) 
                and self.can_hire(state, 1))

    def can_clear_partitioch2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioCh2, self.player,Amount)
                and self.can_access_clockbank(state, 1)
                and self.can_purchase(state, 1)
                and self.can_hire(state, 1))

    def can_clear_partitioch3(self, state: CollectionState, Amount) -> bool:
        return ((state.has(ItemName.PartitioUnlock, self.player, Amount)
                 and state.has(ItemName.PartitioCh3, self.player,Amount)
                 and self.can_access_wellgrove(state, 1)
                 and self.can_purchase(state, 1)
                 and self.can_hire(state, 1))
                and (self.can_clear_partitiowinterbloom(state, 1) # You don't need to finish these?
                    or self.can_clear_partitiototohaha(state,1)       # You only need the item, afaik.
                    or self.can_clear_partitiosai(state, 1)))

    def can_clear_partitioch4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioCh4, self.player,Amount)
                and self.can_access_roqueisland(state, 1)
                and self.can_purchase(state, 1)
                and self.can_hire(state, 1))

    def can_clear_partitiowinterbloom(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioWinterbloom,self.player,Amount)
                and self.can_access_winterbloom(state, 1)
                and self.can_access_canalbrine(state, 1)
                and self.can_access_crackridge(state,1)
                and self.can_access_flamechurch(state, 1)
                and (self.can_have_followers_night(state, 1)  # Canalbrine is Night Follower, Flamechurch is both
                     or self.can_have_followers_day(state, 1)))  # Crackrdige is Day Follower

    def can_clear_partitiototohaha(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioTotohaha,self.player,Amount)
                and self.can_access_tropuhopu(state, 1)
                and self.can_purchase(state, 1))


    def can_clear_partitiosai(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.PartitioSai,self.player,Amount)
                and self.can_access_sai(state, 1)
                and self.can_hire(state, 1))

    def can_clear_agneach1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and state.has(ItemName.AgneaCh1, self.player,Amount)
                and self.can_access_cropdale(state, 1)
                and self.can_allure(state, 1)
                and self.can_entreat(state, 1))

    def can_clear_agneach2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and state.has(ItemName.AgneaCh2, self.player,Amount)
                and self.can_access_newdelsta(state, 1)
                and self.can_entreat(state, 1)
                and self.can_allure(state, 1))

    def can_clear_agneach3(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and state.has(ItemName.AgneaCh3, self.player,Amount)
                and self.can_access_tropuhopu(state, 1)
                and self.can_allure(state, 1)
                and self.can_entreat(state, 1))

    def can_clear_agneach4(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and state.has(ItemName.AgneaCh4, self.player,Amount)
                and self.can_access_sai(state, 1)
                and self.can_entreat(state, 1))

    def can_clear_agneach5(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.AgneaUnlock, self.player, Amount)
                and state.has(ItemName.AgneaCh5, self.player,Amount)
                and self.can_access_merryhills(state, 1)
                and self.can_allure(state, 1))

        # Can Clear Full stories

    def can_clear_osvaldstory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_osvaldch1(state, 1)
                and self.can_clear_osvaldch3(state, 1)
                and self.can_clear_osvaldch4(state, 1)
                and self.can_clear_osvaldch5(state, 1))

    def can_clear_temenosstory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_temenosch1(state, 1)
                and self.can_clear_temenosch2(state,1)
                and self.can_clear_temenosch3crackridge(state, 1)
                and self.can_clear_temenosch3stormhail(state, 1)
                and self.can_clear_temenosch4(state, 1))

    def can_clear_thronestory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_thronech1(state, 1)
                and self.can_clear_thronech2mother(state,1)
                and self.can_clear_thronech2father(state, 1)
                and self.can_clear_thronech3mother(state, 1)
                and self.can_clear_thronech3father(state,1)
                and self.can_clear_thronech4(state, 1))

    def can_clear_ochettestory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_ochettech1(state, 1)
                and self.can_clear_ochettech2acta(state,1)
                and self.can_clear_ochettech2tera(state, 1)
                and self.can_clear_ochettech2glacis(state, 1)
                and self.can_clear_ochettech3(state, 1))

    def can_clear_casttistory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_casttich1(state, 1)
                and self.can_clear_casttich2sai(state,1)
                and self.can_clear_casttich2winterbloom(state, 1)
                and self.can_clear_casttich3(state, 1)
                and self.can_clear_casttich4(state, 1))

    def can_clear_hikaristory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_hikarich1(state, 1)
                and self.can_clear_hikarich2(state, 1)
                and self.can_clear_hikarich3(state, 1)
                and self.can_clear_hikarich4(state, 1)
                and self.can_clear_hikarich5(state, 1))

    def can_clear_partitiostory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_partitioch1(state, 1)
                and self.can_clear_partitioch2(state,1)
                and self.can_clear_partitioch3(state, 1)
                and self.can_clear_partitioch4(state, 1))

    def can_clear_agneastory(self, state: CollectionState, Amount) -> bool:
        return (self.can_clear_agneach1(state, 1)
                and self.can_clear_agneach2(state, 1)
                and self.can_clear_agneach3(state, 1)
                and self.can_clear_agneach4(state, 1)
                and self.can_clear_agneach5(state, 1))

    # Can Clear Dual-Stories
    def can_clear_temenosthronech1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.ThroneUnlock, self.player,Amount)
                and state.has(ItemName.TemenosThroneCh1, self.player, Amount)
                and self.can_access_flamechurch(state,1)
                and self.can_coerce(state, 1)
                and self.can_guide(state, 1))

    def can_clear_temenosthronech2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.TemenosUnlock, self.player, Amount)
                and state.has(ItemName.ThroneUnlock, self.player,Amount)
                and state.has(ItemName.TemenosThroneCh2, self.player, Amount)
                and self.can_access_conningcreek(state,1)
                and self.can_access_harborlands(state, 1)
                and self.can_ambush(state, 1)
                and self.can_steal(state, 1))

    def can_clear_hikariagneach1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount)
                and state.has(ItemName.AgneaUnlock, self.player,Amount)
                and state.has(ItemName.HikariAgneaCh1, self.player, Amount)
                and self.can_access_ryu(state, 1)
                and self.can_bribe(state,1)
            and self.can_entreat(state, 1))

    def can_clear_hikariagneach2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.HikariUnlock, self.player, Amount)
                and state.has(ItemName.AgneaUnlock, self.player,Amount)
                and state.has(ItemName.HikariAgneaCh2, self.player, Amount)
                and self.can_access_ku(state,1)
                and self.can_access_hinoeuma2(state,1)
                and self.can_challenge(state, 1)
                and self.can_entreat(state, 1))

    # Unsure on the Path Actions required for both castti-ochette dual quests, so I put all of them.
        # A: Only Provoke is needed for CasttiOchette2

    def can_clear_casttiochettech1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.OchetteUnlock, self.player,Amount)
                and state.has(ItemName.CasttiOchetteCh1, self.player, Amount)
                and self.can_access_cropdale(state, 1))

    def can_clear_casttiochettech2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.CasttiUnlock, self.player, Amount)
                and state.has(ItemName.OchetteUnlock, self.player,Amount)
                and state.has(ItemName.CasttiOchetteCh2, self.player, Amount)
                and self.can_access_cropdale(state, 1)
                and self.can_provoke(state, 1))

    def can_clear_osvaldpartitioch1(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.PartitioUnlock, self.player, Amount)
                and state.has(ItemName.OsvaldPartitioCh1, self.player, Amount)
                and self.can_access_newdelsta(state, 1)
                and self.can_purchase(state, 1))  # Only need Purchase for pt1

    def can_clear_osvaldpartitioch2(self, state: CollectionState, Amount) -> bool:
        return (state.has(ItemName.OsvaldUnlock, self.player, Amount)
                and state.has(ItemName.PartitioUnlock,self.player, Amount)
                and state.has(ItemName.OsvaldPartitioCh2, self.player, Amount)
                and self.can_access_montwise(state, 1)
                and self.can_mug(state, 1))  # Only need Mug for pt2





class OT2WorldRules(OT2Rules):
    def __init__(self, ot2world: Octopath2World) -> None:
        # These Rules are Always in effect
        super().__init__(ot2world)
        self.region_rules = {
            # Winterlands regions
            RegionName.Winterlands1: lambda state: self.can_access_winterlands1(state, 1),
            RegionName.Ruffians: lambda state: (self.can_access_winterlands1(state, 1) and (state.has(ItemName.Boat, self.player, Amount) or self.can_KO(state,1))),
            RegionName.RuffiansBoss: lambda state: (self.can_access_winterlands1(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.CapeCold: lambda state: self.can_access_capecold(state, 1),
            RegionName.OsvaldCh1: lambda state: self.can_clear_osvaldch1(state, 1),
            RegionName.Winterbloom: lambda state: self.can_access_winterbloom(state, 1),
            RegionName.WinterbloomKO: lambda state: (self.can_access_winterbloom(state, 1) and self.can_KO(state,1)),
            RegionName.ThroneCh2Father: lambda state: self.can_clear_thronech2father(state, 1),
            RegionName.Winterlands2: lambda state: self.can_access_winterlands2(state, 1),
            RegionName.InfernalCastle: lambda state: (self.can_access_winterlands2(state, 1) and self.can_hire(state,1) and self.can_guide(state,1) and self.can_befriend(state,1) and self.can_allure(state,1)),
            RegionName.Stormhail: lambda state: self.can_access_stormhail(state, 1),
            RegionName.StormhailKO: lambda state: (self.can_access_stormhail(state, 1) and self.can_KO(state,1)),
            RegionName.TemenosCh3Stormhail: lambda state: self.can_clear_temenosch3stormhail(state, 1),
            RegionName.HikariCh4: lambda state: self.can_clear_hikarich4(state, 1),
            RegionName.OchetteCh2Glacis: lambda state: self.can_clear_ochettech2glacis(state, 1),
            RegionName.CasttiCh2Winterbloom: lambda state: self.can_clear_casttich2winterbloom(state, 1),
            RegionName.PartitioWinterbloom: lambda state: self.can_clear_partitiowinterbloom(state, 1),
            
            # Crestlands regions
            RegionName.Crestlands: lambda state: self.can_access_crestlands(state, 1),
            RegionName.CrestlandsPass: lambda state: (self.can_access_crestlands(state, 1) and self.can_KO(state,1)),
            RegionName.SpriteCave: lambda state: (self.can_access_crestlands(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.Flamechurch: lambda state: self.can_access_flamechurch(state, 1),
            RegionName.FlamechurchKO: lambda state: (self.can_access_flamechurch(state, 1) and self.can_KO(state,1)),
            RegionName.TemenosCh1: lambda state: self.can_clear_temenosch1(state, 1),
            RegionName.Montwise: lambda state: self.can_access_montwise(state, 1),
            RegionName.MontwiseKO: lambda state: (self.can_access_montwise(state, 1) and self.can_KO(state, 1)),
            RegionName.HikariCh2: lambda state: self.can_clear_hikarich2(state, 1),
            RegionName.OsvaldCh4: lambda state: self.can_clear_osvaldch4(state, 1),
            RegionName.MerryHills: lambda state: self.can_access_merryhills(state, 1),
            RegionName.AgneaCh5: lambda state: self.can_clear_agneach5(state, 1),
            RegionName.ThroneCh3Father: lambda state: self.can_clear_thronech3father(state, 1),
            RegionName.AgneaClear: lambda state: self.can_clear_agneastory(state, 1),
            
            #Brightlands regions
            RegionName.Brightlands: lambda state: self.can_access_brightlands(state, 1),
            RegionName.Waterway: lambda state: self.can_access_brightlands(state, 1),
            RegionName.SunkenMaw: lambda state: (self.can_access_brightlands(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.AbandonedVillage: lambda state: self.can_access_abandonedvillage(state, 1),
            RegionName.NewDelsta: lambda state: self.can_access_newdelsta(state, 1),
            RegionName.NewDelstaAmbush: lambda state: (self.can_access_newdelsta(state, 1) and self.can_ambush(state,1)),
            RegionName.NewDelstaKO: lambda state: (self.can_access_newdelsta(state, 1) and self.can_KO(state,1)),
            RegionName.AgneaCh2: lambda state: self.can_clear_agneach2(state, 1),
            RegionName.Clockbank: lambda state: self.can_access_clockbank(state, 1),
            RegionName.PartitioCh2: lambda state: self.can_clear_partitioch2(state, 1),
            RegionName.Clocktower: lambda state: (self.can_access_clockbank(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.LostseedPass: lambda state: self.can_access_lostseed(state, 1),
            RegionName.Lostseed: lambda state: self.can_access_lostseed(state, 1),
            RegionName.ThroneCh1: lambda state: self.can_clear_thronech1(state, 1),
            RegionName.ThroneClear: lambda state: self.can_clear_thronestory(state, 1),
            RegionName.CasttiCh3: lambda state: self.can_clear_casttich3(state, 1),
            
            # Totohaha regions
            RegionName.Totohaha: lambda state: self.can_access_totohaha(state, 1),
            RegionName.BeastingVillage: lambda state: self.can_access_beasting(state, 1),
            RegionName.BeastingVillageKO: lambda state: (self.can_access_beasting(state, 1) and self.can_KO(state, 1)),
            RegionName.OchetteCh3: lambda state: self.can_clear_ochettech3(state, 1),
            RegionName.Tropuhopu: lambda state: self.can_access_tropuhopu(state, 1),
            RegionName.TropuhopuKO: lambda state: (self.can_access_tropuhopu(state, 1) and self.can_KO(state, 1)),
            RegionName.TropuhopuKOBoat: lambda state: (self.can_access_winterlands1(state, 1) and self.can_KO(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.CavernOfWaves: lambda state: (self.can_access_totohaha(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.TotohahaPass: lambda state: (self.can_access_totohaha(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.SinkingRuins: lambda state: (self.can_access_totohaha(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.NamelessVillage: lambda state: self.can_access_nameless(state, 1),
            RegionName.NamelessVillageKO: lambda state: (self.can_access_nameless(state, 1) and self.can_KO(state, 1)),
            RegionName.TemenosCh4: lambda state: self.can_clear_temenosch4(state, 1),
            RegionName.TemenosClear: lambda state: self.can_clear_temenosstory(state, 1),
            RegionName.OchetteCh1: lambda state: self.can_clear_ochettech1(state, 1),
            RegionName.OchetteClear: lambda state: self.can_clear_ochettestory(state, 1),
            RegionName.PartitioTropuhopu: lambda state: self.can_clear_partitiototohaha(state, 1),
            RegionName.AgneaCh3: lambda state: self.can_clear_agneach3(state, 1),
            
            #Harborlands
            RegionName.Harborlands: lambda state: self.can_access_harborlands(state, 1),
            RegionName.HarborlandsBoat: lambda state: (self.can_access_harborlands(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.HarborlandsKO: lambda state: (self.can_access_totohaha(state, 1) and self.can_KO(state, 1)),
            RegionName.SunMoonCave: lambda state: (self.can_access_harborlands(state, 1) and self.can_be_daytime(state, 1) and self.can_be_nighttime(state,1)),
            RegionName.Canalbrine: lambda state: self.can_access_canalbrine(state, 1),
            RegionName.CanalbrineBoat: lambda state: (self.can_access_canalbrine(state, 1) and state.has(ItemName.Boat, self.player, Amount)),            
            RegionName.CanalbrineBoatKO: lambda state: (self.can_access_totohaha(state, 1) and state.has(ItemName.Boat, self.player, Amount) and self.can_KO(state, 1)),
            RegionName.TemenosCh2: lambda state: self.can_clear_temenosch2(state, 1),
            RegionName.ConningCreek: lambda state: self.can_access_conningcreek(state, 1),
            RegionName.OsvaldCh3: lambda state: self.can_clear_osvaldch3(state, 1),
            RegionName.OchetteCh2Acta: lambda state: self.can_clear_ochettech2Acta(state, 1),
            RegionName.RoqueIsland: lambda state: self.can_access_roqueisland(state, 1),
            RegionName.RoqueIslandKO: lambda state: (self.can_access_roqueisland(state, 1) and self.can_KO(state, 1)),
            RegionName.PartitioCh4: lambda state: self.can_clear_partitioch4(state, 1),
            RegionName.CasttiCh1: lambda state: self.can_clear_casttich1(state, 1),
            RegionName.PartitioClear: lambda state: self.can_clear_partitiostory(state, 1),
            
            # Hinoeuma Regions
            RegionName.Hinoeuma1: lambda state: self.can_access_hinoeuma1(state, 1),
            RegionName.Ryu: lambda state: self.can_access_ryu(state, 1),
            RegionName.Hinoeuma2: lambda state: self.can_access_hinoeuma2(state, 1),
            RegionName.Sai: lambda state: self.can_access_sai(state, 1),
            RegionName.SaiRuins: lambda state: self.can_access_sai(state, 1), # Must add requirements for ruins sidequest here
            RegionName.SaiKO: lambda state: (self.can_access_sai(state, 1) and self.can_KO(state, 1)),
            RegionName.CasttiCh2Sai: lambda state: self.can_clear_casttich2sai(state, 1),
            RegionName.CasttiCh2SaiKO: lambda state: (self.can_clear_casttich2sai(state, 1) and self.can_KO(state, 1)),
            RegionName.Ku: lambda state: self.can_access_ku(state, 1),
            RegionName.HikariCh5: lambda state: self.can_clear_hikarich5(state, 1),
            RegionName.HikariCh1: lambda state: self.can_clear_hikarich1(state, 1),
            RegionName.HikariClear: lambda state: self.can_clear_hikaristory(state, 1),
            RegionName.PartitioSai: lambda state: self.can_clear_partitiosai(state, 1),
            RegionName.AgneaCh4: lambda state: self.can_clear_agneach4(state, 1),
            
            # Leaflands regions
            RegionName.Leaflands: lambda state: self.can_access_leaflands(state, 1),
            RegionName.LeaflandsBoat: lambda state: (self.can_access_leaflands(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.Spring: lambda state: (self.can_access_leaflands(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.Cropdale: lambda state: self.can_access_cropdale(state, 1),
            RegionName.CropdaleBoat: lambda state: (self.can_access_cropdale(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            RegionName.Wellgrove: lambda state: self.can_access_wellgrove(state, 1),
            RegionName.ThroneCh3Mother: lambda state: self.can_clear_thronech3mother(state, 1),
            RegionName.Timberain: lambda state: self.can_access_timberain(state, 1),
            RegionName.TimberainKO: lambda state: (self.can_access_timberain(state, 1) and self.can_KO(state, 1)),
            RegionName.CasttiCh4: lambda state: self.can_clear_casttich4(state, 1),
            RegionName.CasttiClear: lambda state: self.can_clear_casttistory(state, 1),
            RegionName.HikariCh3: lambda state: self.can_clear_hikarich3(state, 1),
            RegionName.PartitioCh3: lambda state: self.can_clear_partitioch3(state, 1),
            RegionName.AgneaCh1: lambda state: self.can_clear_agneach1(state, 1),
            RegionName.ThroneCh2Mother: lambda state: self.can_clear_thronech2mother(state, 1),
            
            # Wildlands Regions
            RegionName.Wildlands1: lambda state: self.can_access_wildlands1(state, 1),
            RegionName.Oresrush: lambda state: self.can_access_oresrush(state, 1),
            RegionName.OresrushKO: lambda state: (self.can_access_oresrush(state, 1) and self.can_KO(state, 1)),
            RegionName.PartitioCh1: lambda state: self.can_clear_partitioch1(state, 1),
            RegionName.Wildlands2: lambda state: self.can_access_wildlands2(state, 1),
            RegionName.Tunnels: lambda state: (self.can_access_wildlands2(state, 1) and self.can_KO(state, 1)),
            RegionName.Crackridge: lambda state: self.can_access_crackridge(state, 1),
            RegionName.CrackridgeKO: lambda state: (self.can_access_crackridge(state, 1) and self.can_KO(state, 1)),
            RegionName.TemenosCh3Crackridge: lambda state: self.can_clear_temenosch3crackridge(state, 1),
            RegionName.OchetteCh2Tera: lambda state: self.can_clear_ochettech2tera(state, 1),
            RegionName.Gravell: lambda state: self.can_access_gravell(state, 1),
            RegionName.OsvaldCh5: lambda state: self.can_clear_osvaldch5(state, 1),
            RegionName.OsvaldClear: lambda state: self.can_clear_osvaldstory(state, 1),
            
            
            # Sea Regions
            RegionName.SunderingSea: lambda state: self.can_access_sea(state, 1),
            RegionName.SeaBehindScourge: lambda state: self.can_access_sea(state, 1),
            RegionName.SeaIslands: lambda state: self.can_access_sea(state, 1),
            RegionName.SeaBehindShark: lambda state: self.can_access_sea(state, 1),
            RegionName.TyranodrakesLair: lambda state: (self.can_access_sea(state, 1) and state.has(ItemName.Boat, self.player, Amount)),
            
            #Side-Stories
            RegionName.ThroneTemenosCh2: lambda state: self.can_clear_temenosthronech2(state, 1),
            RegionName.AgneaHikariCh1: lambda state: self.can_clear_hikariagneach1(state, 1),
            RegionName.AgneaHikariCh2: lambda state: self.can_clear_hikariagneach2(state, 1),
            RegionName.PartitioOsvaldCh1: lambda state: self.can_clear_osvaldpartitioch1(state, 1),
            RegionName.PartitioOsvaldCh2: lambda state: self.can_clear_osvaldpartitioch2(state, 1),
            RegionName.OchetteCasttiCh1: lambda state: self.can_clear_casttiochettech1(state, 1),
            RegionName.OchetteCasttiCh2: lambda state: self.can_clear_casttiochettech2(state, 1),
            
            #Endbosses quests, quests requirements are borked
            RegionName.Vide: lambda state: (self.can_clear_casttiochettech2(state, 1) and self.can_clear_temenosthronech2(state, 1) and self.can_clear_hikariagneach2(state, 1) and self.can_clear_osvaldpartitioch2(state, 1)),
            RegionName.TravelersBag: lambda state: (self.can_clear_casttiochettech2(state, 1) and self.can_clear_temenosthronech2(state, 1) and self.can_clear_hikariagneach2(state, 1) and self.can_clear_osvaldpartitioch2(state, 1)),
            RegionName.PeculiarTomes: lambda state: (self.can_clear_casttiochettech2(state, 1) and self.can_clear_temenosthronech2(state, 1) and self.can_clear_hikariagneach2(state, 1) and self.can_clear_osvaldpartitioch2(state, 1)),
            RegionName.ReachesOfHell: lambda state: (self.can_clear_casttiochettech2(state, 1) and self.can_clear_temenosthronech2(state, 1) and self.can_clear_hikariagneach2(state, 1) and self.can_clear_osvaldpartitioch2(state, 1)),
            RegionName.Galdera: lambda state: (self.can_clear_casttiochettech2(state, 1) and self.can_clear_temenosthronech2(state, 1) and self.can_clear_hikariagneach2(state, 1) and self.can_clear_osvaldpartitioch2(state, 1)),
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
                                                                                            self.player, 1)
            else:
                self.multiworld.completion_condition[self.player] = lambda state: self.kh2_has_all(three_proofs, state)
        # lucky emblem hunt
        elif self.multiworld.Goal[self.player] == "lucky_emblem_hunt":
            final_xemnas_location.access_rule = lambda state: state.has(ItemName.LuckyEmblem, self.player,
                                                                        self.multiworld.LuckyEmblemsRequired[
                                                                            self.player].value)
            if self.multiworld.FinalXemnas[self.player]:
                self.multiworld.completion_condition[self.player] = lambda state: state.has(ItemName.Victory,
                                                                                            self.player, 1)
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
                                                                                            self.player, 1)
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
                                                                                            self.player, 1)
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
