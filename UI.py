import pygame,sys,os,controller
from pygame import K_1,K_2,K_3,K_4,K_5,K_6

pygame.init()
clock = pygame.time.Clock()
width = 750
height = 450
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Uril')
running=True
Left=1
bgColor=(0,0,0)
game=controller.Controller()
help=False

#board and hole images
board_path = os.path.join("images", "board_empty.jpg")
board = pygame.image.load(board_path)
he_path = os.path.join("images", "e.jpg")
he = pygame.image.load(he_path).convert()
h1_path = os.path.join("images", "1.jpg")
h1 = pygame.image.load(h1_path).convert()
h2_path = os.path.join("images", "2.jpg")
h2 = pygame.image.load(h2_path).convert()
h3_path = os.path.join("images", "3.jpg")
h3 = pygame.image.load(h3_path).convert()
h4_path = os.path.join("images", "4.jpg")
h4 = pygame.image.load(h4_path).convert()
h5_path = os.path.join("images", "5.jpg")
h5 = pygame.image.load(h5_path).convert()
hm_path = os.path.join("images", "m.jpg")
hm = pygame.image.load(hm_path).convert()
#wining & turns
player1_path = os.path.join("images", "player1.png")
player1 = pygame.image.load(player1_path).convert()
player2_path = os.path.join("images", "player2.png")
player2 = pygame.image.load(player2_path).convert()
player1wins_path = os.path.join("images", "player1wins.jpg")
player1wins = pygame.image.load(player1wins_path).convert()
player2wins_path = os.path.join("images", "player2wins.jpg")
player2wins = pygame.image.load(player2wins_path).convert()
tie_path = os.path.join("images", "tie.jpg")
tie = pygame.image.load(tie_path).convert()
#Score images
n0_path = os.path.join("images", "n0.jpg")
n0 = pygame.image.load(n0_path).convert()
n1_path = os.path.join("images", "n1.jpg")
n1 = pygame.image.load(n1_path).convert()
n2_path = os.path.join("images", "n2.jpg")
n2 = pygame.image.load(n2_path).convert()
n3_path = os.path.join("images", "n3.jpg")
n3 = pygame.image.load(n3_path).convert()
n4_path = os.path.join("images", "n4.jpg")
n4 = pygame.image.load(n4_path).convert()
n5_path = os.path.join("images", "n5.jpg")
n5 = pygame.image.load(n5_path).convert()
n6_path = os.path.join("images", "n6.jpg")
n6 = pygame.image.load(n6_path).convert()
n7_path = os.path.join("images", "n7.jpg")
n7 = pygame.image.load(n7_path).convert()
n8_path = os.path.join("images", "n8.jpg")
n8 = pygame.image.load(n8_path).convert()
n9_path = os.path.join("images", "n9.jpg")
n9 = pygame.image.load(n9_path).convert()
n10_path = os.path.join("images", "n10.jpg")
n10 = pygame.image.load(n10_path).convert()
n11_path = os.path.join("images", "n11.jpg")
n11 = pygame.image.load(n11_path).convert()
n12_path = os.path.join("images", "n12.jpg")
n12 = pygame.image.load(n12_path).convert()
n13_path = os.path.join("images", "n13.jpg")
n13 = pygame.image.load(n13_path).convert()
n14_path = os.path.join("images", "n14.jpg")
n14 = pygame.image.load(n14_path).convert()
n15_path = os.path.join("images", "n15.jpg")
n15 = pygame.image.load(n15_path).convert()
n16_path = os.path.join("images", "n16.jpg")
n16 = pygame.image.load(n16_path).convert()
n17_path = os.path.join("images", "n17.jpg")
n17 = pygame.image.load(n17_path).convert()
n18_path = os.path.join("images", "n18.jpg")
n18 = pygame.image.load(n18_path).convert()
n19_path = os.path.join("images", "n19.jpg")
n19 = pygame.image.load(n19_path).convert()
n20_path = os.path.join("images", "n20.jpg")
n20 = pygame.image.load(n20_path).convert()
n21_path = os.path.join("images", "n21.jpg")
n21 = pygame.image.load(n21_path).convert()
n22_path = os.path.join("images", "n22.jpg")
n22 = pygame.image.load(n22_path).convert()
n23_path = os.path.join("images", "n23.jpg")
n23 = pygame.image.load(n23_path).convert()
n24_path = os.path.join("images", "n24.jpg")
n24 = pygame.image.load(n24_path).convert()
n25_path = os.path.join("images", "n25.jpg")
n25 = pygame.image.load(n25_path).convert()
n26_path = os.path.join("images", "n26.jpg")
n26 = pygame.image.load(n26_path).convert()
n27_path = os.path.join("images", "n27.jpg")
n27 = pygame.image.load(n27_path).convert()
n28_path = os.path.join("images", "n28.jpg")
n28 = pygame.image.load(n28_path).convert()
n29_path = os.path.join("images", "n29.jpg")
n29 = pygame.image.load(n29_path).convert()
n30_path = os.path.join("images", "n30.jpg")
n30 = pygame.image.load(n30_path).convert()
n_path = os.path.join("images", "n+.jpg")
n = pygame.image.load(n_path).convert()


