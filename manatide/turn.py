class Turn(object):
    def __init__(self, gamestate, player):
        self.gamestate = gamestate
        self.active_player = player

        self.phase = None
        self.step = None

    def beginning_phase(self):
        self.phase = "beginning"

        self.untap_step()
        self.upkeep_step()
        self.draw_step()

    def untap_step():
        self.step = "untap"

        #TODO: handle phase-in/phase-out

        for card in self.gamestate.zone["battlefield"].cards:
            if card.player is self.active_player:
                #TODO Hook continuous effects
                card.untap()

    def upkeep_step(self):
        self.step = "upkeep"

    def draw_step(self):
        self.step = "draw"

        self.gamestate.draw(self.active_player)

    def main_phase(self, pre_combat):
        if pre_combat:
            self.phase = "pre-combat main"
        else:
            self.phase = "pos-combat main"

    def combat_phase(self):
        pass

    def beginning_of_combat_step(self):
        pass

    def declare_attackers_step(self):
        pass

    def declare_blockers_step(self):
        pass

    def combat_damage_step(self):
        pass

    def end_of_combat_step(self):
        pass

    def ending_phase(self):
        pass

    def end_step(self):
        pass

    def cleanup_step(self):
        pass

