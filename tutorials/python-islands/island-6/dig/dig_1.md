### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Dig

```customts
namespace agent {
    /**
    * Your agent checks if there is a fossil below.
    */
    //% block
    export function isFossilBelow(): boolean {
        let block = agent.inspect(AgentInspection.Block, DOWN)
        return block == DEAD_FIRE_CORAL_BLOCK
    }
}

/**
 * Scientist
 */
//% color=purple weight=100 icon="\uf0c3" block="Scientist"
namespace scientist {
    /**
    * A scientist will check if your list contains all the fossils.
    */
    //% block
    export function check(final: any[]): void {

        let solution = [world(1019, 139, 110), world(1018, 139, 111), world(1017, 139, 109)].sort()
        let final_sorted = final.sort()

        let list_equal = true

        if (solution.length !== final_sorted.length) {
            list_equal = false
        };
        for (let i = 0; i < solution.length; i++) {
            if (!positions.equals(solution[i], final_sorted[i])) {
                list_equal = false
            };
        }

        if (list_equal) {
            blocks.place(DIAMOND_BLOCK, world(991, 144, 122))
        } else {
            player.say("\nHmmm...\nAll of the coordinates don't lead to fossils... Try again.")
        }
    }
}
```

## Dig for Dinosaurs @showdialog
Recently, the island archaeology team have discovered some pre-historic artifacts. Use your Agent to find the ancient fossils hidden below the ground!

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/dig/cover.png)

## Lists @showdialog
Your agent will be locating the fossils using its powerful sensors, then passing on the location of each to the archaeological team to excavate.      

To do this, it will store each fossil location in a list, which can be handed over to the team once your survey is complete.   

Here's a reminder on how to create a list...

`||agent:agent.is_fossil_below()||`

```python

my_list = [] # This is an empty list, with no items

```

## Create an Empty List
**Create an empty list called coordinates that you can later add the positions of fossils to.**

```python
coordinates = []
```

## Create Some For Loops
We can use two for loops to cover a 2D space, so that we can check for fossils.

for var in range(start, stop):

**Add two `||loops:for||` loops, one inside the other, that both iterate from 0 to 3.**

**The outer loop should use the variable `row` and the inner loop should use the variable `col`, for column**

**Add a say command so you can see the values of `row` and `col`, to make sure your program is working as expected.**
```python
coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
```

## Move Your Agent
To scan the whole area your agent will need to move.

**Within the inner loop, use `||agent:agent.move||` to move your agent forward 1 block. After each time the inner loop has run you need to move your agent back 3 blocks then left 1 block so you can scan the next row.**

**Outside of both loops you need to return your agent to the start so the agent can scan from the start agent, to do this move your agent to the right by 3 after both loops.**

```python
coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
        agent.move(FORWARD, 1)
    agent.move(BACK, 3)
    agent.move(LEFT, 1)
agent.move(RIGHT, 3)
```

## Appending to lists @showdialog
To add something to the end of a list you need to use the `||arrays:append||` operator.

For example if you wanted to add your agent's coordinates to the coordinates list you would do this:

```python
agent_pos = agent.get_position()
coordinates.append(agent_pos)
```

```ghost
if agent.is_fossil_below():
    scientist.check([])
```

## Check for fossils
You need to mark the fossils for the scientists.

**Before you move your agent in the inner loop check for a fossil below your agent. To do this use `||agent:agent.is_fossil_below||`. If there is a fossil, add your agent's coordinates to the list.**

**At the end of your code `||scientist:scientist.check(coordinates)||` to check your list and finish the task.**

```python
if agent.is_fossil_below():
    coordinates.append(agent.get_position())
```

```ghost
coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
        if agent.is_fossil_below():
            coordinates.append(agent.get_position())
        agent.move(FORWARD, 1)
    agent.move(BACK, 3)
    agent.move(LEFT, 1)
agent.move(RIGHT, 3)

scientist.check(coordinates)
```
