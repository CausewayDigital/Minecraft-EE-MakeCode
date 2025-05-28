def on_player_bounced():
    loc = player.position()
    block_under = blocks.is_under(SLIME_BLOCK, loc)
    if block_under == True:
        target = mobs.target(NEAREST_PLAYER)
        mobs.apply_effect(LEVITATION, target, 1, 10)

player.on_travelled(BOUNCE, on_player_bounced)
