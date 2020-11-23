class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach 

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        if player in self.players:
            return True
        else: return False