### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Ice Walker

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

In Minecraft, there are many vast lakes or oceans to traverse. Following the program flowchart below, create a Python program that:

- Check if player is walking above water.
- If player is walking above water, turn the block below to ice.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)

## Part 1
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/flowchart-landscape_1.png)

Code the flowchart.

```python
def on_move():
```

Create a function that is called when the player moves.

## Part 2
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/flowchart-landscape_2.png)

Code the flowchart.

```python
```
If the block below the player is water, replace it with ice.


```ghost
def on_move():
    pos_below = positions.add(player.position(), pos(0, -1, 0))
    if blocks.test_for_block(WATER, pos_below):
        blocks.place(ICE, pos_below)

player.on_travelled(WALK, on_move)
```

```ghost
def on_move():
    pos_below = positions.add(player.position(), pos(0, -1, 0))
    for i in range(-1, 1):
        for j in range(-1, 1):
            if blocks.test_for_block(WATER, positions.add(pos_below, pos(i, 0, j))):
                blocks.place(ICE, positions.add(pos_below, pos(i, 0, j)))

player.on_travelled(WALK, on_move)
```
