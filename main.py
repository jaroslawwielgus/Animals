from animal import *
from dog import *
from cat import *


dog1 = Dog('rasa', 'brązowe', 5, 500, 100, False, False)

'''
d.age=7
print(d.age)
d.give_voice()
'''

cat1 = Cat('kot sfinks', 'biały', 3, 100, 20, True, False)


for animal in (cat1, dog1):
    print(animal.give_voice())



    

