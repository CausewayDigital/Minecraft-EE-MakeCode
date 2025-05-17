### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Autominer

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

In Minecraft, there are many vast lakes or oceans to traverse. Following the program flowchart below, create a Python program that:

- Check if player is walking above water.
- If player is walking above water, turn the block below to ice.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)

## Part 1
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Part_1.png)

Code the flowchart.

```python
def on_move():
```

Create a function that is called when the player moves.

## Part 2
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Part_2.png)

Code the flowchart.

```python
```
Get the coordinates of the block bellow the player.

## Part 3
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Part_3.png)

Code the flowchart.

```python
```
If the block bellow the player is water, replace it with ice.


```ghost
def on_move():
    pos_bellow = positions.add(player.position(), pos(0, 0, -1))
    if blocks.test_for_block(WATER, pos_bellow):
        blocks.place(ICE, pos_bellow)

player.on_travelled(WALK, on_move)
```
