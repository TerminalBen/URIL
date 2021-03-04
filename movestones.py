boardgame = [4, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4]
last_position_stone = 0
aux_board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]  # unused class variable
score_player1 = 0
score_player2 = 0


def hole_value(hole):
    return boardgame[hole]


def move_stones(a): #a=3
    x=boardgame[a]  #x=4
    last_temp=a+x
    global last_position_stone

    if last_temp>len(boardgame):
        last= last_temp % len(boardgame)
    else:
        last=last_temp

    for i in range(x+1):   
        try:
            boardgame[a+i]+=1 
            x-=1        
            boardgame[a]=0
            #last= a+x
        except IndexError:
            #last=0
            for j in range(x+1):    
                boardgame[j]+=1
                x-=1
                #last +=1
                #print(last)
    print ('last:'+str(last))
    print (boardgame)
    last_position_stone = last


def steal_stones() -> None:  # TODO Fix
    """eats opponent's stones if hole's stones<=3 adding it to the score tuple, or the player.score_update #TODO

        Args:
            playername (str): [name of the player's turn to play]
        """
    #TODO fix last_stone position interaction with playername
    x = last_position_stone
    global score_player2
    global boardgame
    #print(x)
    flag = True
    #while (x<6):
    while flag:
        if (hole_value(x) <= 3):
            score = hole_value(x)
            score_player2 += score
            boardgame[x] = 0
            x -= 1  # check previous hole
        else:
            flag = False

    print('score2: '+str(score_player2))
    #print('score2: '+str(score_player2))
    #print (x)


move_stones(11)
print('last_global:'+str(last_position_stone))
steal_stones()
#print(check_hole_values(boardgame[4]))
#print(boardgame[4])
#print('last_global:'+str(last_position_stone))
