### @flyoutOnly 1


# Circuit Repair


## Step 1

```template
player.onItemInteracted(BLAZE_ROD, function () {
})
```

In this task, you must fix the redstone circuit. The missing pieces are marked with green blocks below.
Your agent has plenty of redstone, ready to be used for this repair. 
Place your code within the ``||player: on item used||`` section, then right click
your **blaze rod** when you want to run the code.
Hit the **Next** button to continue.

## Step 2
First, we need to get our agent to the sections that have been damaged (marked with green).
Try using the ``||agent:agent move forward||`` and ``||agent:agent turn left/right||`` commands to position your agent
above one of the green blocks.

```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 2)
})
```


## Step 3
Now place the redstone using ``||agent:agent place down||`` on a green block, to fix that part of the circuit.
```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    agent.place(DOWN)
})
```


## Step 4
Now have your Agent move backwards and place redstone on the other green marked blocks.
If you find yourself stuck or want to start again, hit the Reset button on the wall.

```package
seymour=github:gbaman/minecraft-ee-seymour-island
```