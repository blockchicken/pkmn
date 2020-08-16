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
