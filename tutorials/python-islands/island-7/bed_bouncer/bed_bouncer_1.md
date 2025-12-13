### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Bed Bouncer

## Introduction @showdialog
Don't you love bouncing on a bed? Following the program flowchart below, create a Python program that:

- Check if player is bouncing above a bed, if so
    - Apply Levitation
    - Apply Regeneration

Follow the flowchart below:

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/Flowchart.png)

## Part 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/flowchart-landscape_1.png)

Code the black part of the flowchart. Stuck? Check the hint. Press *Next* to move onto the next step.

```python
```
Create a function that is called when the player `BOUNCE`'s.

## Part 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/flowchart-landscape_2.png)

Code the black part of the flowchart. Stuck? Check the hint. Press *Next* to move onto the next step.

```python
blocks.test_for_block(BED, player.position())
mobs.apply_effect(LEVITATION, mobs.target(NEAREST_PLAYER), 2, 1)
```

```ghost
def on_jump():
    if blocks.test_for_block(BED, player.position()):
        mobs.apply_effect(LEVITATION, mobs.target(NEAREST_PLAYER), 2, 1)2
        mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 3, 2)

player.on_travelled(BOUNCE, on_jump)
```

If the player is jumping on a bed, apply `LEVITATION` to the player.

See above for some useful code.

## Part 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/bed_bouncer/images/flowchart-landscape_3.png)

Code the black part of the flowchart. Stuck? Check the hint.

```python
```
Within the if statement, apply `REGENERATION` to the player.
