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
mobs.spawn(COW, player.position())
```
- Spawn a cow

## Create the Spawner - 2

![Flow chart of task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/animal_pens/images/flowchart-landscape_2.png)

Now finish it off...

```
```
- Spawn a pig
- Spawn a sheep

## Extension @showdialogue

Here's some ideas to add to your Animal Spawner:

- Spawn in random selection of animals into the pens.
- Try to use a `||loops:for||` loop to spawn in all the animals to each location.
- Try and create an animal pen with fences to keep the animals in.

```ghost
import random

blocks.place(OAK_FENCE, player.position())

pos = positions.add(pos(0, 0, 0), pos(0, 0, 0))

pos_2 = world(0, 0, 0)
pos_3 = pos(0, 0, 0)


for i in range(3):
    rand_num = random.randint(1, 10)
    for i in range(rand_num):
        mobs.spawn(COW, player.position())
        
```