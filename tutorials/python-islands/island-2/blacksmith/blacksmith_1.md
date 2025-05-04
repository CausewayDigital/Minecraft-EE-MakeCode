### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Blacksmith

```customts
/**
 * Gives command to help the blacksmith.
 */
//% color=Grey weight=100 icon="\uf0e3" block="blacksmith"
namespace blacksmith {
    /**
    * Get purity of ore
    */
    //% block"Purity %direction"
    //% direction.defl=FORWARD
    export function purity(direction: SixDirection): number {
        block = agent.inspect(AgentInspection.Block, direction)
        switch(block){
            case IRON_ORE:
                return 4
            case 896:
                // raw_iron_block
                return 3
//            case raw_copper_block:
//                return 2
//            case raw_gold_block:
//                return 1
            default:
                return 0
        }
    }

    /**
    * Accept the ore.
    */
    //% block"Accept Ore"
    export function accept(): void {
        agent.setSlot(1)
        agent.place(UP)
    }

    /**
    * Deny the ore.
    */
    //% block"Deny Ore"
    export function deny(): void {
        agent.setSlot(2)
        agent.place(UP)
    }
}
```

```ghost
if(blacksmith.purity(FORWARD) <= 3) {
    player.say("Purity less than or equal to 3!")
    blacksmith.deny()
} else {
    blacksmith.accept()
}
```

## Extracting Pure Iron @showdialog
Now you have collected the iron ore that is needed. The final step is making sure it is pure enough to use! The Blacksmith has asked you to find the purest of all the iron, using your Agent.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/blacksmith/cover.png)

## Checking ore purity

To help with this task, the blacksmith has equiped your agent with a special function that can check iron purity called ``||blacksmith:blacksmith.purity()||``.

This function takes in a direction such as `FORWARD` in which the agent should check.

*There's no code to write in this step, move on to the next step to start*

## Step 1

As we want the purest of iron from our ores, we will use an ``||logic:if||`` statement, to check if the purity of the block less than 3.

Python includes more than just checking if one item equals another item (using `==`). It also allows you to check for greater than or less than.

**Create an ``||logic:if||``  to check if the pruity of the ore is  `less than or equal` (using  <=  ) to `3`**

```python
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
    // Code goes here in the next step
```

## Step 2
Now, with the if statement ready to check for the iron that is not pure enough to be used, let's use the ``||blacksmith:blacksmith.deny()||`` command, to mark the block as invalid for the Blacksmith.

**Add your ``||blacksmith:blacksmith.deny||`` command, so that it runs when the purity is less than or equal to 3**

```diffpython
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
------------------------------------
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
    blacksmith.deny()
```

## Step 3

Having the code completed for the iron with purity less than or equal to 3, let's add our code for the accepted blocks of iron ore.

To accept an ore, the Blacksmith has given us a command called ``||blacksmith:blacksmith.accept()||``

**Add an `else` statement that executes an ``||blacksmith:blacksmith.accept||`` command below your if statement**

```python
if(blacksmith.purity(FORWARD) <= 3):
    player.say("Purity less than or equal to 3!")
    blacksmith.deny()
else:
    blacksmith.accept()
```

## Check all the ore!
Now with your code complete, run it over and over again until all the iron has been checked!