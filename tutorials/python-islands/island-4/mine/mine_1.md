### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Mine



```customts
namespace agent {
    /**
    * Returns the type of ore
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function check_ore(direction: SixDirection): Block {
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
        if (check_ore(FORWARD) != AIR) {
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
        if (check_ore(FORWARD) != AIR) {
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


## Task 1
First, we want to create the while loop that runs while you haven't yet found all three 3 Diamond ore blocks you are looking for.
To do this, we can use a while loop and check if a variable that we use to keep count of the Diamonds, is less than 3. To do this, we can use the < operator. This means what is on the left is less than what's on the right.
Below is an example of a while loop, move onto step 2 when you're ready

```python
found_diamond = 0
```


```ghost
found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        agent.markDiamond()
        found_diamond = found_diamond + 1
    else:
        agent.markBin()
```