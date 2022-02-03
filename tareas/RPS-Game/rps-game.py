""" # Rock, sissors, paper game

class RPSGame:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        if self.p1 == self.p2:
            print("Tie")
            return
        elif self.p1 == "rock":
            if self.p2 == "scissors":
                self.p1_score += 1
            else:
                self.p2_score += 1
        elif self.p1 == "scissors":
            if self.p2 == "paper":
                self.p1_score += 1
            else:
                self.p2_score += 1
        elif self.p1 == "paper":
            if self.p2 == "rock":
                self.p1_score += 1
            else:
                self.p2_score += 1

    def play_game(self):
        print("Game start")
        for round in range(3):
            print("Round {}".format(round + 1))
            self.play_round()
        print("Game over")
        if self.p1_score > self.p2_score:
            print("{} wins".format(self.p1))
        elif self.p1_score < self.p2_score:
            print("{} wins".format(self.p2))
        else:
            print("Tie")

RPSGame("rock", "scissors").play_game()
RPSGame("rock", "paper").play_game()
RPSGame("scissors", "paper").play_game() """

# Rock, sissors, paper game in function

function_rps = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# generate rock, paper, scissors game with functions
def rps_game(p1, p2):
    if p1 == p2:
        print("Tie")
        return
    elif p1 == "rock":
        if p2 == "scissors":
            print("{} wins".format(p1))
        else:
            print("{} wins".format(p2))
    elif p1 == "scissors":
        if p2 == "paper":
            print("{} wins".format(p1))
        else:
            print("{} wins".format(p2))
    elif p1 == "paper":
        if p2 == "rock":
            print("{} wins".format(p1))
        else:
            print("{} wins".format(p2))

rps_game("rock", "scissors")

 



