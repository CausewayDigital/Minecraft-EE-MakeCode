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
        if (plant == "red_flower") {
            return "hydration 8"
        }
        
        if (plant == "sapling") {
            return "hydration : 3"
        }
        
        if (plant == "deadbush") {
            return "hydration : 0"
        }
        
        return "Unknown : 0"
    }

    /**
    * Gets the nutrition of a plant.
    */
    //% block
    export function getNutrition(plant: any): string {
        if (plant == "red_flower") {
            return "nutrition 4"
        }
        
        if (plant == "sapling") {
            return "nutrition : 5"
        }
        
        if (plant == "deadbush") {
            return "nutrition : 7"
        }
        
        return "Unknown : 0"
    }

    /**
    * Gets the strength of a plant.
    */
    //% block
    export function getStrength(plant: any): string {
        if (plant == "red_flower") {
            return "strength 3"
        }
        
        if (plant == "sapling") {
            return "strength : 5"
        }
        
        if (plant == "deadbush") {
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
        if ([POPPY, OAK_SAPLING, 32].indexOf(block) < 0) {
            player.say("Hmmm, we aren't currently studying that...")
            player.say("Are you sure you are looking at the correct block?")
            return
        }
        
        let proof = [block, getHydration(block), getNutrition(block), getStrength(block)]
        if (proof == answer) {
            for (let e of answer) {
                player.say("{e} - Match")
            }
            player.say("Great! Matches perfectly...")
            //  world.set("1054 154 139", "barrier")
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
