from io import BytesIO
import tkinter as tk
from tkinter import SOLID, font as tkfont
from PIL import Image, ImageTk
import requests
import cat as c
import dog as d
import cow as co
import horse as h
import lion as l
import pyttsx3
from schema import Cat, Dog, Cow, Horse, Lion, Session, engine


'''
Create session to read animals' data from database
'''
local_session = Session(bind=engine)

class AnimalsApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Zwierzęta')
        self.iconbitmap('img/app.ico')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        #self.geometry('500x500')
        self.resizable(0, 0)

        '''
        The container is where we'll stack a bunch of frames
        on top of each other, then the one we want visible
        will be raised above the others
        '''
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwoCats, PageThreeCat1, PageThreeCat2, PageThreeCatW,
         PageThreeCat3, PageThreeCat4, PageThreeCat5, PageTwoDogs, PageThreeDog1, PageThreeDog2,
         PageThreeDog3, PageThreeDog4, PageThreeDog5, PageThreeDogW, PageTwoCows, PageThreeCow1, 
         PageThreeCow2, PageThreeCow3, PageThreeCow4, PageThreeCow5, PageTwoHorses, PageThreeHorse1,
         PageThreeHorse2, PageThreeHorse3, PageThreeHorse4, PageThreeHorse5, PageTwoLions,
         PageThreeLion1, PageThreeLion2, PageThreeLion3, PageThreeLion4):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            '''
            Put all of the pages in the same location;
            the one on the top of the stacking order
            will be the one that is visible.
            '''
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

        '''Polymorphism in action - different voices for different species'''
        engine = pyttsx3.init()
        if page_name == "PageTwoCats":
            cat1 = local_session.query(Cat).first()
            c1 = c.Cat(cat1.race, cat1.color, cat1.height, cat1.weight, cat1.length_of_life, cat1.isWild, cat1.isCatchingMouses) 
            engine.say(c1.give_voice())
            engine.runAndWait()
        elif page_name == "PageTwoDogs":
            dog1 = local_session.query(Dog).first()
            d1 = d.Dog(dog1.race, dog1.color, dog1.height, dog1.weight, dog1.length_of_life, dog1.isWild, dog1.isRetrieving)
            engine.say(d1.give_voice())
            engine.runAndWait()
        elif page_name == "PageTwoCows":
            cow1 = local_session.query(Cow).first()
            co1 = co.Cow(cow1.race, cow1.color, cow1.height, cow1.weight, cow1.length_of_life, cow1.isWild, cow1.isGivingMilk, 
                cow1.isForMeat)
            engine.say(co1.give_voice())
            engine.runAndWait()
        elif page_name == "PageTwoHorses":
            horse1 = local_session.query(Horse).first()
            h1 = h.Horse(horse1.race, horse1.color, horse1.height, horse1.weight, horse1.length_of_life, horse1.isWild, 
                horse1.isDraught, horse1.isSports, horse1.mane)
            engine.say(h1.give_voice())
            engine.runAndWait()
        elif page_name == "PageTwoLions":
            lion1 = local_session.query(Lion).first()
            l1 = l.Lion(lion1.race, lion1.color, lion1.height, lion1.weight, lion1.length_of_life, lion1.isWild, lion1.mane)
            engine.say(l1.give_voice())
            engine.runAndWait()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Witaj!\n To jest aplikacja o zwierzętach", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Pokaż gatunki",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Gatunki", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10)
    
        button1 = tk.Button(self, text='Kot', width=10, command=lambda: controller.show_frame("PageTwoCats"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='Pies', width=10, command=lambda: controller.show_frame("PageTwoDogs"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='Koń', width=10, command=lambda: controller.show_frame("PageTwoHorses"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='Krowa', width=10, command=lambda: controller.show_frame("PageTwoCows"))
        button4.grid(row=2, column=1)
        button5 = tk.Button(self, text='Lew', width=10, command=lambda: controller.show_frame("PageTwoLions"))
        button5.grid(row=3, column=0)

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4, column=1, pady=20)


class PageTwoCats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Koty", font=controller.title_font)
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
        button6 = tk.Button(self, text='Cat\'s trivia', width=15, bg='green', command=lambda: controller.show_frame("PageThreeCatW"))
        button6.grid(row=4, column=1)
        
        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=6, column=1, pady=20)


class PageTwoDogs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Psy", font=controller.title_font)
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

        button6 = tk.Button(self, text='Dog of the while', width=15, bg='green', command=lambda: controller.show_frame("PageThreeDogW"))
        button6.grid(row=4, column=1)

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=6, column=1, pady=20)

