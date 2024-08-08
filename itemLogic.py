# Authors
# Organization: https://github.com/rogueEdit/
# Repository: https://github.com/rogueEdit/OnlineRogueEditor
# Contributors: https://github.com/JulianStiebler/
# Date of release: 23.06.2024 
# Last Edited: 28.06.2024
# Based on: https://github.com/pagefaultgames/pokerogue/

# Unlike the other code, reusing this in your own project is forbidden.

from enum import Enum
from dataclasses import dataclass, field
from typing import Any, List, Optional


# from modules.handler import dec_handleOperationExceptions, OperationCancel, OperationSoftCancel, OperationSuccessful  # noqa: F401
# from modules.handler import fh_getChoiceInput, fh_getCompleterInput, fh_getIntegerInput  # noqa: F401


@dataclass
class Modifier:
    args: Optional[List[Any]]
    className: str
    player: bool
    stackCount: int
    typeId: str
    typePregenArgs: Optional[List[Any]] = None
    description: Optional[str] = field(default=None, repr=True, compare=False)
    customName: Optional[str] = field(default=None, repr=True, compare=False)
    customType: Optional[str] = field(default=None, repr=True, compare=False)
    maxStack: Optional[int] = field(default=None, repr=True, compare=False)
    shortDescription: Optional[str] = field(default=None, repr=True, compare=False)

    def fh_toJSON(self, poke_id: Optional[int] = None, stackCount: int = 1) -> dict:
        tmpArgs = self.args
        stackCount = stackCount if stackCount <= self.maxStack else self.maxStack
        # Create JSON representation
        jsonData = {
            "args": [] if tmpArgs is None else [poke_id if arg is None else arg for arg in tmpArgs],  # Ensures args is None if empty
            "className": self.className,
            "player": self.player,
            "stackCount": stackCount,
            "typeId": self.typeId,
        }

        if self.typePregenArgs is not None:
            jsonData["typePregenArgs"] = self.typePregenArgs

        return jsonData


