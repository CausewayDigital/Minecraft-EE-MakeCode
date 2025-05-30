coordinates = []

for row in range(0, 4):
    for col in range(0,4):
        player.say(row)
        player.say(col)
        if agent.is_fossil_bellow():
            coordinates.append(agent.get_position())
        agent.move(FORWARD, 1)
    agent.move(BACK, 3)
    agent.move(LEFT, 1)
agent.move(RIGHT, 3)

scientist.check(coordinates)
