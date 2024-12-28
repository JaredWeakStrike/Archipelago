import typing

from BaseClasses import MultiWorld, Region

from .Locations import *
from . import LocationName, RegionName, Events_Table, Locations

OT2REGIONS: typing.Dict[str, typing.List[str]] = {
    "Menu":                                 [],
    RegionName.GameStart:                   [
        LocationName.GameStartChar,
        LocationName.GameStartChapter,
        LocationName.GameStartRegion,
    ],

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
        LocationName.FrigitIsleAnchorageIceSoulstone,
        LocationName.OsvaldCh1Clear
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
        LocationName.SnowharesDenInspiritingPlumM,
        LocationName.ThroneCh2FatherClear
    ],
    RegionName.CasttiCh2Winterbloom:            [
        LocationName.CasttiCh2WinterbloomClear
    ],
    RegionName.PartitioWinterbloom:             [
        LocationName.PartitioWinterbloomClear
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
        LocationName.ForbiddenShrineMagicBreaker,
        LocationName.TemenosCh3StormhailClear
    ],
    RegionName.HikariCh4:                [
        LocationName.StormhailCastleMeiThunderSoulstoneM,
        LocationName.StormhailCastleMei16000L,
        LocationName.CastleMeiEastTowerHerbofSerenity,
        LocationName.CastleMeiEastTowerThunderSoulstoneL,
        LocationName.CastleMeiEastTowerHealingGrapeM,
        LocationName.CastleMeiEastTowerNightmareGlaive,
        LocationName.CastleMeiEastTowerThunderstormAmulet,
        LocationName.HikariCh4Clear
    ],
    RegionName.OchetteCh2Glacis:                [
        LocationName.SacredPeakAltaheReinforcingJam,
        LocationName.SacredPeakAltaheIceAmulet,
        LocationName.SacredPeakAltaheIceSoulstoneL,
        LocationName.SacredPeakAltaheAbsoluteZeroBow,
        LocationName.OchetteCh2GlacisClear
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
        LocationName.FlamechurchHealingGrape
    ],
    RegionName.TemenosCh1:                [
        LocationName.FlamechurchCathedralOliveofLife,
        LocationName.FlamechurchCathedralLightSoulstone,
        LocationName.CathedralCellarsLightSoulstone,
        LocationName.CathedralCellarsInspiritingPlum,
        LocationName.CathedralCellarsPilgrimRod,
        LocationName.TemenosCh1Clear
    ],
    RegionName.TemenosThroneCh1:                [
        LocationName.FlamechurchCathedralAngelsRing,
        LocationName.ThroneTemenosCh1Clear
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
        LocationName.MontwiseUndergroundArenaBottleofBlindingDust,
        LocationName.HikariCh2Clear
    ],
    RegionName.ThroneCh3Father:         [
        LocationName.ThroneCh3FatherClear
    ],
    RegionName.OsvaldCh4:                [
        LocationName.UndergroundLaboratory14000L,
        LocationName.UndergroundLaboratoryBottledNightmares1,
        LocationName.UndergroundLaboratoryBottledNightmares2,
        LocationName.UndergroundLaboratoryFireSoulstoneL,
        LocationName.OsvaldCh4Clear
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
        LocationName.StageoftheMoonandSun24000L,
        LocationName.AgneaCh5Clear
    ],
    RegionName.AgneaClear:              [
        LocationName.AgneaStoryClear
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
        LocationName.AbandonedWaterwayWrigglingRoot1,
        LocationName.AbandonedWaterwayHerbElixir,
        LocationName.AbandonedWaterwayWrigglingRoot2,
        LocationName.AbandonedWaterway8000L,
        LocationName.AbandonedWaterwayAntidoteStone,
        LocationName.AbandonedWaterwayWrigglingRoot3,
        LocationName.AbandonedWaterwayFrostAxe
    ],
    RegionName.SunkenMaw:                [
        LocationName.SunkenMawInspiritingPlumM,
        LocationName.SunkenMawShieldofSerenity,
        LocationName.SunkenMawQuartzRod,
        LocationName.SunkenMaw13500L
    ],
    RegionName.AbandonedVillage:                [
        LocationName.MountLiphiaDiffusingSerum,
        LocationName.MountLiphiaOliveofLifeL,
        LocationName.MountLiphiaEnergizingPomegranate,
        LocationName.MountLiphiaElementalWard,
        LocationName.MountLiphia12500L,
        LocationName.MountLiphiaInspiritingPlumBasket
    ],
    RegionName.CasttiCh3:                       [
        LocationName.CasttiCh3Clear
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
    RegionName.ThroneCh1:                   [
        LocationName.ThroneCh1Clear
    ],
    RegionName.AgneaCh2:                [
        LocationName.TheaterBackstageRefreshingJam,
        LocationName.TheaterBackstageLightningAmulet,
        LocationName.TheaterBackstageSimpleCostume,
        LocationName.TheaterBackstageFalconKnife,
        LocationName.TheaterBackstageHealingGrapeM,
        LocationName.AgneaCh2Clear
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
        LocationName.TheRoqueCompanyFactoryProsperityCharm,
        LocationName.PartitioCh2Clear
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
        LocationName.LostseedCastleUpperLevelLightSoulstoneM,
        LocationName.ThroneCh4Clear
    ],
    RegionName.ThroneClear:                 [
        LocationName.ThroneStoryClear
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
    RegionName.OchetteCh1:                  [
        LocationName.OchetteCh1Clear
    ],
    RegionName.OchetteCh3:                [
        LocationName.VerdantWoodEnergizingPomegranateL,
        LocationName.StormyCapeAxeoftheConqueror,
        LocationName.StormyCapeRevitalizingJam,
        LocationName.StormyCapeTornadoBow,
        LocationName.StormyCapeEmpoweringLycheeL,
        LocationName.OchetteCh3Clear
    ],
    RegionName.OchetteClear:                    [
        LocationName.OchetteStoryClear
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
    RegionName.AgneaCh3:                        [
        LocationName.AgneaCh3Clear
    ],
    RegionName.PartitioTropuhopu:                [
        LocationName.PartitioTropuhopuClear
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
        LocationName.RiftedRockVoidAmulet,
        LocationName.TemenosCh4Clear
    ],
    RegionName.TemenosClear:                [
        LocationName.TemenosStoryClear
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
    RegionName.CasttiCh1:                       [
        LocationName.CasttiCh1Clear
    ],
    RegionName.TemenosCh2:                [
        LocationName.SacredGuardShipMace,
        LocationName.SacredGuardShipInspiritingPlumM,
        LocationName.SacredGuardShip5600L,
        LocationName.SacredGuardShipDarkAmulet,
        LocationName.SacredGuardShipEmpoweringLycheeM,
        LocationName.TemenosCh2Clear
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
        LocationName.GuardOutpost7200L,
        LocationName.OsvaldCh3Clear
    ],
    RegionName.OchetteCh2Acta:                [
        LocationName.CavernoftheSeaGodEmpoweringLycheeM,
        LocationName.CavernoftheSeaGodRabbitShield,
        LocationName.CavernoftheSeaGodHealingGrapeBunch,
        LocationName.CavernoftheSeaGod6000L,
        LocationName.OchetteCh2ActaClear
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
        LocationName.TheRoqueCompanyEastTowerRefreshingJam,
        LocationName.PartitioCh4Clear
    ],
    RegionName.PartitioClear:                   [
        LocationName.PartitioStoryClear
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
    RegionName.HikariCh1:                [
        LocationName.HikariCh1Clear
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
        #LocationName.SaiEastDistrictHerbofRevival
    ],
    RegionName.SaiRuins:                [
        #LocationName.SaiEastDistrictBattleHatchet,
        #LocationName.SaiEastDistrictRefinedSword
    ],
    RegionName.SaiKO:                [
        #LocationName.SaiEastDistrictTatteredDress,
        #LocationName.SaiEastDistrictDancerJournal,
        #LocationName.SaiEastDistrictTatteredShoes
    ],
    RegionName.CasttiCh2Sai:                [
        LocationName.SandflowPassEmpoweringLycheeM,
        LocationName.SandflowPassStimulatingBracelet,
        LocationName.SandflowPassStrengtheningSerum,
        LocationName.OldCampsiteDualFlower,
        LocationName.SandLionsDenOliveofLifeL,
        LocationName.SandLionsDenHealingGrapeBunch,
        LocationName.SandLionsDenPoisonedHatchet,
        LocationName.SandLionsDenDiffusingSerum,
        LocationName.CasttiCh2SaiClear
    ],
    RegionName.CasttiCh2SaiKO:                [
        LocationName.SandflowPassQuartzBlade,
        LocationName.SandflowPassSteelLance,
        LocationName.SandflowPassBoneMail
    ],
    RegionName.AgneaCh4:                    [
        LocationName.AgneaCh4Clear
    ],
    RegionName.PartitioSai:                     [
        LocationName.PartitioSaiClear
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
    RegionName.HikariCh5:                [
        LocationName.HikariCh5Clear
    ],
    RegionName.HikariClear:                 [
        LocationName.HikariStoryClear
    ],
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
        LocationName.ForestPathFurArmor, # Not 100% sure it's the boat-locked one
        LocationName.AnimalTrailHerbofSerenity
    ],
    RegionName.AgneaCh1:                [
        LocationName.AgneaCh1Clear
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
        LocationName.MothersGardenRefreshingJam,
        LocationName.ThroneCh3MotherClear
    ],
    RegionName.HikariCh3:                       [
        LocationName.HikariCh3Clear
    ],
    RegionName.PartitioCh3:                     [
        LocationName.PartitioCh3Clear
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
        LocationName.TimberainCastleRoofStrengtheningSerum,
        LocationName.CasttiCh4Clear
    ],
    RegionName.CasttiClear:             [
        LocationName.CasttiStoryClear
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
        # LocationName.SilverMineHealingGrape,
        LocationName.PartitioCh1Clear
    ],
    RegionName.ThroneCh2Mother:             [
        LocationName.ThroneCh2MotherClear
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
        LocationName.FellsunRuinsJadeStaff,
        LocationName.TemenosCh3CrackridgeClear
    ],
    RegionName.OchetteCh2Tera:                [
        LocationName.PathtotheBedoftheTitanEnergizingPomegranateM,
        LocationName.PathtotheBedoftheTitanProtectiveBracelet,
        LocationName.PathtotheBedoftheTitanKnightsGreatbow,
        LocationName.PathtotheBedoftheTitanFireAmulet,
        LocationName.OchetteCh2TeraClear
    ],
    RegionName.Gravell:                [
        LocationName.GravellQuartzShield,
        LocationName.PathtoDuskruinShrineHealingGrapeBunch,
        LocationName.PathtoDuskruinShrineAntiqueCoat,
        LocationName.PathtoDuskruinShrineEnergizingPomegranateM,
        LocationName.DuskruinShrineOliveofLifeL,
        LocationName.DuskruinShrineCriticalNecklace,
        LocationName.DuskruinShrineIceSoulstoneL,
        LocationName.DuskruinShrine25000L,
        LocationName.DuskruinShrineDepthsEmpoweringLycheeL,
        LocationName.DuskruinShrineDepthsAbyssalRod,
        LocationName.DuskruinShrineDepthsHealingGrapeBunch,
        LocationName.DuskruinShrineDepthsShadowSoulstoneL
    ],
    RegionName.OsvaldCh5:               [
        LocationName.OsvaldCh5Clear
    ],
    RegionName.OsvaldClear:             [
        LocationName.OsvaldStoryClear
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
        LocationName.SunderingSeaCuriousNestDecayingDragonsEssence1,
        LocationName.SunderingSeaCuriousNestFangofFerocity,
        LocationName.SunderingSeaCuriousNestTornadoGlaive,
        LocationName.SunderingSeaCuriousNestDecayingDragonsEssence2
    ],
    # Side-Stories
    RegionName.ThroneTemenosCh2:                    [
        LocationName.ThroneTemenosCh2Clear
    ],
    RegionName.AgneaHikariCh1:                    [
        LocationName.AgneaHikariCh1Clear
    ],
    RegionName.AgneaHikariCh2:                    [
        LocationName.AgneaHikariCh2Clear
    ],
    RegionName.PartitioOsvaldCh1:                    [
        LocationName.PartitioOsvaldCh1Clear
    ],
    RegionName.PartitioOsvaldCh2:                    [
        LocationName.PartitioOsvaldCh2Clear
    ],
    RegionName.OchetteCasttiCh1:                    [
        LocationName.OchetteCasttiCh1Clear
    ],
    RegionName.OchetteCasttiCh2:                    [
        LocationName.OchetteCasttiCh2Clear
    ],
    RegionName.Vide:                    [
        LocationName.DefeatVide
    ],
    RegionName.TravelersBag:                    [
        LocationName.TravelersBagClear
    ],
    RegionName.PeculiarTomes:                    [
        LocationName.PeculiarTomesClear
    ],
    RegionName.ReachesOfHell:                    [
        LocationName.FromTheFarReachesOfHellClear
    ],
    RegionName.Galdera:                    [
        LocationName.GalderaDefeated
    ],
    # Regions to add
    # Osvald 5 St 
    # Temenos St 
    # Throne 1 2M 3F 4 St
    # Ochette 1 St
    # Castti 1 2W 3 St
    # Partitio 3 A S G St 
    # Hikari 1 3 St
    # Agnea 1 3 4 St
    
    # HA 1 2
    # OP 1 2
    # TT 2
    # CO 1 2
    
    # Vide Bag Book Hell Galdy
}






# Old KH2 code


def create_regions(self):
    multiworld = self.multiworld
    player = self.player
    active_locations = self.location_name_to_id

    multiworld.regions += [create_region(multiworld, player, active_locations, region, locations) for region, locations in OT2REGIONS.items()]
    # fill the event locations with events
    #multiworld.worlds[player].item_name_to_id.update({event_name: None for event_name in Events_Table})
    for location, item in Locations.event_location_to_item.items():
        multiworld.get_location(location, player).place_locked_item(
                multiworld.worlds[player].create_event_item(item))


def connect_regions(self):
    multiworld = self.multiworld
    player = self.player
    # Connections to review, I fucked up.
    OT2RegionConnections: typing.Dict[str, typing.Set[str]] = {
        #"Menu":                        {RegionName.GoA},
        RegionName.GameStart:               {RegionName.CapeCold, RegionName.Flamechurch, RegionName.NewDelsta, RegionName.BeastingVillage,     
                                             RegionName.Canalbrine, RegionName.Ryu, RegionName.Oresrush, RegionName.Cropdale},
        RegionName.Winterlands1:            {RegionName.CapeCold, RegionName.Ruffians, RegionName.Winterbloom, RegionName.Crestlands, 
                                             RegionName.Brightlands, RegionName.TravelersBag},
        RegionName.Ruffians:                {RegionName.RuffiansBoss},
        RegionName.CapeCold:                {RegionName.Winterlands1, RegionName.OsvaldCh1},
        RegionName.Winterbloom:             {RegionName.WinterbloomKO, RegionName.ThroneCh2Father, RegionName.Winterlands1,            
                                             RegionName.CasttiCh2Winterbloom, RegionName.PartitioWinterbloom},
        RegionName.Winterlands2:            {RegionName.Stormhail, RegionName.InfernalCastle, RegionName.CrestlandsPass},
        RegionName.Stormhail:               {RegionName.StormhailKO, RegionName.Winterlands2, RegionName.OchetteCh2Glacis, 
                                             RegionName.HikariCh4, RegionName.TemenosCh3Stormhail},
        RegionName.Crestlands:              {RegionName.Winterlands1, RegionName.Brightlands, RegionName.CrestlandsPass, 
                                             RegionName.Flamechurch, RegionName.Montwise, RegionName.SpriteCave, RegionName.MerryHills, RegionName.TravelersBag},
        RegionName.CrestlandsPass:          {RegionName.Winterlands2, RegionName.Crestlands},
        RegionName.Flamechurch:             {RegionName.Crestlands, RegionName.FlamechurchKO, RegionName.TemenosThroneCh1, RegionName.TemenosCh1},
        RegionName.Montwise:                {RegionName.Crestlands, RegionName.OsvaldCh4, RegionName.HikariCh2, RegionName.ThroneCh3Father, RegionName.PartitioOsvaldCh2, RegionName.PeculiarTomes, RegionName.ReachesOfHell},
        RegionName.MerryHills:              {RegionName.AgneaCh5, RegionName.Crestlands, RegionName.AgneaClear},
        RegionName.Brightlands:             {RegionName.AbandonedVillage, RegionName.SunkenMaw, RegionName.Waterway, RegionName.Clockbank, 
                                             RegionName.NewDelsta, RegionName.SunderingSea, RegionName.Totohaha, RegionName.Canalbrine, 
                                             RegionName.Wildlands2, RegionName.TravelersBag},
        RegionName.AbandonedVillage:        {RegionName.Brightlands, RegionName.CasttiCh3},
        RegionName.Clockbank:               {RegionName.PartitioCh2, RegionName.Clocktower},
        RegionName.NewDelsta:               {RegionName.AgneaCh2, RegionName.LostseedPass, RegionName.NewDelstaAmbush, RegionName.NewDelstaKO, RegionName.ThroneCh1, RegionName.PartitioOsvaldCh1},
        RegionName.LostseedPass:            {RegionName.Lostseed, RegionName.NewDelsta},
        RegionName.Lostseed:                {RegionName.LostseedPass, RegionName.ThroneClear},
        RegionName.Totohaha:                {RegionName.Brightlands, RegionName.Canalbrine, RegionName.Wildlands2, RegionName.SunderingSea, 
                                             RegionName.BeastingVillage, RegionName.Tropuhopu, RegionName.TotohahaPass, RegionName.CavernOfWaves, RegionName.TravelersBag},
        RegionName.BeastingVillage:         {RegionName.Totohaha, RegionName.BeastingVillageKO, RegionName.OchetteCh3, RegionName.OchetteCh1, RegionName.OchetteClear},
        RegionName.Tropuhopu:               {RegionName.Totohaha, RegionName.TropuhopuKO, RegionName.TropuhopuKOBoat, RegionName.PartitioTropuhopu, RegionName.AgneaCh3},
        RegionName.TotohahaPass:            {RegionName.Totohaha, RegionName.NamelessVillage, RegionName.SinkingRuins},
        RegionName.NamelessVillage:         {RegionName.TotohahaPass, RegionName.NamelessVillageKO, RegionName.TemenosCh4, RegionName.TemenosClear},
        RegionName.Harborlands:             {RegionName.Canalbrine, RegionName.Hinoeuma1, RegionName.Hinoeuma2, RegionName.SunMoonCave, 
                                             RegionName.HarborlandsBoat, RegionName.HarborlandsKO, RegionName.ConningCreek, RegionName.TravelersBag},
        RegionName.Canalbrine:              {RegionName.Harborlands, RegionName.Totohaha, RegionName.Brightlands, RegionName.SunderingSea, 
                                             RegionName.CanalbrineBoat, RegionName.CanalbrineBoatKO, RegionName.TemenosCh2, RegionName.CasttiCh1},
        RegionName.ConningCreek:            {RegionName.Harborlands, RegionName.OsvaldCh3, RegionName.OchetteCh2Acta, RegionName.ThroneTemenosCh2},
        RegionName.Winterlands1:            {RegionName.CapeCold, RegionName.Ruffians, RegionName.Winterbloom, RegionName.Crestlands, 
                                             RegionName.Brightlands},
        RegionName.RoqueIsland:             {RegionName.SunderingSea, RegionName.RoqueIslandKO, RegionName.PartitioCh4, RegionName.PartitioClear},
        RegionName.Hinoeuma1:               {RegionName.Harborlands, RegionName.Wildlands1, RegionName.Ryu, RegionName.TravelersBag},
        RegionName.Ryu:                     {RegionName.Hinoeuma1, RegionName.HikariCh1, RegionName.AgneaHikariCh1},
        RegionName.Hinoeuma2:               {RegionName.Harborlands, RegionName.Leaflands, RegionName.Sai, RegionName.Ku},
        RegionName.Sai:                     {RegionName.Hinoeuma2, RegionName.SaiKO, RegionName.SaiRuins, RegionName.CasttiCh2Sai, RegionName.PartitioSai, RegionName.AgneaCh4},
        RegionName.Ku:                      {RegionName.Hinoeuma2, RegionName.HikariCh5, RegionName.HikariClear, RegionName.AgneaHikariCh2},
        RegionName.Wildlands1:              {RegionName.Hinoeuma1, RegionName.Leaflands, RegionName.Oresrush, RegionName.TravelersBag},
        RegionName.Oresrush:                {RegionName.Wildlands1, RegionName.PartitioCh1, RegionName.OresrushKO},
        RegionName.Wildlands2:              {RegionName.Leaflands, RegionName.Brightlands, RegionName.Totohaha, RegionName.SunderingSea, 
                                             RegionName.Tunnels, RegionName.Crackridge, RegionName.Gravell},
        RegionName.Crackridge:              {RegionName.Wildlands2, RegionName.CrackridgeKO, RegionName.TemenosCh3Crackridge, RegionName.OchetteCh2Tera},
        RegionName.Gravell:                 {RegionName.Wildlands2, RegionName.OsvaldCh5, RegionName.OsvaldClear},
        RegionName.Leaflands:               {RegionName.Hinoeuma2, RegionName.Wildlands1, RegionName.Wildlands2, RegionName.Spring,
                                             RegionName.Cropdale, RegionName.LeaflandsBoat, RegionName.Wellgrove, RegionName.Timberain, RegionName.TravelersBag},
        RegionName.Cropdale:                {RegionName.Leaflands, RegionName.CropdaleBoat, RegionName.AgneaCh1, RegionName.OchetteCasttiCh1, RegionName.OchetteCasttiCh2},
        RegionName.Wellgrove:               {RegionName.Leaflands, RegionName.ThroneCh3Mother, RegionName.HikariCh3, RegionName.PartitioCh3, RegionName.ThroneCh2Mother},
        RegionName.Timberain:               {RegionName.Leaflands, RegionName.TimberainKO, RegionName.CasttiCh4, RegionName.CasttiClear},
        RegionName.SunderingSea:            {RegionName.Brightlands, RegionName.Wildlands2, RegionName.Canalbrine, RegionName.Totohaha, RegionName.Vide, RegionName.Galdera}
    }

    for source, target in OT2RegionConnections.items():
        source_region = multiworld.get_region(source, player)
        source_region.add_exits(target)


def create_region(multiworld, player: int, active_locations, name: str, locations=None):
    ret = Region(name, player, multiworld)
    if locations:
        loc_to_id = {loc: active_locations.get(loc, 0) for loc in locations if active_locations.get(loc, None)}
        ret.add_locations(loc_to_id, OT2Location)
        loc_to_event = {loc: active_locations.get(loc, None) for loc in locations if
                        not active_locations.get(loc, None)}
        ret.add_locations(loc_to_event, OT2Location)

    return ret
    

