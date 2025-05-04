/**
 * Gives command to help the blacksmith.
 */
//% color=Grey weight=100 icon="\uf0e3" block="blacksmith"
namespace blacksmith {
    /**
    * Get purity of ore
    * @param direction Direction to got agent to check in
    */
    //% blockId=blacksmithPurity
    //% block="purity %direction"
    //% direction.shadow=minecraftAgentSixDirection
    export function purity(direction: number): number {
        const block = agent.inspect(AgentInspection.Block, direction)
        switch(block){
            case IRON_ORE:
                return 4
            case 896:
                // raw_iron_block
                return 3
//            case raw_copper_block:
//                return 2
//            case raw_gold_block:
//                return 1
            default:
                return 0
        }
    }

    /**
    * Deny the ore.
    */
    //% block="deny ore"
    export function deny():void {
        agent.setSlot(2)
        agent.place(UP)
    }

    /**
    * Accept the ore.
    */
    //% block="accept ore"
    export function accept():void {
        agent.setSlot(1)
        agent.place(UP)
    }
}