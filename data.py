#INIT#
#import#
import random

#func#
def new_game(file, player):
    #globals#
    global active_player
    global players
    global pokemon_pool
    #setup#
    active_player = player
    players[active_player]['file'] = file
    players[active_player]['name'] = input('Username: ')
    players[active_player]['active_pokemon'] = 0
    starter = random.randint(0, 3)
    players[active_player]['pokemons'] = [{'name':pokemon_pool[starter][0], 'level':1, 'health':[100, 100], 'attack':pokemon_pool[starter][1][0], 'potential':pokemon_pool[starter][1]}]
    players[active_player]['candy'] = 0

def load_game(file, player):
    #globals#
    global active_player
    global players
    global pokemon_pool
    #read#
    file = open(file, 'r')
    player_attributes = file.read()
    file.close()
    #split#
    player_attributes = player_attributes.split('\n')
    print(player_attributes[0])
    #setup#
    active_player = player
    players[active_player]['file'] = file
    players[active_player]['name'] = player_attributes[0]
    players[active_player]['active_pokemon'] = int(player_attributes[1])
    players[active_player]['pokemons'] = []
    pokemons_attributes = player_attributes[2].split(',')[0:-1]
    for attributes in pokemons_attributes:
        attributes = attributes.split('.')
        pokemon = {}
        pokemon['name'] = attributes[0]
        pokemon['level'] = int(attributes[1])
        pokemon['health'] = [int(attributes[2]), int(attributes[3])]
        pokemon['attack'] = int(attributes[4])
        pokemon['potential'] = [int(attributes[5]), int(attributes[6])]
        players[active_player]['pokemons'].append(pokemon)
    players[active_player]['candy'] = int(player_attributes[3])

    pass

def save_game():
    #globals#
    global active_player
    global players
    global pokemon_pool
    #write#
    file = open(players[active_player]['file'], 'w')
    file.write(str(players[active_player]['name']) + '\n')
    file.write(str(players[active_player]['active_pokemon']) + '\n')
    for pokemon in players[active_player]['pokemons']:
        file.write(str(pokemon['name']) + '.')
        file.write(str(pokemon['level']) + '.')
        file.write(str(pokemon['health'][0]) + '.')
        file.write(str(pokemon['health'][1]) + '.')
        file.write(str(pokemon['attack']) + '.')
        file.write(str(pokemon['potential'][0]) + '.')
        file.write(str(pokemon['potential'][1]) + ',')
    file.write('\n' + str(players[active_player]['candy']))
    file.close()

def fill_pokemon_pool():
    #globals#
    global pokemon_pool
    #var#
    pool = []
    #read#
    file = open('PokeList.csv', 'r')
    pokemons = file.read()
    file.close()
    #split#
    pokemons = pokemons.split('\n')[1:-1]
    for pokemon in pokemons:
        attributes = pokemon.split(',')[1:]
        pool.append((attributes[0], (attributes[1], attributes[2])))
    #set#
    pokemon_pool = tuple(pool)

#var#
active_player = 0
players = [{}, {}]
pokemon_pool = ()

#MAIN#
if __name__ == '__main__':
    #testing#
    print('no testing at this point')