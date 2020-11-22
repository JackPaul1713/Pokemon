#TEST#
#add#
#do#
#test#

#INIT#
#import#
import data as data
import resources as resources

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
        inp = input('Selection: ')
        print('\n')
        #exit#
        if inp == 'x':
            break

        #title#
        print('Game Select')
        print('')
        #input#
        if inp != '3':
            file = input('File: ')
        elif inp == '3':
            try:
                print('1.', data.players[0]['name'])
            except:
                print('1. None')
            try:
                print('2.', data.players[1]['name'])
            except:
                print('2. None')
        data.active_player = int(input('Player Number (1, 2): ')) - 1
        #actions#
        if inp != '3':
            actions = [data.new_game, data.load_game]
            actions[int(inp) - 1](file, data.active_player)
        print('\n')
        while True:
            #title#
            print('Game Menu')
            print('')
            print('1. My Pokemon')
            print('2. Battle')
            print('3. Explore')
            print('4. Save Game')
            print('\'b\' to go back')
            #selections#
            inp = input('Selection: ')
            print('\n')
            #exit#
            if inp == 'b':
                break
            #actions#
            if inp == '1':
                while True:
                    #title#
                    print('My Pokemon Menu')
                    print('')
                    #menu#
                    print('1. Active Pokemon')
                    print('2. All Pokemon')
                    print('\'b\' to go back')
                    #selection#
                    inp = input('Selection: ')
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
                            resources.display_active_pokemon()
                            print('')
                            #menu#
                            print('1. Select active pokemon')
                            print('\'b\' to go back')
                            #selection#
                            inp = input('Selection: ')
                            print('\n')
                            #exit#
                            if inp == 'b':
                                break
                            #actions#
                            resources.select_pokemon()
                            #reset#
                            inp = ''
                    elif inp == '2':
                        while True:
                            #title#
                            print('All Pokemon')
                            print('')
                            #disp#
                            resources.display_all_pokemon()
                            print('')
                            #menu#
                            print('1. Level Up')
                            print('2. Heal')
                            print('\'b\' to go back')
                            #selection#
                            inp = input('Selection: ')
                            print('\n')
                            # exit#
                            if inp == 'b':
                                break
                            #actions#
                            actions = [resources.level_up_pokemon(), resources.heal_pokemon()]
                            actions[int(inp)-1]()
                            #reset#
                            inp = ''
                    #reset#
                    inp = ''
            elif inp == '2':
                resources.battle()
            elif inp == '3':
                resources.explore()
            elif inp == '4':
                data.save_game()
            #reset#
            inp = ''

    # DO menus here
    # main:
    #   load_game()
    #   new_game()
    #     switch_players()
    #     my_pokemon:
    #       active:
    #         level_up()
    #         heal()
    #       all_pokemon:
    #         select()
    #     battle()
    #       person
    #       computer
    #     explore()
    #     exit()
    #testing#
    print('no testing at this point')