# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Jack Martin, Cristian Mata, Trent Kubeczka
# Section:     428
# Assignment:  PokemonTBE Group Project
# Date:        24 November 2020

#INIT#
#imports#
import data
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
    parameters: mixed{} pokemon, string type | return: none | author: Jack Martin
    """
    if type == 'short':
        pokemon_str = pokemon['name']
        pokemon_str += ' (level: {}, '.format(pokemon['level'])
        pokemon_str += 'health: {}/{}, '.format(pokemon['health'][0], pokemon['health'][1])
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
    parameters: mixed{} pokemon, int candy | return: mixed{} pokemon, int candy | author: Jack Martin
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
    parameters: mixed{} pokemon | return: mixed{} pokemon | author: Jack Martin
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

def physical_attack(pokemon):
    """
    Generate random attack based off of pokemon
    Parameters: pokemon dictionary | Returns: float damage | Author: Trent Kubeckza
    """
    damage = pokemon['health'][0] / pokemon['level']
    mult = bool(random.getrandbits(1))
    if mult == True:
        damage *= 0.2
    else:
        damage /= 0.2
    return(damage)
def elemental_attack(pokemon):
    """
    generates random attack damage
    parameters: pokemon dictionary | returns: float damage | author: Cristian Mata
    """
    damage = pokemon['attack']
    plus_minus = bool(random.getrandbits(1))
    if plus_minus == True:
        damage *= 0.2
    else:
        damage /= 0.2
    return (damage)
def block():
    """
    Percent blocked by pokemon in attack
    Parameters: int level | Returns: percent blocked| Author: Trent Kubeckza
    """
    percent_blocked = random.randint(5, 10) / 10
    return(percent_blocked)

def get_attack(level, potential):
    """
    gets the attack for a pokemon
    parameters: int level | returns: float attack | author: Cristian Mata
    """
    attack = int(((potential[1] - potential[0]) / 40 * level) + potential[0])
    return(attack)
def get_max_health(level):
    """
    Gets the max health for a pokemon
    Parameters: int level | Return: int max_health | Author: Trent Kubeckza
    """
    max_health = level * 1000
    return(max_health)

def get_opponent(pokemon):
    """
    gets random opponent
    parameters: pokemon dictionary | returns: opponent dictionary | author: Cristian Mata
    """
    poke = data.pokemon_pool[random.randint(0, len(data.pokemon_pool))]
    name = poke[0]
    potential = poke[1]
    level = pokemon['level'] + random.randint(-3, 3)
    attack = get_attack(level, potential)
    health = [get_max_health(level), get_max_health(level)]
    opponent = {'name': name, 'level': level, 'potential': potential, 'attack': attack, 'health': health}
    return opponent


def battle(player, type='tournament'):
    """
    battles active player active pokemon vs random pokemon of similar level (tournament, wild)
    parameters: string type= | return: mixed{} pokemon | author: Cristian Mata, Jack Martin, Trent Kubeckza
    """
    #var#
    poke_damage = 0.0
    poke_defence = 0.0
    opp_damage = 0.0
    opp_defence = 0.0
    pokemon = player['pokemons'][player['active_pokemon']]
    opponent = get_opponent(pokemon)
    #intro#
    print('Battle')
    print('')
    print('You chose {} to fight {}'.format(pokemon['name'], opponent['name']))
    print('')
    display_pokemon(pokemon, 'short')
    display_pokemon(opponent, 'short')
    input('Press enter to continue')
    print('\n')

    #battle#
    while pokemon['health'][0] > 0 and opponent['health'][0] > 0:
        #var#
        poke_damage = 0.0
        poke_defence = 0.0
        #title#
        print('{}\'s turn'.format(pokemon['name']))
        print('')
        #display#
        display_pokemon(pokemon, 'short')
        display_pokemon(opponent, 'short')
        print('')
        #options#
        print('1. Physical attack')
        print('2. Elemental attack')
        print('3. Block')
        #selection#
        inp = protected_input('Selection: ', 0)
        print('')
        #action#
        if inp == '1':
            poke_damage = physical_attack(pokemon)
            print('{} chose physical attack, doing {} damage'.format(pokemon['name'], poke_damage - poke_damage * opp_defence))
        elif inp == '2':
            poke_damage = elemental_attack(pokemon)
            print('{} chose elemental attack, doing {} damage'.format(pokemon['name'], poke_damage - poke_damage * opp_defence))
        elif inp == '3':
            poke_defence = block()
            print('{} chose block, blocking {} % damage next turn'.format(pokemon['name'], poke_defence * 100))
        opponent['health'][0] -= (poke_damage - (poke_damage * opp_defence))
        input('Press enter to continue')
        print('\n')

        #var#
        opp_damage = 0.0
        opp_defence = 0.0
        # title#
        print('{}\'s turn'.format(opponent['name']))
        print('')
        # display#
        display_pokemon(pokemon, 'short')
        display_pokemon(opponent, 'short')
        # random_selection#
        opp_selection = str(random.randint(1, 3))
        print('')
        # action#
        if opp_selection == '1':
            opp_damage = physical_attack(opponent)
            print('{} chose physical attack, doing {} damage'.format(opponent['name'], opp_damage - opp_damage * poke_defence))
        elif opp_selection == '2':
            opp_damage = elemental_attack(opponent)
            print('{} chose elemental attack, doing {} damage'.format(opponent['name'], opp_damage - opp_damage * poke_defence))
        elif opp_selection == '3':
            poke_defence = block()
            print('{} chose block, blocking {} % damage next turn'.format(opponent['name'], opp_defence*100))
        pokemon['health'][0] -= (opp_damage - (opp_damage * poke_defence))
        input('Press enter to continue')
        print('\n')

    #rewards#
    if pokemon['health'][0] > 0:
        print('You win!')
        if type == 'tournament':
            print('You get some candy!')
            player['candy'] += random.randint(1, 16)
        elif type == 'wild':
            print('You throw a pokeball and capture the pokemon!')
            player['pokemons'].append(opponent)
    else:
        print('You where defeated, you suck ig?')
    player['pokemons'][player['active_pokemon']] = pokemon
    return player


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
        player['pokemons'][player['active_pokemon']],  = battle(player['pokemons'][player['active_pokemon']], 'wild')
        print('\n')
    return(player)

#wrappers#
# NOT REALLY FULL FUNCTIONS THEY JUST WRAP THE OTHER FUNCTIONS TO TAKE IN SET PARAMETERS.
# These probably won't count towards the grade, they just make the program cleaner.
def display_pokemon_wrapper():
    """
    wraps display_pokemon to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
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
    player = data.players[data.active_player]
    pokemons = player['pokemons']
    #display#
    for i, pokemon in enumerate(pokemons):
        print(str(i) + '.', end='')
        display_pokemon(pokemon, 'short')

