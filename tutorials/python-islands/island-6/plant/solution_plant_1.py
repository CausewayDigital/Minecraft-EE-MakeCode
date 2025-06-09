# Run 3 times, once for each plant. The agent will move automaticall when you submit the correct info.
block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(blocks.name_of_block(block))

hydration = scientist.get_hydration(block)
nutrition = scientist.get_nutrition(block)
strength = scientist.get_strength(block)

plant_info = [block, hydration, nutrition, strength]

scientist.submit(plant_info)

