### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Factory
Repair the airship


## Repair the Hull @showdialog

![Airship Factory](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/factory/cover.jpg)

It looks like the crew at the airship factory need a hand repairing one of their new airships. Send your Agent in to fix the holes!


Before we get started, close this window and find your agent, it should be inside the airship.   

## Step 1
Now you have found your agent, let's move the agent forward by one block, to have it hover over the first hole for repair.

**Write the code to move your agent forward.**

```python
agent.move(FORWARD, 1)
```

## Step 2
Now with the agent in place, we'll need to move the agent down to the bottom of the docks to collect the fallen blocks below.   

To do this, we will use a while loop that moves the agent down, only running as long as there is air below it.   

**Change your code, using a `||loops:while||` loop and `||agent:agent.inspect||` in the DOWN direction, to make your agent go down until the block is not `AIR`.**

```python
while agent.inspect(AgentInspection.BLOCK, DOWN) == AIR:
    agent.move(DOWN, 1)
```


## Step 3
As the agent is at the bottom of the dock, it can collect the blocks that have broken and fallen down. You can see where these blocks are by using the viewing gallery below the airship.
To collect blocks, use the `||agent:agent.collect_all()||` function.

**Change your code to collect all the items near your agent.**

```python
agent.collect_all()
```


## Getting Your Agents Position @showdialog
With the agent now holding onto the block to repair the airship with, we need to move it back to the correct position, to replace the block.
The Factory worker told you that the `y` coordinate to repair is at `157`.
To get the coordinates of the agent use:
```python
agent.get_position()
```
To get the `y` coordinate from this position use:
```python
agent.get_position().get_value(Axis.Y)
```

## Step 4
Use a `||loops:while||` loop, `||agent:agent.get_position()||` and `||positions:.get_value(AXIS.Y)||` to loop, running  `||agent:agent.move(UP)||`, until the agents `y` coordinate is `157`.


```python
while agent.get_position().get_value(Axis.Y) != 157:
    agent.move(UP, 1)
```

## Placing Blocks @showdialog
Now that the agent is at the correct y (altitude) coordinate, you can place the block that your agent just collected, using the `||agent:agent.set_slot||` and `||agent:agent.place||` functions.

Here's a reminder on how to use those functions...

```python
agent.set_slot(SLOT_NUMBER)
agent.place(DIRECTION)
```

- `SLOT_NUMBER`: The slot the agent should select (to place blocks from).

- `DIRECTION`: The direction that your agent will try to place a block. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.

## Step 5
Use `||agent:agent.set_slot||` and `||agent:agent.place||` functions to place a block from slot number `1` in the `DOWN` direction.


```python
agent.set_slot(1)
agent.place(DOWN)
```
