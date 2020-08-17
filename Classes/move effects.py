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

def UseSwordsDance(User):
    pass

def UseDragonPulse(User, Target):
    pass

def UseTailwind(User, TargetPlayer):
    pass

def UseTrickRoom(User):
    pass

def UseStickyWeb(User, TargetPlayer):
    pass

def UseSurf(User, Player, TargetPlayer):
    pass

def UseDazzlingGleam(User, TargetPlayer):
    pass

def UseOutrage(User, TargetPlayer):
    pass

def UseSandstorm(User):
    pass

def UseProtect(User):
    pass