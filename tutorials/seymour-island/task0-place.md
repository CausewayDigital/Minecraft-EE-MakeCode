

### @flyoutOnly 1

```template
// 
```

# Repair

# 1. Repair

## Repair @unplugged

Now we have some wood for the repair, move the agent over to the area to be repaired.      
![Agent repair](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_0_place_move.gif)

## Move
First, move your agent over to on top of the far emerald (green) block.   
Then hit next.      

```blocks
agent.move(LEFT, 3)

```

## Repair @unplugged
Now that the agent is in the right place, place the wooden block to repair the hull of the ship.
![Agent repair](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/seymour-island/images/seymour_task_0_place.gif)

## Repair
Then use the ``||Agent:agent place left||`` command to place the wood block we just collected
to repair the hull of the ship.

```blocks

agent.move(LEFT, 3)
agent.place(LEFT)


```


```package
seymour=github:CausewayDigital/Minecraft-EE-MakeCode
```
