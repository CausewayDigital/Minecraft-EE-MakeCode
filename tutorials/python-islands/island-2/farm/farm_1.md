### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Farm

```template

```

# Carrot and Wheat Checking @showdialog
Help remove the carrots from the wheat farm!
Peter had some of his wheat and carrot seeds mixed up while planting them. As your agent can detect **any** block, it can be programmed to check the seeds. Let's get started!
![Cover image of Peter](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/farm/PeterCover.png)

## Introduction @showdialog

Peter has two special functions you can use to mark the seeds:

- `accept()`: Marks a wheat seed below.

- `deny()`: Marks a carrot seed below.



## Move Your Agent @showdialog

To start, we will need to move our agent forward 3 blocks, to the first seed marked by the white marker in the world.   

In case you need a refresher, 

```python
agent.move(DIRECTION)
```

Directions available are FORWARD, BACK, LEFT, RIGHT, UP and DOWN.

## Move Your Agent

Now move your agent forward 3 blocks to the first seed marked by the white marker.

```python
agent.move(DIRECTION)
```

Directions available are FORWARD, BACK, LEFT, RIGHT, UP and DOWN.

*************
```Python
def accept():
    agent.place(UP, 1)
def deny():
    agent.place(UP, 2)

# Start of user code
agent.move(     ) 



# Complete the code above You will need multiple lines of code.   
```
*************


## Inspect Blocks With Your Agent @showdialog
Now that your agent is above some seeds. Let's inspect what seeds they are! Your agent can inspect blocks using `||agent:agent.inspect||`:


Here's how it works...

```python
agent.inspect(AgentInspection.BLOCK, DIRECTION)
```

- `DIRECTION`: The direction you want your agent to inspect. The directions are UP, DOWN, LEFT, RIGHT, FORWARD and BACK.

## Inspect Blocks With Your Agent
Make the agent inspect down, and say the value stored in `block`!

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
```
**********************
### *User Code* 
```Python
def accept():
    agent.place(UP, 1)
def deny():
    agent.place(UP, 2)

# Start of user code
block = agent.inspect(     )
# Complete the code above


# Add a say above, saying the value of 'block'
```
************************
