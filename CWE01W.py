from itertools import combinations

combo2 = list(combinations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 18))

# combo2 = [('a', 'u', 'f', 'p', 'g', 't', 'e', 'i', 'n', 's', 'y', 'h', 'b', 'j', 'z', 'w', 'k', 'o')]
# needs to match 2 words for win
cross1 = ['vital', ' alter', ' substance', 'surf', 'undo', 'drum', 'low', 'grid', 'income', 'edge', 'end', 'den',
          'reform', 'strugge', 'tub', 'lt', 'soldier', 'arrow', 'solo', 'lack', 'redeem', 'promenade']


cross2 = ['fact', 'golf', 'sympony', 'earn', 'attach', 'tack', 'portable', 'orchid', 'dull', 'happen', 'yard', 'any',
          'shampoo', 'mt', 'tip', 'recap', 'act', 'alike', 'moth', 'yesterday', 'fear', 'collar']

# one match wins
bonus1 = ['fossil']
bonus2 = ['season']
bonus3 = ['strict']


# word list with duplicates removed
cross1set = []
cross2set = []
bonus1set = []
bonus2set = []
bonus3set = []

win = 0
lose = 0
board1win = 0
board2win = 0
win300000 = 0
win30000 = 0
win10000 = 0
win1000 = 0
win500 = 0
win400 = 0
win200 = 0
win100 = 0
win50 = 0
win40 = 0
win30 = 0
win20 = 0
win10 = 0
bonuswin = 0


def setmaker(arg1, arg2):  # removes duplicate letters from word list
    for i in arg1:
        sets = "".join(set(i))
        arg2.append(sets)


def wordfinder(arg1, arg2):
    words = []
    letters = arg1
    for word in arg2:
        candidate = True
        letterlist = list(letters)
        for letter in word:
            if letter not in letterlist:
                candidate = False
                break
            else:
                letterlist.remove(letter)
        if candidate == True:
            words.append(word)
    return words


# create sets from word lists
setmaker(cross1, cross1set)
setmaker(cross2, cross2set)
setmaker(bonus3, bonus3set)
setmaker(bonus2, bonus2set)
setmaker(bonus1, bonus1set)


for i in combo2:
    combowin = 0
    combolose = 0

    count = len(wordfinder(i, cross1set))
    if int(count) < 2:
        combolose += 1
    elif int(count) == 2:
        win10 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 3:
        win20 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 4:
        win40 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 5:
        win100 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 6:
        win200 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 7:
        win400 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 8:
        win1000 += 1
        combowin += 1
        board1win += 1
    elif int(count) == 9:
        win10000 += 1
        combowin += 1
        board1win += 1
    elif int(count) >= 10:
        win30000 += 1
        combowin += 1
        board1win += 1

    count = len(wordfinder(i, cross2set))
    if int(count) < 2:
        combolose += 1
    elif int(count) == 2:
        win20 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 3:
        win30 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 4:
        win50 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 5:
        win100 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 6:
        win500 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 7:
        win1000 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 8:
        win10000 += 1
        combowin += 1
        board2win += 1
    elif int(count) == 9:
        win30000 += 1
        combowin += 1
        board2win += 1
    elif int(count) >= 10:
        win300000 += 1
        combowin += 1
        board2win += 1

    count = len(wordfinder(i, bonus1set))
    if int(count) == 1:
        combowin += 1
        bonuswin += 1
    elif int(count) == 0:
        combolose += 1

    count = len(wordfinder(i, bonus2set))
    if int(count) == 1:
        combowin += 1
        bonuswin += 1
    elif int(count) == 0:
        combolose += 1

    count = len(wordfinder(i, bonus3set))
    if int(count) == 1:
        combowin += 1
        bonuswin += 1
    elif int(count) == 0:
        combolose += 1

    if combowin >= 1:
        win += 1
    else:
        lose += 1


print("total combos checked " + str(len(combo2)))
print("$10 wins = " + str(win10))
print("$20 wins = " + str(win20))
print("$30 wins = " + str(win30))
print("$40 wins = " + str(win40))
print("$50 wins = " + str(win50))
print("$100 wins = " + str(win100))
print("$200 wins = " + str(win200))
print("$400 wins = " + str(win400))
print("$500 wins = " + str(win500))
print("$1000 wins = " + str(win1000))
print("$10000 wins = " + str(win10000))
print("$30000 wins = " + str(win30000))
print("$300000 wins = " + str(win300000))
print("bonuswins = " + str(bonuswin))
print("board1 wins = " + str(board1win))
print("board2 wins = " + str(board2win))
print("winning combos =" + str(win))
print("losing combos = " + str(lose))