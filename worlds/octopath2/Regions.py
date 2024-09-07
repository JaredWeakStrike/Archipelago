import typing

from BaseClasses import MultiWorld, Region

from .Locations import KH2Location, event_location_to_item
from . import LocationName, RegionName, Events_Table

# Regions done

# Winterlands       Done
# Crestlands        Done
# Brightlands       Done
# Totohaha          Done
# Harborlands       Done
# Hinoeuma          Done
# Leaflands         Done
# Wildlands         Not done
# Sea               Not done

OT2REGIONS: typing.Dict[str, typing.List[str]] = {
    "Menu":
    # Winterlands        
    RegionName.Winterlands1:                [
        LocationName.EasternCapeColdSnowsNeedleDagger,
        LocationName.EasternCapeColdSnowsIceSoulstone,
        LocationName.EasternCapeColdSnowsFurCap,
        LocationName.EasternCapeColdSnows600L,
        LocationName.SouthernCapeColdSnowsOliveofLifeM,
        LocationName.SouthernCapeColdSnowsInspiritingPlumM,
        LocationName.SouthernCapeColdSnowsPilgrimsRobe,
        LocationName.SouthernCapeColdSnowsEmpoweringLychee,
        LocationName.WesternWinterbloomSnowsFalconRing,
        LocationName.WesternWinterbloomSnowsIceSoulstoneM,
        LocationName.WesternWinterbloomSnowsDiffusingSerum
    ],
    RegionName.Ruffians:                [
        LocationName.RuffiansHideoutBottleofBlindingDust,
        LocationName.RuffiansHideout1000L,
        LocationName.RuffiansHideoutHereticsGreatsword,
        LocationName.RuffiansHideoutOliveofLifeM
    ],
    RegionName.RuffiansBoss:                [
        LocationName.RuffiansHideoutWindRobe
    ],
    RegionName.CapeCold:                [
        LocationName.CapeCold2000L,
        LocationName.CapeColdEnergizingPomegranate
    ],
    RegionName.OsvaldCh1:                [
        LocationName.FrigitIslePrisonBottleofBlindingDust,
        LocationName.FrigitIslePrisonInspiritingPlum,
        LocationName.PrisonUndergroundPassageHealingGrape,
        LocationName.PrisonUndergroundPassageInspiritingPlum,
        LocationName.PrisonUndergroundPassageSinnersStaff,
        LocationName.PrisonUndergroundPassageAncientNecklace,
        LocationName.PrisonUndergroundPassageOliveofLife,
        LocationName.FrigitIsleEntranceHealingGrape,
        LocationName.FrigitIsleAnchorageMagicNut,
        LocationName.FrigitIsleAnchorageInspiritingPlum,
        LocationName.FrigitIsleAnchorageIceSoulstone
    ],
    RegionName.Winterbloom:                [
        LocationName.WinterbloomStrengtheningSerum,
        LocationName.WinterbloomIceSoulstoneM,
        LocationName.WinterbloomThievesQuartersEmpoweringLycheeM
    ],
    RegionName.WinterbloomKO:                [
        LocationName.Winterbloom150L,
        LocationName.WinterbloomOldArmor,
        LocationName.WinterbloomHealingGrape,
    ],
    RegionName.ThroneCh2Father:                [
        LocationName.SnowharesDenHealingGrapeM,
        LocationName.SnowharesDenEmpoweringBracelet,
        LocationName.SnowharesDenQuartzDagger,
        LocationName.SnowharesDenShadowSoulstoneM,
        LocationName.SnowharesDenInspiritingPlumM
    ],
    RegionName.Winterlands2:                [
        # LocationName.BeneaththeWallStone,
        LocationName.SouthernStormhailSnows15000L,
        LocationName.SouthernStormhailSnowsIceSoulstoneL,
        LocationName.SouthernStormhailSnowsRagingBeast,
        LocationName.SouthernStormhailSnowsLightningArmor,
        LocationName.SouthernStormhailSnowsHerbofRevival
    ],
    RegionName.InfernalCastle:                [
        LocationName.InfernalCastleInspiritingPlumBasket,
        LocationName.InfernalCastleBlizzardAmulet,
        LocationName.InfernalCastleLostTribesStaff,
        LocationName.InfernalCastleEnergizingPomegranate,
        LocationName.InfernalCastleSerpentSlayer,
        LocationName.InfernalCastleStoneofTruth
    ],
    RegionName.Stormhail:                [
        LocationName.StormhailInspiritingPlumBasket,
        LocationName.StormhailKnightsArmor,
        LocationName.StormhailSacredGuardHeadquartersEnergizingPomegranate,
        LocationName.StormhailSacredGuardHeadquartersLightSoulstoneL
    ],
    RegionName.StormhailKO:                [
        LocationName.StormhailSacredGuardHeadquartersFlayersAdmonishment
    ],
    RegionName.TemenosCh3Stormhail:                [
        LocationName.ForbiddenShrineGleamingAmulet,
        LocationName.ForbiddenShrineOliveofLifeM,
        LocationName.ForbiddenShrineHealingGrapeM,
        LocationName.ForbiddenShrine15000L,
        LocationName.ForbiddenShrineMagicBreaker
    ],
    RegionName.HikariCh4:                [
        LocationName.StormhailCastleMeiThunderSoulstoneM,
        LocationName.StormhailCastleMei16000L,
        LocationName.CastleMeiEastTowerHerbofSerenity,
        LocationName.CastleMeiEastTowerThunderSoulstoneL,
        LocationName.CastleMeiEastTowerHealingGrapeM,
        LocationName.CastleMeiEastTowerNightmareGlaive,
        LocationName.CastleMeiEastTowerThunderstormAmulet
    ],
    RegionName.OchetteCh2Glacis:                [
        LocationName.SacredPeakAltaheReinforcingJam,
        LocationName.SacredPeakAltaheIceAmulet,
        LocationName.SacredPeakAltaheIceSoulstoneL,
        LocationName.SacredPeakAltaheAbsoluteZeroBow
    ],
    #Crestlands
    RegionName.Crestlands:                [
        LocationName.EasternFlamechurchPassFurArmor,
        LocationName.EasternFlamechurchPassFireSoulstone,
        LocationName.EasternFlamechurchPassEnergizingPomegranate,
        LocationName.EasternFlamechurchPassSlumberSage,
        LocationName.BorderfallInspiritingPlumM,
        LocationName.BorderfallShadowBow,
        LocationName.BorderfallThunderSoulstoneM,
        LocationName.BorderfallEmpoweringLychee,
        LocationName.WesternMontwisePassGelidHelm,
        LocationName.WesternMontwisePass800L,
        LocationName.WesternMontwisePassEnergizingPomegranate,
        LocationName.WesternMerryHillsPassHealingGrapeM,
        LocationName.WesternMerryHillsPassSunShield,
        LocationName.WesternMerryHillsPassHerbofAwakening,
        LocationName.WesternMerryHillsPassHerbofSerenity
    ],
    RegionName.CrestlandsPass:                [
        LocationName.NorthernMontwisePassHealingGrapeM,
        LocationName.NorthernMontwisePassGoldDust1,
        LocationName.NorthernMontwisePassLargeSilverOre1,
        LocationName.NorthernMontwisePassGoldDust2,
        LocationName.NorthernMontwisePassSlumberSage,
        LocationName.NorthernMontwisePassShadowSoulstoneM,
        LocationName.NorthernMontwisePassLargeSilverOre2,
        LocationName.NorthernMontwisePassUnerringNecklace
    ],
    RegionName.SpriteCave:                [
        LocationName.SeatoftheWaterSpriteEnlighteningBracelet,
        LocationName.SeatoftheWaterSpriteInspiritingPlumBasket,
        LocationName.SeatoftheWaterSprite10000L,
        LocationName.SeatoftheWaterSpriteOliveofLifeM,
        LocationName.SeatoftheWaterSpriteBlessinginDisguise,
        LocationName.SeatoftheWaterSpriteEnergizingPomegranateL,
        LocationName.SeatoftheWaterSpriteRustyStaff
    ],
    RegionName.Flamechurch:                [
        LocationName.Flamechurch400L,
        LocationName.FlamechurchPilgrimsWayInspiritingPlum,
        LocationName.FlamechurchPilgrimsWayHealingGrape,
        LocationName.FlamechurchPilgrimsWayStimulatingRing,
        LocationName.FlamechurchPilgrimsWayToughNut,
        LocationName.FlamechurchCathedralEntranceShadowSoulstone
    ],
    RegionName.FlamechurchKO:                [
        LocationName.FlamechurchGuardsShield,
        LLocationName.FlamechurchHealingGrape
    ],
    RegionName.TemenosCh1:                [
        LocationName.FlamechurchCathedralOliveofLife,
        LocationName.FlamechurchCathedralLightSoulstone,
        LocationName.CathedralCellarsLightSoulstone,
        LocationName.CathedralCellarsInspiritingPlum,
        LocationName.CathedralCellarsPilgrimRod
    ],
    RegionName.TemenosThroneCh1:                [
        LocationName.FlamechurchCathedralAngelsRing
    ],
    RegionName.Montwise:                [
        LocationName.MontwiseFeatherMantle,
        LocationName.MontwiseLibraryLapisRod,
        LocationName.AbandonedTraverseBottleofPoisonDust,
        LocationName.AbandonedTraverseEnergizingPomegranate,
        LocationName.AbandonedTraverseGuardianAmulet,
        LocationName.AbandonedTraverseIceSoulstoneM,
        LocationName.AbandonedChurchHealingGrapeBunch,
        LocationName.AbandonedChurchBlackDagger,
        LocationName.AbandonedChurchInspiritingPlumBasket,
        LocationName.AbandonedChurchOliveofLifeM,
        LocationName.ForsakenGraveyardGrailofLife,
        LocationName.ForsakenGraveyardVivifyingStone,
        LocationName.ForsakenGraveyardDarkSlasher,
        LocationName.ForsakenGraveyardFireSoulstoneL,
        LocationName.ForsakenGraveyardForbiddenBlade
    ],
    RegionName.MontwiseKO:                [
        LocationName.MontwiseEngagementBow
    ],
    RegionName.HikariCh2:                [
        LocationName.MontwiseUndergroundArenaBottleofBlindingDust
    ],
    RegionName.OsvaldCh4:                [
        LocationName.UndergroundLaboratory14000L,
        LocationName.UndergroundLaboratoryBottledNightmares1,
        LocationName.UndergroundLaboratoryBottledNightmares2,
        LocationName.UndergroundLaboratoryFireSoulstoneL
    ],
    RegionName.MerryHills:                [
        LocationName.MerryHillsEmpoweringLycheeL,
        LocationName.MerryHillsHerbofClamor,
        LocationName.MerryHillsShrineEntrance2700L,
        LocationName.MerryHillsShrineEntranceEmpoweringNecklace
    ],
    RegionName.AgneaCh5:                [
        LocationName.ShrineofUlSterraRefreshingJam,
        LocationName.ShrineofUlSterraElementalAugmentor,
        LocationName.ShrineofUlSterraResplendantCostume,
        LocationName.ShrineofUlSterraBloodstainedKnife,
        LocationName.StageoftheMoonandSun24000L
    ],
    # Brightlands
    RegionName.Brightlands:                [
        LocationName.EasternNewDelstaHighroadIronBlade,
        LocationName.EasternNewDelstaHighroadHealingGrapeM,
        LocationName.EasternNewDelstaHighroad700L,
        LocationName.NewDelstaFlatsEnergizingPomegranate,
        LocationName.NewDelstaFlatsHerbofSerenity,
        LocationName.NewDelstaFlatsKiteShield,
        LocationName.NewDelstaHarborAnchorageSlumberSage,
        LocationName.NewDelstaHarborAnchorageBottleofPoisonDust,
        LocationName.WesternClockbankHighroadInspiritingPlumBasket,
        LocationName.WesternClockbankHighroadFeatheredHat,
        LocationName.WesternClockbankHighroadHerbofClarity,
        LocationName.SouthernClockbankHighroadLightSoulstoneM,
        LocationName.SouthernClockbankHighroadEnergizingPomegranateM,
        LocationName.SouthernClockbankHighroad6300L,
        LocationName.SouthernClockbankHighroadMirageBow
    ],
    RegionName.Waterway:                [
        LocationName.AbandonedWaterwayWrigglingRoot,
        LocationName.AbandonedWaterwayHerbElixir,
        LocationName.AbandonedWaterwayWrigglingRoot,
        LocationName.AbandonedWaterway8000L,
        LocationName.AbandonedWaterwayAntidoteStone,
        LocationName.AbandonedWaterwayWrigglingRoot,
        LocationName.AbandonedWaterwayFrostAxe
    ],
    RegionName.SunkenMaw:                [
        LocationName.SunkenMawInspiritingPlumM,
        LocationName.SunkenMawShieldofSerenity,
        LocationName.SunkenMawQuartzRod,
        LocationName.SunkenMaw13500L
    ],
    RegionName.AbandonnedVillage:                [
        LocationName.MountLiphiaDiffusingSerum,
        LocationName.MountLiphiaOliveofLifeL,
        LocationName.MountLiphiaEnergizingPomegranate,
        LocationName.MountLiphiaElementalWard,
        LocationName.MountLiphia12500L,
        LocationName.MountLiphiaInspiritingPlumBasket
    ],
    RegionName.NewDelsta:                [
        LocationName.NewDelstaEnergizingPomegranate,
        LocationName.NewDelstaHealingGrape,
        LocationName.NewDelstaBackstreetsCriticalNut,
        LocationName.NewDelstaBackstreetsInspiritingPlum,
        LocationName.DiamantesEstate1200L,
        LocationName.DiamantesEstateShadowSoulstone,
        LocationName.DiamantesEstateLongSword,
        LocationName.DiamantesEstateInspiritingPlum,
        LocationName.UndergroundWaterwayProtectiveRing,
        LocationName.UndergroundWaterwayHealingGrape
    ],
    RegionName.NewDelstaAmbush:                [
        LocationName.NewDelstaGameParlorPhysicalBelt,
        LocationName.NewDelstaGameParlor40000L,
        LocationName.NewDelstaGameParlorForbiddenDagger
    ],
    RegionName.NewDelstaKO:                [
        LocationName.NewDelstaBackstreetsDagger
    ],
    RegionName.AgneaCh2:                [
        LocationName.TheaterBackstageRefreshingJam,
        LocationName.TheaterBackstageLightningAmulet,
        LocationName.TheaterBackstageSimpleCostume,
        LocationName.TheaterBackstageFalconKnife,
        LocationName.TheaterBackstageHealingGrapeM
    ],
    RegionName.Clockbank:                [
        LocationName.ClockbankBottleofSleepingDust,
        LocationName.ClockbankPointedHat,
        LocationName.ClockbankInspiritingPlumM,
        LocationName.ClockbankCrestedGreatshield,
        LocationName.ClockbankIndustrialDistrictHealingGrapeBunch
    ],
    RegionName.PartitioCh2:                [
        LocationName.ClockbankIndustrialDistrictSlashingGlaive,
        LocationName.TheRoqueCompanyFactoryEmpoweringLychee,
        LocationName.TheRoqueCompanyFactory7000L,
        LocationName.TheRoqueCompanyFactoryProsperityCharm
    ],
        RegionName.Clocktower:                [
        LocationName.OldClockTowerInfernoAmulet,
        LocationName.OldClockTowerSeraphimSpear
    ],
    RegionName.LostseedPass:                [
        LocationName.DesertedHighroadDragonMail,
        LocationName.DesertedHighroadSlumberSage,
        LocationName.DesertedHighroadEnergizingPomegranate,
        LocationName.DesertedHighroadOliveofLifeL
    ],
    RegionName.Lostseed:                [
        LocationName.LostseedCursedHelm,
        LocationName.LostseedReinforcingJam,
        LocationName.LostseedCastleEmpoweringLycheeM,
        LocationName.LostseedCastleShadowSoulstoneL,
        LocationName.LostseedCastleSprightlyNecklace,
        LocationName.LostseedCastleHerbElixir,
        LocationName.LostseedCastleUpperLevelRuinousDagger,
        LocationName.LostseedCastleUpperLevelEnergizingPomegranateL,
        LocationName.LostseedCastleUpperLevel27500L,
        LocationName.LostseedCastleUpperLevelRevitalizingJam,
        LocationName.LostseedCastleUpperLevelLightSoulstoneM
    ],
    RegionName.Totohaha:                [
        LocationName.NorthBeastingTraverseInspiritingPlumM,
        LocationName.NorthBeastingTraverseEmpoweringLychee,
        LocationName.NorthBeastingTraverseWindSoulstone,
        LocationName.NorthBeastingTraverseWarAxe,
        LocationName.BeastingBayAnchorageSlumberSage,
        LocationName.BeastingBayAnchorageHealingGrapeM,
        LocationName.WesternTropuHopuTraverseEmpoweringLychee,
        LocationName.WesternTropuHopuTraverseQualityJerky,
        LocationName.WesternTropuHopuTraverseLightSoulstoneM,
        LocationName.WesternTropuHopuTraverseSprightlyBracelet,
        LocationName.WesternTropuHopuTraverseHealingGrapeBunch
    ],
    RegionName.BeastingVillage:                [
        LocationName.BeastingVillage1800L,
        LocationName.PathtotheTombsoftheWardenbeastsUnerringRing,
        LocationName.PathtotheTombsoftheWardenbeastsInspiritingPlum,
        LocationName.PathtotheTombsoftheWardenbeastsJerky,
        LocationName.TombsoftheWardenbestsCompositeBow,
        LocationName.TombsoftheWardenbestsBone,
        LocationName.TombsoftheWardenbestsSharpNut
    ],
    RegionName.BeastingVillageKO:                [
        LocationName.BeastingVillageGiantBow,
        LocationName.BeastingVillageResistantNutL,
        LocationName.BeastingVillagePerfectJerky,
        LocationName.BeastingVillageReinforcingJam
    ],
    RegionName.OchetteCh3:                [
        LocationName.VerdantWoodEnergizingPomegranateL,
        LocationName.StormyCapeAxeoftheConqueror,
        LocationName.StormyCapeRevitalizingJam,
        LocationName.StormyCapeTornadoBow,
        LocationName.StormyCapeEmpoweringLycheeL
    ],
    RegionName.Tropuhopu:                [
        LocationName.TropuHopuEnergizingPomegranateM,
        LocationName.TropuHopuShipyeardEmpoweringLycheeM,
        LocationName.TropuHopuFloatingTheaterInspiritingPlumM
    ],
    RegionName.TropuhopuKO:                [
        LocationName.TropuHopuCaitPowder
    ],
    RegionName.TropuhopuKOBoat:                [
        LocationName.TropuHopuPrettyPearl,
        LocationName.TropuHopuSkullHelm
    ],
    RegionName.CavernOfWaves:                [
        LocationName.CavernofWavesSaltedSeafood,
        LocationName.CavernofWavesHealingGrapeBunch,
        LocationName.CavernofWavesOliveofLifeL,
        LocationName.CavernofWavesJPAugmentor,
        LocationName.CavernofWavesRagingBeast,
        LocationName.CavernofWavesRuinousRelic1,
        LocationName.CavernofWavesRuinousRelic2,
        LocationName.CavernofWavesRuinousRelic3
    ],
    RegionName.TotohahaPass:                [
        LocationName.SouthernNamelessVillageTraverseSuperiorJerky,
        LocationName.SouthernNamelessVillageTraverseHerbofSerenity,
        LocationName.SouthernNamelessVillageTraverseWindSoulstoneL,
        LocationName.SouthernNamelessVillageTraverseMentalBelt
    ],
    RegionName.SinkingRuins:                [
        LocationName.SinkingRuinsPerfectJerky,
        LocationName.SinkingRuinsArticulateStone,
        LocationName.SinkingRuinsHerbofGraceBud,
        LocationName.SinkingRuins30000L,
        LocationName.SinkingRuinsSeaGodsSpear,
        LocationName.SinkingRuinsRustyBow
    ],
    RegionName.NamelessVillage:                [
        LocationName.NamelessVillageEmpoweringLycheeM,
        LocationName.NamelessVillageSaltedSeafood,
        LocationName.NamelessVillageStimulatingNecklace,
        LocationName.NamelessVillageBottleofBefuddlingDust
    ],
    RegionName.NamelessVillageKO:                [
        LocationName.NamelessVillageMythicalHorn,
        LocationName.NamelessVillageForbiddenBow
    ],
    RegionName.TemenosCh4:                [
        # LocationName.ShirlutoJerky,
        LocationName.WanderingWoodAntiqueCeremonialMask,
        LocationName.WanderingWoodInspiritingPlumM,
        LocationName.WanderingWoodHealingGrapeBunch,
        LocationName.WanderingWood28000L,
        LocationName.WanderingWoodLightSoulstoneL,
        LocationName.RiftedRockRevitalizingJam,
        LocationName.RiftedRockHallowedRod,
        LocationName.RiftedRockVoidAmulet
    ],
    # Harborlands
    RegionName.Harborlands:                [
        LocationName.WesternCanalbrineCoastHealingGrapeM,
        LocationName.WesternCanalbrineCoastInspiritingPlumM,
        LocationName.WesternCanalbrineCoast1500L,
        LocationName.WesternCanalbrineCoastStickyFlower,
        LocationName.CanalbrineBridgeCleansingLeaf,
        LocationName.CanalbrineBridgeSilverSword,
        LocationName.CanalbrineBridgeHealingGrapeBunch,
        LocationName.CanalbrineBridgeIceSoulstone,
        LocationName.CanalbrineBridgeLance,
        LocationName.CanalbrineBridgeRefreshingJam,
        LocationName.NorthernConningCreekCoastEnergizingPomegranate,
        LocationName.NorthernConningCreekCoastWindSoulstoneM,
        LocationName.NorthernConningCreekCoastHelmcleaver,
        LocationName.WesternConningCreekCoastEmpoweringLychee,
        LocationName.WesternConningCreekCoastSlumberSage,
        LocationName.WesternConningCreekCoastEnergizingPomegranate
    ],
    RegionName.HarborlandsBoat:                [
        LocationName.WesternCanalbrineCoastHerbofSerenity,
        LocationName.WesternCanalbrineCoastTravelersBow,
        LocationName.LairoftheUsurperBottleofSleepingDust,
        LocationName.LairoftheUsurperThunderMace,
        LocationName.LairoftheUsurperOliveofLifeL,
        LocationName.LairoftheUsurperGrailofLife,
        LocationName.LairoftheUsurper6500L,
        LocationName.LairoftheUsurperWeatheredTreasureShield,
        LocationName.LairoftheUsurperEmpoweringLycheeL,
        LocationName.WesternConningCreekCoastUnerringBracelet # Unsure, need to check if that's the one in western that's boat-locked
    ],
    RegionName.HarborlandsKO:                [
        LocationName.NorthernConningCreekCoastMatchingTrident
    ],
    RegionName.SunMoonCave:                [
        LocationName.CavernoftheMoonandSun2400L,
        LocationName.CavernoftheMoonandSunMightyBelt,
        LocationName.CavernoftheMoonandSunLightSoulstoneL
    ],
    RegionName.Canalbrine:                [
        LocationName.CanalbrineSlumberSage,
        LocationName.CanalbrinePathtotheWaterSourceDarkdelion,
        LocationName.CanalbrinePathtotheWaterSourceEmpoweringRing,
        LocationName.CanalbrinePathtotheWaterSourcePlumLeaf,
        LocationName.CanalbrinePathtotheWaterSourceGrapeLeaf
    ],
    RegionName.CanalbrineBoat:                [
        LocationName.CanalbrineResistantNut,
        LocationName.CanalbrinePathtotheWaterSourceGuardsHelm,
        LocationName.CanalbrinePathtotheWaterSourceHerbofHealing,
        LocationName.CanalbrineWaterSourceDiffusingSerum,
        LocationName.CanalbrineWaterSourceCleansingLeaf,
        LocationName.CanalbrineWaterSourceOldArmor,
        LocationName.CanalbrineWaterSourceHerbofHealing
    ],
    RegionName.CanalbrineBoatKO:                [
        LocationName.CanalbrineWoodcuttersGreatAxe
    ],
    RegionName.TemenosCh2:                [
        LocationName.SacredGuardShipMace,
        LocationName.SacredGuardShipInspiritingPlumM,
        LocationName.SacredGuardShip5600L,
        LocationName.SacredGuardShipDarkAmulet,
        LocationName.SacredGuardShipEmpoweringLycheeM
    ],
    RegionName.ConningCreek:                [
        LocationName.ConningCreekBottleofBefuddlingDust,
        LocationName.ConningCreekBlazonofProtection,
        LocationName.ConningCreekOutskirtsInspiritingPlumM, #Triggers unknown
        LocationName.ConningCreekHarborRainbowGlassBottle
    ],
    RegionName.OsvaldCh3:                [
        LocationName.ConningCreekOutskirtsFireSoulstoneM,
        LocationName.GuardOutpostFireSoulstone,
        LocationName.GuardOutpostGuardsArmor,
        LocationName.GuardOutpostEmpoweringLycheeM,
        LocationName.GuardOutpostGuardsHat,
        LocationName.GuardOutpost7200L
    ],
    RegionName.OchetteCh2Acta:                [
        LocationName.CavernoftheSeaGodEmpoweringLycheeM,
        LocationName.CavernoftheSeaGodRabbitShield,
        LocationName.CavernoftheSeaGodHealingGrapeBunch,
        LocationName.CavernoftheSeaGod6000L
    ],
    RegionName.RoqueIsland:                [
        LocationName.RoqueIslandAnchorage22000L,
        LocationName.RoqueIslandAnchorageEnlighteningNecklace,
        LocationName.RoqueIslandAnchorageHealingGrapeBunch,
        LocationName.RoqueIslandHerbofHealing,
        LocationName.RoqueIslandEnergizingPomegranateL,
        LocationName.RoqueIslandHeadquartersCriticalBracelet
    ],
    RegionName.RoqueIslandKO:                [
        LocationName.RoqueIslandEmpoweringLycheeL,
        LocationName.RoqueIsland39800L,
        LocationName.RoqueIslandRejuvenatingJam1,
        LocationName.RoqueIslandRejuvenatingJam2,
        LocationName.RoqueIslandRejuvenatingJam3,
        LocationName.RoqueIslandMagicNutL
    ],
    RegionName.PartitioCh4:                [
        LocationName.TheRoqueCompanyWestTowerInspiritingPlumBasket,
        LocationName.TheRoqueCompanyWestTowerEmpoweringLycheeL,
        LocationName.TheRoqueCompanyWestTowerFireSoulstoneL,
        LocationName.TheRoqueCompanyWestTowerVenomLance,
        LocationName.TheRoqueCompanyEastTower24500L,
        LocationName.TheRoqueCompanyEastTowerLargeSilverOre,
        LocationName.TheRoqueCompanyEastTowerOliveofLifeL,
        LocationName.TheRoqueCompanyEastTowerAgedWine,
        LocationName.TheRoqueCompanyEastTowerMechanicalBow,
        LocationName.TheRoqueCompanyEastTowerRefreshingJam
    ],
    # Hinoeuma
    RegionName.Hinoeuma1:                [
        LocationName.NorthernRyuSandsBottleofBefuddlingDust,
        LocationName.NorthernRyuSandsBoneSpear,
        LocationName.NorthernRyuSandsDiffusingSerum
    ],
    RegionName.Ryu:                [
        LocationName.RyuEmpoweringLychee
    ],
    RegionName.Hinoeuma2:                [
        LocationName.EasternSaiSandsHealingGrapeBunch,
        LocationName.EasternSaiSandsFireSoulstoneM,
        LocationName.EasternSaiSandsWarGlaive,
        LocationName.EasternSaiSandsEmpoweringLycheeM,
        LocationName.SouthernSaiSandsHerbofLight,
        LocationName.SouthernSaiSands6200L,
        LocationName.SouthernSaiSandsEnergizingPomegranateM,
        LocationName.SouthernSaiSandsInspiritingPlumBasket,
        LocationName.WesternSaiSandsIronShield,
        LocationName.WesternSaiSandsOliveofLifeL,
        LocationName.WesternSaiSandsReinforcingJam,
        LocationName.QuicksandGaolRustyAxe,
        LocationName.QuicksandGaolReinforcingJam,
        LocationName.QuicksandGaolWindSoulstoneL,
        LocationName.QuicksandGaolBrightStone,
        LocationName.QuicksandGaolScorchedBoneSpear,
        LocationName.DecayingTempleBottleofSleepingDust,
        LocationName.DecayingTempleEnergizingPomegranate,
        LocationName.DecayingTemple20000L,
        LocationName.DecayingTempleFireDragonsGlaive,
        LocationName.DecayingTempleSnipersBow,
        LocationName.EasternKuSandsEnergizingPomegranateL,
        LocationName.EasternKuSandsThunderSoulstoneL,
        LocationName.EasternKuSandsFirestarter,
        LocationName.EasternKuSandsSlumberSage,
        LocationName.EasternKuSandsHealingGrapeBunch,
        LocationName.TranquilGrottoOliveofLifeL,
        LocationName.TranquilGrottoMysteriousDagger,
        LocationName.TranquilGrottoReinforcingJam,
        LocationName.TranquilGrotto25000L
    ],
    RegionName.Sai:                [
        LocationName.SaiInspiritingPlumM,
        LocationName.SaiWindSoulstoneM,
        LocationName.DragonridgeWindWhisperer,
        LocationName.DragonridgeEmpoweringLychee,
        LocationName.DragonridgeInspiritingPlumBasket,
        LocationName.DragonridgeTempestAmulet,
        LocationName.SaiEastDistrictHerbofRevival
    ],
    RegionName.SaiRuins:                [
        LocationName.SaiEastDistrictBattleHatchet,
        LocationName.SaiEastDistrictRefinedSword
    ],
    RegionName.SaiKO:                [
        LocationName.SaiEastDistrictTatteredDress,
        # LocationName.SaiEastDistrictDancerJournal,
        LocationName.SaiEastDistrictTatteredShoes
    ],
    RegionName.CasttiCh2Sai:                [
        LocationName.SandflowPassEmpoweringLycheeM,
        LocationName.SandflowPassStimulatingBracelet,
        LocationName.SandflowPassStrengtheningSerum,
        LocationName.OldCampsiteDualFlower,
        LocationName.SandLionsDenOliveofLifeL,
        LocationName.SandLionsDenHealingGrapeBunch,
        LocationName.SandLionsDenPoisonedHatchet,
        LocationName.SandLionsDenDiffusingSerum
    ],
    RegionName.CasttiCh2SaiKO:                [
        LocationName.SandflowPassQuartzBlade,
        LocationName.SandflowPassSteelLance,
        LocationName.SandflowPassBoneMail
    ],
    RegionName.Ku:                [
        LocationName.KuCastleTownHealingGrape,
        LocationName.KuCastleTownInspiritingPlum,
        # LocationName.KuCastleTownGuard,
        LocationName.CastleKuEntrance1600L,
        LocationName.CastleKuEntranceCriticalRing,
        LocationName.SouthernKuSandsEnergizingPomegranate,
        LocationName.SouthernKuSandsFireSoulstone,
        LocationName.SouthernKuSandsHerbofLight,
        LocationName.SouthernKuSandsInspiritingPlum,
        LocationName.CastleKuThunderSoulstone,
        LocationName.CastleKuHealingGrape,
        # LocationName.CastleKuOboroJournal,
        LocationName.CastleKuFortifyingNut
    ],
    RegionName.HikariCh5:                [],
    # Leaflands
    RegionName.Leaflands:                [
        LocationName.SouthernCropdaleTrailFestivalGarland,
        LocationName.SouthernCropdaleTrailHealingGrapeM,
        LocationName.SouthernCropdaleTrailWindAmulet,
        LocationName.EasternCropdaleTrailRoundShield,
        LocationName.EasternCropdaleTrailEmpoweringLychee,
        LocationName.EasternCropdaleTrail1600L,
        LocationName.EasternCropdaleTrailSlumberSage,
        LocationName.NorthernWellgroveTrailWindSoulstoneM,
        LocationName.NorthernWellgroveTrailOliveofLifeM,
        LocationName.NorthernWellgroveTrailMagicEater,
        LocationName.NorthernWellgroveTrailGuardsShield,
        LocationName.NorthernWellgroveTrailEnergizingPomegranateL,
        LocationName.EasternWellgroveTrailMagusKnife,
        LocationName.EasternWellgroveTrailRefreshingJam,
        LocationName.EasternWellgroveTrailEmpoweringLycheeL,
        LocationName.EasternWellgroveTrailFireSoulstoneM,
        LocationName.EasternWellgroveTrail7200L,
        LocationName.SouthernTimberainTrailRefreshingJam,
        LocationName.SouthernTimberainTrailHypnoSword,
        LocationName.SouthernTimberainTrailEnergizingPomegranateM,
        LocationName.SouthernTimberainTrail3000L,
        LocationName.HouseWellowsManorOliveofLifeL,
        LocationName.HouseWellowsManorCursedArmor,
        LocationName.HouseWellowsManorHealingGrapeBunch,
        LocationName.HouseWellowsManorForbiddenAxe
    ],
    RegionName.LeaflandsBoat:                [],
    RegionName.Spring:                [
        LocationName.StarfallSpringBottleofSleepingDust,
        LocationName.StarfallSpringShadowSoulstone,
        LocationName.StarfallSpringWakefulStone,
        LocationName.StarfallSpring6000L,
        LocationName.StarfallSpringHighPriestsAmulet
    ],
    RegionName.Cropdale:                [
        LocationName.CropdaleHealingGrape,
        LocationName.CropdaleOliveofLife,
        LocationName.ForestPathHealingGrape,
        LocationName.ForestPathWindSoulstone,
        LocationName.FestivalGrounds500L,
        LocationName.VeilofTreesSprightlyRing,
        LocationName.VeilofTreesHealingGrape,
        LocationName.VeilofTreesInspiritingPlum,
        LocationName.VeilofTreesSlipperyNut,
        LocationName.VeilofTreesOliveofLife
    ],
    RegionName.CropdaleBoat:                [
        LocationName.ForestPathFurArmor, # Not 100% it's the boat-locked one
        LocationName.AnimalTrailHerbofSerenity
    ],
    RegionName.Wellgrove:                [
        LocationName.WellgroveSoldiersBow,
        LocationName.WellgroveAlrondsEstateEmpoweringLycheeL,
        LocationName.WellgroveAlrondsEstateNimbleMantle,
        LocationName.SecretForestLightAmulet,
        LocationName.SecretForestLittleCrow,
        LocationName.SecretForest10000L,
        LocationName.SecretForestRefreshingJam,
        LocationName.RoadtoMothersGardenHerbofValor,
        LocationName.RoadtoMothersGardenStingingDagger,
        LocationName.RoadtoMothersGardenInspiritingPlumM,
        LocationName.RoadtoMothersGardenSilentBandana,
        LocationName.RoadtoMothersGardenEmpoweringLycheeL
    ],
    RegionName.ThroneCh3Mother:                [
        LocationName.MothersGardenHealingGrapeBunch,
        LocationName.MothersGardenCalmingStone,
        LocationName.MothersGardenHornedHelm,
        LocationName.MothersGarden13000L,
        LocationName.MothersGardenRefreshingJam
    ],
    RegionName.Timberain:                [
        LocationName.TimberainProtectiveNecklace,
        LocationName.TimberainCastleTownSquareWindSoulstoneL
    ],
    RegionName.TimberainKO:                [
        LocationName.TimberainCastleTownSquareRustyPolearm
    ],
    RegionName.CasttiCh4:                [
        LocationName.TimberainCastleDiffusingSerum,
        LocationName.TimberainCastleHerbElixir,
        LocationName.TimberainCastleCleaverofDestruction,
        LocationName.TimberainCastleDreamyFlower,
        LocationName.TimberainCastleRoofMagesRobe,
        LocationName.TimberainCastleRoof23000L,
        LocationName.TimberainCastleRoofDragonsHelm,
        LocationName.TimberainCastleRoofEnergizingPomegranateL,
        LocationName.TimberainCastleRoofStrengtheningSerum
    ],
    # Wildlands
    RegionName.Wildlands1:                [
        LocationName.SouthernOresrushWildsThunderSoulstone,
        LocationName.SouthernOresrushWildsNamelessSword,
        LocationName.SouthernOresrushWilds2000L,
        LocationName.SouthernOresrushWildsHerbofValor
    ],
    RegionName.Oresrush:                [
        LocationName.OresrushLightCoinPouch,
        LocationName.OresrushLightNut,
        LocationName.AbandonedSilverMine500L,
        LocationName.AbandonedSilverMineEnlighteningRing,
        LocationName.AbandonedSilverMineLightSoulstone,
        LocationName.AbandonedSilverMineInspiritingPlum,
        LocationName.GiffsManseHealingGrape,
        LocationName.GiffsManseSmallSilverOre,
        LocationName.GiffsManseBronzeShield,
        LocationName.GiffsManseLeatherHelm
    ],
    RegionName.OresrushKO:                [
        LocationName.OresrushFoundryStockedGoods
    ],
    RegionName.PartitioCh1:                [
        # LocationName.SilverMineHealingGrape
    ],
    RegionName.Wildlands2:                [
        LocationName.CrackridgeHarborAnchorageBottleofPoisonDust,
        LocationName.CrackridgeHarborAnchorageHealingGrapeM,
        LocationName.CrackridgeHarborAnchorageKukri,
        LocationName.SouthernCrackridgeWildsEmpoweringLychee,
        LocationName.SouthernCrackridgeWildsHerbofClamor,
        LocationName.SouthernCrackridgeWilds6400L,
        LocationName.SouthernCrackridgeWildsShadowSoulstoneM,
        LocationName.WesternCrackrideWildsHeadgear,
        LocationName.WesternCrackrideWildsBoneMail,
        LocationName.WesternCrackrideWilds8500L,
        LocationName.WesternCrackrideWildsThunderSoulstoneM,
        LocationName.WesternCrackrideWildsInspiritingPlumBasket,
        LocationName.WesternCrackrideWildsOliveofLife,
        LocationName.WesternGravellWildsEnergizingPomegranateL,
        LocationName.WesternGravellWildsBottleofBlindingDust,
        LocationName.WesternGravellWildsThunderSoulstoneL,
        LocationName.WesternGravellWildsHerbofSerenity,
        LocationName.WesternGravellWildsStarsplitter,
        LocationName.WesternGravellWilds23500L,
        LocationName.IvoryRavineEveningMist,
        LocationName.IvoryRavineLostTribesAxe,
        LocationName.IvoryRavineBottleofBefuddlingDust,
        LocationName.IvoryRavineGiantsClub
    ],
    RegionName.Tunnels:                [
        LocationName.UnfinishedTunnel2100L,
        LocationName.UnfinishedTunnelRevitalizingJam,
        LocationName.UnfinishedTunnelOliveofLifeM,
        LocationName.UnfinishedTunnelNaturalMagnetite,
        LocationName.UnfinishedTunnelClarityStone,
        LocationName.UnfinishedTunnel13500L,
        LocationName.UnfinishedTunnelHerbElixir,
        LocationName.UnfinishedTunnelEnfeeblingAmulet
    ],
    RegionName.Crackridge:                [
        LocationName.CrackridgeOliveofLifeM,
        LocationName.AbandonedRoadHealingGrapeM,
        LocationName.AbandonedRoad9200L,
        LocationName.AbandonedRoadBottledNightmares
    ],
    RegionName.CrackridgeKO:                [
        LocationName.CrackridgeFromtheFarReachesofHell
    ],
    RegionName.TemenosCh3Crackridge:                [
        LocationName.FellsunRuinsEnergizingPomegranateL,
        LocationName.FellsunRuinsElementalRobe,
        LocationName.FellsunRuinsJadeStaff
    ],
    RegionName.OchetteCh2Tera:                [
        LocationName.PathtotheBedoftheTitanEnergizingPomegranateM,
        LocationName.PathtotheBedoftheTitanProtectiveBracelet,
        LocationName.PathtotheBedoftheTitanKnightsGreatbow,
        LocationName.PathtotheBedoftheTitanFireAmulet
    ],
    RegionName.Gravell:                [
        LocationName.GravellQuartzShield,
        LocationName.PathtoDuskruinShrineHealingGrapeBunch,
        LocationName.PathtoDuskruinShrineAntiqueCoat,
        LocationName.PathtoDuskruinShrineEnergizingPomegranateM,
        LocationName.DuskruinShrineOliveofLifeL,
        LocationName.DuskruinShrineCriticalNecklace,
        LocationName.DuskruinShrineIceSoulstoneLn,
        LocationName.DuskruinShrine25000L,
        LocationName.DuskruinShrineDepthsEmpoweringLycheeL,
        LocationName.DuskruinShrineDepthsAbyssalRod,
        LocationName.DuskruinShrineDepthsHealingGrapeBunch,
        LocationName.DuskruinShrineDepthsShadowSoulstoneL
    ],
    # Open Seas
    RegionName.SunderingSea:                [
        LocationName.SunderingSeaOntheWaterDiffusingSerum,
        LocationName.SunderingSeaOntheWaterDoubleTomahawk,
        LocationName.SunderingSeaOntheWaterFortuneWand,
        LocationName.SunderingSeaOntheWaterReinforcingJam,
        LocationName.SunderingSeaOntheWaterEXPAugmentor,
        LocationName.SunderingSeaOntheWater20000L,
        LocationName.SunderingSeaOntheWaterBeastlyScarf,
        LocationName.SunderingSeaOntheWaterSunkenGoldStatue,
        LocationName.SunderingSeaOntheWaterOliveofLifeL,
        LocationName.SunderingSeaOntheWaterStrengtheningSerum,
        LocationName.SunderingSeaOntheWaterDualLeaf,
        LocationName.SunderingSeaOntheWaterPlatinumShield,
        LocationName.SunderingSeaOntheWaterInvigoratingNutL,
        LocationName.SunderingSeaOntheWaterGoldNugget
    ],
    RegionName.SeaBehindScourge:                [
        LocationName.SunderingSeaOntheWaterHerbofSerenity,
        LocationName.SunderingSeaOntheWaterLeviathanGreatbow,
        LocationName.SunderingSeaOntheWaterDualFlower,
        LocationName.SunderingSeaOntheWaterSublimeOrnementalArmor,
        LocationName.SunderingSeaOntheWaterInspiritingPlumBasket,
        LocationName.SunderingSeaSkystone,
        LocationName.SunderingSeaDragonsScarf,
        LocationName.SunderingSeaHerbofGraceBud1,
        LocationName.SunderingSeaHerbofGraceBud2,
        LocationName.SunderingSeaHerbofGraceBud3,
        LocationName.SunderingSeaTheLostIsleAncientCursedTalisman1,
        LocationName.SunderingSeaTheLostIsleAncientCursedTalisman2,
        LocationName.SunderingSeaTheLostIsleAncientCursedTalisman3,
        LocationName.SunderingSeaTheLostIsleAncientCursedTalisman4,
        LocationName.SunderingSeaTheLostIsleBlessinginDisguise,
        LocationName.SunderingSeaTheLostIsleGreatSagesStaff,
        LocationName.SunderingSeaTheLostIsleLostTribesDagger
    ],
    RegionName.SeaIslands:                [
        LocationName.SunderingSeaLighthouseIslandOctopuffPot,
        LocationName.SunderingSeaLighthouseIsland12000L,
        LocationName.SunderingSeaNamelessIsleConsciousStone,
        LocationName.SunderingSeaNamelessIsleHealingGrapeBunch,
        LocationName.SunderingSeaNamelessIsleQuartzAxe,
        LocationName.SunderingSeaNamelessIsleFinishersClaws,
        LocationName.SunderingSeaShipwreckoftheEmpressInspiritingPlumBasket,
        LocationName.SunderingSeaShipwreckoftheEmpressThunderSoulstoneL,
        LocationName.SunderingSeaShipwreckoftheEmpressLostTribesSpear,
        LocationName.SunderingSeaShipwreckoftheEmpressCursedShield,
        LocationName.SunderingSeaShipwreckoftheEmpressMasterThiefsSapphireStone,
        LocationName.SunderingSeaShipwreckoftheEmpressRustyDagger
    ],
    RegionName.SeaBehindShark:                [
        LocationName.SunderingSeaOntheWaterGimmickGoggles
    ],
    RegionName.TyranodrakesLair:                [
        LocationName.SunderingSeaCuriousNestHerbofSerenity,
        LocationName.SunderingSeaCuriousNestLostTribesBow,
        LocationName.SunderingSeaCuriousNestDecayingDragonsEssence,
        LocationName.SunderingSeaCuriousNestFangofFerocity,
        LocationName.SunderingSeaCuriousNestTornadoGlaive,
        LocationName.SunderingSeaCuriousNestDecayingDragonsEssence
    ],
}

