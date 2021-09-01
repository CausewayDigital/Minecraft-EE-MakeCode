### @flyoutOnly 1


# Maze coder


## Step 1
![Overhead task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_8.jpg)
In this task, you need to get your Agent to the golden pressure pad. Seems easy, right?...   
The catch... You can't see the obstacles in its way! For that, you will require a friend
to take the position above, with the added benefit of invisible block visibility. They will guide you.    
When you and your partner are ready, hit Next.   

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
agent.turn(LEFT)
```

```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
