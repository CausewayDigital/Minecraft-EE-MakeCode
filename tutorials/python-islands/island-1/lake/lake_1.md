### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - Lake

```template
agent
```

## Getting started with the Agent  @showdialog

In this task, it's time to learn how to move your Agent around!

![Image of Agent on a starting diamond block with their target in shot](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/lake/lake.jpg)

## Python Programs recap

Python programs are made up of one or more instructions, that the computer will execute one after another.

## Your Agent

Have a look around in the world. You should see your Agent, standing on the blue diamond block.

This awesome little robot can move around the world, even fly!

Head to the next step and we'll start telling your agent to move.

## Moving your agent

Move your agent with `||agent:agent.move(DIRECTION, DISTANCE)||`

**Try changing the `DIRECTION` placeholder to *FORWARD*, or perhaps another direction like *BACK* or *LEFT*?**   
**What happens if you increase the `DISTANCE` to 2 or 3?**

```python
agent.move(FORWARD, 1)
```

## Target 1 @showdialog

Now you know how to move your agent up, down, left, right, forward and back, you can now move onto something a little more difficult!

![Target 1](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/lake/target_1.jpg)

## Get to Target 1
Can you move your agent, using `||agent:agent.move(DIRECTION, DISTANCE)||`, to stand on the pressure pad on the golden block?

**Using `||agent:agent.move(DIRECTION, DISTANCE)||`, move your agent to the Golden block.**
