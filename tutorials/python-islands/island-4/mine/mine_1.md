### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Mine

```template
agent
```

```ghost
agent.mark_diamond
agent.mark_bin
```

```customts
namespace agent {
    /**
    * Returns the type of ore
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function check_ore(direction: SixDirection): string {
        if (agent.inspect(AgentInspection.Block, direction) == DEEPSLATE_COPPER_ORE) {
            return DIAMOND_ORE
        } else if (agent.inspect(AgentInspection.Block, direction) == DEEPSLATE_COAL_ORE) {
            return DIRT
        } else {
            return agent.inspect(AgentInspection.Block, direction)
        }
    }

    /**
    * Marks a diamond block
    */
    export function mark_diamond(): void {
        if (check_ore(FORWARD) != AIR) {
            agent.set_slot(2)
            agent.place(UP)
        } else {
            player.say("Unable to detect a block!")
        }
    }

    /**
    * Marks a block for disposal
    */
    export function mark_bin(): void {
        if (check_ore(FORWARD) != AIR) {
            agent.set_slot(1)
            agent.place(UP)
        } else {
            player.say("Unable to detect block")
        }
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
agent
```
