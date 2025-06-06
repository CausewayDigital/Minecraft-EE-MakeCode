# Moves and gets the first apple from the agents starting position
agent.move(BACK, 2)
agent.move(DOWN, 1)
agent.move(LEFT, 3)
agent.destroy(UP)

# Moves and gets the second apple, from where the agent is after running the code above (bellow the first apple)
agent.move(LEFT, 2)
agent.move(FORWARD, 1)
agent.move(UP, 1)
agent.destroy(UP)

# Third apple
agent.move(FORWARD, 3)
agent.destroy(UP)

# Fourth apple
agent.move(RIGHT, 2)
agent.move(BACK, 1)
agent.destroy(UP)

# Fifth apple
agent.move(FORWARD, 4)
agent.move(UP, 1)
agent.destroy(UP)
