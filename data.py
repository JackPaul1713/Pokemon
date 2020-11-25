# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jack Martin, Cristian Mata, Trent Kubeczka
# Section:     428
# Assignment:  PokemonTBE Group Project
# Date:        24 November 2020

#INIT#
#import#
import random

#var#
if 'active_player' not in globals():
    #init#
    active_player = 0
    players = [{'name': '', 'active_pokemon': 0, 'pokemons': [{}], 'candy': 0}, {}]
    pokemon_pool = ()

#func#
def new_game(game_file, player):
    '''
    makes a new game
    parameters: string game_file, int player | return: none | author: Jack Martin
    '''
    #globals#
    global active_player
    global players
    global pokemon_pool
    #setup#
    active_player = player
    players[active_player]['file'] = game_file
    players[active_player]['name'] = input('Username: ')
    players[active_player]['active_pokemon'] = 0
    starter = random.randint(0, 2)
    players[active_player]['pokemons'] = [{'name':pokemon_pool[starter][0], 'level':1, 'health':[1000, 1000], 'attack':pokemon_pool[starter][1][0], 'potential':pokemon_pool[starter][1]}]
    players[active_player]['candy'] = 0

def load_game(game_file, player):
    '''
    loads a game from a file
    parameters: string game_file, int player | return: none | author: Jack Martin
    '''
    #globals#
    global active_player
    global players
    global pokemon_pool
    #read#
    file = open(game_file, 'r')
    player_attributes = file.read()
    file.close()
    #split#
    player_attributes = player_attributes.split('\n')
    #setup#
    active_player = player
    players[active_player]['name'] = player_attributes[0]
    players[active_player]['active_pokemon'] = int(player_attributes[1])
    players[active_player]['pokemons'] = []
    pokemons_attributes = player_attributes[2].split(',')[0:-1]
    for attributes in pokemons_attributes:
        attributes = attributes.split('*')
        pokemon = {}
        pokemon['name'] = attributes[0]
        pokemon['level'] = int(attributes[1])
        pokemon['health'] = [int(attributes[2]), int(attributes[3])]
        pokemon['attack'] = int(attributes[4])
        pokemon['potential'] = [int(attributes[5]), int(attributes[6])]
        players[active_player]['pokemons'].append(pokemon)
    players[active_player]['candy'] = int(player_attributes[3])
    players[active_player]['file'] = game_file

def save_game(player):
    '''
    saves a game
    parameters: string game_file, int player | return: none | author: Jack Martin
    '''
    #globals#
    global active_player
    global players
    global pokemon_pool
    #write#
    player = players[player]
    file = open(player['file'], 'w')
    file.write(str(player['name']) + '\n')
    file.write(str(player['active_pokemon']) + '\n')
    for pokemon in player['pokemons']:
        file.write(str(pokemon['name']) + '*')
        file.write(str(pokemon['level']) + '*')
        file.write(str(pokemon['health'][0]) + '*')
        file.write(str(pokemon['health'][1]) + '*')
        file.write(str(pokemon['attack']) + '*')
        file.write(str(pokemon['potential'][0]) + '*')
        file.write(str(pokemon['potential'][1]) + ',')
    file.write('\n' + str(player['candy']))
    file.close()

def fill_pokemon_pool():
    '''
    fills a pool of potential pokemon
    parameters: none | return: none | author: Jack Martin
    '''
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
        pool.append((attributes[0], (int(attributes[1]), int(attributes[2]))))
    #set#
    pokemon_pool = tuple(pool)

#MAIN#
if __name__ == '__main__':
    #testing#
    game_file = 'TestGame.txt'

    print('\nfill pokemon pool')
    fill_pokemon_pool()

    print('\nnew game')
    new_game(game_file, 0)
    print(players[0])

    print('\nsave game')
    save_game(0)
    print(players[0])

    print('\nload game')
    load_game(game_file, 1)
    print(players[1])