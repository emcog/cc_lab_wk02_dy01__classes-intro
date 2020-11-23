class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        return player in self.players
        # else: return False

    def play_game(self, game_won):
        if game_won:
            self.points += 3
        