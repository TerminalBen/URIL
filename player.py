"""
Define the player's constructors

"""

class Player:
    """
        Generates the player class
    """
    def __init__(self,playername)->None:
        """player init method

        Args:
            playername (String): player name
            score (int): player score
            stone_pos(int): last stone position
        """
        self.playername= playername
        self.score=0
        self.stone_pos=0
    
    def Playername(self)->str:
        """returns the player name

        Returns:
            str: Player's name
        """
        return self.playername
    
    def getscore(self)->int:
        """[returns player score]

        Returns:
            int: [Player's score]
        """
        return self.score

    def stonePos(self)->int:
        """gets the position of the last stone.

        Returns:
            int: stone Position
        """
        return self.stone_pos
    
    def score_update(self,score)->None:
        """Updates player score

        Args:
            score (int): [player score]
        """
        self.score=score