### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Tower

```customts
/**
 * Telescope
 */
//% color=purple weight=100 icon="\uf002" block="Telescope"
namespace telescope {
    /**
    * Tells your agent to start building the towers.
    */
    //% block"Build Tower"
    export function start_building() {
        agent.teleport(world(1018,159,79), WEST)
        build_tower()  // user function
        loops.pause(2000)
        let timer = 0
        while (timer < 30) {
            if (blocks.testForBlock(EMERALD_BLOCK, world(1027,154,60))){
                // Tower A
                agent.teleport(world(1009,159,70), WEST)
                build_tower()
                // Tower B
                agent.teleport(world(1027,159,70), WEST)
                build_tower()
                break
            }
            if (blocks.testForBlock(NETHER_WART_BLOCK, world(1027,154,60))) {
                player.say("There seems to be an issue with the tower")
                throw "Issue with your build_tower, please fix"
            } else {
                loops.pause(1000)
                timer ++
            }
        }
        if (timer === 30) {
            player.say("There seems to be an issue with the tower function")
            player.say("Reset the tower with the builder and start again")
            throw "Issue with your build_tower, please fix"
        }
    }
}

namespace agent {
    /**
    * Has your agent draw a square with block in its inventory
    */
    //% block"Draw Square $size"
    export function draw_square(size: number){
        [FORWARD, RIGHT, BACK, LEFT].forEach((dir) => {
            for(let pos = 0; pos < size-1; pos++){
                agent.place(DOWN)
                agent.move(dir, 1)
            }
        })
    }
}
```

```template

// Write your code above this line
telescope.start_building()
```

## Building the Support towers @showdialog
The local builders have the new telescope ready but need supports built to hold the dish! Help them by building the supports so that they can set up the telescope.

![The telescope](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/tower/cover.jpg)

## Introduction

For this task, we will use `functions`. `Functions` are mini-programs of code, that can be called/ran as many times as you want in your main program. For example, `player.say()` is a function that you call/run to output text into the chat.

As you go through these exercises below, the builders will test and run your function for you.

## Step 1

The builders have asked you to create a `function` called `"build_tower()"`.

do do this we can do we can do ``||functions:def build_tower()||``.

- `def`: Tells Python you want to create a new function.
- `build_tower()`: The name of the new function. You can run the code inside of it by putting `build_tower()` in your code.

```python
def build_tower():
    # Something will go here later
    pass
```

## Step 2

Now that you have the `function` set up, we need it to build a tower that is `15` blocks high. To do this, we need to use a ``||loops:for||`` loop that will run `15` times.

When adding code into a function in Python all the code that runs as part of the function need to be *indented*, this means a 4 spaces needs to be at the start of the line.

**Add a ``||loops:for||`` loop that counts from `0` to `15`.**

```python
def build_tower():
    for height in range(0, 15):
        # Something will go here later
        pass
```

## Step 3

*Note, your Agent will automatically teleport to the diamond block when you start your code.*

After you have the ``||loops:for||`` loop set up, we need to move the Agent up one block each iteration, to build all of the layers for the tower.

**Have your Agent ``||agent:move||`` `UP` `1` block within the for loop.**

```python
def build_tower():
    for height in range(0, 15):
        agent.move(UP, 1)
```

## Step 4

Now each time your Agent moves up, you can build a new layer of the tower. To do this we use the ``||agent:draw_square()||`` function. This allows you to build a square at the point your Agent is standing.

``||agent:draw_square()||`` takes a single input that's the width of the square. For example, 5 for a 5x5 layer.

**Add to your code to run the `draw_square()` function with a width of `3`.**

```python
def build_tower():
    for height in range(0, 15):
        agent.move(UP, 1)
        agent.draw_square(3)
```

## Run your code
When you're done, run your code and, the builders will use your Agent to build the towers.
