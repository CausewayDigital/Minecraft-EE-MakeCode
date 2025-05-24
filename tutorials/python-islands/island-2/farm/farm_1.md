### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Farm

```customts
/**
* Funcitons accept and deny
*/
namespace agent {
    //% block
    export function accept(): void {
        agent.set_slot(1)
        agent.place(UP)
    }

    //% block
    export function deny(): void {
        agent.set_slot(2)
        agent.place(UP)
    }
    
}
```

## Carrot and Wheat Checking @showdialog
Help remove the carrots from the wheat farm!
Peter had some of his wheat and carrot seeds mixed up while planting them. As your agent can detect **any** block, it can be programmed to check the seeds. Let's get started!
![Cover image of Peter](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/farm/PeterCover.png)

Peter has two special functions you can use to mark the seeds:

- `agent.accept()`: Marks a wheat seed below.

- `agent.deny()`: Marks a carrot seed below.

## Move Your Agent

Move your agent forward 3 blocks to the first seed marked by the white marker.

```python
agent.move(DIRECTION, BLOCKS)
```
 
- `DIRECTION`: The direction you want your agent to inspect. The directions are UP, DOWN, LEFT, RIGHT, FORWARD and BACK.
- `BLOCKS`: The number of blocks you want you agent to move in the direction specified.

## Inspect Blocks With Your Agent
Now that your agent is above some seeds. Let's inspect what seeds they are! Your agent can inspect blocks using `||agent:agent.inspect||`:

Make the agent inspect down, and say the value stored in `block`!

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
```

## If Statement Reminder @showdialog

From our last step, the agent outputted the seed that is detected, which was `WHEAT`. Now we want to make some code that will choose what to do when your agent finds wheat. For this, we will use an `if` statement. 
Here's a reminder of what it looks like:

```python
if (condition):
    # Code to run if condition is true
```

**Remember we use one = sign to assign the value of a variable and two (==) for comparison, to check if the value of those variables are equal.**

For example:

```python
name = "bob"
if (name == "bob"):
    say("It's bob!")
```

## Using Inspect with If
Add the code that you want to run bellow the if statement indented once to the right.

`||logic:if (condition):||`
        # Do something

Create an `||logic:if||` statement to check if the block is *equal to* `WHEAT`. If it is, run `||agent:agent.accept||`.

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
if block == WHEAT:
    agent.accept()
```


## Else Statement Reminder @showdialog
Great! Now with all that together, we can use an `else` statement to deny any blocks that are not wheat.
Here's a reminder of what an `else` statement looks like...
```python
if (condition):
    # Code to run if condition is true
else:
    # Code to run if condition is NOT true
```

For example:

```python
name = "bob"
if (name == "bob"):
    say("It's bob!")
else:
    say("It isn't bob!")
```

## Add an Else Statement
`||logic:if (condition):||`
        # Do something
`||logic:else:||`
        # Do something else

Add an else statement to your code that runs the `||agent:deny||` function.

```python
if block == WHEAT:
    agent.accept()
else:
    agent.deny()
```

## Repeat for the Rest
Now you have added the `||logic:else||` statement, run your code a few times to get your agent to the end of the field. Then when you have checked all four spots, Peter will want to have a chat with you.
