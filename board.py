import typing

class Board:
    """
    Generates the constructor
    Initializes the board
    Generic class checks
    Moves stones
    """

    def __init__(self) -> None:
        """
        Gerenrates the board: Array of lenght 12. 6 for each player, with 4 pieces each.
        Gererates auxiliary board with same values of the OG Board
        """
        self.boardgame=[4,4,4,4,4,4,4,4,4,4,4,4]
        self.last_position_stone=0
        self.score_player1=0
        self.score_player2=0

    def game(self)-> typing.List[int]:
        """returns the board array

        Returns:
            typing.List[int]: [board game array]
        """
        return self.boardgame

    def hole_value(self,hole:int)->int:
        """Returns the value of a given hole

        Args:
            hole (int): index of the hole

        Returns:
            int: value of the hole
        """
        return self.boardgame[hole]
    
    def last_stone_pos(self) ->int:
        """funtion that returns the position of the last stone in the board

        Returns:
            int: position of the last stone
        """
        return self.last_position_stone
    
    def scores(self)->typing.Tuple[int,int]:
        """(Function that returns a tuple of the scores of the two players
        (score_player1,score,player2)

        Returns:
            Tuple[int,int]: (score_player1,score_player2)
        """
        score_tuple= (self.score_player1,self.score_player2)
        return score_tuple

    def movestones(self,hole:int,playername:str)->int: 
        """Removes all the stones of a given hole 
            increments the following holes by one
            Player1 can only play from hole 0..5
            Player2 can only play from hole 6..11
        Args:
            hole (int): [selected hole]
            playename (str): [selected player]
        Returns:
            int: last hole changed
        """
        stones = self.boardgame[hole]
        stone_temp=stones
        last_temp = hole+stone_temp

        if last_temp > len(self.boardgame):
            last = last_temp % len(self.boardgame) -1
        else:
            last = last_temp

        for i in range(stones+1):
            try:
                self.boardgame[hole+i] += 1
                stones -= 1  
                self.boardgame[hole] = 0
                stone_aux = stones
            except IndexError: 
                for j in range(stone_aux+1): 
                    self.boardgame[j] += 1
                    stone_aux -= 1
                    
        self.last_position_stone = last
        print ('Ultimo: '+str(self.last_position_stone))
        print(self.boardgame)
        return self.last_position_stone



    def has_stones(self,playername:str)->bool:
        """checks if playername has stones left available in his row. if not he will not be able to play

        Args:
            playername (string): player1 or player2
        Returns:
            stones_left(bool): wether the player in question has stones left to play
        """ 
        stones_left=False
        total=0

        if playername=='Player1':
            x=0
            while x<6:
                total+=self.boardgame[x]
                x+=1
            if total>0:
                stones_left=True

        if playername=='Player2':
            x=6
            while x<11:
                total+=self.boardgame[x]
                x+=1
            if total>0:
                stones_left=True
        return stones_left

    def check_hole_values(self,hole)->bool:
        """Takes hole position, and returns the value of the hole, checking if value [1..3]
            This is still not in use. To be used on steal_stones
        Args:
            hole ([int]): [hole position to check]
        Returns:
            value(bool): wether the hole has [1..3] stones
        """
        stones = self.boardgame[hole]
        value = False
        if (stones > 0 and stones<4):
            value= True 
        else:
            value = False
        return value


    def steal_stones(self,playername:str)->None: #TODO Fix
        """eats opponent's stones if hole's stones<=3 adding it to the score tuple, or the player.score_update #TODO

        Args:
            playername (str): [name of the player's turn to play]
        """
        
        x = self.last_position_stone
        flag = True
        if playername =='Player2':
            if x >= 0:
                if x < 6:
                    while flag:
                        if (self.hole_value(x) <= 3):
                            score = self.hole_value(x)
                            self.score_player2 += score
                            self.boardgame[x] = 0
                            x-=1 
                        else:
                            flag=False

        if playername == 'Player1':
            if x > 5:
                if x < 12:
                    while flag:
                        if (self.hole_value(x)<=3):
                            score = self.hole_value(x)
                            self.score_player1+=score
                            self.boardgame[x]=0
                            x-=1
                        else:
                            flag=False
            
