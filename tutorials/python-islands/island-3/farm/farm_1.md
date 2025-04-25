### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Farm

```ghostpython
agent.move(FORWARD)
agent.place(FORWARD)
agent.destory(FORWARD)
agent.inspect(AgentInspection.Block, DOWN)
```

```template
agent.
```

## Automated Farming and Crop Harvesting @showdialog

Now that you can use ``||loops:for||`` loops. Let's test your skills by having your agent automatically harvest and replant a farm plot!

![Cover image](cover.png)

## Step 1

Peter has given your agent the exact number of seeds you need for planting.

To start, we'll need to move the agent forward before we inspect the first crop.

**Move your agent forward one block!**

```spy
agent.move(FORWARD, 1)
```

## Step 2

Great, now we'll get the agent to inspect block below and store it in a variable.

**Add a new variable called `block` and set it equal to the block the agent inspects**

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
```

## Step 3

Now with the block name stored in a variable. We can use an ``||logic:if||`` statement to choose what to do depending on the block below the agent.

**Add an ``||logic:if||`` statment to check if the block is `WHEAT`**

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
if(block == WHEAT){
    player.say("Wheat!")
}
```

## Step 4

With the code ready for checking when the block is wheat, we can harvest the wheat using ``||agent:agent.destroy()||`` and giving a direction, then place seeds using ``||agent:agent.place()||`` with the direction you want your agent to place the seeds.

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
if(block == WHEAT){
    agent.destory(DOWN)
    agent.place(DOWN)
    player.say("Wheat!")
}
```

## Step 5

With the ``||logic:if||`` statement finished, let's make the ``||logic:elif||`` statement!

**Add an ``||logic:elif||`` statment to plant a seed using ``||agent:agent.place()||`` if the the block is `AIR`**

```spy
const block = agent.inspect(AgentInspection.Block, DOWN)
if(block == WHEAT){
    agent.destory(DOWN)
    agent.place(DOWN)
    player.say("Wheat!")
}else if (block == AIR) {
    agent.place(DOWN)
    player.say("Air!")
}
```

## Step 6

Great! Now with all that together, let's add our for loop to repeat it all, more than once.

**Create a ``||loops: for loop||`` to run the code you already have for the range of `0` to `8`.**

```diffpython
block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destory(DOWN)
        agent.place(DOWN)
        player.say("Wheat!")
    elif block == AIR:
        agent.place(DOWN)
        player.say("Air!")
----------------------
for count in range(0, 8):
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destory(DOWN)
        agent.place(DOWN)
        player.say("Wheat!")
    elif block == AIR:
        agent.place(DOWN)
        player.say("Air!")
```

## Start Harvesting!

Now with all your code together, run it and **call your agent back to the diamond blocks using your whistle**. Happy farming!
