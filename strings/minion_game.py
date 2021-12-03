def minion_game(string):
    consonant = 'bcdfghjklmnpqrstvwxyz'.upper()
    vowel = 'aeiou'.upper()
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if s[i] in vowel:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    # print winner
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print(f'Stuart {stuart}')