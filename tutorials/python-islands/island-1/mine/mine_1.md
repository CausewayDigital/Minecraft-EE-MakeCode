### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - Mining

```template
agent
```

## Mining Coal on the Cliff @showdialog
Mine the coal from the cliff edge!
Use your agent to mine the coal on the edge of the cliff! Nicole and Marvin flew you down to this coal vein to mine as the miners cannot get to it. Can you mine the ore?
![Cover image of coal for mine task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/mine/cover.png)

## Move Your Agent
Now that you're beside the coal. Your agent should be able to fly over and stand in front of it to mine it.
Write the code to move the agent in front of a piece of coal ore.

```python
agent.move(DIRECTION, BLOCKS)
```
## Mine Some Coal @showdialog
![Agent in front of the coal](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/mine/agent_coal.png)
Make sure your agent is in front of the coal ore. (Similar to the image above)


## Mine Some Coal
Now you can mine the block to collect the coal!
With your agent, destroy the block of coal in front.

```python
agent.destroy(DIRECTION)
```
- `DIRECTION`: The direction that your agent will try to break. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.

## Get the Rest
One down, two to go! If you want to leave just talk to Nicole. But if you do, you will begin from the start again.
When you're done, Marvin will fly back to the surface and drop you off with the miner. Good luck!
**Mine the final two pieces of coal!**
