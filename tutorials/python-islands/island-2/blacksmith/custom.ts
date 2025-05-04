/**
 * Gives command to help the blacksmith.
 */
//% color=Grey weight=100 icon="\uf0e3" block="blacksmith"
namespace blacksmith {
    /**
    * Get purity of ore
    */
    //% block"Purity %direction"
    //% direction.defl=FORWARD
    export function purity(direction: SixDirection): number {
        block = agent.inspect(AgentInspection.Block, direction)
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
    * Accept the ore.
    */
    //% block"Accept Ore"
    export function accept(): void {
        agent.setSlot(1)
        agent.place(UP)
    }

    /**
    * Deny the ore.
    */
    //% block"Deny Ore"
    export function deny(): void {
        agent.setSlot(2)
        agent.place(UP)
    }
}