### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Runway
```customts
namespace agent {
    /**
    * Moves your agent back to the left-hand side of the runway.
    */
    //% block
    export function returnAgent(): void {
        let position = agent.getPosition();

        let y = position.getValue(Axis.Y);
        let z = position.getValue(Axis.Z);

        let orientation = agent.getOrientation();

        agent.teleport(world(948, y, z), SOUTH);
    }
}

/**
 * Runway
 */
//% color=purple weight=100 icon="\uf018" block="Runway"
namespace runway {
    /** 
    * Gets a list containing the runway design.
    */
    //% block
    export function getRunwayDesign(): boolean[][] {
        return [[false, false, false, false, false, false, false, false, false, false, false],
        [false, false, false, true, false, false, false, true, false, false, false],
        [false, false, false, true, false, false, false, true, false, false, false],
        [false, false, false, true, false, false, false, true, false, false, false],
        [false, false, false, false, false, false, false, false, false, false, false],
        [false, false, true, true, true, false, true, true, true, false, false],
        [false, false, false, true, false, false, true, false, true, false, false],
        [false, false, false, true, false, false, true, true, true, false, false],
        [false, false, false, true, false, false, true, false, true, false, false],
        [false, false, true, true, false, false, true, true, true, false, false]];
    }
}
```

```template
const runway_design = runway.get_runway_design();
for (const row of ) {
    player.say()
}
```

## Runway Designing @showdialog
Build the launch area for the rocket.

The airport runway are nearly complete. The final step is finishing painting the runway markings, so planes know at which angle to land.   

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/runway/cover.png)
## Working with Lists @showdialog

Malinda, the Airport Manger has given your Agent the locations that she wants marked on the runway, in the form of a list. Before we get started, let's look at an example.

For us to access the small lists, we can use a `||loops:for||` loop. Rather than using `range` we ask for each `small_list` in `large_list`.
```python
large_list = [ [1,2,3], [4,5,6], [7,8,9] ]
for small_list in large_list:
    player.output(smaller_list)
```

## Task 1
**Complete the `||loops:for||` loop to get, and say, every `row` in the runway design.**

```python
runway_design = runway.get_runway_design()
for row in runway_design:
    player.say(row)
```

## Task 2
Now that you can see the individual rows, let's get each block in each row.

For this, we will repeat what we had done before, but instead of getting every `row` in the runway design data, we can get every `block` in each `row`.

**Write another `||loops:for||` loop, inside the for loop you have already written, to get each `block` in each `row`.**

```python
runway_design = runway.get_runway_design()
for row in runway_design:
    for block in row:
        player.say(block)
```

## Task 3

With your code being able to get every block individually in each row, we can now program your Agent to move and place blocks.

If the block is "True" then a block should be placed, otherwise it should not.

**Add an `||logic:if||` statement, `||agent:agent.set_slot||` and `||agent:agent.place||` to place a block in the `DOWN` direction, from slot 1, within the inner loop if `block` is true.**

```python
runway_design = runway.get_runway_design()
for row in runway_design:
    for block in row:
        if block:
            agent.set_slot(1)
            agent.place(DOWN)
```

## Task 4 @showdialog

Now that you have the Agent getting and placing blocks from the list, we can code the Agent to move across the runway.

As we have two loops, we will need to add two `||agent:agent.move||` commands. 

- The first, to move the Agent after each block is placed, to the next block.

- The second at the end of every row, to move the agent forward to the next row.

You can also use the `||agent:agent.return_agent||` function to move your agent back to the left-hand side of the runway once each row is done.

## Task 4

**Add two `||agent:agent.move||` commands. One to move the Agent `RIGHT` after placing a block, and another to move the Agent `FORWARD` after the second loop has finished. Then add an `||agent:agent.return_agent||` command below the second `||agent:agent.move||` command.**

```ghost
for i in range(4):
    pass
```
