import random
import math

class Mon:
    def __init__(self, ID, DexNo, Name, Type1, Type2, BST, BaseHP, BaseATK,
    BaseDEF, BaseSPATK, BaseSPDEF, BaseSPD, Gen, isNFE, isLegal):
        self.ID = ID
        self.DexNo = DexNo
        self.Name = Name
        self.Type1 = Type1
        self.Type2 = Type2
        self.BST = BST
        self.BaseHP = BaseHP
        self.BaseATK = BaseATK
        self.BaseDEF = BaseDEF
        self.BaseSPATK = BaseSPATK
        self.BaseSPDEF = BaseSPDEF
        self.BaseSPD = BaseSPD
        self.Gen = Gen
        self.isNFE = isNFE
        self.isLegal = isLegal
    
class Team_Mon:
    def __init__(self
    , Mon
    , Gender, Item, Ability, Move1, Move2, Move3, Move4, EVHP, EVATK
    , EVDEF, EVSPATK, EVSPDEF, EVSPD, IVHP, IVATK, IVDEF, IVSPATK, IVSPDEF
    , IVSPD, Nature, IsGmax):
        self.__dict__ = Mon.__dict__.copy()
        self.Gender = Gender
        self.Item = Item
        self.Ability = Ability
        self.Move1 = Move1
        self.Move2 = Move2
        self.Move3 = Move3
        self.Move4 = Move4
        self.EVHP = EVHP
        self.EVATK = EVATK
        self.EVDEF = EVDEF
        self.EVSPATK = EVSPATK
        self.EVSPDEF = EVSPDEF
        self.EVSPD = EVSPD
        self.IVHP = IVHP
        self.IVATK = IVATK
        self.IVDEF = IVDEF
        self.IVSPATK = IVSPATK
        self.IVSPDEF = IVSPDEF
        self.IVSPD = IVSPD
        self.Nature = Nature
        self.IsGmax = IsGmax

class Battle_Mon(Team_Mon):
    def __init__(self, *args):
        self.__dict__ = args[0].__dict__.copy()
        self.CurrentHP = 1
        self.HP = 1
        self.ATK = 1
        self.DEF = 1
        self.SPATK = 1
        self.SPDEF = 1
        self.SPD = 1
        self.MovePP1 = 1
        self.MovePP2 = 1
        self.MovePP3 = 1
        self.MovePP4 = 1
        self.IsKnockedOut = False
        self.ATKStage = 0
        self.DEFStage = 0
        self.SPATKStage = 0
        self.SPDEFStage = 0
        self.SPDStage = 0
        self.CritStage = 0
        self.AccStage = 0
        self.EvaStage = 0
        self.Status = 'Healthy'
        self.StatusTurns = 0
        self.LastMoveUsed = None
        self.TurnsOnField = 0
        self.IsDisappeared = False
        self.IsUnderground = False
        self.IsUnderwater = False
        self.IsInAir = False
        self.IsProtected = False
        self.IsFlinching = False
        self.IsConfused = False
        self.IsHelped = False
        self.IsCharging = False
        self.IsRecharging = False
    
    def calc_stats(self):
        self.HP = math.floor((2 * self.BaseHP + self.IVHP + math.floor(self.EVHP/4)) * 50 / 100) + 60
        self.CurrentHP = self.HP
        self.ATK = math.floor(GetNature(self.Nature, 'ATK') * (math.floor((2 * self.BaseATK + self.IVATK + math.floor(self.EVATK/4)) * 50 / 100) + 5))
        self.DEF = math.floor(GetNature(self.Nature, 'DEF') * (math.floor((2 * self.BaseDEF + self.IVDEF + math.floor(self.EVDEF/4)) * 50 / 100) + 5))
        self.SPATK = math.floor(GetNature(self.Nature, 'SPATK') * (math.floor((2 * self.BaseSPATK + self.IVSPATK + math.floor(self.EVSPATK/4)) * 50 / 100) + 5))
        self.SPDEF = math.floor(GetNature(self.Nature, 'SPDEF') * (math.floor((2 * self.BaseSPDEF + self.IVSPDEF + math.floor(self.EVSPDEF/4)) * 50 / 100) + 5))
        self.SPD = math.floor(GetNature(self.Nature, 'SPD') * (math.floor((2 * self.BaseSPD + self.IVSPD + math.floor(self.EVSPD/4)) * 50 / 100) + 5))

