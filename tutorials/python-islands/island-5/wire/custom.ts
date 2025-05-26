namespace positions {
    /**
    * Provides a corrected location
    */
    //% block"Correct Location %pos"
    export function correctLocation(pos: Position) {
        const y = pos.getValue(Axis.Y)-1
        return world(pos.getValue(Axis.X), y, pos.getValue(Axis.Z))
    }
}

namespace agent {
    /**
     * Allows your agent to place down wire.
     */
    //% block="agent place wire %direction"
    //% direction.defl=DOWN
    export function placeWire(direction: SixDirection) {
        agent.setSlot(1)
        if (direction !== DOWN) {
            return
        }
        const agentLoc = agent.getPosition()
        const y = agentLoc.getValue(Axis.Y)-1
        const blockTest = blocks.testForBlock(AIR, world(agentLoc.getValue(Axis.X), y, agentLoc.getValue(Axis.Z)))
        if (blockTest){
            agent.place(DOWN)
        }
    }
}

