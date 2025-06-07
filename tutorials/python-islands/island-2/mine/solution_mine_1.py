# Run multiple times until agent detects unstable ground
if agent.check_ground_unstable():
    agent.alert()
agent.move(FORWARD, 1)

