### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Plant

```customts
/**
 * Scientist
 */
//% color=purple weight=100 icon="\uf0c3" block="Scientist"
namespace scientist {
    /**
    * Gets the hydration of a plant.
    */
    //% block
    export function getHydration(plant: any): string {
        if (plant == ORANGE_TULIP) {
            return "hydration 8"
        }
        
        if (plant == OAK_SAPLING) {
            return "hydration : 3"
        }
        
        if (plant == 32) {
            return "hydration : 0"
        }
        
        return "Unknown : 0"
    }

    /**
    * Gets the nutrition of a plant.
    */
    //% block
    export function getNutrition(plant: any): string {
        if (plant == ORANGE_TULIP) {
            return "nutrition 4"
        }
        
        if (plant == OAK_SAPLING) {
            return "nutrition : 5"
        }
        
        if (plant == 32) {
            return "nutrition : 7"
        }
        
        return "Unknown : 0"
    }

    /**
    * Gets the strength of a plant.
    */
    //% block
    export function getStrength(plant: any): string {
        if (plant == ORANGE_TULIP) {
            return "strength 3"
        }
        
        if (plant == OAK_SAPLING) {
            return "strength : 5"
        }
        
        if (plant == 32) {
            return "strength : 6"
        }
        
        return "Unknown : 0"
    }

    /**
    * A scientist will check the information you provide.
    */
    //% block
    export function submit(answer: any[]) {
        let block = answer[0]
        if ([ORANGE_TULIP, OAK_SAPLING, 32].indexOf(block) < 0) {
            player.say("Hmmm, we aren't currently studying that...")
            player.say("Are you sure you are looking at the correct block?")
            return
        }
        
        let proof: any[] = [block, getHydration(block), getNutrition(block), getStrength(block)]

        if (answer[0] == proof[0] && answer[1] == proof[1] && answer[2] == proof[2] && answer[3] == proof[3]) {
            for (let e of answer) {
                player.say("Match")
            }
            player.say("Great! Matches perfectly...")
            blocks.place(DIAMOND_BLOCK, world(1054, 154, 139))
        } else if (answer.sort() == proof.sort()) {
            player.say("Hmmm, does not seem to be in the right order. Try again...")
        } else {
            player.say("Hmmm, information does not match up. Try again...")
        }  
    }
    
}
```

## Plant Processing @showdialog

The scientists at the Space Research Centre need to select the correct plants to send into space. Your Agent has been given a special device, to allow it to get the properties of the plants. This will allow it to check if they may thrive in space.   

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-6/plant/cover.png)

## Inspect the Block Bellow
**Use `||agent:agent.inspect||` to inspect the block in the down direction and store it in a variable called `block`.**

**Then output the block using `||player:player.say||`.**

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)
```

## Lists @showdialog
In Python we can create a list called `my_list` like this:

```python
my_list = ["A", "B", "C", "D"]
```

All of the items within the list are within square brackets and are seperated with commas.

You can also put variables in the list.

## The Scientists' Functions @showdialog
The scientist has a few functions that you can use to get information about certain plants:

`||scientist:scientist.get_hydration||`

`||scientist:scientist.get_nutrition||`

`||scientist:scientist.get_strength||`

They all take a block as a parameter (which you might get by using `||agent:agent.inspect||`).

## Get the Hydration, Nutrition, and Strength
**Create variables `hydration`, `nutrition`, and `strength` that contain the information returned by their respective functions.**

```python
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)

hydration = scientist.get_hydration(block)
nutrition = scientist.get_nutrition(block)
strength = scientist.get_strength(block)
```

## Information About a Plant
**Create a list containing `block`, `hydration`, `nutrition`, and `strength` in that order and use the `||scientist:scientist.submit||` function to check it against the scientists' results.**

```python
plant_info = [...]

scientist.submit(plant_info)
```
