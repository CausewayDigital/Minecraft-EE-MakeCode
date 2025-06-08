# Run this to get all poppies from a row
while agent.get_item_count(1) < 4:
    agent.move(FORWARD, 1)
    if agent.check_flower(DOWN) == POPPY:
        agent.destroy(DOWN)

# Use this to move an agent to the next row (you may need to replace LEFT with RIGHT)
agent.turn_left()
agent.turn_left()
agent.move(LEFT, 1)