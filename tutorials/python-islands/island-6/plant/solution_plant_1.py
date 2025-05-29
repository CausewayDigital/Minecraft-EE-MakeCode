block = agent.inspect(AgentInspection.BLOCK, DOWN)
player.say(block)

hydration = scientist.get_hydration(block)
nutrition = scientist.get_nutrition(block)
strength = scientist.get_strength(block)

plant_info = [block, hydration, nutrition, strength]

scientist.submit(plant_info)
