

### @flyoutOnly 1

```template
// 
```

# Breaking blocks


# 1. Breaking blocks

## Breaking blocks @unplugged

Now we know how to move our Agent, the captain has asked if we can repair a damaged
section of the ship hull.   
We will need to collect a piece of wood to repair it with.    
Use the Agent to break the orange piece of wood in front of it.   
![Breaking block](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_0_break.gif)

## Breaking blocks
Use the ``||Agent:agent destroy||`` command to break the block we need to use to repair
the ship.

```blocks
agent.destroy(FORWARD)
```

```ghost
agent.move(LEFT)
```

```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
