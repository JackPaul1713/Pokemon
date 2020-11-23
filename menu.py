#INIT#
#import#
import data
import resources

#MAIN#
if __name__ == '__main__':
    #init#
    data.fill_pokemon_pool()
    #menus#
    while True:
        #title#
        print('POKEMON™')
        print('Text Based Edition')
        print('')
        #menu#
        print('1. New Game')
        print('2. Load Game')
        print('3. Active Game')
        print('\'x\' to exit')
        #selection#
        inp = resources.protected_input('Selection: ', 'x')
        print('\n')
        #exit#
        if inp == 'x':
            break
        #title#
        print('Game Select')
        print('')
        #input#
        if inp != '3':
            game_file = resources.protected_file_input('File: ')
        elif inp == '3':
            try:
                print('1.', data.players[0]['name'])
            except KeyError:
                print('1. None')
            try:
                print('2.', data.players[1]['name'])
            except KeyError:
                print('2. None')
        data.active_player = int(resources.protected_input('Player Number (1, 2): ')) - 1
        #actions#
        if inp != '3':
            actions = [data.new_game, data.load_game]
            actions[int(inp) - 1](game_file, data.active_player)
        print('\n')
        while True:
            #title#
            print('Game Menu')
            print('')
            #menu#
            print('1. My Stats')
            print('2. My Pokemon')
            print('3. Battle')
            print('4. Explore')
            print('5. Save Game')
            print('\'b\' to go back')
            #selections#
            inp = resources.protected_input('Selection: ', 'b')
            print('\n')
            #exit#
            if inp == 'b':
                break
            #actions#
            if inp == '1':
                while True:
                    #title#
                    print('My Stats Menu')
                    print('')
                    #disp#
                    print(data.players[data.active_player]['name'])
                    print('candy:', data.players[data.active_player]['candy'])
                    print('pokemon:', len(data.players[data.active_player]['pokemons']))
                    print('')
                    #menu#
                    print('\'b\' to go back')
                    #selection#
                    inp = resources.protected_input('Selection: ', 'b')
                    #exit#
                    if inp == 'b':
                        break
            elif inp == '2':
                while True:
                    #title#
                    print('My Pokemon Menu')
                    print('')
                    #menu#
                    print('1. Active Pokemon')
                    print('2. All Pokemon')
                    print('\'b\' to go back')
                    #selection#
                    inp = resources.protected_input('Selection: ', 'b')
                    print('\n')
                    #exit#
                    if inp == 'b':
                        break
                    #actions#
                    if inp == '1':
                        while True:
                            #title#
                            print('Active Pokemon')
                            print('')
                            #disp#
                            resources.display_pokemon_wrapper()
                            print('')
                            #menu#
                            print('1. Level Up')
                            print('2. Heal')
                            print('\'b\' to go back')
                            #selection#
                            inp = resources.protected_input('Selection: ', 'b')
                            print('\n')
                            #exit#
                            if inp == 'b':
                                break
                            #actions#
                            actions = [resources.level_up_pokemon, resources.heal_pokemon_wrapper]
                            actions[int(inp) - 1]()
                            #reset#
                            inp = ''
                    elif inp == '2':
                        while True:
                            #title#
                            print('All Pokemon')
                            print('')
                            #disp#
                            resources.display_pokemons_wrapper()
                            print('')
                            #menu#
                            print('1. Select active pokemon')
                            print('\'b\' to go back')
                            #selection#
                            inp = resources.protected_input('Selection: ', 'b')
                            print('\n')
                            # exit#
                            if inp == 'b':
                                break
                            #actions#
                            resources.select_pokemon()
                            #reset#
                            inp = ''
                    #reset#
                    inp = ''
            elif inp == '3':
                resources.battle_wrapper()
            elif inp == '4':
                resources.explore_wrapper()
            elif inp == '5':
                data.save_game(data.players[data.active_player])
            #reset#
            inp = ''