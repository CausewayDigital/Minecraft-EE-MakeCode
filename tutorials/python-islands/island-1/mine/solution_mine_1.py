# Moves the agent to and destroys the first piece of coal.
agent.move(UP, 2)
agent.move(LEFT, 1)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)

# From in front of the first piece of coal, moves the agent in front of, and destroys, the second piece of coal.
agent.move(RIGHT, 2)
agent.move(DOWN, 1)
agent.destroy(FORWARD)

# Third piece of coal.
agent.move(DOWN, 2)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