# Old KH2 code


def create_regions(self):
    # Level region depends on level depth.
    # for every 5 levels there should be +3 visit locking
    # level 50
    multiworld = self.multiworld
    player = self.player
    active_locations = self.location_name_to_id

    for level_region_name in level_region_list:
        KH2REGIONS[level_region_name] = []
    if multiworld.LevelDepth[player] == "level_50":
        KH2REGIONS[RegionName.LevelsVS1] = [LocationName.Lvl2, LocationName.Lvl4, LocationName.Lvl7, LocationName.Lvl9,
                                            LocationName.Lvl10]
        KH2REGIONS[RegionName.LevelsVS3] = [LocationName.Lvl12, LocationName.Lvl14, LocationName.Lvl15,
                                            LocationName.Lvl17,
                                            LocationName.Lvl20]
        KH2REGIONS[RegionName.LevelsVS6] = [LocationName.Lvl23, LocationName.Lvl25, LocationName.Lvl28,
                                            LocationName.Lvl30]
        KH2REGIONS[RegionName.LevelsVS9] = [LocationName.Lvl32, LocationName.Lvl34, LocationName.Lvl36,
                                            LocationName.Lvl39, LocationName.Lvl41]
        KH2REGIONS[RegionName.LevelsVS12] = [LocationName.Lvl44, LocationName.Lvl46, LocationName.Lvl48]
        KH2REGIONS[RegionName.LevelsVS15] = [LocationName.Lvl50]

    # level 99
    elif multiworld.LevelDepth[player] == "level_99":
        KH2REGIONS[RegionName.LevelsVS1] = [LocationName.Lvl7, LocationName.Lvl9]
        KH2REGIONS[RegionName.LevelsVS3] = [LocationName.Lvl12, LocationName.Lvl15, LocationName.Lvl17,
                                            LocationName.Lvl20]
        KH2REGIONS[RegionName.LevelsVS6] = [LocationName.Lvl23, LocationName.Lvl25, LocationName.Lvl28]
        KH2REGIONS[RegionName.LevelsVS9] = [LocationName.Lvl31, LocationName.Lvl33, LocationName.Lvl36,
                                            LocationName.Lvl39]
        KH2REGIONS[RegionName.LevelsVS12] = [LocationName.Lvl41, LocationName.Lvl44, LocationName.Lvl47,
                                             LocationName.Lvl49]
        KH2REGIONS[RegionName.LevelsVS15] = [LocationName.Lvl53, LocationName.Lvl59]
        KH2REGIONS[RegionName.LevelsVS18] = [LocationName.Lvl65]
        KH2REGIONS[RegionName.LevelsVS21] = [LocationName.Lvl73]
        KH2REGIONS[RegionName.LevelsVS24] = [LocationName.Lvl85]
        KH2REGIONS[RegionName.LevelsVS26] = [LocationName.Lvl99]
    # level sanity
    # has to be [] instead of {} for in
    elif multiworld.LevelDepth[player] in ["level_50_sanity", "level_99_sanity"]:
        KH2REGIONS[RegionName.LevelsVS1] = [LocationName.Lvl2, LocationName.Lvl3, LocationName.Lvl4, LocationName.Lvl5,
                                            LocationName.Lvl6,
                                            LocationName.Lvl7, LocationName.Lvl8, LocationName.Lvl9, LocationName.Lvl10]
        KH2REGIONS[RegionName.LevelsVS3] = [LocationName.Lvl11, LocationName.Lvl12, LocationName.Lvl13,
                                            LocationName.Lvl14, LocationName.Lvl15,
                                            LocationName.Lvl16, LocationName.Lvl17, LocationName.Lvl18,
                                            LocationName.Lvl19, LocationName.Lvl20]
        KH2REGIONS[RegionName.LevelsVS6] = [LocationName.Lvl21, LocationName.Lvl22, LocationName.Lvl23,
                                            LocationName.Lvl24, LocationName.Lvl25,
                                            LocationName.Lvl26, LocationName.Lvl27, LocationName.Lvl28,
                                            LocationName.Lvl29, LocationName.Lvl30]
        KH2REGIONS[RegionName.LevelsVS9] = [LocationName.Lvl31, LocationName.Lvl32, LocationName.Lvl33,
                                            LocationName.Lvl34, LocationName.Lvl35,
                                            LocationName.Lvl36, LocationName.Lvl37, LocationName.Lvl38,
                                            LocationName.Lvl39, LocationName.Lvl40]
        KH2REGIONS[RegionName.LevelsVS12] = [LocationName.Lvl41, LocationName.Lvl42, LocationName.Lvl43,
                                             LocationName.Lvl44, LocationName.Lvl45,
                                             LocationName.Lvl46, LocationName.Lvl47, LocationName.Lvl48,
                                             LocationName.Lvl49, LocationName.Lvl50]
        # level 99 sanity
        if multiworld.LevelDepth[player] == "level_99_sanity":
            KH2REGIONS[RegionName.LevelsVS15] = [LocationName.Lvl51, LocationName.Lvl52, LocationName.Lvl53,
                                                 LocationName.Lvl54,
                                                 LocationName.Lvl55, LocationName.Lvl56, LocationName.Lvl57,
                                                 LocationName.Lvl58,
                                                 LocationName.Lvl59, LocationName.Lvl60]
            KH2REGIONS[RegionName.LevelsVS18] = [LocationName.Lvl61, LocationName.Lvl62, LocationName.Lvl63,
                                                 LocationName.Lvl64,
                                                 LocationName.Lvl65, LocationName.Lvl66, LocationName.Lvl67,
                                                 LocationName.Lvl68,
                                                 LocationName.Lvl69, LocationName.Lvl70]
            KH2REGIONS[RegionName.LevelsVS21] = [LocationName.Lvl71, LocationName.Lvl72, LocationName.Lvl73,
                                                 LocationName.Lvl74,
                                                 LocationName.Lvl75, LocationName.Lvl76, LocationName.Lvl77,
                                                 LocationName.Lvl78,
                                                 LocationName.Lvl79, LocationName.Lvl80]
            KH2REGIONS[RegionName.LevelsVS24] = [LocationName.Lvl81, LocationName.Lvl82, LocationName.Lvl83,
                                                 LocationName.Lvl84,
                                                 LocationName.Lvl85, LocationName.Lvl86, LocationName.Lvl87,
                                                 LocationName.Lvl88,
                                                 LocationName.Lvl89, LocationName.Lvl90]
            KH2REGIONS[RegionName.LevelsVS26] = [LocationName.Lvl91, LocationName.Lvl92, LocationName.Lvl93,
                                                 LocationName.Lvl94,
                                                 LocationName.Lvl95, LocationName.Lvl96, LocationName.Lvl97,
                                                 LocationName.Lvl98, LocationName.Lvl99]
    KH2REGIONS[RegionName.Summon] = []
    if multiworld.SummonLevelLocationToggle[player]:
        KH2REGIONS[RegionName.Summon] = [LocationName.Summonlvl2,
                                         LocationName.Summonlvl3,
                                         LocationName.Summonlvl4,
                                         LocationName.Summonlvl5,
                                         LocationName.Summonlvl6,
                                         LocationName.Summonlvl7]
    multiworld.regions += [create_region(multiworld, player, active_locations, region, locations) for region, locations in
                           KH2REGIONS.items()]
    # fill the event locations with events
    multiworld.worlds[player].item_name_to_id.update({event_name: None for event_name in Events_Table})
    for location, item in event_location_to_item.items():
        multiworld.get_location(location, player).place_locked_item(
                multiworld.worlds[player].create_item(item))


