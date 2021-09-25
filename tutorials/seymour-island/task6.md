### @flyoutOnly 1


# Multiplayer circuits

## Step 1 @unplugged
![Side task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_6.jpg)
Before you get started, it is important you have a friend in the room beside you to 
help with this task, as it requires 2 players!
It is also recommended that you have completed the fixing circuits single player 
task before attempting this one.   
Once you are ready to proceed, hit the next button.   

```template
//
```

## Step 2

This task involves repairing some circuits together, on a large scale.   
Look down into the circuit area. There are 4 quadrants, 2 of which you have to fix
and 2 that your friend has to fix. They feed into each other across the centre line.
The redstone current travels through the centre purple blocks. 
Note you can only place redstone on the **Green Emerald** blocks.  


## Step 3

Although you could write a program that had instructions for each block to check, why
not just build a program that scans for all emerald blocks, then places redstone?   
Let's start by using ``||agent:agent move left/right||`` to get your agent to a corner to start.

```blocks
agent.move(LEFT, 1)
```

## Step 4

Next, lets check if the block below us equals emerald.  
Start by adding a ``||logic:if then||``, with a ``||logic:0 = 0||`` block within it.   
In the first slot of this, use an ``||agent: agent inspect block down||`` to detect which block is below.   
Then on the right hand side, compare it against an Emerald Block.

```blocks
    agent.move(LEFT, 1)
    if (agent.inspect(AgentInspection.Block, DOWN) == EMERALD_BLOCK) {

    }
```

## Step 5

Within this if statement, if it does correctly detect emerald, then lets place some redstone down using ``||agent:agent place down||``.   
We also want to move forward after our if statement is complete by 1, using ``||agent:agent move forward by 1||``.

```blocks
    agent.move(LEFT, 1)
    if (agent.inspect(AgentInspection.Block, DOWN) == EMERALD_BLOCK) {
        agent.place(DOWN)
    }
    agent.move(FORWARD, 1)
```

## Step 6

You now have all the basic building blocks you need to complete this task. To reduce the amount of code you need to write to
complete this task, make sure to give ``||loops:repeat X times||`` a go as well, as this will make things a lot easier.   
Good luck!


```ghost
    agent.move(LEFT, 1)
    for (let index = 0; index < 9; index++) {
        for (let index = 0; index < 5; index++) {
            if (agent.inspect(AgentInspection.Block, DOWN) == EMERALD_BLOCK) {
                agent.place(DOWN)
            }
            agent.move(FORWARD, 1)
        }
        agent.move(BACK, 5)
        agent.move(RIGHT, 1)
    }
```



```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```