def returnStoneImage(value):
    if value==0:
        return he
    elif value==1:
        return h1
    elif value == 2:
        return h2
    elif value == 3:
        return h3
    elif value == 4:
        return h4
    elif value == 5:
        return h5
    else:
        return hm


def ScoreImages(score):
    if score == 0:
        image = n0
    elif score == 1:
        image = n1
    elif score == 2:
        image = n2
    elif score == 3:
        image = n3
    elif score == 4:
        image = n4
    elif score == 5:
        image = n5
    elif score == 6:
        image = n6
    elif score == 7:
        image = n7
    elif score == 8:
        image = n8
    elif score == 9:
        image = n9
    elif score == 10:
        image = n10
    elif score == 11:
        image = n11
    elif score == 12:
        image = n12
    elif score == 13:
        image = n13
    elif score == 14:
        image = n14
    elif score == 15:
        image = n15
    elif score == 16:
        image = n16
    elif score == 17:
        image = n17
    elif score == 18:
        image = n18
    elif score == 19:
        image = n19
    elif score == 20:
        image = n20
    elif score == 21:
        image = n21
    elif score == 22:
        image = n22
    elif score == 23:
        image = n23
    elif score == 24:
        image = n24
    elif score == 25:
        image = n25
    elif score == 26:
        image = n26
    elif score == 27:
        image = n27
    elif score == 28:
        image = n28
    elif score == 29:
        image = n29
    elif score == 30:
        image = n30
    elif score > 30:
        image = n
    return image
    
def playerScoreImage(scores):
    """Returns the scores of the players as tuple of surfaces

    Args:
        scores (tuple): tuple containing the scores of the players(score_player1,score_player2)

    Returns:
        [tuple]: tuple of images corresponding with the players score
    """
    player1=ScoreImages(scores[0])
    player2=ScoreImages(scores[1])
    scores=(player1,player2)
    return scores

