from animal import Animal

class Canary(Animal):
    ''' The Canary class'''
    def __init__(self, race, color, height, weight, length_of_life, is_wild=False, is_having_mane=False) -> None:
        super().__init__(race, color, height, weight, length_of_life, is_wild)
        self.__is_having_mane = is_having_mane

    def __repr__(self):
        return super().__repr__() + str(f' Czy ma grzywkę: {self.__is_having_mane}')

    def __get_is_having_mane(self):
        return self.__is_having_mane

    def __set_is_having_mane(self, is_having_mane):
        self.__is_having_mane = is_having_mane

    is_having_mane = property(__get_is_having_mane, __set_is_having_mane)

    def give_voice(self):
        return "Ćwik ćwik"