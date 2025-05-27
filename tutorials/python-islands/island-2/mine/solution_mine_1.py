agent.move(RIGHT, 1)
for i in range(3):
    if agent.check_ground_unstable():
        agent.alert()
    agent.move(FORWARD, 1)
if agent.check_ground_unstable():
        agent.alert()
agent.move(LEFT, 1)

for i in range(3):
    if agent.check_ground_unstable():
        agent.alert()
    agent.move(BACK, 1)
if agent.check_ground_unstable():
        agent.alert()
agent.move(LEFT, 1)

for i in range(3):
    if agent.check_ground_unstable():
        agent.alert()
    agent.move(FORWARD, 1)
if agent.check_ground_unstable():
        agent.alert()