class PageTwoCows(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Krowy", font=controller.title_font)
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

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=4, column=1, pady=20)

class PageTwoHorses(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Konie", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')

        button1 = tk.Button(self, text='Koń huculski', width=25, command=lambda: controller.show_frame("PageThreeHorse1"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='Kot małopolski', width=25, command=lambda: controller.show_frame("PageThreeHorse2"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='Kot oldenburski', width=25, command=lambda: controller.show_frame("PageThreeHorse3"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='Holenderski koń gorącokrwisty', width=25, command=lambda: controller.show_frame("PageThreeHorse4"))
        button4.grid(row=2, column=1)
        button5 = tk.Button(self, text='Shire', width=25, command=lambda: controller.show_frame("PageThreeHorse5"))
        button5.grid(row=3, column=0)
        

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=4, column=1, pady=20)

class PageTwoLions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Lwy", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')

        button1 = tk.Button(self, text='azjatycki', width=15, command=lambda: controller.show_frame("PageThreeLion1"))
        button1.grid(row=1, column=0)
        button2 = tk.Button(self, text='wschodnioafrykański', width=15, command=lambda: controller.show_frame("PageThreeLion2"))
        button2.grid(row=1, column=1)
        button3 = tk.Button(self, text='berberyjski', width=15, command=lambda: controller.show_frame("PageThreeLion3"))
        button3.grid(row=2, column=0)
        button4 = tk.Button(self, text='angolski', width=15, command=lambda: controller.show_frame("PageThreeLion4"))
        button4.grid(row=2, column=1)

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageOne"))
        button.grid(row=3, column=1, pady=20)


class PageThreeCat1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cat1 = local_session.query(Cat).filter(Cat.race=="kot sfinks").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat1.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat1.isCatchingMouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)

class PageThreeCat2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cat2 = local_session.query(Cat).filter(Cat.race=="kot bengalski").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat2.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat2.isCatchingMouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)


class PageThreeCat3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cat3 = local_session.query(Cat).filter(Cat.race=="kot perski").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat3.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat3.isCatchingMouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)

class PageThreeCat4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cat4 = local_session.query(Cat).filter(Cat.race=="kot brytyjski").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat4.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat4.isCatchingMouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)


class PageThreeCat5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cat5 = local_session.query(Cat).filter(Cat.race=="ryś").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cat5.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_catching_mouses = tk.Label(self, text='Czy łapie myszy: ' + ("Tak" if cat5.isCatchingMouses else "Nie"))
        is_catching_mouses.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.grid(row=7, column=1, pady=20)


class PageThreeCatW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        race = tk.Label(self, text="Cat\'s trivia", font=controller.title_font)
        race.pack(pady=10)

        url = 'https://meowfacts.herokuapp.com/'
        response = requests.get(url)
        response = response.json()

        text = tk.Label(self, text=response['data'][0])
        text.pack(pady=10)

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCats"))
        button.pack(pady=10)


class PageThreeDog1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        dog1 = local_session.query(Dog).filter(Dog.race=="beagle").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog1.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog1.isRetrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20, sticky='w')

class PageThreeDog2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        dog2 = local_session.query(Dog).filter(Dog.race=="border collie").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog2.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog2.isRetrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)

class PageThreeDog3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        dog3 = local_session.query(Dog).filter(Dog.race=="golden retriever").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog3.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog3.isRetrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)

class PageThreeDog4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        dog4 = local_session.query(Dog).filter(Dog.race=="owczarek niemiecki").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog4.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog4.isRetrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)

class PageThreeDog5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        dog5 = local_session.query(Dog).filter(Dog.race=="yorkshire terier").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if dog5.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_retrieving = tk.Label(self, text='Czy aportuje: ' + ("Tak" if dog5.isRetrieving else "Nie"))
        is_retrieving.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=7, column=1, pady=20)


