#INIT#
#imports#
import random

#func#
def protected_input(prompt, escape_character=0, error='Invalid selection, try again'):
    """
    limits input to only numbers and an escape character
    parameters: string prompt, string escape_character=, string error= | return: mixed inp | author: Jack Martin
    """
    #input#
    while True:
        inp = input(prompt)
        try:
            inp = int(inp)
        except ValueError:
            pass
        if isinstance(inp, int) or inp == escape_character:
            break
        else:
            print(error)
    #return#
    return(str(inp))

def protected_file_input(prompt, error='Invalid file, try again'):
    """
    limits input to only valid files
    parameters: string prompt, string error= | return: mixed inp | author: Jack Martin
    """
    #input#
    while True:
        inp = input(prompt)
        try:
            file = open(inp)
            file.close()
            break
        except FileNotFoundError:
            print(error)
    #return#
    return(inp)

def display_pokemon(pokemon, type='long'):
    """
    displays a pokemon
    parameters: mixed{} pokemon, string type | return: none | author:
    """
    if type == 'short':
        pokemon_str = pokemon['name']
        pokemon_str += ' (level: {}, '.format(pokemon['level'])
        pokemon_str += 'health: {}/{}, '.format(pokemon['health'][0], pokemon['health'][0])
        pokemon_str += 'attack: {}, '.format(pokemon['attack'])
        pokemon_str += 'potential: {}-{})'.format(pokemon['potential'][0], pokemon['potential'][1])
        print(pokemon_str)
    elif type == 'long':
        print(pokemon['name'])
        print('level:', pokemon['level'])
        print('health:', str(pokemon['health'][0]) + '/' + str(pokemon['health'][1]))
        print('attack:', pokemon['attack'])
        print('potential:', str(pokemon['potential'][0]) + '-' + str(pokemon['potential'][1]))

def level_up_pokemon(pokemon, candy):
    """
    levels up a pokemon
    parameters: mixed{} pokemon, int candy | return: mixed{} pokemon, int candy | author:
    """
    #unpack#
    level = pokemon['level']
    health = pokemon['health'][1]
    attack = pokemon['attack']
    potential = pokemon['potential']
    # check#
    if (candy >= 1 and level < 30) or (candy >= 2 and level < 40):
        # level_up#
        level += 1
        health = level * 1000
        attack = int(((potential[1] - potential[0]) / 40 * level) + potential[0])
        candy -= 1
        if level > 30:
            candy -= 1
        #pack#
        pokemon['level'] = level
        pokemon['health'] = [health, health]
        pokemon['attack'] = attack
    else:
        print('You need more candy.')
        input('Press enter to continue')
        print('\n')
    return(pokemon, candy)

def heal_pokemon(pokemon):
    """
    heals a pokemon
    parameters: mixed{} pokemon | return: mixed{} pokemon | author:
    """
    #unpack#
    health = pokemon['health'][0]
    max_health = pokemon['health'][1]
    #heal#
    health += 1000
    if health > max_health:
        health = max_health
    #pack#
    pokemon['health'][0] = health
    #ret#
    return(pokemon)

def battle(pokemon, type='tournament'):
    """
    battles active player active pokemon vs random pokemon of similar level (tournament, wild)
    parameters: string type= | return: mixed{} pokemon | author:
    """
    return(pokemon)

def explore(player):
    """
    random action(wild battle, find candy, nothing)
    parameters: mixed{} player | return: mixed{} player | author: Jack Martin
    """
    action = random.randint(0, 2)
    found_candy = 0
    #title#
    print('Explore')
    print('')
    #nothing#
    if action == 0:
        print('You got lost and found nothing')
        input('Press enter to continue')
        print('\n')
    #candy#
    elif action == 1:
        action = random.randint(0, 2)
        if action == 0:
            found_candy = random.randint(1, 2)
            print('You found some candy growing on a candy tree, plus {} candy'.format(found_candy))
            input('Press enter to continue')
        elif action == 1:
            found_candy = random.randint(2, 4)
            print('You found some kids halloween stash, plus {} candy'.format(found_candy))
            input('Press enter to continue')
        elif action == 2:
            found_candy = random.randint(4, 16)
            print('A strange man in a sketchy white van offers you candy, plus {} candy'.format(found_candy))
            input('Press enter to continue')
        print('\n')
    #pokemon_battle#
    elif action == 2:
        print('You see a pokemon living happily in the wild. Well not anymore, you attack the pokemon')
        input('Press enter to continue')
        player['pokemons'][player['active_pokemon']] = battle(player['pokemons'][player['active_pokemon']], 'wild')
        print('\n')
    return(player)

#wrappers#
def display_pokemon_wrapper():
    """
    wraps display_pokemon to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
    import data
    player = data.players[data.active_player]
    pokemons = player['pokemons']
    pokemon = pokemons[player['active_pokemon']]
    #display#
    display_pokemon(pokemon, 'long')
def display_pokemons_wrapper():
    """
    wraps display_pokemon to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
    import data
    player = data.players[data.active_player]
    pokemons = player['pokemons']
    #display#
    for i, pokemon in enumerate(pokemons):
        display_pokemon(pokemon, 'short')

def level_up_pokemon_wrapper():
    """
    wraps level_up_pokemon to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
    import data
    player = data.players[data.active_player]
    pokemons = player['pokemons']
    candy = player['candy']
    pokemon = pokemons[player['active_pokemon']]
    #level_up#
    pokemon, candy = level_up_pokemon(pokemon, candy)
    #upload#
    pokemons[player['active_pokemon']] = pokemon
    player['candy'] = candy
    player['pokemons'] = pokemons
    data.players[data.active_player] = player

def heal_pokemon_wrapper():
    """
    wraps heal_pokemon to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
    import data
    player = data.players[data.active_player]
    pokemons = player['pokemons']
    pokemon = pokemons[player['active_pokemon']]
    #heal#
    pokemon = heal_pokemon(pokemon)
    #upload#
    pokemons[player['active_pokemon']] = pokemon
    player['pokemons'] = pokemons
    data.players[data.active_player] = player

def battle_wrapper():
    """
    wraps battle to use game data
    parameters: none | return: none | author: Jack Martin
    """

def explore_wrapper():
    """
    wraps explore to use game data
    parameters: none | return: none | author: Jack Martin
    """
    # load#
    import data
    player = data.players[data.active_player]
    # add#
    player = explore(player)
    # upload#
    data.players[data.active_player] = player

#MAIN#
if __name__ == '__main__':
    #testing#
    print('no testing at this point')