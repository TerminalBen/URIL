import typing,player,board
"""Game controller connects the player model and the board model and controls the gameflow

    
"""


class Controller:
    """Game controller connecting player and board classes
    """
    def __init__(self):
        """ initiates the controller with board from Board class
            current_player as player1 from the player class
            other_player as player2 from player class
        """
        self.board = board.Board()
        self.current_player = player.Player('Player1')
        self.other_player  = player.Player('Player2')

    def continue_game(self)->bool:
        """Controls wether to continue the game or not depending if the next player has stones left to play

        Returns:
            bool: 
        """
        return self.board.has_stones(self.other_player.Playername())
    
    def return_hole_value(self,hole:int)->int:
        """Returns the value of a given hole

        Args:
            hole (int): hole number

        Returns:
            int: hole value
        """
        return self.board.hole_value(hole)

    def return_scores(self)->typing.Tuple:
        """Returns the scores of both players(score_Player1,score_player2)

        Returns:
            typing.Tuple: (int,int)
        """
        return self.board.scores()

    def return_player_score(self)->typing.Tuple:
        """returns the player's scores in a tuple of ints

        Returns:
            typing.Tuple: (score_player1,score_player2)
        """
        player1_score=0
        player2_score=0

        if self.current_player.Playername() == 'Player1':
            player1_score= self.current_player.getscore()
            print (f'player 1: {player1_score}')
        elif self.other_player.Playername == 'Player1':
            player2_score= self.other_player.getscore()
            print(f'player 2: {player2_score}')

        if self.current_player.Playername =='Player2':
            player2_score = self.current_player.getscore()
            print(f'player2 {player2_score}')
        elif self.other_player.Playername == 'Player2':
            player2_score = self.current_player.getscore()
            print(f'player2 {player2_score}')

        scoretuple = (player1_score,player2_score)
        return scoretuple
    
    def return_player_turn(self)->str:
        """returns the player's turn

        Returns:
            str: name of the player
        """
        return self.current_player.Playername()

    def switch_player_turn(self)->None:
        temp = self.current_player
        self.current_player=self.other_player
        self.other_player = temp

    def player_select_hole(self,hole:int)->None:
        """Moves the stones of the selected hole;
            Steal stones if any to steal
            Updates the currentPlayer's Score

        Args:
            hole ([int]): [hole number]
        """
        self.board.movestones(hole,self.current_player.Playername())
        self.board.steal_stones(self.current_player.Playername())
        self.switch_player_turn() #TODO fix turns if hole is empty

        Scores=self.board.scores()
        score= 0
        if self.current_player.Playername() == 'Player1':
            score = self.current_player.getscore()
            score= Scores[0]
        elif self.current_player.Playername() == 'Player2':
            score = self.current_player.getscore() 
            score= Scores[1]
        self.current_player.score_update(score)
        


    def end_of_game(self)->None:#TODO
        """Updates the score of the 'Other_player' in the end of the game context
        """
        Scores=self.board.scores()
        if self.other_player.Playername()=='Player2':
            score= Scores[1]
        elif self.other_player.Playername()== 'Player1':
            score=Scores[0]
        self.other_player.score_update(score)

    def winner(self)->str:
        """Compares the score of the players, returning the name of the winner, or tie if there is a tie

        Returns:
            str: [playername or Tie]
        """
        if self.other_player.getscore() == self.current_player.getscore():
            return 'Tie'
        elif self.other_player.getscore() > self.current_player.getscore():
            return self.other_player.Playername()
        else:
            return self.current_player.Playername()

    def capote(self): #TODO
        pass

    def xitada(self,score_1:int,score_2:int)->None:#TODO
        """Compares score player1 to score player2 cheching if any of the scores are perfect

        Args:
            score_1 (int): [Players1's score]
            score_2 (int): [Player2's score]
        """
        pass
