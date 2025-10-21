### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Lawnmower
Tell Rhys what to do
```template
lawnmower.start();
```

```customts
let lawnmowerIsOn: boolean = false;
//% color=green weight=100 icon="\uf085"
namespace lawnmower {
    let reachedEnd: boolean = false;

    export enum until {
        //% block="SELECT"
        n_a,
        //% block="end of lawn"
        endOfLawn,
    }

    //% block="Start lawnmower"
    export function start() {
        lawnmowerIsOn = true;
        blocks.place(DIAMOND_BLOCK, world(-142, -2, -175));
    }

    //% block="Stop lawnmower"
    export function stop() {
        lawnmowerIsOn = false;
        blocks.place(AIR, world(-142, -2, -175));
    }

    //% block="Drive forward until $untilType"
    export function goUntil(untilType: until) {
        if (!lawnmowerIsOn) {
        }

        switch (untilType) {
            case until.n_a: {
                break;
            }
            case until.endOfLawn: {
                while (moveForward()) { }
                break
            }
        }
    }

    //% block="Shift left"
    export function shiftLeft() {
        let pos = agent.getPosition()
        if (pos.getValue(Axis.X) < -132) {
            agent.move(LEFT, 3)
            break_grass()
        }
    }

    export function break_grass() {
        let pos = agent.getPosition()

        let x = pos.getValue(Axis.X)
        let z = pos.getValue(Axis.Z)

        blocks.place(AIR, world(x - 1, 1, z))
        blocks.place(AIR, world(x, 1, z))
        blocks.place(AIR, world(x + 1, 1, z))

        blocks.place(AIR, world(x - 1, 0, z))
        blocks.place(AIR, world(x, 0, z))
        blocks.place(AIR, world(x + 1, 0, z))
    }

    //% block="Return to house"
    export function returnToHouse() {
        agent.turnLeft()
        agent.turnLeft()
        while (lawnmower.moveForward(true)) { }
        agent.turnRight()
        agent.turnRight()
    }

    //% block="Turn $direction"
    export function turn(direction: TurnDirection) {
        // When the agent gets to the end it stops moving
        const agentPos = agent.getPosition()
        if (positions.equals(agentPos, world(-131, 0, -195)) && reachedEnd) {
            return
        }
        switch (direction) {
            case TurnDirection.Left: {
                if (positions.equals(agentPos, world(-131, 0, -195))) {
                    reachedEnd = true;
                    break;
                }
                agent.turnLeft();
                break;
            } case TurnDirection.Right: {
                agent.turnRight();
                break;
            }
        }
    }

    export function moveForward(returning: boolean = false): boolean {
        if (checkInBounds()) {
            agent.move(FORWARD, 1)
            break_grass()
            return true;
        } else {
            return false;
        }
    }

    export function getBlockInFrontCoord(): Position {
        let agentPos = agent.getPosition()
        let facingDirection = agent.getOrientation()

        switch (facingDirection) {
            case 0: {
                return positions.add(agentPos, pos(0, 0, 1));
                break;
            }
            case 90: {
                return positions.add(agentPos, pos(-1, 0, 0));
                break;
            }
            case -90: {
                return positions.add(agentPos, pos(1, 0, 0));
                break;
            }
            default: {
                return positions.add(agentPos, pos(0, 0, -1));
            }
        }
    }

    export function isHouseInFront() {
        let blockInFront = lawnmower.getBlockInFrontCoord()
        let z = blockInFront.getValue(Axis.Z)

        if (z < -194) {
            return true;
        } else {
            return false;
        }
    }

    export function isAtEndOfGarden(): boolean {
        let blockInFront = lawnmower.getBlockInFrontCoord()

        let x = blockInFront.getValue(Axis.X)
        let z = blockInFront.getValue(Axis.Z)

        if ((x <= -138 && z > -176) || z > -169) {
            return true;
        } else {
            return false
        }
    }

    export function checkInBounds(): boolean {
        let blockInFront = lawnmower.getBlockInFrontCoord()

        let x = blockInFront.getValue(Axis.X)
        let z = blockInFront.getValue(Axis.Z)

        if (x >= -144 && x <= -132 && z >= -194 && z <= -170 && !(x >= -145 && x <= -138 && z >= -175 && z <= -166)) {
            return true;
        } else {
            return false;
        }

    }
}
```

## Introduction @showdialog

Let's tell Rhys where to go with the lawnmower. To do this we will use `||codeblocks||`. Bellow is an example of a `||codeblock||`.

```block
lawnmower.start();
```

To use codeblocks simply drag what you want to happen from the list of options on the left into within the block that says "`||on start||`".

**If you get stuck, try clicking the lightbulb symbol for a hint.**


## Start and Stop the Lawnmower
You will see that within the "`||on start||`" block is there already a "`||lawnmower:Start lawnmower||`" command. When Rhys is done he needs to stop the lawnmower. Tell him to do this by dragging the "`||lawnmower:Stop lawnmower||`" command block just bellow the "`||lawnmower:Start lawnmower||`" command block.

```block
lawnmower.start();
lawnmower.stop();
```

## Cut Some Grass
After Rhys has started the lawnmower he should go to the end of the lawn. Use the "`||lawnmower:Drive forward until||`" code block and select the correct option to tell Rhys what to do.

```block
lawnmower.start();
lawnmower.goUntil(lawnmower.until.endOfLawn);
lawnmower.stop();
```

## Return for the Next Row
After Rhys has cut a row of grass he needs to return back to the house to cut the next row of grass. Use the "`||lawnmower:Return to house||`" block to tell him to do this once he has gotten to the end of the lawn.

```block
lawnmower.goUntil(lawnmower.until.endOfLawn);
lawnmower.returnToHouse()
lawnmower.stop()
```

## Move to the Next Row
After Rhys has cut a row of grass, and returned to the house, he needs to move left onto the next row.

To do this use the `||lawnmower:Shift left||` code block which will move him onto the next row. 

```block
lawnmower.returnToHouse()
lawnmower.shiftLeft()
```

## Repeat...
Tell Rhys to repeat this **6 times**, once for each row of the lawn (the lawnmower does three blocks at a time).

You can do this by adding a "`||loops:repeat||`" loop Then drag all the blocks except for "`||lawnmower:Start lawnmower||`" and "`||lawnmower:Stop lawnmower||`" inside the loop.

```blocks
lawnmower.start();
for (let i=0; i < 1; i++) {
    lawnmower.goUntil(lawnmower.until.endOfLawn);
    lawnmower.returnToHouse();
    lawnmower.shiftLeft()
}
lawnmower.stop()
```

## Run
Now run the code and watch Rhys cut the grass.

```ghost
lawnmower.start();
for (let i=0; i < 1; i++) {
    lawnmower.goUntil(lawnmower.until.endOfLawn);
    lawnmower.returnToHouse();
    lawnmower.shiftLeft()
}
lawnmower.stop()
```
