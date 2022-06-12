from animal import Animal

class Cow(Animal):
    ''' The Cow class'''
    def __init__(self, age, race, color, height, length_of_body, weight, length_of_life, is_wild, is_giving_milk) -> None:
        super().__init__(age, race, color, height, length_of_body, weight, length_of_life, is_wild)
        self.__is_giving_milk = is_giving_milk

    def __repr__(self):
        return super().__repr__() + str(f' Czy daje mleko: {self.__is_giving_milk}')

    def __get_is_giving_milk(self):
        return self.__is_giving_milk

    def __set_is_giving_milk(self, is_giving_milk):
        self.__is_giving_milk = is_giving_milk

    is_giving_milk = property(__get_is_giving_milk, __set_is_giving_milk)
    
    def give_voice(self):
        print("Muuuu")
