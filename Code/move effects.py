class HelpingHand(Move):
    def __init__(self, Move, User, Player):
        self.__dict__ = Move.__dict__.copy()
        self.User = User
        self.Player = Player

    def use(self):
        if self.User.Position == 'Left':
            if self.Player.RightMon and not self.Player.RightMon.IsKnockedOut:
                MinusPP(self.Name, self.User)
                self.Player.RightMon.IsHelped = True
        elif self.User.Position == 'Right':
            if self.Player.LeftMon and not self.Player.LeftMon.IsKnockedOut:
                MinusPP(self.Name, self.User)
                self.Player.LeftMon.IsHelped = True