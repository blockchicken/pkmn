''' 

Turn 0: Send out Pokemon

Begin overall loop: 
Turn order:

- Inputs

- Get current priority list (purely speeds, for switches,abilities)

for each action in list: loop:
- Switch Pokemon

- Upon Switch actions
-- Abilities
-- Items
once all switches complete, end loop

- Initial Priority Sorted List

- Execute Moves
--- Check if able to use a move
--- Figure out Targets
--- Check for Immunities from type/abilities/items/weather
----> If so apply
--- Accuracy check
----> Upon miss actions
--- Determine Crit Role
(Loop: Multi Hit moves + crits)
--- Perform damage check
--- Check for Item Usage/Ability after damage
--- Check for fainting/Sub popping
(end loop)
--- Apply effects of moves
--- Remove fainted pokemon from field
----> Remove from Priority Sort
--- Check for victory -> Exit if so
--- Deduct PP
--- Assign "Last Used Move", "Last Damage Dealt", "Last Damage Received" etc
--- Recalc Priority List (Aka dynamic speed)
----> If List not empty, do next move in list

- Check for victory -> Exit

- Get new priority list (pure speeds, for weather etc)

- End of turn abilities

-> Victory Check

- End of turn effects/items/weather/terrain

-> Victory Check

- Select Switches for fainted mon

- Send in mon (need to figure out order if both sides)

- Upon Switch Abilities/Items

- Reset all turn-based flags

Repeat overall loop

'''
