### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# If-Else

```customts
namespace gameplay {
    /**
    * Randomize the current weather
    */
    //% block
    export function randomWeather(): void {
        if (randint(0, 1) == 0) {
            gameplay.setWeather(CLEAR)
        } else {
            gameplay.setWeather(THUNDER)
        }
    }
}

namespace player {
    /**
    * Completes the task
    */
    //% block
    export function complete(): void {
        blocks.place(Block.DiamondBlock, world(112, 150, 194))
        player.say("Task complete")
    }
}
```

```template
gameplay.randomWeather();

if (THUNDER) {
    player.say("");
}
```

## Making decisions in Python @showdialogue

It is common in programming to need to make a decision. In a decision, you want to run some code `||logic:if||` a condition is `||logic:True||`.  

For example, a common decision we have to make all the time is whether to put a rain coat on.     

If it is raining ---> then we should put a coat on!

In Python, we can approach this like below:

```python
if gameplay.weather_query() == RAIN:
    player.say("Put on a coat!")
```

## If Statement

Finish off the program below to check if the `||gameplay:gameplay.weather_query()||` is `||THUNDER||`. Add a message to `||player:player.say||` on line 2, if there is thunder.

```python
if gameplay.weather_query() == THUNDER:
    player.say("Thunder!")
```

## What about if it isn't raining? @showdialogue

We have covered how to handle if something is the case, but what if it isn't?   

What if it isn't raining?

To hand if it is not, we use an `||logic:else||`. `||logic:Else||` allows code to be run **if all else fails** as such.   

Here is an example:

```python
if gameplay.weather_query() == RAIN:
    say("Put on a coat!")
else:
    say("Just put on a jumper")
```

## Else statement

Finish off the program to send a different appropriate message if there is no `||THUNDER||`.

```python
if gameplay.weather_query() == THUNDER:
    player.say("Thunder!")
else:
    player.say("There is no thunder :)")
```

## Indentation

Indentation is the number of blank spaces at the start of a line. In Python, indentation is used to signify which pieces of code are contained within which structure.

**Run the `||player:player.complete||` function to complete the task. Make sure it isn't indented so it will definitely run.**

```python
if gameplay.weather_query() == THUNDER:
    player.say("Thunder!")
else:
    player.say("There is no thunder :)")
player.complete()
```
