from animal import *
from dog import *
from cat import *


dog1 = Dog(10, 'rasa', 'brązowe', 5, 3, 500, 100, False, False)

'''
d.age=7
print(d.age)
d.give_voice()
'''

cat1 = Cat(5, 'kot sfinks', 'biały', 3, 5, 100, 20, True, False)


for animal in (cat1, dog1):
    animal.give_voice()



    