def level_up_pokemon_wrapper():
    """
    wraps level_up_pokemon to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
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
    player = data.players[data.active_player]
    pokemons = player['pokemons']
    pokemon = pokemons[player['active_pokemon']]
    #heal#
    pokemon = heal_pokemon(pokemon)
    #upload#
    pokemons[player['active_pokemon']] = pokemon
    player['pokemons'] = pokemons
    data.players[data.active_player] = player

def battle_wrapper(type='tournament'):
    """
    wraps battle to use game data
    parameters: none | return: none | author: Jack Martin
    """
    #load#
    player = data.players[data.active_player]
    #battle#
    player = battle(player, type)
    #upload#
    data.players[data.active_player] = player

def explore_wrapper():
    """
    wraps explore to use game data
    parameters: none | return: none | author: Jack Martin
    """
    # load#
    player = data.players[data.active_player]
    # add#
    player = explore(player)
    # upload#
    data.players[data.active_player] = player

#MAIN#
if __name__ == '__main__':
    #testing#
    import data
    data.fill_pokemon_pool()
    pokemon = {'name':'poke', 'level':10, 'attack':250.0, 'health':[7500, 10000], 'potential':[200, 300]}
    player = {'name':'Jeff', 'active_pokemon':0, 'pokemons':[pokemon, pokemon], 'candy':12}

    print('\nprotected inputs')
    protected_input('input: ', 'q')
    protected_file_input('file: ')
    input('enter to continue')

    print('\n long')
    display_pokemon(pokemon, type='long')
    print('\ndisplay short')
    display_pokemon(pokemon, type='short')
    input('enter to continue')

    print('\nlevel up')
    print(pokemon)
    print(level_up_pokemon(pokemon, 1))
    input('enter to continue')

    print('\nheal')
    print(pokemon)
    print(heal_pokemon(pokemon))
    input('enter to continue')

    print('\nbattle options')
    print(physical_attack(pokemon))
    print(elemental_attack(pokemon))
    print(block())
    input('enter to continue')

    print('\nattack, max_health')
    print(get_attack(10, [200, 300]))
    print(get_max_health(10))
    input('enter to continue')

    print('\nrandom opponent')
    print(get_opponent(pokemon))
    input('enter to continue')

    print('\nbattle tournament')
    print(battle(player, type='tournament'))
    print('\nbattle wild')
    print(battle(pokemon, type='wild'))
    input('enter to continue')

    print('\nexplore')
    print(explore(player))
    print('end of testing')