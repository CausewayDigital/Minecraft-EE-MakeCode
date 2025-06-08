# Removes the bottom level of logs
agent.destroy(FORWARD)
agent.move(FORWARD, 1)
agent.destroy(FORWARD)
agent.destroy(RIGHT)
agent.move(FORWARD, 1)
agent.destroy(RIGHT)
agent.move(BACK, 1)

# Removes the rest of the tree
for i in range(12):
    agent.destroy(UP)
    agent.move(FORWARD, 1)
    agent.destroy(UP)
    agent.move(RIGHT, 1)
    agent.destroy(UP)
    agent.move(BACK, 1)
    agent.destroy(UP)
    agent.move(LEFT, 1)
    agent.move(UP, 1)
