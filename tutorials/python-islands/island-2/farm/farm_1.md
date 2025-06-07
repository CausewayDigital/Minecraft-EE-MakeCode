### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Farm

```customts
/**
* Functions approve and reject
*/
namespace agent {
    /**
    * Mark the seed below as wheat
    */
    //% block
    export function approve(): void {
        agent.setSlot(1)
        agent.place(UP)
    }

    /**
    * Mark the seed below as carrot
    */
    //% block
    export function reject(): void {
        agent.setSlot(2)
        agent.place(UP)
    }
    
}
```

## Carrot and Wheat Checking @showdialog
Help remove the carrots from the wheat farm!
Peter had some of his wheat and carrot seeds mixed up while planting them. As your agent can detect **any** block, it can be programmed to check the seeds. Let's get started!
![Cover image of Peter](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/farm/PeterCover.png)

Peter has two special functions you can use to mark the seeds:

- `agent.approve()`: Approves the seed below (as a wheat seed)

- `agent.reject()`: Rejects the seed below (as a carrot seed)
## Move Your Agent

**Move your agent forward 3 blocks to the first seed marked by the white marker.**   
   
**Do not run your code just yet!**

```python
agent.move(FORWARD, 3)
```

## Inspect Blocks With Your Agent
Now that your agent is above some seeds. Let's inspect what seeds they are. Your agent can inspect blocks using `||agent:agent.inspect(AgentInspection.BLOCK, DIRECTION)||`:

**Make the agent inspect down, store the result in a new variable called `block`.**
**Then `say` the value stored in the `block` variable.**

```python
agent.move(FORWARD, 3)
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
Add the code that you want to run below the if statement, indented once to the right.

`||logic:if (condition):||`
        # Do something

**Create an `||logic:if||` statement to check if the block is *equal to* `WHEAT`. If it is, run `||agent:agent.approve()||`.**

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
if block == WHEAT:
    agent.approve()
```


## Else Statement Reminder @showdialog
Great! Now with all that together, we can use an `else` statement to reject any blocks that are not wheat.
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

Add an else statement to your code that runs the `||agent:reject||` function.

```python
if block == WHEAT:
    agent.approve()
else:
    agent.reject()
```

## Repeat for the Rest
Now you have added the `||logic:else||` statement, run your code a few times to get your agent to the end of the field. Then when you have checked all four spots, Peter will want to have a chat with you.
