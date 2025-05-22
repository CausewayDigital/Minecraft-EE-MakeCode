/**
 * Functions for working in the mine
 */
namespace agent {
    /**
    * Checks if the ground below the agent is stable
    */
    //% block="agent check ground stable"
    export function check_ground_stable(): boolean{
        const agent_pos = agent.getPosition()
        if (positions.equals(agent_pos, world(88, 146, 167))){
            return true
        }
        return false
    }

    /**
     * Alert ground bellow agent is unstable
     */
    //% block
    export function alert(){
        if(agent.check_ground_stable()){
            player.say("Unstable ground alert!!!")
            agent.destroy(DOWN)
        }else{
            player.say("This seems to be a false alarm, the ground below the agent seems pretty stable... Try moving to a different location")
        }
    }
}