class PageThreeDogW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        header = tk.Label(self, text="Dog of the while", font=controller.title_font)
        header.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
        
        '''
        Get data-image from dogs' api
        '''
        url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(url)
        response = response.json()

        img_url = response['message']
        img_response = requests.get(img_url, stream=True)
        img_data = img_response.content

        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0)
        label2.image=img
        
        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoDogs"))
        button.grid(row=2, column=1, pady=20)


class PageThreeCow1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cow1 = local_session.query(Cow).filter(Cow.race=="holsztyno-fryzyjska").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow1.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow1.isGivingMilk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow1.isForMeat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cow2 = local_session.query(Cow).filter(Cow.race=="jersey").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow2.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow2.isGivingMilk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow2.isForMeat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cow3 = local_session.query(Cow).filter(Cow.race=="duńska-czerwona").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow3.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow3.isGivingMilk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow3.isForMeat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')


        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        cow4 = local_session.query(Cow).filter(Cow.race=="charolaise").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow4.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow4.isGivingMilk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow4.isForMeat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')


        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)

class PageThreeCow5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        cow5 = local_session.query(Cow).filter(Cow.race=="limousine").first()
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
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if cow5.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_giving_milk = tk.Label(self, text='Czy daje mleko: ' + ("Tak" if cow5.isGivingMilk else "Nie"))
        is_giving_milk.grid(row=6, column=1, sticky='w')
        is_for_meat = tk.Label(self, text='Czy na mięso: ' + ("Tak" if cow5.isForMeat else "Nie"))
        is_for_meat.grid(row=7, column=1, sticky='w')


        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoCows"))
        button.grid(row=8, column=1, pady=20)


