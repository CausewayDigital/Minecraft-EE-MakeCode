def on_travelled_walk():
    loc = player.position()
    loc = positions.correct_location(loc)
    agent.teleport(loc, NORTH)
    agent.place_wire(DOWN)
player.on_travelled(WALK, on_travelled_walk)
