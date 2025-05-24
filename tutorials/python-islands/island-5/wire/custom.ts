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

agent.setSlot(1)