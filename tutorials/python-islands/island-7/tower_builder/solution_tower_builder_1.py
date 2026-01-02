def create_layer():
    agent.set_slot(1)
    for sides in range(4):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.turn_right()

agent.set_item(STONE, 64, 1)
agent.set_item(GLOWSTONE, 1, 2)

for i in range(3):
    agent.move(UP, 1)
    create_layer()

agent.move(RIGHT, 1)
agent.set_slot(2)
agent.place(FORWARD)