def connect_regions(self):
    multiworld = self.multiworld
    player = self.player
    # connecting every first visit to the GoA
    KH2RegionConnections: typing.Dict[str, typing.Set[str]] = {
        "Menu":                        {RegionName.GoA},
        RegionName.GoA:                {RegionName.Sp, RegionName.Pr, RegionName.Tt, RegionName.Oc, RegionName.Ht,
                                        RegionName.LoD,
                                        RegionName.Twtnw, RegionName.Bc, RegionName.Ag, RegionName.Pl, RegionName.Hb,
                                        RegionName.Dc, RegionName.Stt,
                                        RegionName.Ha1, RegionName.Keyblade, RegionName.LevelsVS1,
                                        RegionName.Valor, RegionName.Wisdom, RegionName.Limit, RegionName.Master,
                                        RegionName.Final, RegionName.Summon, RegionName.AtlanticaSongOne},
        RegionName.LoD:                {RegionName.ShanYu},
        RegionName.ShanYu:             {RegionName.LoD2},
        RegionName.LoD2:               {RegionName.AnsemRiku},
        RegionName.AnsemRiku:          {RegionName.StormRider},
        RegionName.StormRider:         {RegionName.DataXigbar},
        RegionName.Ag:                 {RegionName.TwinLords},
        RegionName.TwinLords:          {RegionName.Ag2},
        RegionName.Ag2:                {RegionName.GenieJafar},
        RegionName.GenieJafar:         {RegionName.DataLexaeus},
        RegionName.Dc:                 {RegionName.Tr},
        RegionName.Tr:                 {RegionName.OldPete},
        RegionName.OldPete:            {RegionName.FuturePete},
        RegionName.FuturePete:         {RegionName.Terra, RegionName.DataMarluxia},
        RegionName.Ha1:                {RegionName.Ha2},
        RegionName.Ha2:                {RegionName.Ha3},
        RegionName.Ha3:                {RegionName.Ha4},
        RegionName.Ha4:                {RegionName.Ha5},
        RegionName.Ha5:                {RegionName.Ha6},
        RegionName.Pr:                 {RegionName.Barbosa},
        RegionName.Barbosa:            {RegionName.Pr2},
        RegionName.Pr2:                {RegionName.GrimReaper1},
        RegionName.GrimReaper1:        {RegionName.GrimReaper2},
        RegionName.GrimReaper2:        {RegionName.DataLuxord},
        RegionName.Oc:                 {RegionName.Cerberus},
        RegionName.Cerberus:           {RegionName.OlympusPete},
        RegionName.OlympusPete:        {RegionName.Hydra},
        RegionName.Hydra:              {RegionName.OcPainAndPanicCup, RegionName.OcCerberusCup, RegionName.Oc2},
        RegionName.Oc2:                {RegionName.Hades},
        RegionName.Hades:              {RegionName.Oc2TitanCup, RegionName.Oc2GofCup, RegionName.DataZexion},
        RegionName.Oc2GofCup:          {RegionName.HadesCups},
        RegionName.Bc:                 {RegionName.Thresholder},
        RegionName.Thresholder:        {RegionName.Beast},
        RegionName.Beast:              {RegionName.DarkThorn},
        RegionName.DarkThorn:          {RegionName.Bc2},
        RegionName.Bc2:                {RegionName.Xaldin},
        RegionName.Xaldin:             {RegionName.DataXaldin},
        RegionName.Sp:                 {RegionName.HostileProgram},
        RegionName.HostileProgram:     {RegionName.Sp2},
        RegionName.Sp2:                {RegionName.Mcp},
        RegionName.Mcp:                {RegionName.DataLarxene},
        RegionName.Ht:                 {RegionName.PrisonKeeper},
        RegionName.PrisonKeeper:       {RegionName.OogieBoogie},
        RegionName.OogieBoogie:        {RegionName.Ht2},
        RegionName.Ht2:                {RegionName.Experiment},
        RegionName.Experiment:         {RegionName.DataVexen},
        RegionName.Hb:                 {RegionName.Hb2},
        RegionName.Hb2:                {RegionName.CoR, RegionName.HBDemyx},
        RegionName.HBDemyx:            {RegionName.ThousandHeartless},
        RegionName.ThousandHeartless:  {RegionName.Mushroom13, RegionName.DataDemyx, RegionName.Sephi},
        RegionName.CoR:                {RegionName.CorFirstFight},
        RegionName.CorFirstFight:      {RegionName.CorSecondFight},
        RegionName.CorSecondFight:     {RegionName.Transport},
        RegionName.Pl:                 {RegionName.Scar},
        RegionName.Scar:               {RegionName.Pl2},
        RegionName.Pl2:                {RegionName.GroundShaker},
        RegionName.GroundShaker:       {RegionName.DataSaix},
        RegionName.Stt:                {RegionName.TwilightThorn},
        RegionName.TwilightThorn:      {RegionName.Axel1},
        RegionName.Axel1:              {RegionName.Axel2},
        RegionName.Axel2:              {RegionName.DataRoxas},
        RegionName.Tt:                 {RegionName.Tt2},
        RegionName.Tt2:                {RegionName.Tt3},
        RegionName.Tt3:                {RegionName.DataAxel},
        RegionName.Twtnw:              {RegionName.Roxas},
        RegionName.Roxas:              {RegionName.Xigbar},
        RegionName.Xigbar:             {RegionName.Luxord},
        RegionName.Luxord:             {RegionName.Saix},
        RegionName.Saix:               {RegionName.Twtnw2},
        RegionName.Twtnw2:             {RegionName.Xemnas},
        RegionName.Xemnas:             {RegionName.ArmoredXemnas, RegionName.DataXemnas},
        RegionName.ArmoredXemnas:      {RegionName.ArmoredXemnas2},
        RegionName.ArmoredXemnas2:     {RegionName.FinalXemnas},
        RegionName.LevelsVS1:          {RegionName.LevelsVS3},
        RegionName.LevelsVS3:          {RegionName.LevelsVS6},
        RegionName.LevelsVS6:          {RegionName.LevelsVS9},
        RegionName.LevelsVS9:          {RegionName.LevelsVS12},
        RegionName.LevelsVS12:         {RegionName.LevelsVS15},
        RegionName.LevelsVS15:         {RegionName.LevelsVS18},
        RegionName.LevelsVS18:         {RegionName.LevelsVS21},
        RegionName.LevelsVS21:         {RegionName.LevelsVS24},
        RegionName.LevelsVS24:         {RegionName.LevelsVS26},
        RegionName.AtlanticaSongOne:   {RegionName.AtlanticaSongTwo},
        RegionName.AtlanticaSongTwo:   {RegionName.AtlanticaSongThree},
        RegionName.AtlanticaSongThree: {RegionName.AtlanticaSongFour},
    }

    for source, target in KH2RegionConnections.items():
        source_region = multiworld.get_region(source, player)
        source_region.add_exits(target)


