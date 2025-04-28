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
    export function accept(): void {
        agent.set_slot(1)
        agent.place(UP)
    }

    export function deny(): void {
        agent.set_slot(2)
        agent.place(UP)
    }
    
}
```

```template
// Start of user code
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
if ( block == ) {
    // Fill in the condition above
    agent.accept() 
}
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
Complete the `||logic:if||` to check if the block is *equal to* `WHEAT`.

```python
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
Add an else statement to your code that runs the deny function.

```python
if block == WHEAT:
    agent.accept()
else:
    agent.deny()
```

## Repeat for the Rest
Now you have added the else statement, move your agent forward 3 blocks foward and run the same check.

Now run your code a few times to get your agent to the end of the field. Then when you have checked all four spots, Peter will want to have a chat with you.

```python
agent.move(DIRECTION, BLOCKS)
```