class PageThreeHorse1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        horse1 = local_session.query(Horse).filter(Horse.race=="koń huculski").first()
        race = tk.Label(self, text=horse1.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/horses/huculski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + horse1.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(horse1.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(horse1.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(horse1.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if horse1.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_draught = tk.Label(self, text='Czy pociągowy: ' + ("Tak" if horse1.isDraught else "Nie"))
        is_draught.grid(row=6, column=1, sticky='w')
        is_sports = tk.Label(self, text='Czy sportowy: ' + ("Tak" if horse1.isSports else "Nie"))
        is_sports.grid(row=7, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(horse1.mane))
        mane.grid(row=8, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoHorses"))
        button.grid(row=9, column=1, pady=20)

class PageThreeHorse2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        horse2 = local_session.query(Horse).filter(Horse.race=="koń małopolski").first()
        race = tk.Label(self, text=horse2.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/horses/malopolski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + horse2.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(horse2.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(horse2.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(horse2.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if horse2.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_draught = tk.Label(self, text='Czy pociągowy: ' + ("Tak" if horse2.isDraught else "Nie"))
        is_draught.grid(row=6, column=1, sticky='w')
        is_sports = tk.Label(self, text='Czy sportowy: ' + ("Tak" if horse2.isSports else "Nie"))
        is_sports.grid(row=7, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(horse2.mane))
        mane.grid(row=8, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoHorses"))
        button.grid(row=9, column=1, pady=20)


class PageThreeHorse3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        horse3 = local_session.query(Horse).filter(Horse.race=="koń oldenburski").first()
        race = tk.Label(self, text=horse3.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/horses/oldenburski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + horse3.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(horse3.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(horse3.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(horse3.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if horse3.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_draught = tk.Label(self, text='Czy pociągowy: ' + ("Tak" if horse3.isDraught else "Nie"))
        is_draught.grid(row=6, column=1, sticky='w')
        is_sports = tk.Label(self, text='Czy sportowy: ' + ("Tak" if horse3.isSports else "Nie"))
        is_sports.grid(row=7, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(horse3.mane))
        mane.grid(row=8, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoHorses"))
        button.grid(row=9, column=1, pady=20)

class PageThreeHorse4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        horse4 = local_session.query(Horse).filter(Horse.race=="Holenderski koń gorącokrwisty").first()
        race = tk.Label(self, text=horse4.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/horses/Holenderski koń gorącokrwisty.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + horse4.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(horse4.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(horse4.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(horse4.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if horse4.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_draught = tk.Label(self, text='Czy pociągowy: ' + ("Tak" if horse4.isDraught else "Nie"))
        is_draught.grid(row=6, column=1, sticky='w')
        is_sports = tk.Label(self, text='Czy sportowy: ' + ("Tak" if horse4.isSports else "Nie"))
        is_sports.grid(row=7, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(horse4.mane))
        mane.grid(row=8, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoHorses"))
        button.grid(row=9, column=1, pady=20)

class PageThreeHorse5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        horse5 = local_session.query(Horse).filter(Horse.race=="Shire").first()
        race = tk.Label(self, text=horse5.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/horses/shire.JPG'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + horse5.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(horse5.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(horse5.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(horse5.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if horse5.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        is_draught = tk.Label(self, text='Czy pociągowy: ' + ("Tak" if horse5.isDraught else "Nie"))
        is_draught.grid(row=6, column=1, sticky='w')
        is_sports = tk.Label(self, text='Czy sportowy: ' + ("Tak" if horse5.isSports else "Nie"))
        is_sports.grid(row=7, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(horse5.mane))
        mane.grid(row=8, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoHorses"))
        button.grid(row=9, column=1, pady=20)


class PageThreeLion1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lion1 = local_session.query(Lion).filter(Lion.race=="lew azjatycki").first()
        race = tk.Label(self, text=lion1.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/lions/azjatycki.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + lion1.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(lion1.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(lion1.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(lion1.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if lion1.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(lion1.mane))
        mane.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoLions"))
        button.grid(row=7, column=1, pady=20)


class PageThreeLion2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lion2 = local_session.query(Lion).filter(Lion.race=="lew wschodnioafrykański").first()
        race = tk.Label(self, text=lion2.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/lions/wschodnioafrykański.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + lion2.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(lion2.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(lion2.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(lion2.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if lion2.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(lion2.mane))
        mane.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoLions"))
        button.grid(row=7, column=1, pady=20)


class PageThreeLion3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lion3 = local_session.query(Lion).filter(Lion.race=="lew berberyjski").first()
        race = tk.Label(self, text=lion3.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/lions/berberyjski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + lion3.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(lion3.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(lion3.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(lion3.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if lion3.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(lion3.mane))
        mane.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoLions"))
        button.grid(row=7, column=1, pady=20)


class PageThreeLion4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lion4 = local_session.query(Lion).filter(Lion.race=="lew angolski").first()
        race = tk.Label(self, text=lion4.race.capitalize(), font=controller.title_font)
        race.grid(row=0, column=0, columnspan=2, pady=10, sticky='we')
    
        img = ImageTk.PhotoImage(Image.open('img/lions/angolski.jpg'))
        label2 = tk.Label(self, image=img, relief=SOLID)
        label2.grid(row=1, column=0, rowspan=8, sticky='w')
        label2.image=img

        color = tk.Label(self, text='Umaszczenie: ' + lion4.color)
        color.grid(row=1, column=1, sticky='w')
        height = tk.Label(self, text='Wysokość: ' + str(lion4.height) + "m")
        height.grid(row=2, column=1, sticky='w')
        weight = tk.Label(self, text= 'Waga: ' + str(lion4.weight) + "kg")
        weight.grid(row=3, column=1, sticky='w')
        length_of_life = tk.Label(self, text='Dlugość życia: ' + str(lion4.length_of_life))
        length_of_life.grid(row=4, column=1, sticky='w')
        is_wild = tk.Label(self, text='Czy dziki: ' + ("Tak" if lion4.isWild else "Nie"))
        is_wild.grid(row=5, column=1, sticky='w')
        mane = tk.Label(self, text='Wielkość grzywy: ' + str(lion4.mane))
        mane.grid(row=6, column=1, sticky='w')

        button = tk.Button(self, text="Wróć", bg='purple',
                           command=lambda: controller.show_frame("PageTwoLions"))
        button.grid(row=7, column=1, pady=20)


if __name__ == "__main__":
    app = AnimalsApp()
    app.mainloop()

