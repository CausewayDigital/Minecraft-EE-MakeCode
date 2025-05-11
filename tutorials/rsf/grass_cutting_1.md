### @flyoutOnly true

# Grass cutting

```template
lawnmower.startCuttingGrass()
```

```customts

//% color="#AA278D" weight=100
namespace lawnmower {
    agent.teleport(world(-16, -60, 71), NORTH)
    let cutting = false;
    //% block
    export function startCuttingGrass() {
    cutting = true;

    }
     //% block
    export function stopCuttingGrass() {

    }

    // note that Caml casing yields lower case
    // block text with spaces

     /**
     * This is a statement block with a parameter
     */
    //% block
    export function moveForward(distance: number) {
        for (let index = 0; index < distance; index++) {
            if (cutting === true && agent.detect(AgentDetection.Block, FORWARD)){
                agent.destroy(FORWARD)
            }
            agent.move(FORWARD, 1)
        }    
    }

     // note that Caml casing yields lower case
    // block text with spaces

     /**
     * This is a statement block with a parameter
     */
    //% block
    export function moveBack(distance: number) {
        for (let index = 0; index < distance; index++) {
            if (cutting === true && agent.detect(AgentDetection.Block, BACK)){
                agent.destroy(BACK)
            }
            agent.move(BACK, 1)
        }    
    }

    //% shim=ENUM_GET
    //% blockId=direction_enum_shim
    //% block="Direction $arg"
    //% enumName="Directions"
    //% enumMemberName="direction"
    //% enumPromptHint="e.g. Left, Right, ..."
    //% enumInitialMembers="Left, Right"
    export function _directionEnumShim(arg: number) {
        // This function should do nothing, but must take in a single
        // argument of type number and return a number value.
        return arg;
    }

        /**
     * In a function that uses an enum shadow block, the argument it takes in
     * should be of type "number" (not the enum type)
     */
    //% blockId=show_direction
    //% block="turn $direction"
    //% color.shadow="direction_enum_shim"
    export function turnDirection(direction: TurnDirection) {
        agent.turn(direction)
    }
}
```

## Cutting the grass
There's too much grass in the garden to play football!
You will need to talk Bob through cutting the grass.   

```ghost
for (let index = 0; index < 4; index++) {
}
lawnmower.startCuttingGrass()
lawnmower.stopCuttingGrass()
lawnmower.moveForward(1)
lawnmower.turnDirection(LEFT_TURN)
```

## Moving
Use the ``||lawnmower:lawnmower.moveForward(1)||`` block to move lawnmower forward by that many blocks.  