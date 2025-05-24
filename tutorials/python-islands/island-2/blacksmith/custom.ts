/**
 * Gives command to help the blacksmith.
 */
//% color=Grey weight=100 icon="\uf0e3" block="blacksmith"
namespace blacksmith {
    /**
    * Get purity of ore
    */
    //% block="purity %direction"
    //% direction.defl=FORWARD
    export function purity(direction: SixDirection): number {
        const block = agent.inspect(AgentInspection.Block, direction)
        switch(block){
            case IRON_ORE:
                return 4
            case 896:
                // raw_iron_block
                return 3
            case 153:  // Nether quartz ore
                return 2
            case 765: // Block of netherite
                return 1
            default:
                return 0
        }
    }

    /**
    * Deny the ore.
    */
    //% block="Deny Ore"
    export function deny():void {
        agent.setSlot(2)
        agent.place(UP)
    }

    /**
    * Accept the ore.
    */
    //% block="Accept Ore"
    export function accept():void {
        agent.setSlot(1)
        agent.place(UP)
    }
}