/**
 * Provides the ability to decode the telescope feed.
 */
//% color=purple weight=100 icon="\uf002" block="Telescope"
namespace telescope {
    /**
    * Tells the Telescope to run your decode function.
    */
    //% block"Decode telescope bit signal"
    export function decode_signals(): void {
        // This is a bodge: makecode doesn't support Record<> for objects so `object[key]` doesn't work in the ts compiler
        const index_key = [WHITE_CONCRETE_POWDER, MAGENTA_CONCRETE_POWDER, LIGHT_BLUE_CONCRETE_POWDER, YELLOW_CONCRETE_POWDER]
        const index_value = ["a", "b", "c", "d"]
        // List of expected bits from user's decode() function
        const list_of_numbers: number[] = [1, 2, 4, 3, 2, 1]

        let counter = 0  // Counter used for checking how far we're through the message

        for(let bit_index = 0; bit_index < list_of_numbers.length; bit_index++){
            const bit = list_of_numbers[bit_index]
            const inspect = agent.inspect(AgentInspection.Block, FORWARD)
            // get block
            const block_key_index: number = index_key.indexOf(inspect)
            let block = "Z"
            if (block_key_index >= 0){
                block = index_value[block_key_index]
            }

            counter++
            const num = decode(block)  // Runs user's decode

            if (num === undefined) {
                throw "No number given! Please fix your function, or Reset Bit Input and try again."
            }
            player.say(`Decoded bit as : ${num}`)

            if (num !== bit) {
                player.say("Incorrect bit given!")
                throw "Incorrect bit! Please fix your function, or Reset Bit Input and try again."
            } else {
                if (counter === 6) {  // If we recieve the last bit
                    player.say("Received full all the data, task complete!")
                    player.say("Data: 1, 2, 4, 3, 2, 1")
                    loops.pause(1000)
                } else { // Load next bit
                    player.say("Loading Next Bit")
                }
                mobs.spawn(21, world(1007, 150, 132))  // 21 is a Snow Golem
            }
            loops.pause(1000)
        }
        mobs.spawn(21, world(1014, 148, 132))  // 21 is a Snow Golem
    }
}
