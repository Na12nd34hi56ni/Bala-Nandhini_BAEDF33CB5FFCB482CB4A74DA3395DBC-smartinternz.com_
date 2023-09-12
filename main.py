class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is batting!")

class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is bowling!")

# Creating objects of Batsman and Bowler classes
batsman_obj = Batsman("M.S.Dhoni")
bowler_obj = Bowler("virat koli")

# Calling the play() method for each object
batsman_obj.play()
bowler_obj.play()