# customName needs to be localized later
class ModifierType(Enum):
    # 属性伤害提升道具
    SILK_SCARF = Modifier(args=[None, 0, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[0],
                          description='Boosts NORMAL types.', customName='丝绸围巾', customType='StatBooster', maxStack=99)
    BLACK_BELT = Modifier(args=[None, 1, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[1],
                          description='Boosts FIGHT types.', customName='黑带', customType='StatBooster', maxStack=99)
    SHARP_BEAK = Modifier(args=[None, 2, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[2],
                          description='Boosts FLYING types.', customName='锐利鸟嘴', customType='StatBooster', maxStack=99)
    POISON_BARB = Modifier(args=[None, 3, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[3],
                           description='Boosts POISON types.', customName='毒针', customType='StatBooster', maxStack=99)
    SOFT_SAND = Modifier(args=[None, 4, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[4],
                         description='Boosts GROUND types.', customName='柔软沙子', customType='StatBooster', maxStack=99)
    HARD_STONE = Modifier(args=[None, 5, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[5],
                          description='Boosts ROCK types.', customName='硬石头', customType='StatBooster', maxStack=99)
    SILVER_POWDER = Modifier(args=[None, 6, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[6],
                             description='Boosts BUG types.', customName='银粉', customType='StatBooster', maxStack=99)
    SPELL_TAG = Modifier(args=[None, 7, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[7],
                         description='Boosts GHOST types.', customName='咒术之符', customType='StatBooster', maxStack=99)
    METAL_COAT = Modifier(args=[None, 8, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[8],
                          description='Boosts STEEL types.', customName='金属膜', customType='StatBooster', maxStack=99)
    CHARCOAL = Modifier(args=[None, 9, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[9],
                        description='Boosts FIRE types.', customName='木炭', customType='StatBooster', maxStack=99)
    MYSTIC_WATER = Modifier(args=[None, 10, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[10],
                            description='Boosts WATER types.', customName='神秘水滴', customType='StatBooster', maxStack=99)
    MIRACLE_SEED = Modifier(args=[None, 11, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[11],
                            description='Boosts GRASS types.', customName='奇迹种子', customType='StatBooster', maxStack=99)
    MAGNET = Modifier(args=[None, 12, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[12],
                      description='Boosts ELECTRIC types.', customName='磁铁', customType='StatBooster', maxStack=99)
    TWISTED_SPOON = Modifier(args=[None, 13, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[13],
                             description='Boosts PSYCHO types.', customName='弯曲的汤匙', customType='StatBooster', maxStack=99)
    NEVER_MELT_ICE = Modifier(args=[None, 14, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[14],
                              description='Boosts ICE types.', customName='不融冰', customType='StatBooster', maxStack=99)
    DRAGON_FANG = Modifier(args=[None, 15, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[15],
                           description='Boosts DRAGON types.', customName='龙之牙', customType='StatBooster', maxStack=99)
    BLACK_GLASSES = Modifier(args=[None, 16, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[16],
                             description='Boosts DARK types.', customName='黑色眼镜', customType='StatBooster', maxStack=99)
    FAIRY_FEATHER = Modifier(args=[None, 17, 20], className='AttackTypeBoosterModifier', player=True, stackCount=1, typeId='ATTACK_TYPE_BOOSTER', typePregenArgs=[17],
                             description='Boosts FAIRY types.', customName='妖精之羽', customType='StatBooster', maxStack=99)
    # 能力提升剂
    HP_UP = Modifier(args=[None, 0], className='PokemonBaseStatModifier', player=True, stackCount=1, typeId='BASE_STAT_BOOSTER', typePregenArgs=[0], description='Increases HP.',
                     customName='ＨＰ增强剂', customType='Vitamin', maxStack=20)
    PROTEIN = Modifier(args=[None, 1], className='PokemonBaseStatModifier', player=True, stackCount=1, typeId='BASE_STAT_BOOSTER', typePregenArgs=[1],
                       description='Increases Attack.', customName='攻击增强剂', customType='Vitamin', maxStack=20)
    IRON = Modifier(args=[None, 2], className='PokemonBaseStatModifier', player=True, stackCount=1, typeId='BASE_STAT_BOOSTER', typePregenArgs=[2],
                    description='Increases Defense.', customName='防御增强剂', customType='Vitamin', maxStack=20)
    CALCIUM = Modifier(args=[None, 3], className='PokemonBaseStatModifier', player=True, stackCount=1, typeId='BASE_STAT_BOOSTER', typePregenArgs=[3],
                       description='Increases Special Attack.', customName='特攻增强剂', customType='Vitamin', maxStack=20)
    ZINC = Modifier(args=[None, 4], className='PokemonBaseStatModifier', player=True, stackCount=1, typeId='BASE_STAT_BOOSTER', typePregenArgs=[4],
                    description='Increases Special Defense.', customName='特防增强剂', customType='Vitamin', maxStack=20)
    CARBOS = Modifier(args=[None, 5], className='PokemonBaseStatModifier', player=True, stackCount=1, typeId='BASE_STAT_BOOSTER', typePregenArgs=[5],
                      description='Increases Speed.', customName='速度增强剂', customType='Vitamin', maxStack=20)
    # 5回合能力上升
    X_ATTACK = Modifier(args=[0, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[0],
                        description='Increases Attack', customName='力量强化', customType='XItem', maxStack=99)
    X_DEFENSE = Modifier(args=[1, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[1],
                         description='Increases Defense', customName='防御强化', customType='XItem', maxStack=99)
    X_SP_ATK = Modifier(args=[2, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[2],
                        description='Increases Special Attack', customName='特攻强化', customType='XItem', maxStack=99)
    X_SP_DEF = Modifier(args=[3, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[3],
                        description='Increases Special Defense', customName='特防强化', customType='XItem', maxStack=99)
    X_SPEED = Modifier(args=[4, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[4],
                       description='Increases Speed', customName='速度强化', customType='XItem', maxStack=99)
    X_ACCURACY = Modifier(args=[5, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[5],
                          description='Increases Accuracy', customName='命中强化', customType='XItem', maxStack=99)
    X_DIRE_HIT = Modifier(args=[6, 5], className='TempBattleStatBoosterModifier', player=True, stackCount=1, typeId='TEMP_STAT_BOOSTER', typePregenArgs=[6],
                          description='Increases Critical%', customName='要害攻击', customType='XItem', maxStack=99)
    # 树果
    APICOT_BERRY = Modifier(args=[None, 6], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[6],
                            description='Raises Sp. Def if HP is below 25%.', customName='杏仔果', customType='Berry', maxStack=3, shortDescription='+SP Def when below 25% HP')
    ENIGMA_BERRY = Modifier(args=[None, 2], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[2],
                            description='Restores 25% HP if hit by a super effective move.', customName='谜芝果', customType='Berry', maxStack=2,
                            shortDescription='Heals 25% when critical hit')
    GANLON_BERRY = Modifier(args=[None, 4], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[4],
                            description='Raises Defense if HP is below 25%.', customName='龙睛果', customType='Berry', maxStack=3, shortDescription='Raise Defense when below 25% HP')
    LANSAT_BERRY = Modifier(args=[None, 8], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[8],
                            description='Raises critical hit ratio if HP is below 25%.', customName='兰萨果', customType='Berry', maxStack=3,
                            shortDescription='Raise Crit when below 25% HP')
    LIECHI_BERRY = Modifier(args=[None, 3], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[3],
                            description='Raises Attack if HP is below 25%.', customName='枝荔果', customType='Berry', maxStack=3, shortDescription='Raise ATK when below 25% HP')
    LEPPA_BERRY = Modifier(args=[None, 10], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[10],
                           description='Restores 10 PP to a move if its PP reaches 0.', customName='苹野果', customType='Berry', maxStack=2,
                           shortDescription='Restore 10 PP when empty')
    LUM_BERRY = Modifier(args=[None, 1], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[1],
                         description='Cures any non-volatile status condition and confusion', customName='木子果', customType='Berry', maxStack=2,
                         shortDescription='Cures non-volatiles status')
    PETAYA_BERRY = Modifier(args=[None, 5], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[5],
                            description='Raises Sp. Atk if HP is below 25%.', customName='龙火果', customType='Berry', maxStack=3)
    SALAC_BERRY = Modifier(args=[None, 7], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[7], description='Raises Speed if HP is below 25%.',
                           customName='沙鳞果', customType='Berry', maxStack=3)
    SITRUS_BERRY = Modifier(args=[None, 0], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[0],
                            description='Restores 25% HP if HP is below 50%.', customName='文柚果', customType='Berry', maxStack=2)
    STARF_BERRY = Modifier(args=[None, 9], className='BerryModifier', player=True, stackCount=1, typeId='BERRY', typePregenArgs=[9], description='+Random stat if HP is below 25%.',
                           customName='星桃果', customType='Berry', maxStack=3)
    BERRY_POUCH = Modifier(args=None, className='PreserveBerryModifier', player=True, stackCount=1, typeId='BERRY_POUCH', typePregenArgs=None,
                           description='33% chance used berry to not be used.', customName='树果袋', customType='Berry', maxStack=3)
    # 被动技能
    GOLDEN_POKEBALL = Modifier(args=None, className='ExtraModifierModifier', player=True, stackCount=1, typeId='GOLDEN_POKEBALL', typePregenArgs=None,
                               description='Adds 1 extra item option at the end of every battle.', customName='黄金精灵球', customType='PassiveBoost', maxStack=3,
                               shortDescription='One more shop item')
    AMULET_COIN = Modifier(args=None, className='MoneyMultiplierModifier', player=True, stackCount=1, typeId='AMULET_COIN', typePregenArgs=None,
                           description='Increases money rewards from all sources by 20%.', customName='护符金币', customType='PassiveBoost', maxStack=5,
                           shortDescription='+20% Money from all sources')
    LOCK_CAPSULE = Modifier(args=None, className='LockModifierTiersModifier', player=True, stackCount=1, typeId='LOCK_CAPSULE', typePregenArgs=None,
                            description='Allows you to lock item rarities when rerolling items.', customName='上锁的容器', customType='PassiveBoost', maxStack=1,
                            shortDescription='Lock rarity in shops')
    CANDY_JAR = Modifier(args=None, className='LevelIncrementBoosterModifier', player=True, stackCount=1, typeId='CANDY_JAR', typePregenArgs=None,
                         description='Increases the number of levels added by Rare Candy items by 1.', customName='糖果罐', customType='PassiveBoost', maxStack=99,
                         shortDescription='+1 level per rare candy')
    EXP_SHARE = Modifier(args=None, className='ExpShareModifier', player=True, stackCount=1, typeId='EXP_SHARE', typePregenArgs=None,
                         description="Non-participants receive 20% of a single participant's EXP. Points.", customName='学习装置', customType='PassiveBoost', maxStack=5,
                         shortDescription='Share +20% XP with all')
    EXP_BALANCE = Modifier(args=None, className='ExpBalanceModifier', player=True, stackCount=1, typeId='EXP_BALANCE', typePregenArgs=None,
                           description='Balances 20% of your total earned exp towards the lowest leveled party member(s).', customName='均衡型学习装置', customType='PassiveBoost',
                           maxStack=4, shortDescription='Weakest mon gets more XP')
    EXP_CHARM = Modifier(args=[25], className='ExpBoosterModifier', player=True, stackCount=1, typeId='EXP_CHARM', typePregenArgs=None,
                         description='Increases gain of EXP. Points by 25%.', customName='经验护符', customType='PassiveBoost', maxStack=99, shortDescription='+25% EXP Gain')
    SUPER_EXP_CHARM = Modifier(args=[60], className='ExpBoosterModifier', player=True, stackCount=1, typeId='SUPER_EXP_CHARM', typePregenArgs=None,
                               description='Increases gain of EXP. Points by 60%. ', customName='超级经验护符', customType='PassiveBoost', maxStack=30, shortDescription='+60% EXP Gain')
    GOLDEN_EXP_CHARM = Modifier(args=[100], className='ExpBoosterModifier', player=True, stackCount=1, typeId='GOLDEN_EXP_CHARM', typePregenArgs=None,
                                description='Increases gain of EXP. Points by 100%. ', customName='黄金经验护符', customType='PassiveBoost', maxStack=10,
                                shortDescription='+100% EXP Gain')
    SHINY_CHARM = Modifier(args=None, className='ShinyRateBoosterModifier', player=True, stackCount=1, typeId='SHINY_CHARM', typePregenArgs=None,
                           description='Dramatically increases the chance of a wild Pokémon being Shiny.', customName='闪耀护符', customType='PassiveBoost', maxStack=4,
                           shortDescription='Increase shiny encounter %')
    ABILITY_CHARM = Modifier(args=None, className='HiddenAbilityRateBoosterModifier', player=True, stackCount=1, typeId='ABILITY_CHARM', typePregenArgs=None,
                             description='Dramatically increases the chance of a wild Pokémon having a Hidden Ability.', customName='特性护符', customType='PassiveBoost', maxStack=4,
                             shortDescription='Wild pokemon hidden ability chance increased')
    MEGA_BRACELET = Modifier(args=None, className='MegaEvolutionAccessModifier', player=True, stackCount=1, typeId='MEGA_BRACELET', typePregenArgs=None,
                             description='Mega Stones become available.', customName='超级手镯', customType='PassiveBoost', maxStack=1)
    DYNAMAX_BAND = Modifier(args=None, className='GigantamaxAccessModifier', player=True, stackCount=1, typeId='DYNAMAX_BAND', typePregenArgs=None,
                            description='Max Mushrooms become available.', customName='极巨腕带', customType='PassiveBoost', maxStack=1)
    TERA_ORB = Modifier(args=None, className='TerastallizeAccessModifier', player=True, stackCount=1, typeId='TERA_ORB', typePregenArgs=None,
                        description='Tera Shards become available.', customName='太晶珠', customType='PassiveBoost', maxStack=3)
    HEALING_CHARM = Modifier(args=[1.1], className='HealingBoosterModifier', player=True, stackCount=1, typeId='HEALING_CHARM', typePregenArgs=None,
                             description='Increases the effectiveness of HP restoring moves and items by 10% (excludes Revives).', customName='治疗护符', customType='PassiveBoost',
                             maxStack=5, shortDescription='HP restoring moves heal 10% more')
    # 其他可持有物品
    REVIVER_SEED = Modifier(args=[None], className='PokemonInstantReviveModifier', player=True, stackCount=1, typeId='REVIVER_SEED', typePregenArgs=None,
                            description='Revives the holder for 1/2 HP upon fainting.', customName='复活种子', customType='OtherHoldable', maxStack=1)
    GOLDEN_PUNCH = Modifier(args=[None], className='DamageMoneyRewardModifier', player=True, stackCount=1, typeId='GOLDEN_PUNCH', typePregenArgs=None,
                            description='Grants 50% of damage inflicted as money.', customName='黄金拳头', customType='OtherHoldable', maxStack=5)
    WIDE_LENS = Modifier(args=[None, 5], className='PokemonMoveAccuracyBoosterModifier', player=True, stackCount=1, typeId='WIDE_LENS', typePregenArgs=None,
                         description='Increases move accuracy by 5 (maximum 100).', customName='广角镜', customType='OtherHoldable', maxStack=3)
    BATON = Modifier(args=[None], className='SwitchEffectTransferModifier', player=True, stackCount=1, typeId='BATON', typePregenArgs=None,
                     description='Allows passing along effects when switching Pokémon, which also bypasses traps.', customName='接力棒', customType='OtherHoldable', maxStack=1,
                     shortDescription='Pass on effects when switching Pokemon')
    FOCUS_BAND = Modifier(args=[None], className='SurviveDamageModifier', player=True, stackCount=1, typeId='FOCUS_BAND', typePregenArgs=None,
                          description='10% chance to cheat death with 1HP', customName='气势头带', customType='OtherHoldable', maxStack=4)
    GRIP_CLAW = Modifier(args=[None, 10], className='ContactHeldItemTransferChanceModifier', player=True, stackCount=1, typeId='GRIP_CLAW', typePregenArgs=None,
                         description="Upon attacking, there is a 10% chance the foe's held item will be stolen.", customName='紧缠钩爪', customType='OtherHoldable', maxStack=5,
                         shortDescription='10% onhit to steal enemy item')
    QUICK_CLAW = Modifier(args=[None], className='BypassSpeedChanceModifier', player=True, stackCount=1, typeId='QUICK_CLAW', typePregenArgs=None,
                          description='Adds a 10percent chance to move first regardless of speed (after priority)', customName='先制之爪', customType='OtherHoldable', maxStack=3,
                          shortDescription='10% chance to go first ignoring speed')
    KINGS_ROCK = Modifier(args=[None], className='FlinchChanceModifier', player=True, stackCount=1, typeId='KINGS_ROCK', typePregenArgs=None,
                          description='Adds a 10% chance an attack move will cause the opponent to flinch.', customName='王者之证', customType='OtherHoldable', maxStack=3,
                          shortDescription='10% onhit to make enemy flinch')
    LEFTOVERS = Modifier(args=[None], className='TurnHealModifier', player=True, stackCount=1, typeId='LEFTOVERS', typePregenArgs=None,
                         description="Heals 1/16 of a Pokémon's maximum HP every turn.", customName='吃剩的东西', customType='OtherHoldable', maxStack=4)
    SHELL_BELL = Modifier(args=[None], className='HitHealModifier', player=True, stackCount=1, typeId='SHELL_BELL', typePregenArgs=None,
                          description="Heals 1/8 of the Pokemon's dealt damage.", customName='贝壳之铃', customType='OtherHoldable', maxStack=4)
    SOOTHE_BELL = Modifier(args=[None], className='PokemonFriendshipBoosterModifier', player=True, stackCount=1, typeId='SOOTHE_BELL', typePregenArgs=None,
                           description='Increases friendship gain per victory by 50%.', customName='安抚之铃', customType='OtherHoldable', maxStack=3,
                           shortDescription='+50% more friendship per win')
    SOUL_DEW = Modifier(args=[None], className='PokemonNatureWeightModifier', player=True, stackCount=1, typeId='SOUL_DEW', typePregenArgs=None,
                        description="Increases the influence of a Pokémon's nature on its stats by 10% (additive).", customName='心之水滴', customType='OtherHoldable', maxStack=10,
                        shortDescription='Increase nature influence (additive +10%)')
    MULTI_LENS = Modifier(args=[None], className='PokemonMultiHitModifier', player=True, stackCount=1, typeId='MULTI_LENS', typePregenArgs=None,
                          description='Attacks hit one additional time at the cost of a 60/75/82.5% power reduction per stack respectively.', customName='多重镜',
                          customType='OtherHoldable', maxStack=3, shortDescription='Attacks hit one additional time')
    MINI_BLACK_HOLE = Modifier(args=[None], className='TurnHeldItemTransferModifier', player=True, stackCount=1, typeId='MINI_BLACK_HOLE', typePregenArgs=None,
                               description='Every turn, the holder acquires one held item from the foe.', customName='迷你黑洞', customType='OtherHoldable', maxStack=1,
                               shortDescription='Steal one item each turn from enemy')
    LUCKY_EGG = Modifier(args=[None, 40], className='PokemonExpBoosterModifier', player=True, stackCount=1, typeId='LUCKY_EGG', typePregenArgs=None,
                         description="Increases the holder's gain of EXP. Points by 40%.", customName='幸运蛋', customType='OtherHoldable', maxStack=99,
                         shortDescription='+40% EXP Gain')
    GOLDEN_EGG = Modifier(args=[None, 100], className='PokemonExpBoosterModifier', player=True, stackCount=1, typeId='GOLDEN_EGG', typePregenArgs=None,
                          description="Increases the holder's gain of EXP. Points by 100%. ", customName='黄金精灵球', customType='OtherHoldable', maxStack=99,
                          shortDescription='+100% EXP Gain')
    # FORM_CHANGE_ITEM0 = Modifier(args=[None, 0, True], className='PokemonFormChangeItemModifier', player=True, stackCount=1, typeId='FORM_CHANGE_ITEM', typePregenArgs=[0], description='Causes certain Pokémon to change form.', customName='FormChangeItem', customType='OtherHoldable', maxStack=1)
    # the form change exists from 0-70... 
    ENEMY_ATTACK_BURN_CHANCE = Modifier(args=[6, 5], className='EnemyAttackStatusEffectChanceModifier', player=False, stackCount=1, typeId='ENEMY_ATTACK_BURN_CHANCE',
                                        typePregenArgs=None, description='Adds a 5% chance to inflict burn with attack moves.', customName='Token: Burn', customType='Token',
                                        maxStack=10, shortDescription='On-hit 5% burn')
    ENEMY_ATTACK_PARALYZE_CHANCE = Modifier(args=[3, 2.5], className='EnemyAttackStatusEffectChanceModifier', player=False, stackCount=1, typeId='ENEMY_ATTACK_PARALYZE_CHANCE',
                                            typePregenArgs=None, description='Adds a 2.5% chance to inflict paralysis with attack moves.', customName='Token: Paralzye',
                                            customType='Token', maxStack=10, shortDescription='On-hit 2.5% paralyze')
    ENEMY_ATTACK_POISON_CHANCE = Modifier(args=[1, 5], className='EnemyAttackStatusEffectChanceModifier', player=False, stackCount=1, typeId='ENEMY_ATTACK_POISON_CHANCE',
                                          typePregenArgs=None, description='Adds a 5% chance to inflict poisoning with attack moves.', customName='Token: Poison',
                                          customType='Token', maxStack=10, shortDescription='On-hit 5% poison')
    ENEMY_DAMAGE_BOOSTER = Modifier(args=[5.000000000000004], className='EnemyDamageBoosterModifier', player=False, stackCount=1, typeId='ENEMY_DAMAGE_BOOSTER',
                                    typePregenArgs=None, description='Increases damage by 5%', customName='Token: Damage Increase', customType='Token', maxStack=50)
    ENEMY_DAMAGE_REDUCTION = Modifier(args=[2.500000000000002], className='EnemyDamageReducerModifier', player=False, stackCount=1, typeId='ENEMY_DAMAGE_REDUCTION',
                                      typePregenArgs=None, description='Reduces incoming damage by 2.5%', customName='Token: Damage Take Reduce', customType='Token', maxStack=50)
    ENEMY_ENDURE_CHANCE = Modifier(args=[2], className='EnemyEndureChanceModifier', player=False, stackCount=1, typeId='ENEMY_ENDURE_CHANCE', typePregenArgs=None,
                                   description='Adds a 2% chance of enduring a hit.', customName='Token: Endure', customType='Token', maxStack=10)
    ENEMY_FUSED_CHANCE = Modifier(args=[1], className='EnemyFusionChanceModifier', player=False, stackCount=1, typeId='ENEMY_FUSED_CHANCE', typePregenArgs=None,
                                  description='Adds a 1% chance that a wild species will be a fusion.', customName='Token: Wild Fusions', customType='Token', maxStack=10,
                                  shortDescription='1% more chance on wild fusions')
    ENEMY_HEAL = Modifier(args=[2], className='EnemyTurnHealModifier', player=False, stackCount=1, typeId='ENEMY_HEAL', typePregenArgs=None,
                          description='Heals 2% of max HP every turn.', customName='Token: Heal', customType='Token', maxStack=5, shortDescription='')
    ENEMY_STATUS_EFFECT_HEAL_CHANCE = Modifier(args=[2.5], className='EnemyStatusEffectHealChanceModifier', player=False, stackCount=1, typeId='ENEMY_STATUS_EFFECT_HEAL_CHANCE',
                                               typePregenArgs=None, description='Adds a 2.5% chance every turn to heal a status condition.', customName='Token: Heal status',
                                               customType='Token', maxStack=10, shortDescription='2.5% per round to drop any negatives')
    # Dangerous Items
    IV_SCANNER = Modifier(args=None, className='IvScannerModifier', player=True, stackCount=1, typeId='IV_SCANNER', typePregenArgs=None,
                          description='Allows scanning the IVs of wild Pokémon. 2 IVs are revealed per stack. The best IVs are shown first.', customName='个体扫描仪',
                          customType='Danger', maxStack=1, shortDescription='Scan enemy IVs')
    TOXIC_ORB = Modifier(args=[None], className='TurnStatusEffectModifier', player=True, stackCount=1, typeId='TOXIC_ORB', typePregenArgs=None,
                         description='Badly poisons its holder at the end of the turn if they do not have a status condition already', customName='剧毒宝珠', customType='Danger',
                         maxStack=1, shortDescription='Poison your pokemon')
    FIRE_ORB = Modifier(args=[None], className='TurnStatusEffectModifier', player=True, stackCount=1, typeId='FIRE_ORB', typePregenArgs=None,
                        description='Burns its holder at the end of the turn if they do not have a status condition already.', customName='火焰宝珠', customType='Danger', maxStack=1,
                        shortDescription='Burn your pokemon')


if __name__ == '__main__':
    all_values = [e.value for e in ModifierType.__members__.values()]
    print(ModifierType['MEGA_BRACELET'].value.fh_toJSON() == {
        "player": True,
        "typeId": "MEGA_BRACELET",
        "args": [],
        "stackCount": 1,
        "className": "MegaEvolutionAccessModifier"
    })
