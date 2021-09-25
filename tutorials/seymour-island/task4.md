### @flyoutOnly 1


# Auto Miner level 3


## Step 1 @unplugged
![Side task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_4.jpg)
In this task, you must use your agent to mine **only** the ores!   
You need to be careful, if you mine out the other stone around it, there is a chance the mine might collapse...   

This task is an **advanced** task, it is highly recommended you have completed Auto Miner 1 and 2 first!

WARNING - This task includes a 50 second timer, that resets your agent back to the start after 50 seconds.   

```template
//
```

## Step 2

In this task, there are a few different ways to check each of the ore blocks.   
One option is though is a collection of ``||logic: or ||`` commands nested within each other. 
Alternatively, instead of telling the agent which blocks it **should** mine, we could use ``||logic: not ||`` to tell it which blocks not to mine.       

Beyond this, the rest of the task is up to you. The final program will be similar to Autominer 2.   


```ghost
    for (let index = 0; index < 8; index++) {
        for (let index = 0; index < 3; index++) {
            if (agent.inspect(AgentInspection.Block, RIGHT) == IRON_ORE) {
                agent.destroy(RIGHT)
            } else if (agent.inspect(AgentInspection.Block, RIGHT) == REDSTONE_ORE) {
                agent.destroy(RIGHT)
            } else if (agent.inspect(AgentInspection.Block, RIGHT) == GOLD_ORE) {
                agent.destroy(RIGHT)
            } else if (agent.inspect(AgentInspection.Block, RIGHT) == DIAMOND_ORE) {
                agent.destroy(RIGHT)
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