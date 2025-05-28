for i in range(4):
    for j in range(12):
        if agent.check_flower(DOWN) == POPPY:
            agent.destroy(DOWN)
        agent.move(FORWARD, 1)
    if i % 2 == 0:
        agent.turn_right()
        agent.move(FORWARD, 1)
        agent.turn_right()
    else:
        agent.turn_left()
        agent.move(FORWARD, 1)
        agent.turn_left()
    

