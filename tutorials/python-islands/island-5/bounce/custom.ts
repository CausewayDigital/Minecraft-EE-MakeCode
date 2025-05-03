namespace blocks {
    /**
    * Check if a block is under a position
    */
    //% block"Is the block %block under %pos"
    //% block.defl=SLIME_BLOCK
    export function isUnder(block: Block, pos: Position): boolean {
        for (let y = 0; y < 10; y++) {
            const yPos = pos.getValue(Axis.Y) - y
            const checkPos = world(pos.getValue(Axis.X), yPos, pos.getValue(Axis.Z))
            if (blocks.place(block, checkPos)){
                return true
            }
        }
        return false
    }
}