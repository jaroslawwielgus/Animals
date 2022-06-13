from ctypes import alignment
import tkinter as tk
from tkinter import SOLID, font as tkfont
from PIL import Image, ImageTk
from cat import *
from dog import *
from cow import *
import pyttsx3


'''Creating animal instances'''
cat1 = Cat('kot sfinks', 'zróżnicowane', 0.28, 4.5, 13.5, False, False)
cat2 = Cat('kot bengalski', 'zróżnicowane', 0.4, 7, 12, False, False)
cat3 = Cat('kot perski', 'białe, rude, mieszane', 0.32, 4.5, 14, False, True)
cat4 = Cat('kot brytyjski', 'szare, cynamonowe, mieszane', 0.33, 6, 12, False, False)
cat5 = Cat('ryś', "szare, rdzawe bądź żółtawe z czarnymi plamami", 0.9, 24, 14, True, True)

dog1 = Dog('beagle', 'biało-brązowo-czarne', 0.37, 13, 14, False, True)
dog2 = Dog('border collie', 'biało-czarne', 0.52, 17, 14, False, False)
dog3 = Dog('golden retriever', 'biało-beżowe lub ciemno-złote', 0.58, 32, 11, False, True)
dog4 = Dog('owczarek niemiecki', 'rudo-czarne', 0.63, 35, 11, False, True)
dog5 = Dog('yorkshire terier', 'zróżnicowane', 0.19, 3, 15, False, True)

cow1 = Cow('holsztyno-fryzyjska', 'biało-czarne', 1.4, 700, 6, False, True, False)
cow2 = Cow('jersey', 'brązowo-białe', 1.25, 420, 6, False, True, False)
cow3 = Cow('duńska-czerwona', 'czerwone', 1.34, 640, 6, False, True, False)
cow4 = Cow('charolaise', 'białe', 1.4, 800, 6, False, False, True)
cow5 = Cow('limousine', 'jasno brązowe', 1.35, 730, 6, False, False, True)

'''
horse1 = Horse()
horse2 = Horse()
horse3 = Horse()
horse4 = Horse()
horse5 = Horse()

lion1 = Lion()
lion2 = Lion()
lion3 = Lion()
lion4 = Lion()
lion5 = Lion()
'''


class AnimalsApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Animals')
        self.iconbitmap('img/app.ico')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.resizable(0, 0)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwoCats, PageThreeCat1, PageThreeCat2,
         PageThreeCat3, PageThreeCat4, PageThreeCat5, PageTwoDogs, PageThreeDog1, PageThreeDog2,
         PageThreeDog3, PageThreeDog4, PageThreeDog5, PageTwoCows, PageThreeCow1, PageThreeCow2, 
         PageThreeCow3, PageThreeCow4, PageThreeCow5):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

        '''polymorphism in action - different voices for different species'''
        engine = pyttsx3.init()
        if page_name == "PageTwoCats":
            engine.say(cat1.give_voice())
            engine.runAndWait()
        elif page_name == "PageTwoDogs":
            engine.say(dog1.give_voice())
            engine.runAndWait()
        elif page_name == "PageTwoCows":
            engine.say(cow1.give_voice())
            engine.runAndWait()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hello!\n This is Animals app", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Show species",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Species", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10)
    
        button1 = tk.Button(self, text='Cat', width=10, command=lambda: controller.show_frame("PageTwoCats"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='Dog', width=10, command=lambda: controller.show_frame("PageTwoDogs"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='Horse', width=10, command=lambda: controller.show_frame("PageTwoHorses"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='Cow', width=10, command=lambda: controller.show_frame("PageTwoCows"))
        button4.grid(row=2, column=1)
        button5 = tk.Button(self, text='Lion', width=10, command=lambda: controller.show_frame("PageTwoLions"))
        button5.grid(row=3, column=0)

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4, column=1, pady=20)


class PageTwoCats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Cats", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')

        button1 = tk.Button(self, text='Kot sfinks', width=15, command=lambda: controller.show_frame("PageThreeCat1"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='Kot bengalski', width=15, command=lambda: controller.show_frame("PageThreeCat2"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='Kot perski', width=15, command=lambda: controller.show_frame("PageThreeCat3"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='Kot brytyjski', width=15, command=lambda: controller.show_frame("PageThreeCat4"))
        button4.grid(row=2, column=1)
        button5 = tk.Button(self, text='Ryś', width=15, command=lambda: controller.show_frame("PageThreeCat5"))
        button5.grid(row=3, column=0)
        

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=4, column=1, pady=20)

class PageTwoDogs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Dogs", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')

        button1 = tk.Button(self, text='Beagle', width=15, command=lambda: controller.show_frame("PageThreeDog1"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='Border collie', width=15, command=lambda: controller.show_frame("PageThreeDog2"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='Golden retriever', width=15, command=lambda: controller.show_frame("PageThreeDog3"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='Owczarek niemiecki', width=15, command=lambda: controller.show_frame("PageThreeDog4"))
        button4.grid(row=2, column=1)
        button5 = tk.Button(self, text='Yorkshire terier', width=15, command=lambda: controller.show_frame("PageThreeDog5"))
        button5.grid(row=3, column=0)

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=4, column=1, pady=20)

class PageTwoCows(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Cows", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')

        button1 = tk.Button(self, text='Holsztynowo-fryzyjska', width=20, command=lambda: controller.show_frame("PageThreeCow1"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='Jersey', width=20, command=lambda: controller.show_frame("PageThreeCow2"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='Duńska-czerwona', width=20, command=lambda: controller.show_frame("PageThreeCow3"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='Charolaise', width=20, command=lambda: controller.show_frame("PageThreeCow4"))
        button4.grid(row=2, column=1)
        button5 = tk.Button(self, text='Limousine', width=20, command=lambda: controller.show_frame("PageThreeCow5"))
        button5.grid(row=3, column=0)

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=4, column=1, pady=20)

class PageThreeCat1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cat1.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        '''
        if animal == cat1:
            img = ImageTk.PhotoImage(Image.open('img/cats/sfinks.png'))
        elif animal == cat2:
            img = ImageTk.PhotoImage(Image.open('img/cats/bengalski.jpg'))
        elif animal == cat3:
            img = ImageTk.PhotoImage(Image.open('img/cats/kot_perski.jpg'))
        elif animal == cat4:
            img = ImageTk.PhotoImage(Image.open('img/cats/kot-brytyjski.jpg'))
        elif animal == cat5:
            img = ImageTk.PhotoImage(Image.open('img/cats/ryś.jpg'))
        '''
        img = ImageTk.PhotoImage(Image.open('img/cats/sfinks.png'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cat1.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cat1.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cat1.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cat1.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat1.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat1.is_catching_mouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)

class PageThreeCat2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cat2.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cats/bengalski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cat2.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cat2.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cat2.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cat2.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat2.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat2.is_catching_mouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)


class PageThreeCat3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cat3.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cats/kot_perski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img
        
        color = tk.Label(self, text='Umaszczenie: ' + cat3.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cat3.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cat3.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cat3.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat3.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat3.is_catching_mouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)

class PageThreeCat4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cat4.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cats/kot-brytyjski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cat4.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cat4.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cat4.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cat4.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat4.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat4.is_catching_mouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)


class PageThreeCat5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cat5.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cats/ryś.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cat5.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cat5.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cat5.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cat5.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat5.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat5.is_catching_mouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)


class PageThreeDog1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=dog1.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        img = ImageTk.PhotoImage(Image.open('img/dogs/beagle.jpeg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + dog1.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(dog1.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(dog1.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(dog1.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog1.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog1.is_retrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20, sticky='w')

class PageThreeDog2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=dog2.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        img = ImageTk.PhotoImage(Image.open('img/dogs/border_collie.jpeg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + dog2.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(dog2.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(dog2.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(dog2.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog2.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog2.is_retrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)

class PageThreeDog3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=dog3.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        img = ImageTk.PhotoImage(Image.open('img/dogs/golden-retriever.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + dog3.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(dog3.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(dog3.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(dog3.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog3.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog3.is_retrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)

class PageThreeDog4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=dog4.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        img = ImageTk.PhotoImage(Image.open('img/dogs/owczarek_niemiecki.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + dog4.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(dog4.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(dog4.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(dog4.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog4.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog4.is_retrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)

class PageThreeDog5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=dog5.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        img = ImageTk.PhotoImage(Image.open('img/dogs/Yorkshire-terier.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + dog5.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(dog5.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(dog5.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(dog5.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog5.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog5.is_retrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)


class PageThreeCow1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cow1.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cows/holsztynowo-fryzyjska.jpeg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cow1.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cow1.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cow1.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cow1.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow1.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow1.is_giving_milk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow1.is_for_meat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cow2.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cows/jersey.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cow2.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cow2.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cow2.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cow2.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow2.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow2.is_giving_milk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow2.is_for_meat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')

        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cow3.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cows/duńska-czerwona.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cow3.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cow3.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cow3.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cow3.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow3.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow3.is_giving_milk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow3.is_for_meat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')


        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cow4.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cows/charolaise.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cow4.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cow4.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cow4.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cow4.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow4.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow4.is_giving_milk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow4.is_for_meat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')


        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text=cow5.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/cows/Limousine.JPG'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8)
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + cow5.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(cow5.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(cow5.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(cow5.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow5.is_wild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow5.is_giving_milk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow5.is_for_meat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')


        button = tk.Button(self, text="Back", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)


if __name__ == "__main__":
    app = AnimalsApp()
    app.mainloop()