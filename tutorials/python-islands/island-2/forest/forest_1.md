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
    export function next(): void {
        mobs.spawn(HORSE, pos(166, 153, 220))
    }
}
```

```ghost
player.say(agent.is_nest())
if (agent.is_nest()){
    agent.harvest()
}
agent.next()
```


## Collecting Forest Wood @showdialog

The island's forest has a thick fog over it, making it nearly impossible for the forest explorers to harvest wood for the island!

TJ has asked if you and your agent could harvest some wood from the trees. You can then **keep some for your ladders** as well.

You need to be **extremely** careful though, not to disturb the birds, that are nesting in the trees!

## Introduction @showdialog

TJ has given your agent a few special functions for your agent to use in this forest task:

- ``||agent:agent.is_nest()||``: If there is a birds nest in front of your agent, return back `True`. Otherwise, return back `False`.

- ``||agent:agent.harvest()||``: Carefully harvests the wood in front of your agent and then drops it to the ground.

- ``||agent:agent.next()||``: TJ will move your agent for you, to the next branch.

## Step 1

TJ has moved the agent to directly in front of a branch. Your first job to check (without being able to see the agent), whether there is a nest on the branch.

You can use the ``||agent:agent.is_nest()||`` function for this. It will return a `True` if there is a nest, or a `False` if there is just normal wood.

**Using ``||player:player.say()||`` check if there's a nest infront of the agent.**

```spy
player.say(agent.is_nest())
```

## Step 2

Now that you know how to use ``||agent:agent.is_nest()||``, we can use it with an ``||logic:if||`` statement, to check **if** the block in front is a nest.

If there is a nest, we want to leave it alone and run ``||agent:agent.next()||`` to go to the next area.

**Create an ``||logic:if||`` statment that moves to the next area is ``||agent:agent.is_nest()||`` returns `True`**

```spy
if(agent.is_next()){
    agent.next()
}
```

## Step 3

Next, we want to add an ``||logic:else||``, to let us harvest other blocks and then go to the next area.

**Add a ``||agent:agent.harvest()||`` in an ``||logic:else||`` statment you created.**
```diffspy
if(agent.is_nest()){
    agent.next()
}
--------------------
if(agent.is_nest()){
    agent.next()
} else {
    agent.harvest()
}
```

## Step 4

With all of that together, you can run this program a few times, until you find enough wood. Just make sure you don't disturb the birds! Good luck!