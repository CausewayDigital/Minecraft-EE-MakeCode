### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Python Islands 1 - Forest 2

```template
agent
```

## Apple Picking @showdialog
After investigating, you realise that Nicole is stuck at the top of the tree, with her bird called Marvin. He seems to be nesting at the top of the tree because he's hungry. Let's go and get him some apples!
![Cover Image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/forest/cover2.png)
Go down the ladder and find your agent, then when you're ready to let's go and pick our first apple! 

## Get to an Apple
To pick the apples, you need to position your agent in front of them. Remember your agent can go UP, DOWN, LEFT, RIGHT, FORWARD and BACK.
Move your agent using `||agent:agent.move||` (and your whistle) to the first apple you want to pick!


```python
agent.move(DIRECTION, BLOCKS)
```


## Picking up an Apple @showdialog
Make sure your agent is next to an apple. (Similar to the image below)
![Agent position before picking apple](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/forest/agent_before_pick.png)

## Picking up an Apple
With your agent in front of an apple, you can use the `||agent:agent.destroy||` command to break a block in a certain direction.
```python

agent.destroy(DIRECTION)

```
- `DIRECTION`: The direction that your agent will try to break. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.


## Get the Rest
Great! Now with the first apple gone, we still need to get 4 more.
Now search around and pick four more then return to Nicole when you're finished.
