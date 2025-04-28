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

Here's how it works...

`||agent:agent.inspect(AgentInspection.BLOCK, DIRECTION)||`

- `DIRECTION`: The direction you want your agent to inspect. The directions are UP, DOWN, LEFT, RIGHT, FORWARD and BACK.

Make the agent inspect down, and say the value stored in `block`!

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
```
