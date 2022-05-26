### @flyoutOnly 1


# Fish collector


## Step 1

```template
//
```

In this task, we need to move clownfish and pufferfish from the ship, over onto the pier. First, let's go collect some fish! Use the ``||agent:agent move forward 2||`` command to position your Agent over a fish collection point. 
Then use the ``||agent:agent collect CLOWNFISH||`` command to pick up only clownfish for now.   
Place your code within the ``||on start||`` section, then click the run button to run your code.

```blocks
agent.move(FORWARD, 2)
agent.collect(CLOWNFISH)

```

## Step 2
With some clownfish now collected, let's also collect clownfish from the rest of the pickup points. Why not try and put your code in a ``||loops:Repeat 3 times loop||`` (or ``||loops:for loop||`` in Python).

```blocks
for (let index = 0; index < 3; index++) {
    agent.move(FORWARD, 2)
    agent.collect(CLOWNFISH)
}

```

## Step 3
With all your clownfish now collected, next write a program to take your Agent over to the correct drop off point on the pier and use the ``||agent:agent drop items one at a time||`` command to drop all the fish into the bucket.

```ghost
agent.dropAllItemsIndividually(FORWARD)

```

## Clownfish Diagram @unplugged
![Clownfish Diagram](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/master/tutorials/seymour-island/images/task_5_map_clownfish.jpg)
Use the diagram above to measure the distance the agent will need to travel to drop off the fish!

## Step 4
Try putting all this within a ``||loops:Repeat times loop||`` to keep picking up fish and dropping them off.

## Step 5
Finally, replicate the same process to handle pufferfish. It is recommended to do this separately.

## Pufferfish Diagram @unplugged
![Pufferfish Diagram](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/master/tutorials/seymour-island/images/task_5_map_pufferfish.jpg)
Use the diagram above to measure the distance the agent will need to travel to drop off the fish!

```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension
```
