agent.move(FORWARD, 1)
while agent.inspect(AgentInspection.BLOCK, DOWN) == AIR:
    agent.move(DOWN, 1)

agent.collect_all()

while agent.get_position().get_value(Axis.Y) != 157:
    agent.move(UP, 1)

agent.set_slot(1)
agent.place(DOWN)