# cave fight:fire/guard
# hades escape logic:fire,blizzard,slide dash, base tools
# windows:chicken little.fire element,base tools
# chasm of challenges:reflect, blizzard, trinity limit,chicken little
# living bones: magnet
# some things for barbosa(PR), chicken little
# hyneas(magnet,reflect)
# tt2: reflect,chicken,form, guard,aerial recovery,finising plus,
# corridors,dancers:chicken little or stitch +demyx tools
# 1k: guard,once more,limit form,
# snipers +before: stitch, magnet, finishing leap, base tools, reflect
# dragoons:stitch, magnet, base tools, reflect
# oc2 tournament thing: stitch, magnet, base tools, reflera
# lock,shock and barrel: reflect, base tools
# carpet section: magnera, reflect, base tools,
# sp2: reflera, stitch, basse tools, reflera, thundara, fantasia/duck flare,once more.
# tt3: stitch/chicken little, magnera,reflera,base tools,finishing leap,limit form
# cor

def create_region(multiworld, player: int, active_locations, name: str, locations=None):
    ret = Region(name, player, multiworld)
    if locations:
        loc_to_id = {loc: active_locations.get(loc, 0) for loc in locations if active_locations.get(loc, None)}
        ret.add_locations(loc_to_id, KH2Location)
        loc_to_event = {loc: active_locations.get(loc, None) for loc in locations if
                        not active_locations.get(loc, None)}
        ret.add_locations(loc_to_event, KH2Location)

    return ret
