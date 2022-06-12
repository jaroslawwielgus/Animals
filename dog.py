from animal import Animal

class Dog(Animal):
    ''' The Dog class'''
    def __init__(self, age, race, color, height, length_of_body, weight, length_of_life, is_wild, is_retrieving) -> None:
        super().__init__(age, race, color, height, length_of_body, weight, length_of_life, is_wild)
        self.__is_retrieving = is_retrieving

    def __repr__(self):
        return super().__repr__() + str(f' Czy aportuje: {self.__is_retrieving}')

    def __get_is_retrieving(self):
        return self.__is_retrieving

    def __set_is_retrieving(self, is_retrieving):
        self.__is_retrieving = is_retrieving

    is_retrieving = property(__get_is_retrieving, __set_is_retrieving)

    def give_voice(self):
        print("Hauuu")