def updateScreen():
    #hole count
    count11=ScoreImages(game.return_hole_value(11))
    count10=ScoreImages(game.return_hole_value(10))
    count9=ScoreImages(game.return_hole_value(9))
    count8=ScoreImages(game.return_hole_value(8))
    count7=ScoreImages(game.return_hole_value(7))
    count6=ScoreImages(game.return_hole_value(6))
    count5=ScoreImages(game.return_hole_value(5))
    count4=ScoreImages(game.return_hole_value(4))
    count3=ScoreImages(game.return_hole_value(3))
    count2=ScoreImages(game.return_hole_value(2))
    count1=ScoreImages(game.return_hole_value(1))
    count0=ScoreImages(game.return_hole_value(0))
    #draw  top row
    screen.blit(count11, (180,275)) # 237x167
    screen.blit(count10, (237,275)) # 294x167
    screen.blit(count9, (294,275)) # 351x167
    screen.blit(count8, (398,275)) # 455x167
    screen.blit(count7, (455,275)) # 512x167
    screen.blit(count6, (512,275)) # 569x167
    #draw bottom row
    screen.blit(count0, (180,342)) #237x234
    screen.blit(count1, (237,342)) #294x234
    screen.blit(count2, (294,342)) #351x234
    screen.blit(count3, (398,342)) #455x234
    screen.blit(count4, (455,342)) #521x234
    screen.blit(count5, (512,342)) #569x234
    #draw player scores and player's turn
    screen.blit(currentPlayerImage,(600,40))
    scores=game.return_scores()
    scoresImg = playerScoreImage(scores)
    screen.blit(scoresImg[0],(664,130))                 #TODO change this to final position
    screen.blit(scoresImg[1],(28,130))                  #TODO change this to final position
    #draw stones on the board
    hole11=returnStoneImage(game.return_hole_value(11))
    hole10=returnStoneImage(game.return_hole_value(10))
    hole9=returnStoneImage(game.return_hole_value(9))
    hole8=returnStoneImage(game.return_hole_value(8))
    hole7=returnStoneImage(game.return_hole_value(7))
    hole6=returnStoneImage(game.return_hole_value(6))
    hole5=returnStoneImage(game.return_hole_value(5))
    hole4=returnStoneImage(game.return_hole_value(4))
    hole3=returnStoneImage(game.return_hole_value(3))
    hole2=returnStoneImage(game.return_hole_value(2))
    hole1=returnStoneImage(game.return_hole_value(1))
    hole0=returnStoneImage(game.return_hole_value(0))
    # draw top row stones
    screen.blit(hole11, (180,110)) # 237x167
    screen.blit(hole10, (237,110)) # 294x167
    screen.blit(hole9, (294,110)) # 351x167
    screen.blit(hole8, (398,110)) # 455x167
    screen.blit(hole7, (455,110)) # 512x167
    screen.blit(hole6, (512,110)) # 569x167
    #draw bottom row stones
    screen.blit(hole0, (180,177)) #237x234
    screen.blit(hole1, (237,177)) #294x234
    screen.blit(hole2, (294,177)) #351x234
    screen.blit(hole3, (398,177)) #455x234
    screen.blit(hole4, (455,177)) #521x234
    screen.blit(hole5, (512,177)) #569x234
    #update screen
    pygame.display.flip()

#####################################################################			
#####################################################################
## game loop
#####################################################################
#####################################################################

currentPlayer=player1
while running:
    for event in pygame.event.get():
        if game.return_player_turn() == 'Player1':
            currentPlayerImage=player1
        elif game.return_player_turn() == 'Player2':
            currentPlayerImage=player2
        
        if event.type == pygame.QUIT:
            running= False
        if game.continue_game():
            if event.type == pygame.KEYDOWN:
                if game.return_player_turn() == 'Player1':
                    if event.key == K_1:
                        value =0
                        game.player_select_hole(value)
                    if event.key == K_2:
                        value =1
                        game.player_select_hole(value)
                    if event.key == K_3:
                        value =2
                        game.player_select_hole(value)
                    if event.key == K_4:
                        value =3
                        game.player_select_hole(value)
                    if event.key == K_5:
                        value =4
                        game.player_select_hole(value)
                    if event.key == K_6:
                        value =5
                        game.player_select_hole(value)

                elif game.return_player_turn() == 'Player2':
                    if event.key == K_1:
                        value =6
                        game.player_select_hole(value)
                    if event.key == K_2:
                        value =7
                        game.player_select_hole(value)
                    if event.key == K_3:
                        value =8
                        game.player_select_hole(value)
                    if event.key == K_4:
                        value =9
                        game.player_select_hole(value)
                    if event.key == K_5:
                        value =10
                        game.player_select_hole(value)
                    if event.key == K_6:
                        value =11
                        game.player_select_hole(value)
            screen.fill(bgColor)
            screen.blit(board,(172,100))
            updateScreen()
        else:
            game.end_of_game()
            updateScreen()
            winner=game.winner()
            if winner == 'Player1':
                screen.blit(player1wins,(355,40))
            elif winner == 'Player2':
                screen.blit(player2wins,(355,40))
            elif winner == 'Tie':
                screen.blit(tie,(355,40))
            
            pygame.display.flip()

                    
