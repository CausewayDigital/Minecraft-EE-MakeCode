### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Wire

```customts
namespace positions {
    /**
    * Provides a corrected location
    */
    //% block"Correct Location %pos"
    export function correctLocation(pos: Position) {
        const y = pos.getValue(Axis.Y)-1
        return world(pos.getValue(Axis.X), y, pos.getValue(Axis.Z))
    }
}

namespace agent {
    /**
     * Allows your agent to place down wire.
     */
    //% block="agent place wire %direction"
    //% direction.defl=DOWN
    export function placeWire(direction: SixDirection) {
        agent.setSlot(1)
        if (direction !== DOWN) {
            return
        }
        const agentLoc = agent.getPosition()
        const y = agentLoc.getValue(Axis.Y)-1
        const blockTest = blocks.testForBlock(AIR, world(agentLoc.getValue(Axis.X), y, agentLoc.getValue(Axis.Z)))
        if (blockTest){
            agent.place(DOWN)
        }
    }
}
```

```ghost
function test() {
    return
}

player.onTravelled(WALK, function () {
    let loc = player.position()
    loc = positions.correctLocation(loc)
    agent.teleport(loc, NORTH)
    agent.placeWire(DOWN)
})

```

## Wire to the Power Station @showdialog

With the telescope built and ready to start searching the stars, the final thing it needs is power! You need to hook up a wire between the Power Station and the transformer building on the telescope island.

As the wire is fragile, you will use your agent to do this.

Could you program your Agent to follow you along the bridge and place down the wire as it does?

![Picture of Power station](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/wire/cover.jpg)

## Step 1

To begin, you'll need to create a function that will run every time you move. To do this we first need to make a function that Minecraft will call when we move, we'll call this `on_travelled_walk()`.

**Can you start by creating a function called `on_travelled_walk()`**

```python
def on_travelled_walk():
    # We'll add code here in the steps to come
    pass
```

## Step 2

Now your program will need to know where you've walked, to do this we'll add a *variable* called `loc` and assign it ``||player:player.position()||``.

```python
def on_travelled_walk():
    loc = player.position()
```

## Step 3
As you walk, you need to get the exact location for your Agent to place down the wire. For this, we can use the `loc` variable we just added.

To correct the location for the Agent to use, we'll run the `||positions:positions.correct_location()||` function and pass in our `loc` variable. Then storing the result as our new `loc`.

**On a new line, set `loc`, to equal to the `||positions:positions.correct_location()||` function and pass our `loc` variable as the `position`.**

```python
def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
```

## Step 4
The next step is to teleport your Agent to the corrected position. To teleport your Agent you can use ``||agent:agent.teleport()||``.

**Add the code to teleport your Agent to our `loc` variable facing `NORTH`.**

```python
def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
    agent.teleport(loc, NORTH)
```

## Step 5
The last step is to have your Agent place down the wire to make the connection.

The Power Station staff have already given your Agent some wire and a function that allows your agent to place the wire. All you need to do is use ``||agent:agent.place_wire()||`` to place it `DOWN`.

**Add an ``||agent:agent.place_wire||`` below so it places `DOWN`.**

```python
def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
    agent.teleport(loc, NORTH)
    agent.place_wire(DOWN)
```

## Step 5
The final step is to make sure the game triggers our code when we travel, to do this we can use ``||player:player.on_travelled()||``. This two parameters the mode of travel which is `WALK` for us to lay the wire, and the second being the name of the function we want to trigger.

**At the end of your code outside of the function we created add in ``||player:player.on_travelled()||`` with the parameters of `WALK` and the name of our function `on_travelled_walk` that we made**

## Start placing wire!

When you're ready, run your code and slowly walk on the path to the right of the bridge, so your Agent will follow and place the wire. You should start from the "**External Power Station Plug**".
