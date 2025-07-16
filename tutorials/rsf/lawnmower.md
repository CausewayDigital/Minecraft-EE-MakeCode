### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Lawnmower
Tell your friend what to do
```template
lawnmower.start();
```

```customts
//% color=green weight=100 icon="\uf085"
namespace lawnmower {
    let lawnmowerIsOn: boolean = false;
    let reachedEnd: boolean = false;
    
    export enum until {
        //% block="SELECT"
        n_a,
        //% block="next block"
        nextBlock,
        //% block="end of lawn"
        endOfLawn,
    }

    //% block="Start lawnmower"
    export function start() {
        lawnmowerIsOn = true;
        blocks.place(DIAMOND_BLOCK, world(0, 0, 0));
        player.say("Tim: I've started the lawnmower")
    }

    //% block="Stop lawnmower"
    export function stop() {
        lawnmowerIsOn = false;
        blocks.place(AIR, world(0, 0, 0));
        player.say("Tim: I've stopped the lawnmower")
    }

    //% block="Drive forward until $untilType"
    export function goUntil(untilType: until) {
        // When the agent gets to the end it stops moving
        const agentPos = agent.getPosition();
        if (positions.equals(agentPos, world(-131, 0, -195)) && reachedEnd) {
            return;
        }

        switch (untilType) {
            case until.n_a: {
                player.say("Tim: When am I supposed to stop driving forwards?");
                break;
            }
            case until.nextBlock: {
                if (checkInBounds()) {
                    agent.move(FORWARD, 1);
                } else {
                    player.say("Tim: I can't go there");
                }
                break
            }
            case until.endOfLawn: {
                while (moveForward()) { }
                break
            }
        }
    }
    //% block="Return to house"
    export function returnToHouse() {
        agent.turnLeft()
        agent.turnLeft()
        while (lawnmower.moveForward(true)) { }
        agent.turnRight()
        agent.turnRight()
        player.say("Tim: I am back at the house.")
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
            return true;
        } else if (goalPostInFront()) {
            // makes sure lawnmower comes back the same way it went
            if (returning) {
                agent.turnLeft()
                agent.move(FORWARD, 1)
                agent.turnRight()
                agent.move(FORWARD, 2)
                agent.turnRight()
                agent.move(FORWARD, 1)
                agent.turnLeft()
            } else {
                agent.turnRight()
                agent.move(FORWARD, 1)
                agent.turnLeft()
                agent.move(FORWARD, 2)
                agent.turnLeft()
                agent.move(FORWARD, 1)
                agent.turnRight()
            }
            return true;
        } else {
            player.say("Tim: I've reached the end of the lawn.")
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

        if (z < -195) {
            return true;
        } else {
            return false;
        }
    }

    export function goalPostInFront(): boolean {
        let blockInFront = lawnmower.getBlockInFrontCoord()

        let x = blockInFront.getValue(Axis.X)
        let z = blockInFront.getValue(Axis.Z)

        if ((x === -132 && z === -168) || (x === -137 && z === -168)) {
            return true;
        } else {
            return false;
        }
    }

    export function isAtEndOfGarden(): boolean {
        let blockInFront = lawnmower.getBlockInFrontCoord()

        let x = blockInFront.getValue(Axis.X)
        let z = blockInFront.getValue(Axis.Z)

        if ((x <= -139 && z > -175) || z > -166) {
            return true;
        } else {
            return false
        }
    }

    export function checkInBounds(): boolean {
        let blockInFront = lawnmower.getBlockInFrontCoord()

        let x = blockInFront.getValue(Axis.X)
        let z = blockInFront.getValue(Axis.Z)

        if (x >= -145 && x <= -131 && z >= -195 && z <= -166 && !(x >= -145 && x <= -139 && z >= -174 && z <= -166) && !(x === -132 && z === -168) && !(x === -137 && z === -168)) {
            return true;
        } else {
            return false;
        }

    }
}
```

## Introduction @showdialog

Let's tell your friend where to go with the lawnmower. To do this we will use `||codeblocks||`. Bellow is an example of a `||codeblock||`.

```block
lawnmower.start();
```

To use codeblocks simply drag what you want to happen from the list of options on the left into within the block that says "`||on start||`".

**If you get stuck, try clicking the lightbulb symbol for a hint.**


## Start and Stop the Lawnmower
You will see that within the "`||on start||`" block is there already a "`||lawnmower:Start lawnmower||`" command. When Tim is done he needs to stop the lawnmower. Tell him to do this by dragging the "`||lawnmower:Stop lawnmower||`" command block just bellow the "`||lawnmower:Start lawnmower||`" command block.

```block
lawnmower.start();
lawnmower.stop();
```

## Cut Some Grass
After Tim has started the lawnmower he should go to the end of the lawn. Use the "`||lawnmower:Drive forward until||`" code block and select the correct option to tell Tim what to do.

```block
lawnmower.start();
lawnmower.goUntil(lawnmower.until.endOfLawn);
lawnmower.stop();
```

## Return for the Next Row
After Tim has cut a row of grass he needs to return back to the house to cut the next row of grass. Use the "`||lawnmower:Return to house||`" block to tell him to do this once he has gotten to the end of the lawn.

```block
lawnmower.goUntil(lawnmower.until.endOfLawn);
lawnmower.returnToHouse()
lawnmower.stop()
```

## Move to the Next Row
After Tim has cut a row of grass, and returned to the house, he needs to move onto the next row. To do this he needs to turn towards the next row, move forward, and turn back so he is facing the correct direction.

Use the "`||lawnmower:Turn||`" and "`||lawnmower:Drive forward until||`" command blocks to tell Tim what to do.

```block
lawnmower.returnToHouse()
lawnmower.turn(TurnDirection.Left)
lawnmower.goUntil(lawnmower.until.nextBlock)
lawnmower.turn(TurnDirection.Right)
```

## Repeat...
Tell Tim to repeat this 15 times, once for each row of the lawn.

You can do this by adding a "`||loops:for||`" loop from **0 to 14**. Then drag all the blocks except for "`||lawnmower:Start lawnmower||`" and "`||lawnmower:Stop lawnmower||`" inside the loops.

```blocks
lawnmower.start();
for (let i=0; i <= 14; i++) {
    lawnmower.goUntil(lawnmower.until.endOfLawn);
    lawnmower.returnToHouse();
    lawnmower.turn(TurnDirection.Left);
    lawnmower.goUntil(lawnmower.until.nextBlock);
    lawnmower.turn(TurnDirection.Right);
}
lawnmower.stop()
```

## Run
Now run the code and watch Tim cut the grass.

```ghost
lawnmower.start();
for (let i=0; i <= 14; i++) {
    lawnmower.goUntil(lawnmower.until.endOfLawn);
    lawnmower.returnToHouse();
    lawnmower.turn(TurnDirection.Left);
    lawnmower.goUntil(lawnmower.until.nextBlock);
    lawnmower.turn(TurnDirection.Right);
}
lawnmower.stop()
```
