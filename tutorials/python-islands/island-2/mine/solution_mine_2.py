# Walk over to an entrace of a mineshaft (use shift to crouch and go into it)
# Call your agent using your whistle
# Run the code below (and repeat for all the other mineshafts
agent.move(FORWARD, 4)
if agent.inspect(AgentInspection.BLOCK, FORWARD) == IRON_ORE:
    agent.destroy(FORWARD)