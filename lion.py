from animal import Animal

class Lion(Animal):
    ''' The Lion class'''
    def __init__(self, race, color, height, weight, length_of_life, is_wild=True, mane="niewielka") -> None:
        super().__init__(race, color, height, weight, length_of_life, is_wild)
        self.__mane = mane

    def __repr__(self):
        return super().__repr__() + str(f' Wielkość grzywy: {self.__mane}')

    def __get_mane(self):
        return self.__mane

    def __set_mane(self, mane):
        self.__mane = mane

    mane = property(__get_mane, __set_mane)

    def give_voice(self):
        return "Yyy"