def GetNature(name,stat):
    if stat == 'ATK':
        if name in ('Lonely', 'Brave', 'Adamant', 'Naughty'):
            return 1.1
        elif name in ('Bold', 'Modest', 'Calm', 'Timid'):
            return 0.9
        else:
            return 1.0
    elif stat == 'DEF':
        if name in ('Bold', 'Impish', 'Lax', 'Relaxed'):
            return 1.1
        elif name in ('Lonely', 'Mild', 'Gentle', 'Hasty'):
            return 0.9
        else:
            return 1.0
    elif stat == 'SPATK':
        if name in ('Modest', 'Mild', 'Rash', 'Quiet'):
            return 1.1
        elif name in ('Adamant', 'Impish', 'Careful', 'Jolly'):
            return 0.9
        else:
            return 1.0
    elif stat == 'SPDEF':
        if name in ('Calm', 'Gentle', 'Careful', 'Sassy'):
            return 1.1
        elif name in ('Naughty', 'Lax', 'Rash', 'Naive'):
            return 0.9
        else:
            return 1.0
    elif stat == 'SPD':
        if name in ('Timid', 'Hasty', 'Jolly', 'Naive'):
            return 1.1
        elif name in ('Brave', 'Relaxed', 'Quiet', 'Sassy'):
            return 0.9
        else:
            return 1.0
    else:
        return 1.0
        
        
# Pika = Mon(1,25,'Pikachu','Electric','None',320,35,55,40,50,50,90,1,True,True)

# TeamPika = Team_Mon(Pika, 'M', 'Light Ball', 'Lightning Rod', 'Volt Tackle', 'Protect', 'Fake Out', 'Iron Tail', 4, 252, 0, 0, 0, 252, 31,31,31,31,31,31, 'Jolly', True)

# BattlePika = Battle_Mon(TeamPika)

# print(BattlePika.HP)

# BattlePika.calc_stats()

# print(BattlePika.HP)
# print(BattlePika.ATK)
# print(BattlePika.DEF)
# print(BattlePika.SPATK)
# print(BattlePika.SPDEF)
# print(BattlePika.SPD)

class Player:
    def __init__(self, ID, Name, Mon1, Mon2, Mon3, Mon4, Mon5, Mon6):
        self.ID = ID
        self.Name = Name
        self.Mon1 = Mon1
        self.Mon2 = Mon2
        self.Mon3 = Mon3
        self.Mon4 = Mon4
        self.Mon5 = Mon5
        self.Mon6 = Mon6
    
    def GetMon(self):
        return [Mon1, Mon2, Mon3, Mon4, Mon5, Mon6]

class Battle_Player(Player):
    def __init__(self, *args):
        self.__dict__ = args[0].__dict__.copy()
        self.LeftMon = self.Mon1
        self.RightMon = self.Mon2
        self.PartyMon1 = self.Mon1
        self.PartyMon2 = self.Mon2
        self.PartyMon3 = self.Mon3
        self.PartyMon4 = self.Mon4
    
    def GetTeam(self):
        return [self.PartyMon1, self.PartyMon2, self.PartyMon3, self.PartyMon4]
    
    def GetActive(self):
        if not self.LeftMon:
            return [self.RightMon]
        elif not self.RightMon:
            return [self.LeftMon]
        else:
            [self.LeftMon, self.RightMon]

class Move:
    def __init__(self, ID, Name, BasePower, BaseAcc, CantMiss, Priority, Category, Type
                , MaxPP, TargetSpread, IsContact, CanSnatch, CanMagicCoat, CanMirrorMove
                , IsSound, IsFlyingPress):
        self.ID = ID
        self.Name = Name
        self.BasePower = BasePower
        self.BaseAcc = BaseAcc
        self.CantMiss = CantMiss
        self.Priority = Priority
        self.Category = Category
        self.Type = Type
        self.MaxPP = MaxPP
        self.TargetSpread = TargetSpread
        self.IsContact = IsContact
        self.CanSnatch = CanSnatch
        self.CanMagicCoat = CanMagicCoat
        self.CanMirrorMove = CanMirrorMove
        self.IsSound = IsSound
        self.IsFlyingPress = IsFlyingPress

