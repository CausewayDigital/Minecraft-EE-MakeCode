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

Using a **While Loop**, your agent will keep collecting poppies **while you don't have enough**. Once you have enough poppies (4), your agent will stop.   

## Get Item Count @showdialog
The first thing you need to set up is your loop. In this task, you'll need to check how many poppies your agent has in its inventory. As you destroy the poppies, the gardener will place them into **slot 1** of you agent. You can then use `||agent:agent.get_item_count||` to get the count of items in a given slot. We need *4* poppies to make enough dye for the airship.

Here's how `||agent:agent.get_item_count||` works:
```python
agent.get_item_count(slot)
```
- slot: The slot number of the items you want to count (usually slot 1).

## Task 1
**Complete the code below, using `||agent:agent.get_item_count||` to make a while loop that runs when there are less than 4 poppies in slot 1 of the agent's inventory.**

```python
while agent.get_item_count(1) < 4:
    player.say("I need more poppies!")
```

## Task 2

**Replace `||player:player.say||` with `||agent:agent.move||` to move you agent in the 'FORWARD' direction while the agent has less than 4 poppies.**

Remember you can call your agent back with the whistle at any time.

```python
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
```

## Check Flower and Destroy @showdialog
Now that you've got your agent moving, it needs to check what flower is below and decide if it should harvest(*destroy*) it or not.    
To do this, you can use `||agent:agent.check_flower||`, this will return the type of flower below the agent. With this information, you can use it within an `||logic:if||` statement, to check if the flower is a `"POPPY"`. If it is a poppy you can use `||agent:agent.destroy||` to pick the flower `DOWN` below your agent.

Both `||agent:agent.check_flower||` and `||agent:agent.destroy||` take one parameter, direction. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.
## Task 3
**Add an `||logic:if||` statement within your while loop to check if the flower is a `"POPPY"`, if it is call the `||agent:agent.destroy||` function. Your code should be checking bellow your agent.**

```python
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
    if agent.check_flower(DOWN) == POPPY:
        agent.destroy(DOWN)
```

## Task 4
Now that your agent has checked one row of flowers, you need to move to the next row. To do this add `||agent:agent.move||` and `||agent:agent.turn||` above your while loop so that your agent will start the next row.
Repeat this a few more times, changing the direction that the agent turns each time, to search all the rows.

```python
agent.move(direction)
agent.turn(turn_direction)
```
- direction: The direction we want the agent to move. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.
- turn_direction: The direction your agent should turn. The directions you can use are: LEFT, RIGHT.
