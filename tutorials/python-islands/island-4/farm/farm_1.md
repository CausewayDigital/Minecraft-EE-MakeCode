### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Farm
```customts
namespace agent {
    /**
    * Returns the flower in the specified direction.
    */
    //% block
    export function checkFlower(direction: SixDirection): Block {
        let block = agent.inspect(AgentInspection.Block, direction);
        if (block == POINTED_DRIPSTONE) {
            return POPPY;
        } else {
            return block;
        }
    }
}
```


## Automated Flower Picking and Sorting @showdialog
![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/farm/cover.jpg)

**Gardener** - "*Welcome to the Botanical Gardens! We need your help picking some poppies, to make into the red dye you need. Can you and your agent help pick those poppies for me?*"   

Using a `||loops:while||` loop, your agent will keep collecting poppies **while you don't have enough**. Once you have enough poppies (4), your agent will stop.   

## Task 1
**Setup a `||loops:while||` loop and set it's condition to use `||agent:agent.get_item_count||` with the slot number as the only parameter (1). Repeat this loop while there are less than 4 poppies in slot 1.**

```python-ignore
while agent.get_item_count(1) < 4:
```

## Task 2

**Within the loop, add `||agent:agent.move||` to move you agent in the 'FORWARD' direction while the agent has less than 4 poppies.**

Remember you can call your agent back with the whistle at any time.

```python
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
```

## Check Flower and Destroy @showdialog
Now that you've got your agent moving, it needs to check what flower is below and decide if it should harvest (*destroy*) it or not.    
To do this, you can use `||agent:agent.check_flower||` (and the direction `DOWN`), which returns back the type of flower below the agent.    
With this information, you can use it within an `||logic:if||` statement, to check if the flower is a `"POPPY"`.    
If it is a poppy you can use `||agent:agent.destroy||` (and the direction `DOWN`) to pick the flower  below your agent.

## Task 3
**Add an `||logic:if||` statement within your while loop to check if the flower is a `"POPPY"` using `||agent:agent.check_flower||`.**    
**If it is, call the `||agent:agent.destroy||` method. Your code should be checking below (DOWN) your agent.**

```python
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
    if agent.check_flower(DOWN) == POPPY:
        agent.destroy(DOWN)
```

## Task 4
Now that your agent has checked one row of flowers, you need to move to the next row. To do this add `||agent:agent.move||` and `||agent:agent.turn||` above your while loop so that your agent will start the next row.
Repeat this a few more times, changing the direction that the agent turns each time, to search all the rows.

```ghost
agent.turn(LEFT)
```
