def DamageCalc(Move, User, Target, Power, Player, TargetPlayer, Field, IsSpread, IsCritical):
    modifier = 1
    basepower = Power
    # Get effective ATK stat from User
    effatk = 1
    if effatk < 1:
        effatk = 1
    # Get effective DEF stat from Target
    effdef = 1
    if effdef < 1:
        effdef = 1
    # Get Weather/Terrain from Field
    if Field.Weather == 'Harsh Sunlight':
        pass
    elif Field.Weather == 'Rain':
        pass
    elif Field.Weather == 'Extremely Harsh Sunlight':
        pass
    elif Field.Weather == 'Heavy Rain':
        pass
    elif Field.Weather == 'Sandstorm':
        pass
    elif Field.Weather == 'Hail':
        pass
    elif Field.Weather == 'Strong Winds':
        pass

    if Field.Terrain == 'Psychic':
        pass
    elif Field.Terrain == 'Grassy':
        pass
    elif Field.Terrain == 'Misty':
        pass
    elif Field.Terrain == 'Electric':
        pass

    # Get Critical
    if IsCritical:
        if User.Ability == 'Sniper':
            modifier = modifier * 2.25
        else:
            modifier = modifier * 1.5
    
    # Determine Move's Type, User's Type
    movetype = Move.Type
    usertype = [User.Type1, User.Type2]
    targettype = [Target.Type1, Target.Type2]
    ### Add in logic for Soak/ForestCurse/TrickOrTreat/MagicPowder/Electrify/IonDeluge/Normalize/Pixilate, etc

    # STAB
    if movetype in usertype:
        modifier = modifier * 1.5

    # Type Effectiveness

    modifier = modifier * GetTypeMult(movetype, targettype, Move.Name == 'Flying Press')

    # Check for Burn/Guts/Facade
    
    if User.Status == 'Burn':
        if Move.Category == 'Physical':
            if User.Ability != 'Guts': # Guts boost applies below
                if Move.Name != 'Facade': # Facade boost from Move Class
                    modifier = modifier * 0.5
         
    # Screens
    if User.Ability != 'Infiltrator':
        if 'Light Screen' in TargetPlayer.FieldEffs or 'Aurora Veil' in TargetPlayer.FieldEffs:
            if Move.Category == 'Special':
                if IsSpread:
                    modifier = modifier * 0.66
                else:
                    modifier = modifier * 0.5

        elif 'Reflect' in TargetPlayer.FieldEffs or 'Aurora Veil' in TargetPlayer.FieldEffs:
            if Move.Category == 'Physical':
                if IsSpread:
                    modifier = modifier * 0.66
                else:
                    modifier = modifier * 0.5

    # Ability Modifiers

    # Item Modifiers

    # Generate random int between 85-100 incl, / 100
    modifier = modifier * (random.randint(85,100) / 100)

    # Generate Spread Calc

    # Multiply it all together
    damage = ((22 * basepower * effatk / effdef) / 50 + 2) * modifier 
    return damage