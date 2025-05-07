### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Rocket
Check the rocket is ready to launch

```template
let accepted_blocks = [COAL_BLOCK, CONCRETE, GRAY_STAINED_GLASS, BLOCK_OF_QUARTZ, QUARTZ_STAIRS, IRON_BARS];

let block = agent.inspect(AgentInspection.Block, FORWARD);

if () {
    // Complete the if statement above
    player.say("Accept")
    agent.accept()
}
```

```customts
namespace agent {
    /**
    * Mark the block as accepted for the scientists.
    */    
    //% block
    export function accept(): void {
        agent.set_active(1);
        agent.place(BACK);
    }

    /**
    * Mark the block as denyed for the scientists.
    */   
    //% block
    export function deny(): void {
        agent.set_active(2);
        agent.place(BACK);
    }
}

```

## Rocket Repairs @showdialog

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/rocket/cover.png)
The rocket needs to be checked for cracks! Use your agent to detect if there are any damaged/cracked blocks. If there are, you should mark these for repair.

## Checking Lists @showdialog

We need to check if the block in front of the agent is included in a list of `accepted_blocks` that was given to the agent from the scientist. These blocks are the acceptable state of each block.    

We can check each block very easily, using a keyword `in`. 

With `in` we can check if a value is **in a list**. If it is in the list, then it returns `True`. Here's an example:

```python
my_list = ["A", "B", "C", "D"]
if "B" in my_list:
    say("True!") # This would print "True!" as "B" is in my_list
```

## Step 1
**Use the 'in' keyword to complete the if statement to check if the 'block' is 'in' the 'accepted_blocks' list.**

`||logic:if item in list:||`

```python
if block in accepted_blocks:
    player.say("Accept")
    agent.accept()
```


## Step 2
With the accepted blocks noted and flagged up to the scientists, let's turn our attention to the deny blocks.

**Add an else statement to your code with `||player:player.say("Deny")||` and `||agent:agent.deny()||`.**

```python
if block in accepted_blocks:
    player.say("Accept")
    agent.accept()
else:
    player.say("Deny")
    agent.deny()
```

## Step 3
To wrap all of your code up, we're going to use a `for loop` to check each block above your Agent. The scientist has told you that the rocket is 26 blocks high.

**Wrap your 'if else' statement in a `||loops:for||` loop where at the end of your loop you use `||agent:agent.move||` to move your agent 'UP' 1 block. Your code should loop until the agent gets to the top of the rocket (26 times).** 

```python
for i in range(26):
    player.say("Looping 26 times.")
```

```ghost
agent.move(UP, 1)
```

```ghost
agent.accept()
agent.deny()
```

