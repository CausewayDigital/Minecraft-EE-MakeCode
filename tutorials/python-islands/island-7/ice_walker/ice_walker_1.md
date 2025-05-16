
### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Autominer

```customts
namespace player {
    export function testBlockBellow(block: Block): boolean {
        let player_pos = player.position();
        let pos_bellow = positions.add(player_pos, pos(0, 0, -1));
        return blocks.testForBlock(block, pos_bellow);
    }
}
```

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

In Minecraft, there are many vast lakes or oceans to traverse. Following the program flowchart below, create a Python program that:

- Check if player is walking above water.
- If player is walking above water, turn the block below to ice.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/ice_walker/images/Flowchart.png)

## Part 1

Code the flowchart.

```python
```
