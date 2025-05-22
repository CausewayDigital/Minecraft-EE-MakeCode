### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Bounce

```customts
namespace blocks {
    /**
    * Check if a block is under a position
    */
    //% block"Is the block %block under %pos"
    //% block.defl=SLIME_BLOCK
    export function isUnder(block: Block, pos: Position): boolean {
        for (let y = 0; y < 10; y++) {
            const yPos = pos.getValue(Axis.Y) - y
            const checkPos = world(pos.getValue(Axis.X), yPos, pos.getValue(Axis.Z))
            if (blocks.place(block, checkPos)){
                return true
            }
        }
        return false
    }
}
```

## Finish the Telescope @showdialog

The new telescope has been put up, but they need to attach the final beacon to complete the build. Can you jump up and place it?

To help you jump a little higher, you will learn how to "levitate" to give you a bit of an extra boost, each time you bounce!

![Image of telescope build](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/bounce/cover.jpg)

## Step 1

First you'll need to create a function that will be triggered when we bounce. To do this we'll first create a function called `on_player_bounced()`

** Create a function called `on_player_bounced()`**

```python
def on_player_bounced():
    # Code will go here later
    pass
```

## Step 2

Now we have a function we need to know where the place was when the function was triggered, to do this we'll add a *variable* called `loc` and assign it ``||player:player.position()||``.

```python
def on_player_bounced():
    loc = player.position()
```

## Step 3

We only want to give the helping boost when we've bounced on slime block. To do this, the builders have given you a special function called ``||blocks:blocks.is_under()||`` which takes two inputs, first a block type, such as `SLIME_BLOCK` and the second being the location under we want to check.

**After the `loc` you added in the last step add in a new variable called `block_under` and set it to ``||blocks:blocks.is_under()||`` passing in the two variables `SLIME_BLOCK` and our variable `loc`**.

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
```

## Step 4

Now we want to use a ``||logic:if||`` statement to check if the variable `block_under` we set in the last step is `True`.

** Create an ``||logic:if||`` for when `block_under` is `True`**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        # We'll add some code here in the next step
```

## Step 5

If the ``||logic:if||`` statement is `True` we first need to need to know our `target`, to do this, we can variable for the `target` of who will be affected by our levitate effect.

For this we can use ``||mobs:mobs.target(NEAREST_PLAYER)||`` to find the nearest play, (you) to apply the effect onto.

**To do this lets create a new variable called `target` and we can use ``||mobs:mobs.target(NEAREST_PLAYER)||``**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        target = mobs.target(NEAREST_PLAYER)
```

## Step 6

Now we know know our `target` we can use ``||mobs:mobs.apply_effect()||`` to apply the effect.

To this we want to pass it in 4 parameters, first the affect we want to use, which is `LEVITATION`. Second is the target, which will be `target` variable we set in the last step. Third is the duration the effect lasts for of `1` second, and finally is amplifier which is how strong we want the effect to be.

**Add ``||mobs:mobs.apply_effect()||`` to run if it's `True`**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        target = mobs.target(NEAREST_PLAYER)
        mobs.apply_effect(LEVITATION, target, 1, 10)
```

## Step 7

The final step is to make sure the game triggers our code when we travel, to do this we can use ``||player:player.on_travelled()||``. This this two parameters the mode of travel which is `BOUNCE` for us to get up onto the telescope, and the second being the name of the function we want to trigger.

**At the end of your code outside of the function we created add in ``||player:player.on_travelled()||`` with the parameters of `BOUNCE` and the name of our function `on_player_bounced` that we made**

```python
def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        target = mobs.target(NEAREST_PLAYER)
        mobs.apply_effect(LEVITATION, target, 1, 10)

player.on_travelled(BOUNCE, on_player_bounced)
```

## place the beacon!

Nice! Now that you have the code complete. Test it out and see if you can get onto the antenna to place the beacon!

*Note - You can modify the duration and amplifier for the `LEVITATION` effect if you are finding the jumping is a little difficult.*

![Bounce path](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-5/bounce/bounce_path.jpg)

*Above is the recommended bouncing path.*