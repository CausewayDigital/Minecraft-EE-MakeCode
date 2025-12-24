### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0
### @explicitHints true

# Ice Walker

```customts
const LAKE_WATER = 9
```

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

In Minecraft, there are many vast lakes or oceans to traverse. Following the program flowchart below, create a Python program that:

- Loops continuously.
- Changes the blocks surrounding the player from LAKE_WATER to ICE.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)


## Ice Walker

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)

You should also set the blocks around the player to ICE. (Not just the block below).
You should use positions relative to yourself using `||positions:pos||`.

**Note: You need to create a box around your feet of ice (-1 and 1 coordinates). You will need to change the pair of coordinates in the replace method (more details in the hint).**

### ~ tutorialhint
**Tips**
- Watch out! The replace method expects the new block (ICE), then the old block (LAKE_WATER).
- Unsure about the coordinates to use? Check the below diagram.
![Player coords](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/player_coords.jpg)

**Starter code**
```python
def on_forever():
    # Your code here
    pass
loops.forever(on_forever)
```



```ghost
def on_forever():
    blocks.replace(ICE,
        blocks.block_by_id(LAKE_WATER),
        pos_camera(-1, -1, -1),
        pos_camera(1, -1, 1))
loops.forever(on_forever)
```
