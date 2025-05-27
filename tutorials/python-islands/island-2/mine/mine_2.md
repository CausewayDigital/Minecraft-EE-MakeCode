### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Mine - 2

```ghost
agent.destroy(FORWARD)
if (agent.inspect(AgentInspection.Block, FORWARD) == IRON_BLOCK){
    agent.destroy(FORWARD)
} else {
    player.say("Agent didn't find iron!")
}
```

## Exploring the mineshaft @showdialog

Use your agent to explore the old mineshafts in search of iron.

![Old mineshafts](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/mine/mine_2.gif)

## Finding Iron @showdialog

![Dark mineshaft](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/mine/dark_mine.jpg)

There seems to be a collection of old mineshafts, going off from the main tunnel. Rumour has it that these have unexplored deposits of iron.

Unfortunately, though, it's too dark to what is at the end of the shafts. Perhaps you should guide your agent down the shafts to check if there is iron?

## Programming your agent

Using your agent, check each of the 5 mine shafts, to see if they have any iron ore right at the end, in the darkness. If there is, you should mine it!

You will likely need to use each of the below commands at least once in your program.

- ``||agent:agent.move()||``
- ``||agent:agent.destroy()||``
- ``||agent:agent.inspect()||``

Finally, don't forget to use your **whistle** with this task!

## Write your program
**Write a program that, if your agent detects `IRON_ORE`, it breaks it. Be careful though not to break any other blocks!**

Once you have finished the program, hit the run button above. To complete this task, you must search all five mineshafts to find which shafts contain iron ore blocks at the end of them.

```python
if agent.inspect(AgentInspection.Block, FORWARD) == IRON_ORE:
    player.say("This is iron ore")
```
