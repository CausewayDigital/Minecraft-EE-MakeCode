/**
 * Telescope
 */
//% color=purple weight=100 icon="\uf002" block="Telescope"
namespace telescope {
    /**
    * Tells your agent to start building the towers.
    */
    //% block"Build Tower"
    export function start_building() {
        agent.teleport(world(1018,159,79), NORTH)
        build_tower()  // user function
        loops.pause(2000)
        let timer = 0
        while (timer < 30) {
            if (blocks.testForBlock(EMERALD_BLOCK, world(1027,154,60))){
                // Tower A
                agent.teleport(world(1009,159,70), NORTH)
                build_tower()
                // Tower B
                agent.teleport(world(1027,159,70), NORTH)
                build_tower()
                break
            }
            if (blocks.testForBlock(NETHER_WART_BLOCK, world(1027,154,60))) {
                player.say("There seems to be an issue with the tower")
                throw "Issue with your build_tower, please fix"
            } else {
                loops.pause(1000)
                timer ++
            }
        }
        if (timer === 30) {
            player.say("There seems to be an issue with the tower function")
            player.say("Reset the tower with the builder and start again")
            throw "Issue with your build_tower, please fix"
        }
    }
}

namespace agent {
    /**
    * Has your agent draw a square with block in its inventory
    */
    //% block"Draw Square $size"
    export function draw_square(size: number){
        [FORWARD, RIGHT, BACK, LEFT].forEach((dir) => {
            for(let pos = 0; pos < size-1; pos++){
                agent.place(DOWN)
                agent.move(dir, 1)
            }
        })
    }
}