import random
first_names, last_names = [x.strip().lower() for x in list(open('first_names.txt'))], [x.strip().lower() for x in list(open('last_names.txt'))]

game_mode = ''

# Copied off of Khan Academy because I couldn't figure it out
def mp(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

class Character:
    def __init__(self):
        self.name = f'{random.choice(first_names)} {random.choice(last_names)}'
        self.height = {
            'feet': random.choice((6, 6, 6, 7))
        }
        self.height['inch'] = random.randint(0, 11) if self.height['feet'] == 6 else random.randint(0, 5)
        self.two_point_fpg = random.uniform(35, 55) + (self.height['feet'] * 12 + self.height['inch']) / 12
        self.three_point_fgp = random.uniform(35, 50) - (self.height['feet'] * 12 + self.height['inch']) / 15
        self.clutch = random.uniform(-5, 5) # Adds fgp stats at end of close games
        self.interior_def = random.uniform(-5, 5) + (self.height['feet'] * 12 + self.height['inch']) / 20 # Subtracts two_point_fgp of attacker
        self.exterior_def = random.uniform(-3, 3) + (self.height['feet'] * 12 + self.height['inch']) / 30 # Sbutracts three_point_fgp of attacker
        self.turnover = random.uniform(0.5, 5) # How prone they are to turning over the ball %
        self.teammate = random.uniform(-1, 2) # Adds stats to every teammate
        self.overall = round(mp(self.two_point_fpg +\
                                self.three_point_fgp +\
                                self.clutch * 2 +\
                                self.interior_def +\
                                self.exterior_def -\
                                self.turnover +\
                                (self.teammate * 3), 55, 131, 71, 100), 2)

characters = []
for i in range(100):
    characters.append(Character())

m = -100000
n = 50000000000
for i in characters:
    m = max(m, i.overall)
    n = min(n, i.overall)
print(m, n)

exit()

def duels():
    pass

while True:
    game_mode = input('Choose a gamemode:')
    match game_mode:
        case 'duels':
            pass