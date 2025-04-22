/**
 * Functions for working in the Library
 */
namespace agent {
    /**
    * Checks if the Spellbook is in shelf
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function found_book(direction: SixDirection): boolean {
        let block = agent.inspect(AgentInspection.Block, direction)
        if (block === DEAD_BRAIN_CORAL_BLOCK) {
            return true
        }
        return false
    }

    /**
     * Marks the shelf the Spellbook is in
     */
    //% block="agent mark book %direction"
    //% direction.defl=FORWARD
    export function mark_book(direction: SixDirection){
        if(direction === FORWARD){
            agent.place("back", 1)
        }else{
            player.say("Seems like the agent can only mark facing forward of the bookshelf")
        }
    }
}