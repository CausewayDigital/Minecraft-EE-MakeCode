### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Factory - 2
Repair the airship

```template
while (agent == ) {
    // Complete the while loop above
    // Step 1
    agent.move(FORWARD, 1)

    // Step 2
    while (agent.inspect(AgentInspection.BLOCK, DOWN) == AIR) {
        agent.move(DOWN, 1)
    }

    // Step 3
    agent.collect_all()

    // Step 4
    while (agent.get_position().get_value(Axis.Y) != 157) {
        agent.move(UP, 1)
    }

    // Step 5
    agent.set_slot(1)
    agent.place(DOWN)
}
```

## Automate Fixing the Airship
Great, now that you have successfully guided your agent through fixing one block, let's put all of the previous code together into one big `while` loop to automate fixing the rest of the airship.

**Complete the outer while loop so that the outer while loop runs while `||agent:agent.inspect||` in the FORWARD direction is equal to `"AIR"`.**
```python
agent.inspect(AgentInspection.BLOCK, DIRECTION)
```

- `DIRECTION`: The direction that your agent will try to place a block. The directions you can use are: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.
