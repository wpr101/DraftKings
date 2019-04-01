# SLPM per minute, TD per 15 min
# Some assumption that additional points scored after TD
# from both advances and strikes
class Player():
    def __init__(self, name, slpm, td, points):
        self.name = str(name)
        self.slpm = float(slpm)
        self.td = float(td)
        self.points = points

    def __repr__(self):
        return 'Player(name=%s, slpm=%s, td=%s, points=%s)' % \
    (self.name, self.slpm, self.td, self.points)

def run_sim():
    fighters = []
    fighters.append(Player('Holloway', 6.9, .32, 0))
    fighters.append(Player('Poirier', 5.59, 1.75, 0))
    fighters.append(Player('Gastelum', 3.86, .82, 0))
    fighters.append(Player('Adesanya', 4.47, 0, 0))
    fighters.append(Player('Anders', 3.12, 2.05, 0))
    fighters.append(Player('Rountree', 2.3, 0, 0))

    for fighter in fighters:
        fighter.points += fighter.slpm * 15
        fighter.points += fighter.td * 10

    for fighter in fighters:
        print fighter.name, fighter.points

run_sim()
