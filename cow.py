from animal import Animal

class Cow(Animal):
    ''' The Cow class'''
    def __init__(self, race, color, height, weight, length_of_life, is_wild, is_giving_milk, is_for_meat) -> None:
        super().__init__(race, color, height, weight, length_of_life, is_wild)
        self.__is_giving_milk = is_giving_milk
        self.__is_for_meat = is_for_meat

    def __repr__(self):
        return super().__repr__() + str(f' Czy daje mleko: {self.__is_giving_milk} Czy na mięso: {self.__is_for_meat}')

    def __get_is_giving_milk(self):
        return self.__is_giving_milk

    def __set_is_giving_milk(self, is_giving_milk):
        self.__is_giving_milk = is_giving_milk

    is_giving_milk = property(__get_is_giving_milk, __set_is_giving_milk)

    def __get_is_for_meat(self):
        return self.__is_for_meat

    def __set_is_for_meat(self, is_for_meat):
        self.__is_for_meat = is_for_meat

    is_for_meat = property(__get_is_for_meat, __set_is_for_meat)
    
    def give_voice(self):
        return "Muuuu"
