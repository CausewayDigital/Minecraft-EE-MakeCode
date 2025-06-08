# Positions agent above the first piece of cobblestone
agent.move(FORWARD, 1)

# Gets all the gold in a row, then click the button to move agent to the next row and run all the code again
for i in range(3):
    for dig in range(3):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        if agent.inspect(AgentInspection.BLOCK, DOWN) == GOLD_ORE:
            agent.destroy(DOWN)
    agent.move(UP, 3)
    agent.move(FORWARD, 2)