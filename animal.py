from abc import ABC, abstractmethod

class Animal(ABC):
    ''' The Animal class'''
    def __init__(self, age, race, color, height, length_of_body, weight, length_of_life, is_wild) -> None:
        self.__age = age
        self.__race = race
        self.__color = color
        self.__height = height
        self.__length_of_body = length_of_body
        self.__weight = weight
        self.__length_of_life = length_of_life
        self.__is_wild = is_wild

    def __repr__(self):
        return f'Wiek: {self.__age} Rasa: {self.__race} Umaszczenie: {self.__color} Wysokość: {self.__height} Długość ciała: {self.__length_of_body} Waga: {self.__weight} Długość życia: {self.__length_of_life} Czy dzikie: {self.__is_wild}'

    def __get_age(self):
        return self.__age

    def __set_age(self, age):
        self.__age = age

    age = property(__get_age, __set_age)

    def __get_race(self):
        return self.__race

    def __set_race(self, race):
        self.__race = race

    race = property(__get_race, __set_race)

    def __get_color(self):
        return self.__color

    def __set_color(self, color):
        self.__color = color

    color = property(__get_color, __set_color)

    def __get_height(self):
        return self.__height

    def __set_height(self, height):
        self.__height = height

    height = property(__get_height, __set_height)

    def __get_length_of_body(self):
        return self.__length_of_body

    def __set_length_of_body(self, length):
        self.__length_of_body = length

    length_of_body = property(__get_length_of_body, __set_length_of_body)

    def __get_weight(self):
        return self.__weight

    def __set_weight(self, weight):
        self.__weight = weight

    weight = property(__get_weight, __set_weight)
    
    def __get_length_of_life(self):
        return self.__length_of_life

    def __set_lenght_of_life(self, length_of_life):
        self.__length_of_life = length_of_life

    length_of_life = property(__get_length_of_life, __set_lenght_of_life)

    def __get_is_wild(self):
        return self.__is_wild

    def __set_is_wild(self, is_wild):
        self.__is_wild = is_wild

    is_wild = property(__get_is_wild, __set_is_wild)

    @abstractmethod
    def give_voice(self):
        pass



'''
age - w ktorym osiaga wymiary - jest dorosle
rasa - race
kolor - umaszczenie -color
height
length_of_body
weight
length_of_life
isWild = False
'''
