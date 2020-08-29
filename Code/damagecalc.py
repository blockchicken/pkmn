def DamageCalc(Move, User, Target, Power, Player, TargetPlayer, Field, IsSpread, IsCritical):
    modifier = 1
    basepower = Power

    # Get effective ATK/DEF stat from User
    
    if Move.Category == 'Physical':
    	effatk = User.ATK * StageCalc('ATK',User.ATKStage,IsCritical,Target.Ability == 'Unaware')
   		effdef = Target.DEF * StageCalc('DEF',Target.DEFStage,IsCritical,User.Ability == 'Unaware')
    
    if Move.Category == 'Special':
    	effatk = User.SPATK * StageCalc('SPATK',User.SPATKStage,IsCritical,Target.Ability == 'Unaware')
   		effdef = Target.SPDEF * StageCalc('SPDEF',Target.SPDEFStage,IsCritical,User.Ability == 'Unaware')

    if Move.Name == 'Body Press':
    	effatk = User.DEF * StageCalc('ATK',User.DEFStage,IsCritical,Target.Ability == 'Unaware')

    if Move.Name in ('Darkest Lariat', 'Sacred Sword'):
    	effdef = Target.DEF 

    if Move.Name in ('Psyshock', 'Psystrike', 'Secret Sword'):
    	effdef = Target.DEF * StageCalc('DEF',Target.DEFStage,IsCritical,User.Ability == 'Unaware')

    ### Photon Geyser 
    if Move.Name == 'Photon Geyser':
    	pass

    ### Shell Side Arm
    if Move.Name == 'Shell Side Arm':
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
    
    ### Soak
    if User.IsSoaked:
    	usertype = ['Water']
    if Target.IsSoaked:
    	targettype = ['Water']

    ### Magic Powder
    if User.IsMagicPowdered:
    	usertype = ['Psychic']
    if Target.IsMagicPowdered:
    	targettype = ['Psychic']

    ### Forest Curse
    if User.IsForestCurse and 'Grass' not in usertype:
    	usertype.append('Grass')
    if Target.IsForestCurse and 'Grass' not in targettype:
    	targettype.append('Grass')	

    ### Trick-or-Treat
    if User.IsTrickOrTreat and 'Ghost' not in usertype:
    	usertype.append('Ghost')
    if Target.IsTrickOrTreat and 'Ghost' not in targettype:
    	targettype.append('Ghost')	

    ### Add in logic for Electrify/IonDeluge, etc

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

    ### Techno Blast

    if Move.Name == 'Techno Blast':
        if User.Item == 'Douse Drive':
            movetype = 'Water'
        elif User.Item == 'Burn Drive':
            movetype = 'Fire'
        elif User.Item == 'Chill Drive':
            movetype = 'Ice'
        elif User.Item == 'Shock Drive':
            movetype = 'Electric'

    # Ability Modifiers

    ### Aerilate/Galvanize/Refrigerate/Pixilate

    if User.Ability == 'Aerilate':
    	if movetype == 'Normal':
    		movetype = 'Flying'
    		basepower = basepower * 1.2

    if User.Ability == 'Galvanize':
        if movetype == 'Normal':
            movetype = 'Electric'
            basepower = basepower * 1.2

    if User.Ability == 'Refrigerate':
        if movetype == 'Normal':
            movetype = 'Ice'
            basepower = basepower * 1.2

    if User.Ability == 'Pixilate':
        if movetype == 'Normal':
            movetype = 'Fairy'
            basepower = basepower * 1.2

    ### Analytic

    if User.Ability == 'Analytic':
    	#if moving last
    	modifier = modifier * 1.3

    ### Aura Break/Dark Aura/Fairy Aura

    if Player.LeftMon.Ability == 'Fairy Aura' or Player.RightMon.Ability == 'Fairy Aura' or TargetPlayer.LeftMon.Ability == 'Fairy Aura' or TargetPlayer.RightMon.Ability == 'Fairy Aura':
    	if Player.LeftMon.Ability == 'Aura Break' or Player.RightMon.Ability == 'Aura Break' or TargetPlayer.LeftMon.Ability == 'Aura Break' or TargetPlayer.RightMon.Ability == 'Aura Break':
    		if movetype == 'Fairy':
    			modifier = modifier / 1.33
    	else:
    		if movetype == 'Fairy':
    			modifier = modifier * 1.33
  
    if Player.LeftMon.Ability == 'Dark Aura' or Player.RightMon.Ability == 'Dark Aura' or TargetPlayer.LeftMon.Ability == 'Dark Aura' or TargetPlayer.RightMon.Ability == 'Dark Aura':
    	if Player.LeftMon.Ability == 'Aura Break' or Player.RightMon.Ability == 'Aura Break' or TargetPlayer.LeftMon.Ability == 'Aura Break' or TargetPlayer.RightMon.Ability == 'Aura Break':
    		if movetype == 'Dark':
    			modifier = modifier / 1.33
    	else:
    		if movetype == 'Dark':
    			modifier = modifier * 1.33     

    ### Battery

    if Player.LeftMon.Ability == 'Battery' and Player.RightMon.Name == User.Name:
    	if Move.Category == 'Special':
    		modifier = modifier * 1.3
    elif Player.RightMon.Ability == 'Battery' and Player.LeftMon.Name == User.Name:
    	if Move.Category == 'Special':
    		modifier = modifier * 1.3

    ### Blaze/Overgrow/Swarm/Torrent
    if User.Ability == 'Blaze':
        if movetype == 'Fire' and (3 * User.CurrentHP) <= (User.HP):
        	modifier = modifier * 1.5
    
    if User.Ability == 'Overgrow'
        if movetype == 'Grass' and (3 * User.CurrentHP) <= (User.HP):
            modifier = modifier * 1.5

    if User.Ability == 'Swarm'
        if movetype == 'Bug' and (3 * User.CurrentHP) <= (User.HP):
            modifier = modifier * 1.5

    if User.Ability == 'Torrent'
        if movetype == 'Water' and (3 * User.CurrentHP) <= (User.HP):
            modifier = modifier * 1.5

    ### Dry Skin

    if Target.Ability == 'Dry Skin':
    	if movetype == 'Fire':
    		modifier = modifier * 1.25

    ### Filter/Solid Rock/Prism Armor
    if Target.Ability in ('Filter','Solid Rock','Prism Armor'):
        if GetTypeMult(movetype, targettype, Move.Name == 'Flying Press') > 1:
    		modifier = modifier / 1.25

    ### Flare Boost
    if User.Ability == 'Flare Boost' and User.Status = 'Burn':
    	if Move.Category == 'Special':
    		basepower = basepower * 1.5

    ### Flower Gift
    if Field.Weather in ('Harsh Sunlight', 'Extremely Harsh Sunlight'):
	    if Player.RightMon.Ability == 'Flower Gift' or Player.LeftMon.Ability == 'Flower Gift':
	    	

    ### Fluffy

    if Target.Ability == 'Fluffy':
    	if movetype == 'Fire':
    		modifier = modifier * 2
    	if Move.IsContact and User.Ability != 'Long Reach':
    		modifier = modifier * 0.5

    ### Friend Guard

    if TargetPlayer.LeftMon.Ability == 'Friend Guard' and TargetPlayer.RightMon.Name == Target.Name:
        modifier = modifier / 1.25
    elif TargetPlayer.RightMon.Ability == 'Friend Guard' and TargetPlayer.LeftMon.Name == Target.Name:
        modifier = modifier / 1.25

    ### Fur Coat

    if Target.Ability == 'Fur Coat':
    	if Move.Category == 'Physical':
    		modifier = modifier * 0.5

    ### Gorilla Tactics

    if User.Ability == 'Gorilla Tactics':
        if Move.Category == 'Physical':
            effatk = effatk * 1.5

    ### Grass Pelt

    if Target.Ability == 'Grass Pelt':
        if Move.Category == 'Physical':
            effdef = effdef * 1.5

    ### Heatproof

    if Target.Ability == 'Heatproof':
        if movetype == 'Fire':
            modifier = modifier * 0.5

    ### Huge Power/ Pure Power

    if User.Ability in ('Huge Power', 'Pure Power'):
        if Move.Category == 'Physical':
            effatk = effatk * 2

    ### Hustle

    if User.Ability == 'Hustle':
        if Move.Category == 'Physical':
            effatk = effatk * 1.5

    ### Ice Scales

    if Target.Ability == 'Ice Scales':
        if Move.Category == 'Special':
            modifier = modifier * 0.5

    ### Iron Fist

    if User.Ability == 'Iron Fist':
        if Move.IsPunch:
            basepower = basepower * 1.2

    ### Liquid Voice

    if User.Ability == 'Liquid Voice':
        if Move.IsSound:
            movetype = 'Water'

    ### Mega Launcher

    if User.Ability == 'Mega Launcher':
        if Move.Name in ('Aura Sphere', 'Dark Pulse', 'Dragon Pulse', 'Origin Pulse', 'Terrain Pulse', 'Water Pulse'):
           basepower = basepower * 1.5 

    ### Minus/Plus

    if Player.RightMon.Ability in ('Plus', 'Minus') and Player.LeftMon.Ability in ('Plus', 'Minus'):
        if Move.Category == 'Special':
            effatk = effatk * 1.5

    ### Multiscale/Shadow Shield

    if Target.Ability in ('Multiscale', 'Shadow Shield') and Target.CurrentHP == Target.HP:
        modifier = modifier * 0.5

    ### Neuroforce

    if User.Ability == 'Neuroforce':
        if GetTypeMult(movetype, targettype, Move.Name == 'Flying Press') > 1:
            modifier = modifier * 1.25

    ### Normalize

    if User.Ability == 'Normalize':
    	movetype = 'Normal'

    ### Rivalry

    if User.Ability == 'Rivalry':
    	if User.Gender == 'F' and Target.Gender == User.Gender:
    		basepower = basepower * 1.25
        if User.Gender == 'M' and Target.Gender == User.Gender:
            basepower = basepower * 1.25
    	elif User.Gender == 'M' and Target.Gender == 'F':
    		basepower = basepower * 0.75
    	elif User.Gender == 'F' and Target.Gender == 'M':
    		basepower = basepower * 0.75

    ### Power Spot

    if Player.LeftMon.Ability == 'Power Spot' and Player.RightMon.Name == User.Name:
        basepower = basepower * 1.3
    elif Player.RightMon.Ability == 'Power Spot' and Player.LeftMon.Name == User.Name:
        basepower = basepower * 1.3

    ### Punk Rock

    if User.Ability == 'Punk Rock':
        if Move.IsSound:
            basepower = basepower * 1.3

    if Target.Ability == 'Punk Rock':
        if Move.IsSound:
            modifier = modifier * 0.5

    ### Reckless

    if User.Ability == 'Reckless' and Move.Name in ('Brave Bird', 'Double Edge', 'Flare Blitz', 'Head Charge', 'Head Smash', 'High Jump Kick', 'Jump Kick', 'Light of Ruin', 'Submission', 'Take Down', 'Volt Tackle', 'Wood Hammer', 'Wild Charge'):
        basepower = basepower * 1.2

    ### Sand Force

    if User.Ability == 'Sand Force':
        if Field.Weather == 'Sandstorm':
            if movetype in ('Rock', 'Ground', 'Steel'):
                basepower = basepower * 1.3

    ### Slow Start

    if User.OtherEffs['Slow Start'] > 0:
        if Category == 'Physical':
            effatk = effatk * 0.5

    ### Sheer Force

    if User.Ability == 'Sheer Force':
    	if Move.EffSheerForce:
    		modifier = modifier * 1.3

    ### Solar Power

    if User.Ability == 'Solar Power':
        if Field.Weather in ('Harsh Sunlight', 'Extremely Harsh Sunlight'):
            if Move.Category == 'Special':
                effatk = effatk * 1.5

    ### Stakeout

    if User.Ability == 'Stakeout' and Target.TurnsOnField == 0:
        basepower = basepower * 2
    
    ### Steelworker

    if User.Ability == 'Steelworker':
        if movetype == 'Steel':
            basepower = basepower * 1.5

    ### Steely Spirit

    if Player.LeftMon.Ability == 'Steely Spirit' or Player.RightMon.Ability == 'Steely Spirit':
        if movetype == 'Steel':
            basepower = basepower * 1.5

    ### Strong Jaw

    if User.Ability == 'Strong Jaw' and Move.IsJaw:
        basepower = basepower * 1.5

    ### Technician

    if User.Ability == 'Technician':
        if Power <= 60:
            basepower = basepower * 1.5

    ### Tough Claws

    if User.Ability == 'Tough Claws' and Move.IsContact:
        basepower = basepower * 1.3

    ### Toxic Boost

    if User.Ability == 'Toxic Boost' and User.Status in ('Poison', 'Toxic'):
        if Move.Category == 'Physical':
            basepower = basepower * 1.5

    ### Water Bubble

    if User.Ability == 'Water Bubble':
    	if movetype == 'Water':
    		basepower = basepower * 2

    if Target.Ability == 'Water Bubble':
    	if movetype == 'Fire':
    		modifier = modifier * 0.5

    # Item Modifiers

    ### Adamant Orb

    if User.DexNo == 483 and User.Item == 'Adamant Orb':
    	if movetype in ('Dragon', 'Steel'):
    		basepower = basepower * 1.2

    ### Assault Vest

    if Target.Item == 'Assault Vest':
    	if Move.Category == 'Special' and Move.Name not in ('Psyshock','Psystrike','Sacred Sword'):
    		effdef = effdef * 1.5

    ### Black Belt/Fist Plate

    if User.Item in ('Black Belt', 'Fist Plate'):
    	if movetype == 'Fighting':
    		basepower = basepower * 1.2

    ### Black Glasses/Dread Plate

    if User.Item in ('Black Glasses', 'Dread Plate'):
    	if movetype == 'Dark':
    		basepower = basepower * 1.2

    ### Charcoal/Flame Plate

    if User.Item in ('Charcoal', 'Flame Plate'):
    	if movetype == 'Fire':
    		basepower = basepower * 1.2

    ### Choice Band

    if User.Item == 'Choice Band' and Move.Category == 'Physical' and not User.IsDynamaxed:
    	effatk = effatk * 1.5

    ### Choice Specs

    if User.Item == 'Choice Specs' and Move.Category == 'Special' and not User.IsDynamaxed:
    	effatk = effatk * 1.5

    ### Deep Sea Scale

    if Target.DexNo == 366 and Target.Item == 'Deep Sea Scale':
		if Move.Category == 'Special' and Move.Name not in ('Psyshock','Psystrike','Sacred Sword'):
    		effdef = effdef * 2

    ### Deep Sea Tooth

    if User.DexNo == 366 and User.Item == 'Deep Sea Tooth' and Move.Category == 'Special':
    	effatk = effatk * 2

    ### Dragon Fang/Draco Plate
    
    if User.Item in ('Dragon Fang', 'Draco Plate'):
    	if movetype == 'Dragon':
    		basepower = basepower * 1.2
    
    ### Eviolite

    if Target.Item == 'Eviolite' and Target.IsNFE:
    	effdef = effdef * 1.5

    ### Expert Belt

    if GetTypeMult(movetype, targettype, Move.Name == 'Flying Press') > 1:
    	modifier = modifier * 1.2

    ### Griseous Orb

    if User.DexNo == 487 and User.Item == 'Griseous Orb':
    	if movetype in ('Dragon', 'Ghost'):
    		basepower = basepower * 1.2

    ### Hard Stone/Stone Plate/Rock Incense
    
    if User.Item in ('Hard Stone', 'Stone Plate', 'Rock Incense'):
    	if movetype == 'Rock':
    		basepower = basepower * 1.2
    
    ### Life Orb

    if User.Item == 'Life Orb':
    	basepower = basepower * (5324/4096)

    ### Light Ball

	if User.DexNo == 25 and User.Item == 'Light Ball':
    	effatk = effatk * 2

    ### Lustrous Orb

    if User.DexNo == 484 and User.Item == 'Lustrous Orb':
    	if movetype in ('Dragon', 'Water'):
    		basepower = basepower * 1.2

    ### Magnet/Zap Plate
    
    if User.Item in ('Magnet', 'Zap Plate'):
    	if movetype == 'Electric':
    		basepower = basepower * 1.2
    
    ### Metal Coat/Iron Plate
    
    if User.Item in ('Metal Coat', 'Iron Plate'):
    	if movetype == 'Steel':
    		basepower = basepower * 1.2
    
    ### Metal Powder

    if Target.DexNo == 132 and Target.Item == 'Metal Powder':
    	### Note: Doesn't apply when Transformed, will need to add flag
    	### but Transform will likely be implemented much later anyway
    	if Move.Category == 'Physical' or Move.Name in ('Psyshock','Psystrike','Sacred Sword'):
    		effdef = effdef * 2

    ### Miracle Seed/Meadow Plate/Rose Incense
    
    if User.Item in ('Miracle Seed', 'Meadow Plate', 'Rose Incense'):
    	if movetype == 'Grass':
    		basepower = basepower * 1.2
    
    ### Muscle Band 
    
    if User.Item == 'Muscle Band' and Move.Category == 'Physical':
    	basepower = basepower * 1.1

    ### Mystic Water/Splash Plate/Sea Incense/Wave Incense
    
    if User.Item in ('Mystic Water', 'Splash Plate', 'Sea Incense', 'Wave Incense'):
    	if movetype == 'Water':
    		basepower = basepower * 1.2
    
    ### Never Melt Ice/Icicle Plate
    
    if User.Item in ('Never Melt Ice', 'Icicle Plate'):
    	if movetype == 'Ice':
    		basepower = basepower * 1.2
    
    ### Pixie Plate
    
    if User.Item in ('Pixie Plate'):
    	if movetype == 'Fairy':
    		basepower = basepower * 1.2
    
    ### Poison Barb/Toxic Plate
    
    if User.Item in ('Poison Barb', 'Toxic Plate'):
    	if movetype == 'Poison':
    		basepower = basepower * 1.2
    
    ### Sharp Beak/Sky Plate
    
    if User.Item in ('Sharp Beak', 'Sky Plate'):
    	if movetype == 'Flying':
    		basepower = basepower * 1.2
    
    ### Silk Scarf
    
    if User.Item in ('Silk Scarf'):
    	if movetype == 'Normal':
    		basepower = basepower * 1.2
    
    ### Silver Powder/Insect Plate
    
    if User.Item in ('Silver Powder', 'Insect Plate'):
    	if movetype == 'Bug':
    		basepower = basepower * 1.2
    
    ### Soft Sand/Earth Plate
    
    if User.Item in ('Soft Sand', 'Earth Plate'):
    	if movetype == 'Ground':
    		basepower = basepower * 1.2
    
    ### Soul Dew

    if User.DexNo in (380,381) and User.Item == 'Soul Dew':
    	if movetype in ('Dragon', 'Psychic'):
    		basepower = basepower * 1.2

    ### Spell Tag/Spooky Plate
    
    if User.Item in ('Spell Tag', 'Spooky Plate'):
    	if movetype == 'Ghost':
    		basepower = basepower * 1.2
    
    ### Thick Club

	if User.DexNo in (104,105) and User.Item == 'Thick Club' and Move.Category == 'Physical':
    	effatk = effatk * 2

    ### Twisted Spoon/Mind Plate/Odd Incense
    
    if User.Item in ('Twisted Spoon', 'Mind Plate', 'Odd Incense'):
    	if movetype == 'Psychic':
    		basepower = basepower * 1.2
    
    ### Wise Glasses

    if User.Item == 'Wise Glasses' and Move.Category == 'Special':
    	basepower = basepower * 1.1

    # Other Modifiers

    if User.IsHelped:
    	basepower = basepower * 1.5

    # Generate random int between 85-100 incl, / 100
    
    modifier = modifier * (random.randint(85,100) / 100)

    # STAB

    if movetype in usertype:
    	if User.Ability == 'Adapability':
    		modifier = modifier * 2
    	else:
    		modifier = modifier * 1.5

	# Type Effectiveness

    modifier = modifier * GetTypeMult(movetype, targettype, Move.Name == 'Flying Press')

    ### Weather
    
    if Player.LeftMon.Ability not in ('Air Lock','Cloud Nine') and Player.RightMon.Ability not in ('Air Lock','Cloud Nine') and TargetPlayer.LeftMon.Ability not in ('Air Lock','Cloud Nine') and TargetPlayer.RightMon.Ability not in ('Air Lock','Cloud Nine'):
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
	        if movetype == 'Fire':
	        	modifier = modifier * 1.5
	        if movetype == 'Water':
	        	modifier = modifier * 0

	    elif Field.Weather == 'Heavy Rain':
	        if movetype == 'Water':
	        	modifier = modifier * 1.5
	        if movetype == 'Fire':
	        	modifier = modifier * 0
	        if Move.Name in ('Solar Beam', 'Solar Blade'):
	        	basepower = basepower * 0.5

	    elif Field.Weather == 'Sandstorm':
	    	if 'Rock' in targettype:
	    		if Move.Category == 'Special' and Move.Name not in ('Psyshock','Psystrike','Sacred Sword'):
    				effdef = effdef * 1.5
    		if Move.Name in ('Solar Beam', 'Solar Blade'):
    			basepower = basepower * 0.5

	    elif Field.Weather == 'Hail':
	        if Move.Name in ('Solar Beam', 'Solar Blade'):
    			basepower = basepower * 0.5

	    elif Field.Weather == 'Strong Winds':
	    	if 'Flying' in targettype:
	        	if movetype in ('Electric', 'Ice', 'Rock'):
	        		modifier = modifier * 0.5

	### Terrains

    if Field.Terrain == 'Psychic':
    	if movetype == 'Psychic':
	        if 'Flying' not in usertype and User.Ability != 'Levitate' and not User.IsInAir:
	        	basepower = basepower * 1.3
    
    elif Field.Terrain == 'Grassy':
        if movetype == 'Grass':
	        if 'Flying' not in usertype and User.Ability != 'Levitate' and not User.IsInAir:
	        	basepower = basepower * 1.3
	    if Move.Name in ('Earthquake', 'Bulldoze', 'Magnitude') and not Target.IsUnderground:
	    	basepower = basepower * 0.5
    
    elif Field.Terrain == 'Misty':
        if movetype == 'Dragon':
        	if 'Flying' not in targettype and Target.Ability != 'Levitate' and not Target.IsInAir:
        		basepower = basepower * 0.5
    
    elif Field.Terrain == 'Electric':
        if movetype == 'Electric':
	        if 'Flying' not in usertype and User.Ability != 'Levitate' and not User.IsInAir:
	        	basepower = basepower * 1.3

    # Just make sure nothing breaks 
    
    if effatk < 1:
        effatk = 1
    if effdef < 1:
        effdef = 1

    # Multiply it all together
    
    damage = ((22 * basepower * effatk / effdef) / 50 + 2) * modifier 

    # Ensure 1 damage except when Immune
    
    if damage < 1 and modifier != 0:
    	damage = 1

    return damage