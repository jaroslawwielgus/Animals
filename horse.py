from animal import Animal

class Horse(Animal):
    ''' The Horse class'''
    def __init__(self, race, color, height, weight, length_of_life, is_wild, is_draught, is_sports, mane) -> None:
        super().__init__(race, color, height, weight, length_of_life, is_wild)
        self.__is_draught = is_draught
        self.__is_sports = is_sports
        self.__mane = mane

    def __repr__(self):
        return super().__repr__() + str(f' Czy pociągowy: {self.__is_draught} Czy sportowy: {self.__is_sports} Wielkość grzywy: {self.__mane}')

    def __get_is_draught(self):
        return self.__is_draught

    def __set_is_draught(self, is_draught):
        self.__is_draught = is_draught

    is_draught = property(__get_is_draught, __set_is_draught)

    def __get_is_sports(self):
        return self.__is_sports

    def __set_is_sports(self, is_sports):
        self.__is_sports = is_sports
    
    is_sports = property(__get_is_sports, __set_is_sports)

    def __get_mane(self):
        return self.__mane

    def __set_mane(self, mane):
        self.__mane = mane

    mane = property(__get_mane, __set_mane)

    def give_voice(self):
        return "Ihaaa"