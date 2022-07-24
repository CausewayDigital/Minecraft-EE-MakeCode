### @flyoutOnly 1


# Auto Miner level 2


## Step 1 @unplugged
![Side task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_3.jpg)
In this task, you must use your agent to mine **only** the iron ore!   
You need to be careful, if you mine out the other stone around it, there is a chance the mine might collapse...   

When you are ready to get started, hit next.   

```template
//
```

## Step 2

The first step will be detecting the iron ore. We can start with checking the block below the agent.   
Start by adding a ``||logic:if then||``, with a ``||logic:0 = 0||`` block within it.   
In the first slot of this, use an ``||agent: agent inspect block down||`` to detect which block is below.   
Then on the right-hand side of the comparison block, compare it against an Iron Ore Block.   
Within this if statement, add an ``||agent:agent destroy down||``.   
Now try your code. You can reset the task at any point by using your phone.   

```blocks
if (agent.inspect(AgentInspection.Block, DOWN) == IRON_ORE) {
            agent.destroy(DOWN)
        }
```

## Step 3

Using the code you built for the previous exercise, can you check and destroy the rest of the wall as well?  
Place this section within a ``||loops:repeat 3 times||`` command and and move the agent up 1 each time.   
Don't forget to bring the agent back down again.   
Now try your code. You can reset the task at any point by using your phone. 

```blocks
    if (agent.inspect(AgentInspection.Block, DOWN) == IRON_ORE) {
        agent.destroy(DOWN)
    }
    for (let index = 0; index < 3; index++) {
        if (agent.inspect(AgentInspection.Block, LEFT) == IRON_ORE) {
            agent.destroy(LEFT)
        }
        agent.move(UP, 1)
    }
    agent.move(DOWN, 2)

```

## Step 4

Finally, encase the entire code within a further ``||loops:repeat X times||`` command. You will have to count how many blocks you need it to go forward.    
You are on your own for this last bit, good luck!

(remember though, you can hit the Reset Agent button in your phone at any time to move the agent back and try again)


```ghost
    for (let index = 0; index < 8; index++) {
        if (agent.inspect(AgentInspection.Block, DOWN) == IRON_ORE) {
            agent.destroy(DOWN)
        }
        for (let index = 0; index < 3; index++) {
            if (agent.inspect(AgentInspection.Block, LEFT) == IRON_ORE) {
                agent.destroy(LEFT)
            }
            agent.move(UP, 1)
        }
        agent.move(DOWN, 2)
        agent.move(FORWARD, 1)
    }

```

```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
