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

def GetTypeMult(Move,TypeList,IsFlyingPress=False):
    mult = 1.0
    typelist = TypeList
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

def MinusPP(Move,User):
    if User.Move1 == Move:
        User.MovePP1 -= 1
    elif User.Move2 == Move:
        User.MovePP2 -= 1
    elif User.Move3 == Move:
        User.MovePP3 -= 1
    elif User.Move4 == Move:
        User.MovePP4 -= 1

def StageCalc(Stat,Stage,Unaware = False):
    if Unaware == True:
        return 1
    if Stat in ('ATK', 'DEF', 'SPATK', 'SPDEF', 'SPD'):
        if Stage == 0:
            return 1
        elif Stage > 0:
            return (2 + Stage) / 2
        elif Stage < 0:
            return 2 / (2 + math.abs(Stage))
    if Stat in ('Acc', 'Eva'):
        if Stage == 0:
            return 1
        elif Stage > 0:
            return (3 + Stage) / 3
        elif Stage < 0:
            return 3 / (3 + math.abs(Stage))
    return 1
# def UseMove(User,Move,Target):
#     if Target = 'Self':
#     elif Target = 'None'
#     elif Target = 'Any Other'
#     elif Target = 'All Foe'
#     elif Target = 'All Other'
#     elif Target = 'User Side'
#     elif Target = 'Foe Side'
#     elif Target = 'Ally'
#     elif Target = 'Field'
#     elif Target = 'Random Foe'

def SelfMove(Move, User): #Swords Dance, Recover etc
    eval("'Use' + Move + '(' + User + ')'")
def FieldMove(Move, User): #TR, Weather
    eval("'Use' + Move + '(' + User + ')'")
def MultiTargetMove(Move, User, Player, TargetPlayer): #Surf, EQ
    eval("'Use' + Move + '(' + User + ',' + Player + ',' + TargetPlayer + ')'")
def FoeTargetMove(Move, User, TargetPlayer): #Gleam, HyperVoice
    eval("'Use' + Move + '(' + User + ',' + TargetPlayer + ')'")
def SideMove(Move, User, TargetPlayer): #Hazards, Tailwind etc
    eval("'Use' + Move + '(' + User + ',' + TargetPlayer + ')'")
def SingleTargetMove(Move, User, Target): #anything where you pick one target (exc self)
    eval("'Use' + Move + '(' + User + ',' + Target + ')'")
def AllyMove(Move, User, Player): #Helping Hand, Coaching
    eval("'Use' + Move + '(' + User + ',' + Player + ')'")
def RandMove(Move, User, TargetPlayer): #Outrage
    eval("'Use' + Move + '(' + User + ',' + TargetPlayer + ')'")
