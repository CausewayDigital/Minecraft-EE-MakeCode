### @flyoutOnly 1


# Maze coder


## Step 1 @unplugged
![Overhead task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_8.jpg)
In this task, you need to get your Agent to the golden pressure pad. Seems easy, right?...   
The catch... You can't see the obstacles in its way! For that, you will require a friend
to take the position above, with the added benefit of invisible block visibility. They will guide you.    
When you and your partner are ready, hit Next.   

```template
//
```

## Step 2
To move your agent, you can use the ``||agent:agent move FORWARD||`` command.   
You are also able to use the ``||agent:agent turn LEFT||`` command if you wish.

Place your code within the ``||player: on start||`` section, then click
the play button in the bottom right corner to run your code.

Good luck!

```blocks
agent.move(FORWARD, 1)
```

```ghost
    agent.move(LEFT, 4)
    agent.move(FORWARD, 2)
    agent.move(RIGHT, 2)
    agent.move(LEFT, 2)
    agent.move(BACK, 2)
    agent.move(RIGHT, 8)
    agent.move(FORWARD, 6)
    agent.move(LEFT, 2)
    agent.move(RIGHT, 2)
    agent.move(BACK, 6)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 5)
    agent.move(LEFT, 1)
    agent.move(FORWARD, 1)
    agent.move(BACK, 1)
    agent.move(RIGHT, 1)
    agent.move(BACK, 5)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(RIGHT, 1)
    agent.move(FORWARD, 7)
    agent.move(RIGHT, 4)
    agent.move(BACK, 1)
    agent.move(RIGHT, 3)
    agent.move(FORWARD, 3)
    agent.move(LEFT, 4)
    agent.turn(LEFT)

```

```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
