import random
first_names, last_names = [x.strip().lower() for x in list(open('first_names.txt'))], [x.strip().lower() for x in list(open('last_names.txt'))]

game_mode = ''
class Character:
    def __init__(self, name, height, two_point_fgp, three_point_fgp, interior_def, exterior_def, overall):
        self.name = f'{random.choice(first_names)} {random.choice(last_names)}'
        pass
    
def duels():
    pass

while True:
    game_mode = input('Choose a gamemode:')
    match game_mode:
        case 'duels':
            pass