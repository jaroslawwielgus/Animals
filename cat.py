from animal import Animal

class Cat(Animal):
    ''' The Cat class'''
    def __init__(self, age, race, color, height, length_of_body, weight, length_of_life, is_wild, is_catching_mouses) -> None:
        super().__init__(age, race, color, height, length_of_body, weight, length_of_life, is_wild)
        self.__is_catching_mouses = is_catching_mouses

    def __repr__(self):
        return super().__repr__() + str(f' Czy łapie myszy: {self.__is_catching_mouses}')

    def __get_is_catching_mouses(self):
        return self.__is_catching_mouses

    def __set_is_catching_mouses(self, is_catching_mouses):
        self.__is_catching_mouses = is_catching_mouses

    is_catching_mouses = property(__get_is_catching_mouses, __set_is_catching_mouses)

    def give_voice(self):
        print("Miauuu")
