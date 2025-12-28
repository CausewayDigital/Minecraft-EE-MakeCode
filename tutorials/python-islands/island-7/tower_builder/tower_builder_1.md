### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Tower Builder

```customts
agent.teleport(world(-517, 139, 712), WEST)
let agent_or = agent.getOrientation()
if (agent_or == EAST) {
    agent.turnLeft()
    agent.turnLeft()
}

if (agent_or == SOUTH) {
    agent.turnRight()
}

if (agent_or == EAST) {
    agent.turnLeft()
}
```

```template
function create_layer(): void{

}
```

## Introduction @showdialog

As an explorer, you need to be able to trace your steps to return to your base. In this exercise, you will build a program in Python that creates a tower by following two separate flowcharts:

- The first flowchart shows a function which creates a layer.
- The second flowchart uses this function to create a tower then glowstone is placed at the top of the tower.

### Layer Function

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-function.png)

### Main Flowchart

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart.png)

## Function - Part 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape-function_1.png)

Define the function provided to match the boxes in black.

```python
def create_layer():
    for i in range(4):
        pass
```

- Within the function named create_layer, create a for loop that **loops 4 times**

## Function - Part 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape-function_2.png)

Add to your function, within the loop, to make it match the flowchart.

```
```

- Place a stone (slot 1) down
- Move the agent forwards

## Function - Part 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape-function_3.png)

Add to your function, within the loop, to make it match the flowchart.

```
```

- Place a stone (slot 1) down
- Move the agent forwards
- Turn your agent right

## Main Code - Part 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_1.png)

Now below the function you have just created, code the piece of the flowchart shown in black.

```
```

- Give the agent 64 stone (slot 1)
- Give the agent 1 glowstone (slot 2)

## Main Code - Part 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_2.png)

Now create the loop shown in black.

```
```

- Create a loop that loops 3 times (the height of your tower)

## Main Code - Part 3

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_3.png)

Complete the loop with the code shown in black.

```
```

- Move your agent up one block
- Run the function you previously created

## Main Code - Part 4

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/tower_builder/images/flowchart-landscape_4.png)

Code the part of the flowchart shown in black to place glowstone at the top of your tower.

```
```

- Move your agent right
- Set active slot to 2
- Place glowstone forwards

```ghost
def create_layer():
    agent.set_slot(1)
    for sides in range(4):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.turn_right()

agent.set_item(STONE, 64, 1)
agent.set_item(GLOWSTONE, 1, 2)

for i in range(3):
    agent.move(UP, 1)
    create_layer()

agent.move(RIGHT, 1)
agent.set_slot(2)
agent.place(FORWARD)
```
