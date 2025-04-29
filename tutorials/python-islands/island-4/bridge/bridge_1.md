### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Bridge
```template

while(== AIR) {
    agent.move()
}

player.say("I've reached the end")
```

## Getting started with the `while` loop @showdialog

In Island 3, you were introduced to **For Loops**. On this island, you're going to get to grips with the other type of loop, the **While Loop**. You use this if you don't know how many times you are going to loop for.



Here's an example of a **while loop**

```python

while condition_1 == condition_2:

    player.say("Condition_1 is equal to condition_2")

```

The code above will run **as long as** the condition is met, just like `if` statements, we use conditions for `while` loops. We use these conditions to check if we should stop looping.

## Bridging the gap @showdialog

![Bridging the gap](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/bridge/blind.jpg)


**Mine Manager** - "*So could you and your Agent build a bridge through the fog and investigate what might be over there?*"

To begin, you'll need to get your agent to run a while loop, to see if it has reached another landmass (island). To do this you can have your Agent check if the block in front of it is `AIR` and if so, the move forward (inside the **While Loop**). When your Agent gets to another landmass, the block in front will no longer be `AIR`, so you can stop.

## Step 1
To do this you can use `||agent:agent.inspect||` and `||agent:agent.move||` and a `||loops:while||` loop:

Add the `||agent:agent.inspect||` to the `||loops:while||` loop below so that the agent checks the block in the direction `FORWARD` is air.

*remember you can stop the code in the code window*

```python
while (agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR):
    agent.move(FORWARD, 1)
```

`agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR` checks if the block in front is air.


## Bridging the gap @showdialog

![Bridging the gap](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/bridge/blind.jpg)

**Mine Manager** - "*I've given your agent some **stone** (in slot 1), to build a bridge over to the island. Can you place the stone blocks below the agent, to form a bridge until it reaches the island in the distance and no longer has air in front of it?*"


## Step 2
Now that you have your agent moving for as long as the loop is running, we need to place blocks down to bridge over to the other island.    

To do this, we can use `||agent:agent.set_slot||` and `||agent:agent.place||` to place down blocks.

Don't forget you can use your whistle to call your agent back so that you can run your completed code.

**Have your agent place stone blocks (from slot 1) `DOWN` below itself. Then investigate the other island!**


```python
agent.set_slot(slot_id)
agent.place(DIRECTION)
```

- `slot_id`: The slot number in the agent's inventory that we want to select (so we can place blocks from it).

- `DIRECTION`: The direction we want the agent to place a block. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.
