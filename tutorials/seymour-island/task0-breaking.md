

### @flyoutOnly 1

# Breaking blocks

```template
player.onItemInteracted(BLAZE_ROD, function () {
})

```

# 1. Breaking blocks

## Breaking blocks @unplugged

Now we know how to move our Agent, the captain has asked if we can repair a damaged
section of the ship hull.   
We will need to collect a piece of wood to repair it with.    
Use the Agent to break the orange piece of wood in front of it.   
![Breaking block](https://github.com/gbaman/minecraft-ee-seymour-island/raw/master/media/task0-break.gif)

## Breaking blocks
Use the ``||Agent:agent destroy||`` command to break the block we need to use to repair
the ship.

```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    agent.destroy(FORWARD)
})
```

```ghost
agent.move(LEFT)
```

```package
seymour=github:gbaman/minecraft-ee-seymour-island
```
