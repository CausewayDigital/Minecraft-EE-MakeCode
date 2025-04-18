### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - Forest 1

```template
agent
```

## Climbing the Tree @showdialog
Using our agent, let's rebuild the broken ladder to investigate the smoke coming from the top of the tree.   

Marcus has already loaded your agent with some ladders.   

![Cover Image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/forest/cover.png)

## Get Agent to the Ladder
First you need to get your agent to the ladder using `||agent:agent.move(DIRECTION, BLOCKS)||`
```python
agent.move(FORWARD, 1)
```

## Fixing the Ladder
Now you're ready to start fixing the ladder up the tree.
To place blocks, you can use `||agent:agent.place(DIRECTION)||`. 
Add an `||agent:agent.place||`, to place a ladder in front (`FORWARD`) of your agent.
```python
agent.move(FORWARD, 1)
agent.place(FORWARD)
```

## Fix the Rest
With the first ladder replaced, there seems to be another missing ladder above...
Complete the path by replacing the second ladder (using `||agent:agent.move||` and `||agent:agent.place||`).

## All Done
Now climb up the ladder and investigate the smoke!
