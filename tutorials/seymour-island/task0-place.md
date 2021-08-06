

### @flyoutOnly 1

# Repair

```template
player.onItemInteracted(BLAZE_ROD, function () {
})
```

# 1. Repair

## Repair @unplugged

Now we have some wood for the repair, move the agent over to the area to be repaired.      
![Agent repair](https://github.com/gbaman/minecraft-ee-seymour-island/raw/master/media/task0-place.gif)

## Move
First, move your agent over to on top of the far golden block.   
Then hit next.      

```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    agent.move(LEFT, 3)
})
```

## Repair
Then use the ``||Agent:agent place left||`` command to place the wood block we just collected
to repair the hull of the ship

```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    agent.move(LEFT, 3)
    agent.place(LEFT)
})

```

```package
seymour=github:gbaman/minecraft-ee-seymour-island
```