def GetTypeMult(Move,Target,IsFlyingPress=False):
    mult = 1.0
    typelist = [Target.Type1, Target.Type2]
    for i in typelist:
        if i == 'Fire':
            if Move in ('Ground', 'Rock', 'Water'):
                mult = mult * 2
            elif Move in ('Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel'):
                mult = mult * 0.5
        elif i == 'Bug':
            if Move in ('Fire', 'Flying', 'Rock'):
                mult = mult * 2
            elif Move in ('Fighting', 'Grass', 'Ground'):
                mult = mult * 0.5
        elif i == 'Electric':
            if Move in ('Ground'):
                mult = mult * 2
            elif Move in ('Electric', 'Flying', 'Steel'):
                mult = mult * 0.5
        elif i == 'Grass':
            if Move in ('Bug', 'Fire', 'Flying', 'Ice', 'Poison'):
                mult = mult * 2
            elif Move in ('Electric','Grass','Ground','Water'):
                mult = mult * 0.5
        elif i == 'Normal':
            if Move in ('Fighting'):
                mult = mult * 2
            elif Move in ('Ghost'):
                mult = mult * 0
        elif i == 'Rock':
            if Move in ('Fighting', 'Grass', 'Ground', 'Steel', 'Water'):
                mult = mult * 2
            elif Move in ('Fire', 'Flying', 'Normal', 'Poison'):
                mult = mult * 0.5
        elif i == 'Dark':
            if Move in ('Bug', 'Fighting', 'Fairy'):
                mult = mult * 2
            elif Move in ('Dark', 'Ghost'):
                mult = mult * 0.5
            elif Move in ('Psychic'):
                mult = mult * 0
        elif i == 'Fairy':
            if Move in ('Poison', 'Steel'):
                mult = mult * 2
            elif Move in ('Bug', 'Dark', 'Fighting'):
                mult = mult * 0.5
            elif Move in ('Dragon'):
                mult = mult * 0
        elif i == 'Flying':
            if Move in ('Electric', 'Ice', 'Rock'):
                mult = mult * 2
            elif Move in ('Bug', 'Fighting', 'Grass'):
                mult = mult * 0.5
            elif Move in ('Ground'):
                mult = mult * 0
        elif i == 'Ground':
            if Move in ('Grass', 'Ice', 'Water'):
                mult = mult * 2
            elif Move in ('Poison', 'Rock'):
                mult = mult * 0.5
            elif Move in ('Electric'):
                mult = mult * 0
        elif i == 'Poison':
            if Move in ('Ground', 'Psychic'):
                mult = mult * 2
            elif Move in ('Bug', 'Fairy', 'Fighting', 'Grass', 'Poison'):
                mult = mult * 0.5
        elif i == 'Steel':
            if Move in ('Fighting', 'Fire', 'Ground'):
                mult = mult * 2
            elif Move in ('Bug', 'Dragon', 'Fairy', 'Flying', 'Grass', 'Ice'
                         , 'Normal', 'Psychic', 'Rock', 'Steel'):
                mult = mult * 0.5
            elif Move in ('Poison'):
                mult = mult * 0
        elif i == 'Dragon':
            if Move in ('Dragon', 'Ice', 'Fairy'):
                mult = mult * 2
            elif Move in ('Electric', 'Fire', 'Grass', 'Water'):
                mult = mult * 0.5
        elif i == 'Fighting':
            if Move in ('Fairy', 'Flying', 'Psychic'):
                mult = mult * 2
            elif Move in ('Bug', 'Dark', 'Rock'):
                mult = mult * 2
        elif i == 'Ghost':
            if Move in ('Ghost', 'Dark'):
                mult = mult * 2
            elif Move in ('Bug', 'Poison'):
                mult = mult * 0.5
            elif Move in ('Normal', 'Fighting'):
                mult = mult * 0
        elif i == 'Ice':
            if Move in ('Fighting', 'Fire', 'Rock', 'Steel'):
                mult = mult * 2
            elif Move in ('Ice'):
                mult = mult * 0.5
        elif i == 'Psychic':
            if Move in ('Bug', 'Dark', 'Ghost'):
                mult = mult * 2
            elif Move in ('Psychic', 'Fighting'):
                mult = mult * 0.5
        elif i == 'Water':
            if Move in ('Eletric', 'Grass'):
                mult = mult * 2
            elif Move in ('Fire', 'Ice', 'Steel', 'Water'):
                mult = mult * 0.5
    if IsFlyingPress:
        return mult * GetTypeMult('Flying', Target, False)
    else:
        return mult