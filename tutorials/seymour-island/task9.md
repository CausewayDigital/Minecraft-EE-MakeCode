

### @flyoutOnly 1

# Carpet Builder

```template
player.onItemInteracted(BLAZE_ROD, function () {
})

```

# 8. Building Carpet

## Introduction step @unplugged

# Carpet building

![Meet-Agent](https://github.com/gbaman/minecraft-ee-seymour-island/raw/master/media/carpet.gif)

## Step 2

In this task, you must use your agent to build out a carpet, following the patterns
in each of the 4 sections provided.   
To do this, we will use Lists/Arrays to "save" a copy of the carpet already, then 
play this back line by line to build the required design.   
Hit the Next button to get started!

## Step 3
First, lets create a blank list/array. Use the ``||Arrays:set list to||`` command
and using the minus button, remove the default contents (1 and 2) from the list/array.   
You can also change the name of the list at this point from `list` to any other name.
For example, you could use `floor`.   
Remember at any time, you can hit the **Reset Agent and Task** button on the wall.

```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    floor = [];
})
```

## Step 4
With somewhere to store the block below block IDs now, lets start filling the list/array.   
Use the ``||Agent: agent inspect block below||`` command to get the agent to check
the block below it. Then use the ``||Arrays: add value to end||`` command to append
the block id to the end of the list.   

```blocks
let floor: number[] = []
player.onItemInteracted(BLAZE_ROD, function () {
    floor = []
    floor.push(agent.inspect(AgentInspection.Block, DOWN))
})

```

## Step 5
We can now move onto the next block. by moving left using ``||Agent:agent move left by 1||``.

```blocks
let floor: number[] = []
player.onItemInteracted(BLAZE_ROD, function () {
    floor = []
    floor.push(agent.inspect(AgentInspection.Block, DOWN))
    agent.move(LEFT, 1)
})

```

## Step 6
Could you now add a ``||Loops:repeat times do||`` loop to scan all 5 blocks, without having to copy/paste
all the code? Be careful not to reset your array each time, it should only be 
set up as an empty array at the start once for now!   
Also make sure to bring him back to the starting position as well once all the blocks
have been scanned.

```blocks
let floor: number[] = []
player.onItemInteracted(BLAZE_ROD, function () {
    floor = []
    for (let index = 0; index < 4; index++) {
        floor.push(agent.inspect(AgentInspection.Block, DOWN))
        agent.move(LEFT, 1)
    }
    agent.move(RIGHT, 4)
})
```

## Step 7
Now it's time to start placing blocks. You will be able to use the 
``||Agent:place floor block with||`` command to place down a block, but first we need
the block IDs. To get each one at a time, lets use the ``||Loops:for element in value of list||``
command after everything we have done so far. We can then put ``value`` within ``||Agent:place floor block with||``.
   
Don't forget to also to ``||Agent:agent move left by 1||`` inside the loop to 
go to the next gap!  

```blocks
let floor: number[] = []
player.onItemInteracted(BLAZE_ROD, function () {
    floor = []
    for (let index = 0; index < 4; index++) {
        floor.push(agent.inspect(AgentInspection.Block, DOWN))
        agent.move(LEFT, 1)
    }

    //hello world

    agent.move(RIGHT, 4)
    agent.move(FORWARD, 1)
    for (let value of floor) {
    	seymour.placeFloor(value)
    }
})
```

## Step 8
Now you have a floor building program, you should extend this with another 
``||Loops:repeat times do||`` to complete that quarter.   
Next, using the ``||Agent:agent move||`` and ``||Agent:agent turn||`` commands, position
your Agent at the start of the next quarter to run the code again.   

```blocks
let floor: number[] = []
player.onItemInteracted(BLAZE_ROD, function () {
    floor = []
    for (let index = 0; index < 4; index++) {
        floor.push(agent.inspect(AgentInspection.Block, DOWN))
        agent.move(LEFT, 1)
    }
    agent.move(RIGHT, 4)
    agent.move(FORWARD, 1)
    for (let index = 0; index < 4; index++) {
        for (let value of floor) {
        	seymour.placeFloor(value)
        }
        agent.move(RIGHT, 4)
        agent.move(FORWARD, 1)
    }
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 6)
})

```

```package
seymour=github:gbaman/minecraft-ee-seymour-island
```
