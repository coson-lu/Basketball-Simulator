"""
TODO
  - Add offensive rebound stat

BRAINSTORM
    - Defensive Techniques:
        - Zone:
            - Description: Players cover a certain area as opposed to face guarding another player
            - Variations:
                - 2-3: 2 on outside 3 on inside
                    - Pros: Better interior defense
                    - Cons: Worse exterior defense
                - 3-2: 3 on outside 2 on inside
                    - Pros: Better exterior defense
                    - Cons: Worse interior defense
        - Man-to-man
            - Description: Players guard the optimal other player
            - Pros: Good to defend teams that have balanced comp (some 3p shooters some 2p shooters)
"""


import random
FIRST_NAMES, LAST_NAMES = [x.strip().lower() for x in list(open('first_names.txt'))], [x.strip().lower() for x in list(open('last_names.txt'))]

game_mode = ''

# Copied off of Khan Academy because I couldn't figure it out
def mp(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

class Player:
    def __init__(self):
        self.name = f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}'
        self.height = {
            'feet': random.choice((6, 6, 6, 7))
        }
        self.height['inch'] = random.randint(0, 11) if self.height['feet'] == 6 else random.randint(0, 5)
        self.two_point_fpg = random.uniform(35, 55) + (self.height['feet'] * 12 + self.height['inch']) / 12
        self.three_point_fgp = random.uniform(35, 50) - (self.height['feet'] * 12 + self.height['inch']) / 15
        self.clutch = random.uniform(-5, 5) # Adds fgp stats at end of close games
        self.interior_def = random.uniform(-5, 3) + (self.height['feet'] * 12 + self.height['inch']) / 25 # Subtracts two_point_fgp of attacker
        self.exterior_def = random.uniform(-3, 1) + (self.height['feet'] * 12 + self.height['inch']) / 35 # Sbutracts three_point_fgp of attacker
        self.turnover = random.uniform(0.5, 5) # How prone they are to turning over the ball %
        self.teammate = random.uniform(-1, 2) # Adds stats to every teammate
        self.fatigue = random.uniform(0.5, 2) # How much stats decrease as game progresses
        self.game_stats = {
            'points': 0,
            'total_fg_attempted': 0,
            'total_fg_made': 0,
            '3p_fg_attempted': 0,
            '3p_fg_made': 0,
            '2p_fg_attempted': 0,
            '2p_fg_attempted': 0,
            'turnovers': 0
        }
        self.offensive_overall = round(mp(
            self.two_point_fpg +\
            self.three_point_fgp +\
            self.clutch * 2 +\
            self.teammate * 3 -\
            self.fatigue, 
        58, 120, 50, 100), 2)
        self.defensive_overall = round(mp(
            self.interior_def +\
            self.exterior_def,
        10, -4.2, 50, 100), 2)
        self.overall = round((self.defensive_overall + self.offensive_overall) / 2, 2)

players = []
for i in range(50000):
    players.append(Player())

m = -100000
n = 50000000000
for i in players:
    m = max(m, i.offensive_overall)
    n = min(n, i.offensive_overall)
print(m, n)

class User:
    def __init__(self):
        self.players = []
    
    def add_player(self, p):
        self.players.append(p)

    def substitution(self, cur_player, sub_player):
        pass


class Duel:
    def __init__(self):
        self.p1 = User()
    pass

while True:
    game_mode = input('Choose a gamemode:')
    match game_mode:
        case 'duels':
            pass