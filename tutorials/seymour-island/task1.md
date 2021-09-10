### @flyoutOnly 1


# Circuit Repair


## Step 1 @unplugged

![Overhead task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_1_overhead.jpg)
In this task, you must fix the redstone circuit. The missing pieces are marked with green blocks below.
Your agent has plenty of redstone, ready to be used for this repair.
Place your code within the ``||loops: on start||`` section and when you are ready to run your code, click the **play** button in the bottom right.
Hit the **Next** button to continue.

## Step 2
First, we need to get our agent to the sections that have been damaged (marked with green).
Try using the ``||agent:agent move forward||`` and ``||agent:agent turn left/right||`` commands to position your agent
above one of the green blocks.

```template
//
```

```block
agent.move(FORWARD, 1)
agent.turn(LEFT_TURN)
agent.move(FORWARD, 2)

```


## Step 3
Now place the redstone using ``||agent:agent place down||`` on a green block, to fix that part of the circuit.
```blocks
agent.place(DOWN)
```


## Step 4
Now you know what you are doing, code your agent to place redstone on the other 2 green blocks.
If you find yourself stuck or want to start again, use your phone to reset the task.

```ghost
    agent.move(FORWARD, 1)
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
    agent.place(DOWN)
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 1)
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
    agent.place(DOWN)
    agent.turn(RIGHT_TURN)
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
    agent.place(DOWN)
```

```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
