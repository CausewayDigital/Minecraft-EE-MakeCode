for i in range(6):
    for j in range(5):
        if agent.check_book_on_shelf(FORWARD) == True:
            player.say("Found the book!")
            agent.mark_book(FORWARD)
        else:
            player.say("No book here!")
        agent.move(UP, 1)
    agent.move(DOWN, 5)
    agent.move(BACK, 1)
    agent.move(RIGHT, 2)
    agent.move(FORWARD, 1)
