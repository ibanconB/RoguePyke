from typing import Tuple

class Entity:
    """
        Generic object to represent players, enemies, items
    """

    def __init__(self, x:int, y: int, char: str, color: Tuple[int,int,int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color


    def move(self, dx:int,dy:int)-> None:
        """
            Move entity by given amount

        :param dx: variable to modify entity movemente
        :param dy:variable to modify entity movemente

        """

        self.x += dx
        self.y += dy

