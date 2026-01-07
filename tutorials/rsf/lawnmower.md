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
let next_block = world(-132, -2, -195); // -> -194, -193 ...

function increment_block() {
    next_block = positions.add(world(0, 0, 1), next_block)
}
function enter_exit_loop(entering: Boolean) {
    if (entering) {
        next_block = positions.add(world(-1, 0, 0), next_block)
    } else {
        next_block = positions.add(world(1, 0, 0), next_block)
    }
}

//% color=green weight=100 icon="\uf085"
namespace lawnmower {
    

    //% block="Start lawnmower"
    export function start() {
        blocks.place(PLANKS_ACACIA, next_block);
        increment_block();
    }

    //% block="Stop lawnmower"
    export function stop() {
        blocks.place(BAMBOO_PLANKS, next_block);
        increment_block();
    }

    //% block="Drive forward until end of lawn"
    export function goUntil() {
        blocks.place(PLANKS_BIRCH, next_block);
        increment_block();
    }

    //% block="Shift left"
    export function shiftLeft() {
        blocks.place(CHERRY_PLANKS, next_block);
        increment_block();
    }

    //% block="Return to house"
    export function returnToHouse() {
        blocks.place(CRIMSON_PLANKS, next_block);
        increment_block();
    }
}

//% color="#0fbc11" icon="\uf01e"
namespace loop {
    /**
     * Do something several times.
     */
    //% block="repeat $count times"
    //% handlerStatement=1
    export function customRepeat(count: number, handler: () => void) {
        if (count < 5) {
            blocks.place(PLANKS_DARK_OAK, next_block)
        } else {
            blocks.place(PLANKS_JUNGLE, next_block)
        }
        increment_block()
        enter_exit_loop(true)
        handler()
        enter_exit_loop(false)
    }
}
```

## Introduction @showdialog

Let's tell Rhys where to go with the lawnmower. To do this we will use `||codeblocks||`. Below is an example of a `||codeblock||`.

```block
lawnmower.start();
```

To use codeblocks simply drag what you want to happen from the list of options on the left into within the block that says "`||on start||`".

**If you get stuck, try clicking the lightbulb symbol for a hint.**


## Start and Stop the Lawnmower
Within the "`||on start||`" block, there is a "`||lawnmower:Start lawnmower||`" block. When Rhys is done he needs to stop the lawnmower. to do this drag the "`||lawnmower:Stop lawnmower||`" command block below the "`||lawnmower:Start lawnmower||`".

```block
lawnmower.start();
lawnmower.stop();
```

## Cut Some Grass
After Rhys has started the lawnmower he should go to the end of the lawn. Use the "`||lawnmower:Drive forward until end of lawn||`" code block.

```block
lawnmower.start();
lawnmower.goUntil();
lawnmower.stop();
```

## Return for the Next Row
After Rhys has cut a row of grass he needs to return back to the house to cut the next row of grass. Use the "`||lawnmower:Return to house||`" block to tell him to do this once he has gotten to the end of the lawn.

```block
lawnmower.goUntil();
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
Tell Rhys to repeat this **5 times**, each row of the lawn (the lawnmower cuts three blocks at a time).
You can do this by adding a "`||loops:repeat||`" loop Then drag all the blocks except for "`||lawnmower:Start lawnmower||`" and "`||lawnmower:Stop lawnmower||`" inside the loop.

```blocks
lawnmower.start();
loop.customRepeat(5,  function() {
    lawnmower.goUntil();
    lawnmower.returnToHouse();
    lawnmower.shiftLeft()
})
lawnmower.stop()
```

## Run
Now run the code and watch Rhys cut the grass.

```ghost
lawnmower.start();
loop.customRepeat(5,  function() {
    lawnmower.goUntil();
    lawnmower.returnToHouse();
    lawnmower.shiftLeft()
})
lawnmower.stop()
```
