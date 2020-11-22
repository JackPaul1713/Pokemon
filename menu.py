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
        print('1. Select Game')
        print('2. Load Game')
        print('\'x\' to exit')
        #selection#
        inp = input('Selection: ')
        print('')
        #exit#
        if inp == 'x':
            break

        #title#
        print('Game Select')
        print('')
        #input#
        file = input('File: ')
        player_num = input('Player Number (1, 2): ')
        #actions#
        actions = [data.new_game, data.load_game]
        actions[int(inp) - 1](file, player_num)
        while True:
            #title#
            print('Game Menu')
            print('')
            print('1. My Pokemon')
            print('2. Battle')
            print('3. Explore')
            print('\'b\' to go back')
            #selections#
            inp = input('Selection: ')
            print('')
            #exit#
            if inp == 'b':
                break
            #actions#
            actions = ['tournament', 'wild']
            if inp == 1:
                while True:
                    #title#
                    print('My Pokemon Menu')
                    print('')
                    #menu#
                    print('1. All Pokemon')
                    print('2. Active Pokemon')
                    print('\'b\' to go back')
                    #selection#
                    inp = input('Selection: ')
                    print('')
                    #exit#
                    if inp == 'b':
                        break
                    #actions#
                    actions = []
                    #reset#
                    inp = ''
            else:
                resources.battle(actions[int(inp) - 2])
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