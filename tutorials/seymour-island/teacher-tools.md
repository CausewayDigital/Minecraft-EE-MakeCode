

### @flyoutOnly 1

# Teacher tools

```template
//  Player teleporter program
//  This program teleports all students to a starting boat.
//  Once run with the play button, type "run" to launch the program.
let base_x = -853
let base_y = 64
let base_z = 292
function make_ships() {
    let i: number;
    let ships = []
    for (i = 1; i < 11; i++) {
        ships.push([base_x - i * 50, base_y, base_z])
    }
    for (i = 1; i < 11; i++) {
        ships.push([base_x - i * 50, base_y, base_z - 70])
    }
    for (i = 1; i < 11; i++) {
        ships.push([base_x - i * 50, base_y, base_z - 140])
    }
    return ships
}

player.onItemInteracted(DIAMOND_SWORD, function tp_ships() {
    let ships = make_ships()
    for (let i = 0; i < 30; i++) {
        player.execute("tp @e[x=-867,y=119,z=370,r=20,c=1,type=player] " + ("" + ships[i][0]) + " " + ("" + ships[i][1]) + " " + ("" + ships[i][2]) + " ")
    }
})


```

# Teacher tools

## Teacher tools @unplugged

Welcome to Seymour Island. Once all your students have made it into the world, hit the play button below and right click while holding your diamond sword.   
This will distribute all the students onto their individual ships, ready to go! 
## Boats
Hit the play button and right click with your switch to distribute all your students onto their boats.   


```package
seymour=github:gbaman/minecraft-ee-seymour-island
```
