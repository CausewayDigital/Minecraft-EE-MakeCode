### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Animal Pen

## Introduction @showdialogue

In this exercise, you will build a program in Python that follows the flowchart below:

![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart.png)

## Create the Spawner - 1

![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart-landscape_1.png)

Start by creating this first bit. Use the hint if you need help.

```python
for i in range(5):
    mobs.spawn(COW, player.position())
```

## Create the Spawner - 2

![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart-landscape_1.png)

Now finish it off...

## Extension @showdialogue

Here's some ideas to add to your Animal Spawner:

- Spawn in random selection of animals into the pens.
- Try to use a `||loops:for||` loop to spawn in all the animals to each location.   
- Try and create an animal pen with fences to keep the animals in.   
