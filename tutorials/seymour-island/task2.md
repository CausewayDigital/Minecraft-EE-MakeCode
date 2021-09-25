### @flyoutOnly 1


# Auto Miner level 1


## Step 1 @unplugged

![Side task](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_2.jpg)
The mine ahead is too dangerous for a miner to go in. Do you think your Agent is up for the task?
Let's use the agent to dig a mine shaft ahead. First, why not try breaking
the block ahead of the Agent, using ``||agent:agent destroy forward||``.
Place your code within the ``||player: on start||`` section, then click the **play** button in the bottom right.

```template
//
```

```blocks
agent.destroy(FORWARD)
```

## Step 2
Lets now combine that with an ``||agent:agent move up||`` command, followed by another
``||agent:agent destroy forward||``.
Can you try getting your Agent to break the first column of **3** stone blocks?

```blocks
agent.destroy(FORWARD)
agent.move(UP, 1)
agent.destroy(FORWARD)
agent.move(UP, 1)
agent.destroy(FORWARD)
agent.move(UP, 1)
```


## Step 3
Surely there is bound to be a better way to do the same action 3 times, instead of just
putting the same code 3 times?   
The answer, loops!   
You can use the ``||loops:Repeat 3 times do||`` command to repeat the commands contained
within the command, 3 times.  
So why not add the ``||agent:agent destroy forward||`` and ``||agent:agent move up||``
inside a ``||loops:Repeat 3 times do||``?

```blocks
for (let index = 0; index < 3; index++) {
    agent.destroy(FORWARD)
    agent.move(UP, 1)
}

```


## Step 4
Finally, using what you have learnt so far, can you use another ``||loops:Repeat 7 times do||``  to dig out the rest of the mine shaft right up to
the golden block at the end?


```ghost
    for (let index = 0; index < 7; index++) {
        for (let index = 0; index < 3; index++) {
            agent.destroy(FORWARD)
            agent.move(UP, 1)
        }
        agent.move(DOWN, 3)
        agent.move(FORWARD, 1)
    }
```

```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
