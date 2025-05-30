### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Forest

```customts
namespace agent {
    /**
     * Harvest block infront of the agent
    */
    //% block Harvest block
    export function harvest(): void {
        let inspect = agent.inspect(AgentInspection.Block, FORWARD);
        if (inspect === STONE) {
            agent.destroy(FORWARD)
            agent.drop(FORWARD, 2, 1)
        } else if (inspect === 18) {  // Leaves
            agent.destroy(FORWARD)
            agent.drop(FORWARD, 1, 1)
        }
    }

    /**
    * Checks if the block infront of agent is a nest, returns True is there is, else False.
    */
    //% block Check if block is nest
    export function is_nest(): boolean {
        let inspect = agent.inspect(AgentInspection.Block, FORWARD)
        if (inspect === STONE) {
            return true
        }
        return false
    }

    /**
    * Moves agent to the next location
    */
    //% block Move to next location
    export function next_location(): void {
        // 21 is a Snow Golem
        mobs.spawn(21, world(166, 153, 220))
    }
}
```

```ghost
player.say(agent.is_nest())
if (agent.is_nest()){
    agent.harvest()
}
agent.next_location()
```


## Collecting Forest Wood @showdialog

The island's forest has a thick fog over it, making it nearly impossible for the forest explorers to harvest wood for the island!

TJ has asked if you and your agent could harvest some wood from the trees. You can then **keep some for your ladders** as well.

You need to be **extremely** careful though, not to disturb the birds, that are nesting in the trees!

![Cover image of forest](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/forest/ForestCover.png)

## Introduction @showdialog

TJ has given your agent a few special functions for your agent to use in this forest task:

- ``||agent:agent.is_nest()||``: If there is a birds nest in front of your agent, return back `True`. Otherwise, return back `False`.

- ``||agent:agent.harvest()||``: Carefully harvests the wood in front of your agent and then drops it to the ground.

- ``||agent:agent.next_location()||``: TJ will move your agent for you, to the next branch.

## Step 1

TJ has moved the agent to directly in front of a branch. Your first job to check (without being able to see the agent), whether there is a nest on the branch.

You can use the ``||agent:agent.is_nest()||`` function for this. It will return a `True` if there is a nest, or a `False` if there is just normal wood.

**Using ``||player:player.say()||`` to display the result, check if there's a nest in front of the agent.**

```spy
player.say(agent.is_nest())
```

## Step 2

Now that you know how to use ``||agent:agent.is_nest()||``, we can use it with an ``||logic:if||`` statement, to check **if** the block in front is a nest.

If there is a nest, we want to leave it alone and run ``||agent:agent.next()||`` to go to the next area.

**Create an ``||logic:if||`` statement that moves to the next area if ``||agent:agent.is_nest()||`` returns `True`**

```spy
if(agent.is_nest()){
    agent.next_location()
}
```

## Step 3

Next, we want to add an ``||logic:else:||`` so we are able to harvest other blocks and then go to the next area.

**Add a ``||agent:agent.harvest()||`` in an ``||logic:else:||`` statement you created.**    
**Remember to go to the next location after harvesting as well!**

## Step 4

With all of that together, you can run this program a few times, until you find enough wood. Just make sure you don't disturb the birds! Good luck!
