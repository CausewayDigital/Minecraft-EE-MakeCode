### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Mine

```template
let found_diamond = 0;
while (found_diamond < 3) {

}
```

```customts
namespace agent {
    /**
    * Returns the type of ore
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function checkOre(direction: SixDirection): Block {
        if (agent.inspect(AgentInspection.Block, direction) == RED_NETHER_BRICK) {
            return DIAMOND_ORE
        } else if (agent.inspect(AgentInspection.Block, direction) == NETHER_BRICK) {
            return DIRT
        } else {
            return agent.inspect(AgentInspection.Block, direction)
        }
    }

    /**
    * Marks a diamond block
    */
    //% block="agent mark diamond"
    export function markDiamond(): void {
        if (checkOre(FORWARD) != AIR) {
            agent.setSlot(2)
            agent.place(UP)
        } else {
            player.say("Unable to detect a block!")
        }
        loops.pause(300)
    }

    /**
    * Marks a block for disposal
    */
    //% block="agent mark bin"
    export function markBin(): void {
        if (checkOre(FORWARD) != AIR) {
            agent.setSlot(1)
            agent.place(UP)
        } else {
            player.say("Unable to detect block")
        }
        loops.pause(300)
    }
}
```

## Sort the Mined Material @showdialog
![Farming](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/mine/cover.jpg)

Welcome to the Mine! The miners need a hand with sorting today's mined ores. However, the sorting room has too much dust for you to go in. So your agent has been sent in. Program it to sort and mark ores ready for processing.
You will need to find 3 Diamond ores in this task.


## While Loops @showdialog
First, we want to create the `||loops:while||` loop that runs while you haven't yet found all three 3 Diamond ore blocks you are looking for.

To do this, we can use a `||loops:while||` loop and check if a variable that we use to keep count of the Diamonds, is less than 3, using the `<` symbol. This means what is on the left of the symbol is less than what's on the right.

Below is an example of a `||loops:while||` loop.


```python
found_diamond = 0
while found_diamond < 3:
    player.say("I keep looping!")
```

## Task 1

**Add an `||logic:if||` statement inside the loop to check if the block in front of your agent is `DIAMOND_ORE`, if it is increment the found_diamond counter and `||player:player.say||` "`diamond found`".**

```python
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        player.say("diamond found")
        found_diamond = found_diamond + 1
```

## Marking Diamonds @showdialog
Now that we know how to check for diamond ore, we need to mark the blocks that contain it for the miners. To do this, we can use `||agent:agent.mark_diamond||`, which will mark the diamond ore ready for processing by the mine.

We also need to mark the other ores that are not diamond, to be disposed of, to do this we can use an `||logic:else||` statement after the if statement and `||agent:agent.mark_bin||`, to mark an ore to be disposed of. An `||logic:else||` statement is run when the `||logic:if||` statement above it isn't triggered.

## Task 2
**Change the `||player:player.say||` function to the `||agent:agent.mark_diamond||` function so the miners know where the diamond ore is.**

```python
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        agent.mark_diamond()
        found_diamond = found_diamond + 1
```

## Task 3
**Add an `||logic:else||` statement within the `||loops:while||` loop that runs `||agent:agent.mark_bin||` if the ore is not diamond ore so the miners know to get rid of it.**


```ghost
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        agent.mark_diamond()
        found_diamond = found_diamond + 1
    else:
        agent.mark_bin()
```
