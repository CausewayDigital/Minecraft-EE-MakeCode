### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Tower Builder

```customts
agent.teleport(world(-517, 139, 712), WEST)
let agent_or = agent.getOrientation()
if (agent_or == EAST) {
    agent.turnLeft()
    agent.turnLeft()
}

if (agent_or == SOUTH) {
    agent.turnRight()
}

if (agent_or == EAST) {
    agent.turnLeft()
}
```

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart.png)

As an explorer, you need to be able to trace your steps to return to your base. Create a Python program that uses your agent to:

- Build a 3x3x3 tower out of stone.
- Places a glowstone block at the top of the tower.

## Part 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_1.png)

Code the flowchart.

```python
agent.set_item(STONE, 64, 1)
```

- Give 64 stone to your agent
- Give 64 glowstone to your agent

## Part 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_2.png)

Code the flowchart.

```
```
- Create a for loop that **loops 3 times**

## Part 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_3.png)

Code the flowchart.

```
```
Within the loop:
- Move the agent up
- Create a new loop

## Part 4

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_4.png)

Code the flowchart (within the loop you just created).

```
```
Within the new loop:
- Place stone bellow the agent
- Move the agent forward
- Place stone bellow the agent
- Move the agent forward
- Turn the agent right

## Part 5

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_5.png)

Code the flowchart (After all the loops).

```
```

- Move your agent to the right
- Place glowstone forwards

```ghost
agent.set_item(STONE, 64, 1)
agent.set_item(GLOWSTONE, 1, 2)
agent.set_slot(1)

for i in range(3):
    agent.move(UP, 1)
    for j in range(4):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.turn_right()

agent.set_slot(2)
agent.move(RIGHT, 1)
agent.place(FORWARD)
```
