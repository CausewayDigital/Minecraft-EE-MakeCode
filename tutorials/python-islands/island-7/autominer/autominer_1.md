### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Autominer

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

Have the agent create a mineshaft for you to work in. Following the program flowchart below, create a Python program that uses your agent to:
Mine a tunnel 2 blocks tall in front of it.
Checks if there's air, water or lava below itself, if so
Place a block below

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/Flowchart.png)

## Part 1
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/Part_1.png)

Code the flowchart.

```python
```
Give your agent 64 stone.

## Part 2
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/Part_2.png)

Code the flowchart.

```
```
Create a for loop that iterates from 0 to 19.

## Part 3
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/Part_3.png)

Code the flowchart.

```
```
Within the loop; destroy the block in front of the agent, move the agent forward one block, then destroy the block above the agent.


## Part 4
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/autominer/images/Part_4.png)

Code the flowchart.

```
```
If the block below the agent is lava, water, or air, place a stone block below the agent.


```ghost
agent.set_item(STONE, 64, 1)
agent.set_slot(1)

for i in range(19):
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    agent.destroy(UP)

    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block in [LAVA, WATER, AIR]:
        agent.place(DOWN)
```
