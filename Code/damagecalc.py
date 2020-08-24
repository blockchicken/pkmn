def DamageCalc(Move, User, Target, Power, Player, TargetPlayer, Field, IsSpread, IsCritical):
    modifier = 1
    basepower = Power

    # Get effective ATK/DEF stat from User
    
    if Move.Category == 'Physical':
    	effatk = User.ATK * StageCalc('ATK',User.ATKStage,Target.Ability == 'Unaware')
    	effdef = Target.DEF * StageCalc('DEF',Target.DEFStage,User.Ability == 'Unaware')
    if Move.Category == 'Special':
    	effatk = User.SPATK * StageCalc('SPATK',User.SPATKStage,Target.Ability == 'Unaware')
    	effdef = Target.SPDEF * StageCalc('SPDEF',Target.SPDEFStage,User.Ability == 'Unaware')

    if Move.Name == 'Body Press':
    	effatk = User.DEF * StageCalc('DEF',User.DEFStage) # Need to check Unaware

    if Move.Name == 'Darkest Lariat':
    	effdef = Target.DEF 

    # Just make sure nothing breaks 
    if effatk < 1:
        effatk = 1
    if effdef < 1:
        effdef = 1

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
    ### Add in logic for Soak/ForestCurse/TrickOrTreat/MagicPowder/Electrify/IonDeluge, etc

    # STAB

    if movetype in usertype:
    	if User.Ability == 'Adapability':
    		modifier = modifier * 2
    	else:
    		modifier = modifier * 1.5

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

    # Minimize Nonsense + Dig/Fly/Dive Nonsense
    #### Literally no one knows that these are a thing, even pro VGC players
    ###### The Accuracy bypass will be in a separate check

    if Target.IsMinimized: # I was really tempted to just call this 'IsSmol'
    	if Move.Name in ('Body Slam', 'Dragon Rush', 'Flying Press', 'Heat Crash'
    					, 'Heavy Slam', 'Malicious Moonsault', 'Steamroller', 'Stomp'):
    		modifier = modifier * 2

    if Target.IsUnderground:
    	if Move.Name in ('Magnitude', 'Earthquake'):
    		modifier = modifier * 2

    if Target.IsUnderwater:
    	if Move.Name in ('Whirlpool', 'Surf'):
    		modifier = modifier * 2

    if Target.IsInAir:
    	if Move.Name in ('Gust', 'Twister'):
    		modifier = modifier * 2

    # Ability Modifiers

    ### Aerilate

    if User.Ability == 'Aerilate':
    	if movetype == 'Normal':
    		movetype = 'Flying'
    		modifier = modifier * 1.2

    ### Analytic

    ### Battery

    ### Blaze

    ### Dry Skin

    if Target.Ability == 'Dry Skin':
    	if movetype == 'Fire':
    		modifier = modifier * 1.25

    ### Fluffy

    if Target.Ability == 'Fluffy':
    	if movetype == 'Fire':
    		modifier = modifier * 2
    	if Move.IsContact and User.Ability != 'Long Reach':
    		modifier = modifier * 0.5

    ### Fur Coat

    if Target.Ability == 'Fur Coat':
    	if Move.Category == 'Physical':
    		modifier = modifier * 0.5

    ### Normalize

    if User.Ability == 'Normalize':
    	movetype = 'Normal'

    ### Sheer Force

    if User.Ability == 'Sheer Force':
    	if Move.EffSheerForce:
    		modifier = modifier * 1.3

    ### Water Bubble

    if User.Ability == 'Water Bubble':
    	if movetype == 'Water':
    		basepower = basepower * 2

    if Target.Ability == 'Water Bubble':
    	if movetype == 'Fire':
    		modifier = modifier * 0.5

    # Item Modifiers

    # Other Modifiers

    if User.IsHelped:
    	modifier = modifier * 1.5

    # Generate random int between 85-100 incl, / 100
    modifier = modifier * (random.randint(85,100) / 100)

    # Generate Spread Calc

	# Type Effectiveness

    modifier = modifier * GetTypeMult(movetype, targettype, Move.Name == 'Flying Press')

    # Get Weather/Terrain from Field
    if Field.Weather == 'Harsh Sunlight':
        if movetype == 'Fire':
        	modifier = modifier * 1.5
        if movetype == 'Water':
        	modifier = modifier * 0.5

    elif Field.Weather == 'Rain':
        if movetype == 'Water':
        	modifier = modifier * 1.5
        if movetype == 'Fire':
        	modifier = modifier * 0.5
        if Move.Name in ('Solar Beam', 'Solar Blade'):
        	basepower = basepower * 0.5

    elif Field.Weather == 'Extremely Harsh Sunlight':
        pass
    elif Field.Weather == 'Heavy Rain':
        pass
    elif Field.Weather == 'Sandstorm':
        pass
    elif Field.Weather == 'Hail':
        pass
    elif Field.Weather == 'Strong Winds':
    	if 'Flying' in targettype:
        	if movetype in ('Electric', 'Ice', 'Rock'):
        		modifier = modifier * 0.5

    if Field.Terrain == 'Psychic':
        pass
    elif Field.Terrain == 'Grassy':
        pass
    elif Field.Terrain == 'Misty':
        pass
    elif Field.Terrain == 'Electric':
        pass


    # Multiply it all together
    damage = ((22 * basepower * effatk / effdef) / 50 + 2) * modifier 
    return damage