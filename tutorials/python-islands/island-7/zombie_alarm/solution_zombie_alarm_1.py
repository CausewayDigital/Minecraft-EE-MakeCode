def on_entity_spawned(mob, spawner):
    if mob == ZOMBIE:
        music.play_sound(Sound.THUNDER)
        player.say("Zombie Spawned!")
events.on_entity_spawned(on_entity_spawned)